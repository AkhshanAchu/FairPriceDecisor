import streamlit as st
from collections import defaultdict

st.set_page_config(
    page_title="Other Pages"
)
st.sidebar.success("Select a page above")

st.title("NIT Hackathon")
st.header("Distribution Path")

storeType = st.selectbox(
    'Select the Crop Required',
    ('Potatos','Tomatos','Onions','Beans','Cabbage','Banana','Wheat','Mango','Paddy'))

st.write('You selected:', storeType)


destina = st.text_input(
    'Enter the Required Places (For experiment: b-y) : ')

st.write('You selected:', destina)

items = st.text_input(
    'Enter the Required stocks: ')



if st.button("Check Availablity"):
 
    from collections import defaultdict

    
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



    nodes=['W-House','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
    edges = [
    ( 'W-House' , 'b',   8),
    ( 'W-House' , 'c',  14),
    ( 'c' , 'd',   4),
    ( 'c' , 'j',   2),
    ( 'j' , 'f',   8),
    ( 'j' , 'd',   8),
    ( 'j' , 'e',   2),
    ( 'l' , 'e',   2),
    ( 'k' , 'l',   8),
    ( 'k' , 'j',   7),
    ( 'i' , 'j',   6),
    ( 'i' , 'h',   3),
    ( 'i' , 'g',   8),
    ( 'l' , 'n',   8),
    ( 'l' , 'm',  12),
    ( 'm' , 'o',   3),
    ( 'n' , 'o',   8),
    ( 'w' , 'v',   2),
    ( 'k' , 'x',   1),
    ( 'w' , 'l',  12),
    ( 'v' , 'x',  14),
    ( 'x' , 'y',   7),
    ( 'v' , 't',   7),
    ( 't' , 'u',   5),
    ( 't' , 'o',   4),
    ( 'o' , 'p',   2),
    ('p', 'q', 7),
    ('q', 's', 8),
    ('q', 'r', 2)
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

    import numpy as np
    import pandas as pd
    edg = np.array(edges)
    Startpoint="W-House"
    g = list(map(str,destina.split()))
    #print(g)
    f = storeType
    stockWt=  list(map(int,items.split()))
    c=[]
    storeType=f
    df = pd.read_csv(".\pages\dataset\Selling.csv")
    #destin=["d","e","f"]

    def call():
        c=[]
        #print("call called")
        for jag in g:
            #print("j-value")
            #print(jag)
            a=dijsktra(graph,Startpoint,jag)
            #print(a)
            b=0
            for ind in range(len(a)-1):
                b+=int(edg[((edg[:,0]==a[ind]) * (edg[:,1]==a[ind+1])) + ((edg[:,1]==a[ind]) * (edg[:,0]==a[ind+1]))][0,2])
            c.append([a,b])

            #print("Total : ",c)

        c1 = np.array(c,dtype=object)
        ink=c1[c1[:,1] == min(c1[:,1])][0,0]
        #print("Selected : ",ink)
        return ink

    output=[]
    i=call()
    if(sum(stockWt)>int(df[f])):
        #st.subheader("Sorry! Stock Not Available")
        print("Sorry! Stock Not Available")
    else:
        dest=[Startpoint]
        while(len(g)!=0):
            i=call()
            #print("path: ",i)
            #print("g before",g)
            g.remove(i[-1])
            #print("g after",g)
            output.append(i[:-1])
            Startpoint = i[-1]
            

    #     s=""
    #     for j in range(1,len(dest)+1):
    #         if(j==len(dest)):
    #             s += dest[-j]
    #         else:
    #             f=dest[0]
    #             s += dest[-j]+"  -->  "
    #     print(s)
    s=""
    for i in output:
        for j in i:
            s+=j
            s+=" =>"
    s=s[:len(s)-3]
    st.subheader("You may follow the below path for Better Transport : ")
    st.subheader(s)
    df = pd.DataFrame(df)
    df.to_csv(".\pages\dataset\Selling.csv", index = False, header=True)

    