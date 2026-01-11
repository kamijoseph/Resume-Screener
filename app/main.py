
import streamlit as st
import pickle
import re
import nltk

nltk.download("punkt")
nltk.download("stopwords")

# loading artifacts
@st.cache_resource
def load_artifacts(base_path):

    # model
    with open(f"{base_path}/model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # encoder
    with open(f"{base_path}/encoder.pkl", "rb") as f:
        encoder = pickle.load(f)

    # vectorizer
    with open(f"{base_path}/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    return model, encoder, vectorizer

model, encoder, vectorizer = load_artifacts("app/../resources")

# title
def main():
    st.title("Resume Screener Web Application")
    st.write("Resume Screener Web Application is an NLP powered to screen a resume to show what field the resume belongs to")


if __name__ == "__main__":
    main()