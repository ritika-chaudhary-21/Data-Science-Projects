import pickle
import streamlit as st

# Load the model
model = pickle.load(open("house_price_model.pkl", "rb"))

# Define the Streamlit app function
def predict_price():
    st.title("House Price Prediction")

    # Get user input for the area, number of bedrooms, and age of the house
    area = st.number_input("Enter the area value:", min_value=0, step=1)
    bedrooms = st.number_input("Enter the number of bedrooms:", min_value=0, step=1)
    age = st.number_input("Enter the age of the house:", min_value=0, step=1)

    # Predict the price
    if st.button("Predict"):
        prediction = model.predict([[area, bedrooms, age]])
        st.write(f"Predicted price is: {prediction[0]}")

# Run the app
if __name__ == "__main__":
    predict_price()
