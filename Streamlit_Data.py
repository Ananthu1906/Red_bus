import streamlit as st
import pandas as pd

# Load the data
chandigarh_data = pd.read_csv("Chandigarh_Data.csv")
westbengal_data = pd.read_csv("WestBengal_Data.csv")
goa_data = pd.read_csv("Goa_Data.csv")
punjab_data = pd.read_csv("Punjab_Data.csv")
kaac_data = pd.read_csv("KAAC_Data.csv")
telangana_data = pd.read_csv("Telangana_Data.csv")  # Load Telangana data
bihar_data = pd.read_csv("Bihar_Data.csv")          # Load Bihar data
jammu_data = pd.read_csv("Jammu_Data.csv")          # Load Jammu data
kerala_data = pd.read_csv("Kerala_Data.csv")        # Load Kerala data
jodhpur_data = pd.read_csv("Jodhpur_Data.csv")

# Add a 'state' column to each DataFrame
chandigarh_data['state'] = 'Chandigarh'
westbengal_data['state'] = 'West Bengal'
goa_data['state'] = 'Goa'
punjab_data['state'] = 'Punjab'
kaac_data['state'] = 'KAAC'
telangana_data['state'] = 'Telangana'
bihar_data['state'] = 'Bihar'
jammu_data['state'] = 'Jammu'
kerala_data['state'] = 'Kerala'
jodhpur_data['state'] = 'Jodhpur'

# Combine the data into a single DataFrame and remove unnamed columns
all_data = pd.concat([chandigarh_data, westbengal_data, goa_data, punjab_data, kaac_data,telangana_data, bihar_data, jammu_data, kerala_data,jodhpur_data], ignore_index=True)
all_data = all_data.loc[:, ~all_data.columns.str.contains('^Unnamed')]

# Sidebar filters
st.sidebar.title('Filter Options')
state = st.sidebar.selectbox('Select State', all_data['state'].unique())
route = st.sidebar.selectbox('Select Route', all_data[all_data['state'] == state]['route_name'].unique())
bus_type = st.sidebar.selectbox('Select Bus Type', all_data[all_data['state'] == state]['bustype'].unique())
star_rating = st.sidebar.slider('Select Star Rating', 0, 5, (0, 5))
price_range = st.sidebar.slider('Select Price Range', int(all_data['price'].min()), int(all_data['price'].max()), (int(all_data['price'].min()), int(all_data['price'].max())))

# Filter data based on selections
filtered_data = all_data[
    (all_data['state'] == state) &
    (all_data['route_name'] == route) &
    (all_data['bustype'] == bus_type) &
    (all_data['star_rating'] >= star_rating[0]) &
    (all_data['star_rating'] <= star_rating[1]) &
    (all_data['price'] >= price_range[0]) &
    (all_data['price'] <= price_range[1])
]

# Display the filtered data
st.title('Bus Timings Data')
st.subheader('Filtered Bus Data')
st.dataframe(filtered_data)

# Display bus timings details
if not filtered_data.empty:
    st.subheader('Bus Timings')
    bus_name = filtered_data.iloc[0]['busname']
    departure_time = filtered_data.iloc[0]['departing_time']
    arrival_time = filtered_data.iloc[0]['reaching_time']
    price = filtered_data.iloc[0]['price']
    
    st.markdown(f"*Bus Name:* {bus_name}")
    st.markdown(f"*Departure Time:* {departure_time}")
    st.markdown(f"*Arrival Time:* {arrival_time}")
    st.markdown(f"*Price:* ₹{price}")
else:
    st.write("No data available for the selected filters.")
