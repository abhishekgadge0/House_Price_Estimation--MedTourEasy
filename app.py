import streamlit as st
import joblib
import numpy as np
import base64

# Load the model
model = joblib.load("stacked_model_pipeline.pkl")

# Function to encode the image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encode the local image
img_base64 = get_base64_of_bin_file('home.jpg')

# Custom CSS styling with the local background image and overlay
background_image_style = f"""
    <style>
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), 
                        url("data:image/png;base64,{img_base64}");
            background-size: cover;
        }}
        .content {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
        }}
        .title {{
            font-size: 48px;
            font-weight: bold;
            color: #2E2E2E;
            text-align: center;
        }}
        .subtitle {{
            font-size: 24px;
            text-align: center;
            margin-bottom: 50px;
            color: #4B4B4B;
        }}
        .divider {{
            border-top: 2px solid #bbb;
            margin: 20px 0;
        }}
        .input-label {{
            font-size: 18px;
            margin-bottom: 5px;
            color: #4B4B4B;
        }}
        .prediction {{
            font-size: 24px;
            color: #FF6347;
            font-weight: bold;
            text-align: center;
        }}
        .footer {{
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #4B4B4B;
        }}
    </style>
"""

# Apply the custom CSS
st.markdown(background_image_style, unsafe_allow_html=True)

# App content within a div with the class "content"
st.markdown('<div class="content">', unsafe_allow_html=True)

# App title and description
st.markdown('<div class="title">House Price Estimator App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">This is Abhishek\'s House Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Input fields organized in columns
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-label">Number of Bedrooms</div>', unsafe_allow_html=True)
    number_of_bedrooms = st.number_input("", min_value=0, value=0, key='bedrooms')
    
    st.markdown('<div class="input-label">Living Area (sq ft)</div>', unsafe_allow_html=True)
    living_area = st.number_input("", min_value=1000, value=1000, key='livingarea')
    
    st.markdown('<div class="input-label">Lot Area (sq ft)</div>', unsafe_allow_html=True)
    lot_area = st.number_input("", min_value=2000, value=2000, key='lotarea')

with col2:
    st.markdown('<div class="input-label">Number of Bathrooms</div>', unsafe_allow_html=True)
    number_of_bathrooms = st.number_input("", min_value=0, value=0, key='bathrooms')
    
    st.markdown('<div class="input-label">Number of Floors</div>', unsafe_allow_html=True)
    number_of_floors = st.number_input("", min_value=0, value=0, key='floors')
    
    st.markdown('<div class="input-label">Area of the House (excluding basement) (sq ft)</div>', unsafe_allow_html=True)
    area_excluding_basement = st.number_input("", min_value=1000, value=1000, key='area_excluding_basement')

st.markdown('<div class="input-label">Number of Schools Nearby</div>', unsafe_allow_html=True)
number_of_schools_nearby = st.number_input("", min_value=0, value=0, key='numberofschools')

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Prepare the input for the model
input_features = np.array([[number_of_bedrooms, number_of_bathrooms, living_area, lot_area, number_of_floors, area_excluding_basement, number_of_schools_nearby]])

# Predict button
if st.button("Estimate Price"):
    st.balloons()
    # Perform prediction
    prediction = model.predict(input_features)
    # Display the prediction
    st.markdown(f'<div class="prediction">Estimated Price: ${prediction[0]:,.2f}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Created by Abhishek</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close the content div
