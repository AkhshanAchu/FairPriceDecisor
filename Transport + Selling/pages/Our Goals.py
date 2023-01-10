import streamlit as st
from PIL import Image

st.title("Scope -")

st.markdown("- Farming is said to be the backbone of the country. But Farmers aren't the ones who decide the prices for their product, instead the Middlemen does that which in most cases results in negative trades. The succession generations are not into farming as the profit percentage is merely on the margin which is the result of the negative trades among the farmers and the middle men.")

image1 = Image.open(r"pages\assets\img1.jpeg")

st.image(image1,width=400)

st.markdown("- A direct interaction between farmers and customers in which there are no middlemen engaged in the exchange of goods is referred to as a farmer-consumer system. As it enables a more effective and economical operation, this kind of technology can be advantageous for both farmers and customers. In contrast to having to sell through a middleman who gets a percentage of the profits, selling directly to consumers can be more beneficial for farmers because they can get paid the entire worth of their products. Additionally, it might provide farmers more power over the prices they set for their goods.")
st.markdown("- In order to make a livelihood and maintain their businesses, farmers must be paid fairly for their goods. But to remove the middle men completely from the supply chain isn’t a good option, it becomes difficult for the farmers to effectively sell the products to the consumer if the middle men are removed from the supply chain.")
st.markdown("- A fair price for farmers should include a decent profit margin in addition to covering the cost of production, which includes charges for things like seed, fertiliser, labour, and equipment. The fair price is to be determined by the criteria such as total availability of the product on that respective areas, Gross production, Production cost (includes Pesticides, Fertilizers, etc.), farmers expectation, seasonal loses, seasonal Trend, Demand, Quality and micelles. This ensures the decent profit margin for the farmers. ")
st.markdown("- To maintain the balance in the producers in the supply chain can be optimized by introducing another block (which is an organization preferably government) is to be inserted in the supply chain between the Producers and the middle men. The producers sell their production by a fixed price and the middle men interact with the organisation for the products.")
st.markdown("- The fixed price is determined by the Machine Learning model with the deciding parameters using Data Analysis from the past trends. It should also ensure that the middle men also gets a min profit margin. ")

image2 = Image.open(r"pages\assets\img2.jpeg")
st.image(image2,width=400)

st.markdown("- The other middle men in the supply chain can also be reduced if the organization is able to handle the transportations in the places using hotspot networks where the smaller middle men can get the production in the nearby places which reduces the transportation costs and removes some more components of the middle men.")
st.markdown("- As the result, the farmers can be benefitted as they get a fair price and reduces other processing charges. The consumers are also benefitted as the increase in price is proportional to the number of middle men. As a whole, the supply chain is benefited to a significant extend.")