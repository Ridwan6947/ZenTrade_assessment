import streamlit as st
import pandas as pd
import json
import requests

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"

try:
    response = requests.get(url)
    response.raise_for_status()

    # Save the JSON data to a file
    with open("assignment_data.json", "w") as file:
        file.write(response.text)

    print("Data downloaded successfully.")
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")

# Load data from the JSON file
with open("assignment_data.json", "r") as file:
    data = json.load(file)

# Extract the 'products' dictionary
products_data = data.get("products", {})

# Create a DataFrame from the product data
products_df = pd.DataFrame.from_dict(products_data, orient='index')

# Streamlit UI
st.title("Product Data Filter")

# Filter products by top category
top_category_options = ['All'] + list(products_df['subcategory'].unique())
selected_top_category = st.selectbox("Select Top Category", top_category_options)

# Filter products by subcategory (optional)
if selected_top_category != 'All':
    subcategories = ['All'] + list(products_df[products_df['subcategory'] == selected_top_category]['title'].unique())
    selected_subcategory = st.selectbox("Select Subcategory (Optional)", subcategories)
else:
    selected_subcategory = 'All'

# Apply filters
filtered_products = products_df.copy()
if selected_top_category != 'All':
    filtered_products = filtered_products[filtered_products['subcategory'] == selected_top_category]
if selected_subcategory != 'All':
    filtered_products = filtered_products[filtered_products['title'] == selected_subcategory]

# Sort by descending popularity
filtered_products = filtered_products.sort_values(by='popularity', ascending=False)

# Display handling options
all_columns = filtered_products.columns
display_options = st.multiselect('Select Fields to Display', all_columns)

# Display selected columns
st.table(filtered_products[display_options])
