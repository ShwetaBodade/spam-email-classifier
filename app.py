import streamlit as st
import pickle
import re

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# App title
st.title("📧 Spam Email Classifier")

st.write("Enter an email or message below to check if it is Spam or Not Spam.")

# User input
user_input = st.text_area("Email / Message")

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Prediction
if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        cleaned = clean_text(user_input)
        text_vec = vectorizer.transform([cleaned])
        prediction = model.predict(text_vec)

        if prediction[0] == 1:
            st.error("🚨 This is a SPAM message")
        else:
            st.success("✅ This is NOT a spam message")
