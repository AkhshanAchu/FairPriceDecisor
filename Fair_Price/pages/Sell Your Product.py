import streamlit as st
import numpy as np
import pandas as pd


crop = st.selectbox(
    'Select the Crop',
    ('Ajwan', 'Alasande Gram', 'Alasande+Gram', 'Almond(Badam)',
     'Alsandikai', 'Amaranthus', 'Ambada+Seed', 'Amla(Nelli Kai)',
     'Amla(Nelli+Kai)', 'Amphophalus', 'Antawala', 'Anthorium', 'Apple',
     'Arecanut(Betelnut/Supari)', 'Arhar (Tur/Red Gram)(Whole)',
     'Arhar+Dal(Tur+Dal)', 'Ashgourd', 'Avare+Dal', 'Balekai', 'Bamboo',
     'Banana', 'Banana+-+Green', 'Barley+(Jau)', 'Beans', 'Beaten+Rice',
     'Beetroot', 'Betal+Leaves', 'Bitter+gourd', 'Black+pepper',
     'Bottle+gourd', 'Bran', 'Brinjal', 'Broken+Rice', 'Bull',
     'Bunch+Beans', 'Butter', 'Cabbage', 'Calf', 'Capsicum',
     'Cardamoms', 'Carrot', 'Cashewnuts', 'Castor+Seed', 'Cauliflower',
     'Chapparad+Avare', 'Chennangi+Dal', 'Cherry', 'Chikoos(Sapota)',
     'Chili+Red', 'Chilly+Capsicum', 'Chow+Chow',
     'Chrysanthemum(Loose)', 'Cloves', 'Cluster+beans', 'Coca', 'Cock',
     'Cocoa', 'Coconut', 'Coconut+Oil', 'Coconut+Seed', 'Coffee',
     'Colacasia', 'Copra', 'Coriander(Leaves)', 'Corriander+seed',
     'Cotton', 'Cotton+Seed', 'Cow', 'Cowpea(Veg)', 'Cucumbar(Kheera)',
     'Cummin+Seed(Jeera)', 'Dalda', 'Dhaincha', 'Drumstick',
     'Dry+Chillies', 'Dry+Fodder', 'Dry+Grapes', 'Duck', 'Duster+Beans',
     'Egg', 'Elephant+Yam+(Suran)', 'Field+Pea', 'Firewood', 'Fish',
     'Galgal(Lemon)', 'Garlic', 'Ghee', 'Gingelly+Oil', 'Ginger(Dry)',
     'Ginger(Green)', 'Goat', 'Gram+Raw(Chholia)', 'Gramflour',
     'Grapes', 'Green+Avare+(W)', 'Green+Chilli', 'Green+Fodder',
     'Green+Peas', 'Ground+Nut+Seed', 'Groundnut', 'Groundnut+(Split)',
     'Groundnut+pods+(raw)', 'Guar', 'Guava', 'Gur(Jaggery)', 'Gurellu',
     'He+Buffalo', 'Hen', 'Hippe+Seed', 'Honge+seed', 'Hybrid+Cumbu',
     'Indian+Beans+(Seam)', 'Indian+Colza(Sarson)',
     'Isabgul+(Psyllium)', 'Jack+Fruit', 'Jamun(Narale+Hannu)',
     'Jasmine', 'Jowar(Sorghum)', 'Jute', 'Karbuja(Musk+Melon)',
     'Kartali+(Kantola)', 'Khoya', 'Kinnow', 'Knool+Khol',
     'Kodo+Millet(Varagu)', 'Kulthi(Horse+Gram)', 'Lak(Teora)',
     'Leafy+Vegetable', 'Lemon', 'Lime', 'Linseed', 'Lint', 'Litchi',
     'Long+Melon(Kakri)', 'Lotus+Sticks', 'Lukad', 'Mace', 'Mahedi',
     'Mahua', 'Maida+Atta', 'Maize', 'Mango', 'Mango+(Raw-Ripe)',
     'Marigold(Calcutta)', 'Marigold(loose)', 'Mashrooms', 'Masur+Dal',
     'Mataki', 'Methi(Leaves)', 'Methi+Seeds', 'Millets',
     'Mint(Pudina)', 'Moath+Dal', 'Mousambi(Sweet+Lime)', 'Mustard',
     'Mustard+Oil', 'Myrobolan(Harad)', 'Neem+Seed',
     'Niger+Seed+(Ramtil)', 'Nutmeg', 'Onion', 'Onion+Green', 'Orange',
     'Other+Pulses', 'Ox', 'Paddy(Dhan)(Basmati)',
     'Paddy(Dhan)(Common)', 'Papaya', 'Papaya+(Raw)', 'Peach',
     'Pear(Marasebu)', 'Peas(Dry)', 'Peas+Wet', 'Peas+cod',
     'Pepper+garbled', 'Pepper+ungarbled', 'Persimon(Japani+Fal)',
     'Pigs', 'Pineapple', 'Plum', 'Pomegranate', 'Potato', 'Pumpkin',
     'Raddish', 'Ragi+(Finger+Millet)', 'Rajgir', 'Ram', 'Rice',
     'Ridge+gourd(Tori)', 'Ridgeguard(Tori)', 'Rose(Local)',
     'Rose(Loose)', 'Round+gourd', 'Rubber', 'Sabu+Dan', 'Sabu+Dana',
     'Safflower', 'Sajje', 'Same/Savi', 'Season+Leaves',
     'Seemebadnekai', 'Seetafal', 'Seetapal', 'She+Buffalo', 'She+Goat',
     'Sheep', 'Siddota', 'Snake+gourd', 'Snakeguard', 'Soanf', 'Soji',
     'Soyabean', 'Spinach', 'Sponge+gourd', 'Sugar', 'Sugarcane',
     'Sunflower', 'Sunhemp', 'Surat+Beans+(Papadi)', 'Suva+(Dill+Seed)',
     'Suvarna+Gadde', 'Sweet+Potato', 'Sweet+Pumpkin', 'T.V.+Cumbu',
     'Tamarind+Fruit', 'Tamarind+Seed', 'Tapioca', 'Taramira',
     'Tender+Coconut', 'Thogrikai', 'Thondekai', 'Tinda', 'Tobacco',
     'Tomato', 'Toria', 'Tube+Rose(Loose)', 'Turmeric',
     'Turmeric+(raw)', 'Turnip', 'Walnut', 'Water+Melon', 'Wheat',
     'Wheat+Atta', 'White+Peas', 'White+Pumpkin', 'Wood', 'Yam',
     'Yam+(Ratalu)'))


season = st.selectbox(
    'Select the Season',
    ('Pre-Monsoon', 'Monsoon', 'Post-Monsoon'))

output = st.number_input('Area Production')
ind_output = st.number_input('Individual Production')
quality = int(st.selectbox(
    'Select Quality',
    ('1', '2', '3', '4', '5')))
input = st.number_input('Cost of Cultivation')
demand = int(st.number_input('Demand in area(1-10)'))
area = st.number_input('Cultivation Area in Acres')

if st.button('Submit'):
    class Price:
        def __init__(self, season, crop, output, ind_output, quality, input, demand, area):
            self.season = season
            self.crop = crop
            self.mean = 0
            self.output = output
            self.ind_output = ind_output
            self.quality = quality
            self.input = input
            self.demand = demand
            self.area = area
            self.price = 0


        def extract(self):

            if self.season == "Pre-Monsoon":
                self.data = pd.read_csv(".\pages\dataset\pre.csv")
                self.mean = self.data[self.data["commodity_name"]
                                      == self.crop]["Predicted_price"].mean()

            if self.season == "Post-Monsoon":
                self.data = pd.read_csv(".\pages\dataset\post.csv")
                self.mean = self.data[self.data["commodity_name"]
                                      == self.crop]["Predicted_price"].mean()

            if self.season == "Monsoon":
                self.data = pd.read_csv(".\pages\dataset\mon.csv")
                self.mean = self.data[self.data["commodity_name"]
                                      == self.crop]["Predicted_price"].mean()

        def resultant_produce(self):
            self.quality = self.quality / 5
            mini = self.data[self.data["commodity_name"]
                             == self.crop]["min_price"].mean()

            self.price = self.mean - ((self.mean - mini)*(1-self.quality))

        def decider(self):

            boost = {"Pre-Monsoon": 2, "Monsoon": 10, "Post-Monsoon": 5}
            portion = (self.ind_output / self.output)

            price_market = (self.price * self.ind_output)
            need = (self.demand * self.price)
            adv_boost = (boost[self.season]*self.area)

            x = np.array([price_market, self.input, need, adv_boost])
            y = np.array([0.6, 0.1, portion, 0.05])

           
            final_output = round(x@y.T)
            st.subheader("You can collect Rs. " +
                         str(final_output) + " for your Yield!")

        def all(self):
            self.extract()
            self.resultant_produce()
            self.decider()

    G = Price(season, crop, output, ind_output, quality, input, demand, area)
    G.all()
