# **UPI Shield - A UPI Fraud Detection App**
### **An ML-Powered Web Application**

A Python-based application using the **Streamlit** framework to detect fraudulent Unified Payments Interface (**UPI**) transactions. The core of the app is a pre-trained **XGBoost classifier** that analyzes transaction data to predict potential fraud. This tool is designed for ease of use, allowing for both single-transaction analysis and bulk processing of data.

---

### **Key Features** 🚀

* **Fraud Prediction**: The app's main function is to predict if a transaction is fraudulent based on its features.
* **Flexible Input**: Users can test single transactions by manually entering data or upload a **CSV file** for batch predictions.
* **Downloadable Results**: After processing a CSV, users can download the results as a new CSV file that includes the fraud predictions.
* **Built for Simplicity**: The user interface is straightforward, with easy-to-use dropdowns and input fields.
* **One-Hot Encoding**: Categorical features within the transaction data are automatically one-hot encoded for model compatibility.

---

### **The Machine Learning Model** 🧠

* **Model**: **XGBoost Classifier**
* **Trained on**: The model was trained on key transaction details, including **`Amount`**, `Date` and `Time` (month/year), **`Transaction_Type`**, **`Payment_Gateway`**, **`Transaction_State`**, and **`Merchant_Category`**.
* **File**: The trained model is stored as a pickle file named **`UPI Fraud Detection Final.pkl`**.

---

### **Tech Stack** 🛠️

* **Python**: The primary programming language.
* **Streamlit**: For creating the interactive web interface.
* **Pandas & NumPy**: Used for data manipulation and numerical operations.
* **XGBoost**: The machine learning library for the classification model.
* **Base64**: Utilized for handling the CSV file download functionality.

---

### **Getting Started** ▶️

1.  **Clone the Repository**:
    ```bash
    git clone <repo-url>
    cd <project-folder>
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```
4.  **Access**: Open your web browser and go to `http://localhost:8501`.

---

### **File Structure** 📁

````

📦project-folder/
├── app.py                      # Main Streamlit app
├── UPI Fraud Detection Final.pkl # Trained ML model
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
````

---
### **Data Format** 📋

When uploading a CSV file, ensure it contains the following columns exactly as listed:

* `Date` (format: `DD-MM-YYYY`)
* `Amount`
* `Transaction_Type`
* `Payment_Gateway`
* `Transaction_State`
* `Merchant_Category`

The app will add a new column named `fraud` to the processed data, where a value of **`1`** indicates a **fraudulent** transaction and **`0`** indicates a **non-fraudulent** one.