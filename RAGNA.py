import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import networkx as nx

st.set_page_config(layout="wide")

df = pd.read_excel('datakopi.xlsx')

G = nx.from_pandas_edgelist(df, 'from', 'to', ['nilai'], create_using=nx.DiGraph())

# Position the nodes using a random layout
pos = nx.shell_layout(G)
# pos = nx.spring_layout(G)

# Prepare edge traces
edge_x = []
edge_y = []
for edge in G.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines'
)

# Prepare node traces
node_x = []
node_y = []
node_values = []  # For node colors
node_text = []    # For hover text
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_values.append(df[df['from'] == node]['nilai'].sum())  # Sum of 'Value' for node
    node_text.append(f'Node: {node}<br>Value: {node_values[-1]}')

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        reversescale=True,
        color=node_values,
        size=10,
        colorbar=dict(
            thickness=15,
            title='Nilai Perdagangan (USD)',
            xanchor='left',
        ),
        line_width=2
    )
)

node_trace.text = node_text

# Create the figure
fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                     showlegend=False,
                     hovermode='closest',
                     margin=dict(b=20, l=5, r=5, t=40),
                     xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                     yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                 )
# Create a list of unique nodes
all_nodes = list(pd.concat([df['from'], df['to']]).unique())

# Create mapping from node names to indices
node_indices = {node: i for i, node in enumerate(all_nodes)}

# Create the Sankey diagram data
sankey_data = go.Sankey(
    node=dict(
        pad=15,  # Padding between nodes
        thickness=20,  # Thickness of nodes
        line=dict(color='black', width=0.5),
        label=all_nodes,  # Node labels
        color=['blue'] * len(all_nodes)  # Color for nodes (you can customize this)
    ),
    link=dict(
        source=[node_indices[src] for src in df['from']],  # Source indices
        target=[node_indices[tgt] for tgt in df['to']],  # Target indices
        value=df['nilai']  # Values for the links
    )
)

# Create the figure
fig2 = go.Figure(data=[sankey_data])

input = st.sidebar.text_input("masukan kata untuk melihat referensi HS Code")
if input == 'kopi':
    st.sidebar.write('0901 | Kopi, digongseng atau dihilangkan kafeinnya maupun tidak; sekam dan kulit kopi; pengganti kopi mengandung kopi dengan perbandingan berapapun.')
option = st.sidebar.selectbox(
    "pilih HS Code yang sesuai",
    (" ", "0901"),
)

if option == '0901':
    st.write('Data dipilih: 0901 | Kopi, digongseng atau dihilangkan kafeinnya maupun tidak; sekam dan kulit kopi; pengganti kopi mengandung kopi dengan perbandingan berapapun.')

    tab1, tab2 = st.tabs(["Network Graph", "Sankey Chart"])
    with tab1:
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.plotly_chart(fig2, use_container_width=True)

    st.write('Penjelasan')

    #prompt : cari dimana peluang paling besar bagi UMKM untuk melakukan ekspor kopi
    messages = st.container(height=300)
    messages.chat_message("assistant").write(f"RAGNA: openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.")
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(f"User: {prompt}")
        messages.chat_message("assistant").write(f"RAGNA: openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.")
