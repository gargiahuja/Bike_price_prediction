import streamlit as st
import pickle,joblib
st.set_page_config(
    page_title="project",
    page_icon= "🚲",
    layout="centered"
)
model=pickle.load(open("model.pkl",'rb'))
brand_dict = {
    'TVS': 0, 'Royal Enfield': 1, 'Triumph': 2, 'Yamaha': 3, 'Honda': 4,
    'Hero': 5, 'Bajaj': 6, 'Suzuki': 7, 'Benelli': 8, 'KTM': 9,
    'Mahindra': 10, 'Kawasaki': 11, 'Ducati': 12, 'Hyosung': 13,
    'Harley-Davidson': 14, 'Jawa': 15, 'BMW': 16, 'Indian': 17,
    'Rajdoot': 18, 'LML': 19, 'Yezdi': 20, 'MV': 21, 'Ideal': 22
}
owner_dict={"First Owner":0,
            "Second Owner":1,
            "Third Owner":2,
            "Fourth Owner":3}
def prediction(owner_code, brand_code, kms_driven_bike, age_bike, power_bike):
    input_data=[[owner_code,
                brand_code,
                kms_driven_bike,
                age_bike,
                power_bike]]
    return model.predict(input_data)[0]

st.title("Bike Price Prediction")
st.divider()
st.header("Welcome to the Bike Price Prediction Tool!")
st.write("This website helps you estimate the value of your used bike based on various factors.")
with st.form(key="bike_info_form"):
    selected_brand = st.selectbox(
        "Choose Bike Brand",
        options=list(brand_dict.keys()),
        help="Select the brand of the used bike from the dropdown"
    )
    brand_code = brand_dict[selected_brand] 
    selected_owner = st.selectbox(
        "Choose Owner",
        options=list(owner_dict.keys()),
        help="Select the owner of the used bike from the dropdown"
    )
    owner_code=owner_dict[selected_owner]
    age_bike=st.number_input("Age")
    power_bike=st.number_input("Power")
    kms_driven_bike=st.number_input("kms_driven")
    predictionn=st.form_submit_button("Predict Price")
    if predictionn:
        price = prediction(owner_code, brand_code, kms_driven_bike, age_bike, power_bike)
        st.success(f"Estimated Bike Price: ₹ {price:.2f}")