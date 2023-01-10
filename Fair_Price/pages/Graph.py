import graphviz
import streamlit as st

# Create a graphlib graph object
graph = graphviz.Graph()
graph.edge('Village-1', 'Village-2')
graph.edge('Village-2', 'Village-4')
graph.edge('Village-1', 'A-Cold')
graph.edge('A-Cold', 'Village-8')
graph.edge('A-Cold', 'Village-3')
graph.edge('Village-3', 'Village-9')
graph.edge('Village-3', 'B-Cold')
graph.edge('Village-9', 'Village-10')
graph.edge('Village-10', 'Village-7')
graph.edge('B-Cold', 'Village-7')
graph.edge('B-Dry', 'B-Cold')
graph.edge('B-Dry', 'Village-7')
graph.edge('Village-7', 'Village-6')
graph.edge('Village-6', 'C-Cold')
graph.edge('C-Cold', 'Village-5')
graph.edge('Village-4', 'Village-5')
graph.edge('A-Cold', 'A-Dry')
graph.edge('A-Dry', 'Village-3')
graph.edge('Village-4', 'A-Dry')
graph.edge('Village-4', 'C-Cold')
graph.edge('Village-5', 'B-Dry')
graph.edge('Village-9', 'B-Cold')


st.graphviz_chart(graph,use_container_width=True)