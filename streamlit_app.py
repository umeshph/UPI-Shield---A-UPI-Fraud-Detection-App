import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import datetime
from datetime import datetime as dt
import base64
import pickle
from xgboost import XGBClassifier

# Load the XGBoost model
pickle_file_path = "UPI Fraud Detection Final.pkl"
loaded_model = pickle.load(open(pickle_file_path, 'rb'))

# Dropdown options
tt = ["Bill Payment", "Investment", "Other", "Purchase", "Refund", "Subscription"]
pg = ["Google Pay", "HDFC", "ICICI UPI", "IDFC UPI", "Other", "Paytm", "PhonePe", "Razor Pay"]
ts = ['Andhra pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
      'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 
      'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
mc = ['Donations and Devotion', 'Financial services and Taxes', 'Home delivery', 'Investment', 'More Services', 
      'Other', 'Purchases', 'Travel bookings', 'Utilities']

# Streamlit UI
st.title("UPI Shield - A UPI Transaction Fraud Detector")


tran_date = st.date_input("Select the date of your transaction", datetime.date.today())
selected_date = dt.combine(tran_date, dt.min.time())
month, year = selected_date.month, selected_date.year

tran_type = st.selectbox("Select transaction type", tt)
pmt_gateway = st.selectbox("Select payment gateway", pg)
tran_state = st.selectbox("Select transaction state", ts)
merch_cat = st.selectbox("Select merchant category", mc)
amt = st.number_input("Enter transaction amount", step=0.1)

st.write("OR upload a CSV file:")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV Preview:", df)

button_clicked = st.button("Check transaction(s)")

if button_clicked:
    with st.spinner("Checking transactions..."):
        def one_hot_encode(value, categories):
            """One-hot encodes a categorical value"""
            encoding = [1 if value == cat else 0 for cat in categories]
            return encoding

        if uploaded_file:
            df[['Month', 'Year']] = df['Date'].str.split('-', expand=True)[[1, 2]].astype(int)
            df.drop(columns=['Date'], inplace=True)
            
            feature_list = []
            for _, row in df.iterrows():
                features = [
                    row['Amount'], row['Year'], row['Month']
                ] + one_hot_encode(row['Transaction_Type'], tt) \
                  + one_hot_encode(row['Payment_Gateway'], pg) \
                  + one_hot_encode(row['Transaction_State'], ts) \
                  + one_hot_encode(row['Merchant_Category'], mc)

                feature_list.append(features)

            input_array = np.array(feature_list)
            predictions = loaded_model.predict(input_array)
            df['fraud'] = predictions

            st.success("Transactions checked!")
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download Output CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

        else:
            input_features = [
                amt, year, month
            ] + one_hot_encode(tran_type, tt) \
              + one_hot_encode(pmt_gateway, pg) \
              + one_hot_encode(tran_state, ts) \
              + one_hot_encode(merch_cat, mc)

            input_array = np.array([input_features])
            result = loaded_model.predict(input_array)[0]

            st.success("Transaction checked!")
            st.write("Fraudulent Transaction" if result else "Not a fraudulent transaction.")
