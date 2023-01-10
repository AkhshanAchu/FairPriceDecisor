import streamlit as st
from collections import defaultdict

Sources=[['A-Cold','a'],['B-Dry','b'],['B-Dry','c'],['B-Cold','d'],['C-Dry','e'],['Village-1','f'],['Village-2','g'],['Village-3','h'],['Village-4','i'],['Village-5','j'],['Village-6','k'],['Village-7','l'],['Village-8','m'],['Village-9','n'],['Village-10','o']]
mapping = {'A-Cold':'a','B-Dry':'b','B-Dry':'c','B-Cold':'d','C-Dry':'e','Village-1':'f','Village-2':'g','Village-3':'h','Village-4':'i','Village-5':'j','Village-6':'k','Village-7':'l','Village-8':'m','Village-9':'n','Village-10':'o'}
st.set_page_config(
    page_title="Other Pages"
)
st.sidebar.success("Select a page above")

st.title("NIT Hackathon")
st.header("Fair Price Detector")

stockWt = int(st.number_input('Enter the Stock Weight'))
st.write('The current number is ', stockWt)
storeOption = st.selectbox(
    'Select the place where you want to store',
    ('Cold', 'Dry'))

st.write('You selected:', storeOption)


startPt = st.selectbox(
    'Select the starting vertex',
    ('Village-1','Village-2','Village-3','Village-4','Village-5','Village-6','Village-7','Village-8','Village-9','Village-10'))

st.write('You selected:', startPt)



if st.button("Check Availablity"):
 
    class Graph():
        def __init__(self):
            self.edges = defaultdict(list)
            self.weights = {}
        
        def add_edge(self, from_node, to_node, weight):
            # Note: assumes edges are bi-directional
            self.edges[from_node].append(to_node)
            self.edges[to_node].append(from_node)
            self.weights[(from_node, to_node)] = weight
            self.weights[(to_node, from_node)] = weight




    graph = Graph()



    nodes=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    edges = [
    ( 'a' , 'b',   8),
    ( 'a' , 'f',  14),
    ( 'a' , 'h',   4),
    ( 'a' , 'm',   2),
    ( 'b' , 'a',   8),
    ( 'b' , 'b',   8),
    ( 'b' , 'h',   2),
    ( 'b' , 'i',   2),
    ( 'c' , 'd',   8),
    ( 'c' , 'h',   7),
    ( 'c' , 'l',   6),
    ( 'c' , 'n',   3),
    ( 'd' , 'c',   8),
    ( 'd' , 'e',   8),
    ( 'd' , 'j',  12),
    ( 'd' , 'l',   3),
    ( 'e' , 'd',   8),
    ( 'e' , 'i',   2),
    ( 'e' , 'j',   1),
    ( 'e' , 'k',  12),
    ( 'f' , 'a',  14),
    ( 'f' , 'g',   7),
    ( 'g' , 'f',   7),
    ( 'g' , 'i',   5),
    ( 'h' , 'a',   4),
    ( 'h' , 'b',   2),
    ('h', 'c', 7),
    ('h', 'n', 8),
    ('i', 'b', 2),
    ('i', 'e', 2),
    ('i', 'g', 5),
    ('i', 'j', 3),
    ('j', 'd', 12),
    ('j', 'e', 1),
    ('j', 'i', 3),
    ('k', 'e', 12),
    ('k', 'l', 9),
    ('l', 'c', 6),
    ('l', 'd', 3),
    ('l', 'k', 9),
    ('l', 'o', 11),
    ('m', 'a', 2),
    ('n', 'c', 3),
    ('n', 'h', 8),
    ('n', '0', 12),
    ('o', 'l', 11),
    ('o', 'n', 12),
    ]

    for edge in edges:
        graph.add_edge(*edge)


    def dijsktra(graph, initial, end):
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()
        
        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        path = path[::-1]
        return path

    # for i in range(10):
    #     if(Sources[i][0]==startPt):
    #         startPt=Sources[i][1]
    #         break
    startPt  = mapping[startPt]



    import numpy as np
    import os
    edg = np.array(edges)
    c=[]
    d=[0,3]
    e=[1,2,4]
    path = ".\pages\dataset\dataBase.csv"
    assert os.path.isfile(path)
    import pandas as pd

    df = pd.read_csv(path)



    Col = []
    Dr = []
    for i in d:
        Col.append([i,df["Storage"][i]])
    for j in e:
        Dr.append([j,df["Storage"][j]])
    print(Col)
    print(Dr)



    f=storeOption
    h=startPt
    stock=stockWt
    if(f=='Cold'):
        g=d
        for i in Col:
            if(stock>i[1]):
                g.remove(i[0])
    else:
        g=e
        for i in Dr:
            if(stock>i[1]):
                g.remove(i[0])
    if(len(g)==0):
        st.subheader("Sorry! Warehouse Not Available")
    else:
        for i in g:
            a=dijsktra(graph,h,nodes[i])
            b=0
            for i in range(len(a)-1):
                b+=int(edg[((edg[:,0]==a[i]) * (edg[:,1]==a[i+1])) + ((edg[:,1]==a[i]) * (edg[:,0]==a[i+1]))][0,2])
            c.append([a,b])
        c1 = np.array(c,dtype=object)
        i=c1[c1[:,1] == min(c1[:,1])][0,0]


        s=""
        for j in range(len(i)):
            for k in range(len(Sources)):
                if(Sources[k][1]==i[j]):
                    if(j!=len(i)-1):
                        s += Sources[k][0]+" --> "
                    else:
                        f=Sources[k][0]
                        s += Sources[k][0]

        for ind in range(len(d)+len(e)):
            if(nodes[ind]==i[-1]):
                df['Storage'][ind]-=stock
                break
        
        st.write(Col[0][1])
        st.subheader("Destination : "+f)
        st.subheader("Preferred Path : "+s)


        df = pd.DataFrame(df)
        df.to_csv(path, index = False, header=True)



import graphviz


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