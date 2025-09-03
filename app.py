import streamlit as st 
import joblib
import pandas as pd

st.set_page_config(
    page_title="BMW App",
    layout="wide"
)

st.header("BMW Features")

# load model
model = joblib.load("src/model/model.pkl")

# choose for catggorical 
model_types = ["5 Series","i8","X3","7 Series","M5","3 Series","X1","M3","X5","i3","X6"]
regions = ["Asia", "North America", "Middle East", "South America", "Europe", "Africa"]
fuel_types = ["Petrol", "Diesel", "Hybrid", "Electric"]
transmissions = ["Automatic", "Manual"]
colors = ["Black", "White", "Blue", "Red", "Grey"]


# Input form
with st.form("BMW Form"):

    st.subheader("Enter BMW Car :")

    # fields : 
    Model = st.selectbox("Model Type" , model_types)
    year = st.number_input("Year", min_value=2010, max_value=2024, step=1, value=2020)
    mileage = st.number_input("Mileage KM")
    engine_size = st.number_input("Engine Size (L)", min_value=1.5, max_value=6.0, step=0.1)
    price = st.number_input("Price USD",min_value=30000 )
    sales = st.number_input("Sales Volume" , min_value=100)
    fuel_type = st.selectbox("Fuel Type", fuel_types)
    region = st.selectbox("Region", regions)
    color = st.selectbox("Color",colors)
    transmission = st.selectbox("Transmission",transmissions)

    submitted = st.form_submit_button("Submit")

if submitted:
    all_columns = ['Model','Year','Region','Color','Fuel_Type','Transmission', 'Engine_Size_L', 'Mileage_KM' , 'Price_USD','Sales_Volume']

    # Put inputs into DataFrame
    input_data = pd.DataFrame([[Model,year , region , color , fuel_type , transmission , engine_size , mileage, price , sales]],
                              columns=all_columns)

    # Predict
    prediction = model.predict(input_data)[0]
    

    prediction_text = "Low" if prediction == 0 else "High"
    color = "#ff4b4b" if prediction == 0 else "#4caf50" # red for low, green for high

    st.markdown(
        f"""
        <div style="
            padding: 2.5rem; 
            border-radius: 20px; 
            background-color: #f7f9fc; 
            border: 2px solid #e0e4eb;
            text-align: center; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        ">
            <h2 style="
                color: #333; 
                margin-bottom: 0.5rem; 
                font-size: 1.5rem; 
                font-weight: 600;
            ">
                Predicted BMW Class:
            </h2>
            <span style="
                color: {color}; 
                font-weight: bold; 
                font-size: 3rem; 
                display: block; 
                line-height: 1;
            ">
                {prediction_text}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )