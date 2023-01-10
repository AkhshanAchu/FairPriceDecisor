import streamlit as st
from collections import defaultdict
import os
st.set_page_config(
    page_title="Other Pages"
)
st.sidebar.success("Select a page above")

st.title("NIT Hackathon")
st.header("Fair Price Detector")

stockWt = int(st.number_input('Enter the Stock Required'))
st.write('The current number is ', stockWt)
storeType = st.selectbox(
    'Select the Crop Required',
    ('Potatos','Tomatos','Onions','Beans','Cabbage','Banana','Wheat','Mango','Paddy'))

st.write('You selected:', storeType)

path = ".\pages\dataset\Available_area.csv"
assert os.path.isfile(path)
Startpoint = st.selectbox(
    'Select the Destination vertex',
    ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'))

st.write('You selected:', Startpoint)



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



    nodes=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
    edges = [
    ( 'a' , 'b',   8),
    ( 'a' , 'c',  14),
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


    def call():
        c=[]
        for jag in g:
            a=dijsktra(graph,Startpoint,jag)
            b=0
            for ind in range(len(a)-1):
                b+=int(edg[((edg[:,0]==a[ind]) * (edg[:,1]==a[ind+1])) + ((edg[:,1]==a[ind]) * (edg[:,0]==a[ind+1]))][0,2])
            c.append([a,b])
        c1 = np.array(c,dtype=object)
        ink=c1[c1[:,1] == min(c1[:,1])][0,0]
        return ink

    def find(stockWt):
        # a=[700,900,1000]
        z=len(a)
        b=[0,0,0]
        s=[0,0,0]
        c=stockWt
        d=c+1000
        e=c
        while(c>0):
            for i in range(z):
                if(c%a[i]==0):
                    b[i]+=c/a[i]
                    d=c
                    c=0
                    break
            for i in range(z):
                if(c==0):
                    break
                
                e=c
                for j in range(int(c/a[i])):
                        if(c==0):
                            break
                        e-=a[i]
                        for p in range(z):
                            k=e
                            if(e%a[p]==0):
                                b=[0,0,0]
                                b[i]=j+1
                                b[p]+=int(e/a[p])
                                d=c
                                c=0
                                break
                            
                            else:
                                k=e
                                for edhukku  in range(int(e/a[p])):
                                    if(c==0):
                                        break
                                    k-=a[p]
                                    for qw in range(z):
                                        if(e%a[qw]==0):
                                            b=[0,0,0]
                                            b[qw]+=int(k/a[qw])
                                            b[i]=j+1
                                            b[p]=edhukku+1
                                            d=c
                                            c=0
                                            break
                                        elif(k-a[qw]<0):
                                            s=[0,0,0]
                                            s[i]=j+1
                                            s[p]=edhukku+1
                                            s[qw]=qw+2
                                            final=a[i]*s[i]+s[p]*a[p]+s[qw]*a[qw]
                                        
                                            if(d)>final and final>c:
                                            
                                                d=final
                                                b=s
                                    s=[0,0,0]
                                    s[i]=j+1
                                    s[p]=edhukku+2
                                    final=a[i]*s[i]+s[p]*a[p]
                                    if(d)>final and final>c:
                                        
                                        if(a[i]==a[p]):
                                            s[i]=s[i]+s[p]
                                            d=final
                                            b=s           
                                s=[0,0,0]
                                s[i]=j+1
                                s[p]=1
                                final=a[i]*s[i]+s[p]*a[p]
                                if(d)>=final and final>c:
                                
                                    if(a[i]==a[p]):
                                        s[i]=s[i]+s[p]
                                    d=final
                                    b=s

                                    
                        s=[0,0,0]
                        s[i]=j+2
                        final=a[i]*(s[i])
                        if(final<=d and final>c):
                        
                            d=final
                            b=s
                            
            c=0             
            # print(d)
            # print(b)
            return b
            
    import numpy as np
    import pandas as pd
    edg = np.array(edges)
    # Startpoint='r'
    # stockWt=15550
    c=[]
    a=[700,900,1000]
    der=[]
    ind=0
    lorry=[]
    # storeType='Cabbage'
    df = pd.read_csv(path)
    g=list(df[df.loc[:,storeType]>0]['Nodes'])
    # print(g)

    every=[]
    der=find(stockWt)
    for i in range(len(der)):
        for j in range(int(der[i])):
            every.append(a[i])
    print(every)
    
    dup=Startpoint
    for ilk in every[::-1]:
        ind+=1
        print(ilk)
        stockWt=ilk
        i=call()
        if(len(g)<=1 and int(df[df['Nodes']==i[-1]][storeType]) < stockWt):
            st.subheader("Sorry! Stock Not Available")
        else:
            dest=[Startpoint]
            while(stockWt!=0):
                i=call()
                if(int(df[df['Nodes']==i[-1]][storeType]) > stockWt):
                    # print('stockWt at file')
                    # print(int(df[df['Nodes']==i[-1]][storeType]))
                    df[storeType][df['Nodes']==i[-1]] -= stockWt
                    # print('stockWt at file-Changed')
                    # print(int(df[df['Nodes']==i[-1]][storeType]))
                    stockWt=0
                    #g.remove(i[-1])
                    dest+=i[1:]
                elif(int(df[df['Nodes']==i[-1]][storeType]) <= stockWt):
                    # print('stockWt')
                    # print(stockWt)
                    stockWt-= int(df[storeType][df['Nodes']==i[-1]])
                    # print('stockWt-Changed')
                    # print(stockWt)
                    df[storeType][df['Nodes']==i[-1]]=0
                    Startpoint=i[-1]
                    x=i[-1]+"(stop)"
                    dest+=i[1:-1]
                    dest.append(x)
                    g.remove(i[-1])
            Startpoint=dup
            s=""
            for j in range(1,len(dest)+1):
                if(j==len(dest)):
                    s += dest[-j]
                else:
                    f=dest[0]
                    s += dest[-j]+"  -->  "
            lorry.append(s)
            dest=[]
        st.subheader("Lorry "+str(ind)+" of Capacity "+str(every[-ind])+"Kg")
        # st.subheader("Destination : "+f)
        st.subheader("Preferred Path : "+s)

    df = pd.DataFrame(df)
    df.to_csv(path, index = False, header=True)
 