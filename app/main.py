
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

# resume cleaner
def clean_resume(text):
    cleaned_text = re.sub("http\S+\s", " ", text)
    cleaned_text = re.sub("RT|CC", " ", cleaned_text)
    cleaned_text = re.sub("@\S+", " ", cleaned_text)
    cleaned_text = re.sub("#\S+", " ", cleaned_text)
    cleaned_text = re.sub("[%s]" % re.escape("""|#$%&'()*+,-./:;<=>?@[\]^_'{|}~"""), " ", cleaned_text)
    cleaned_text = re.sub(r"[^\x00-\x7f]", " ", cleaned_text)
    cleaned_text = re.sub("\s+", " ", cleaned_text)
    return cleaned_text


# title
def main():
    st.title("**Resume Screener Web Application**")
    st.write(
        "NLP powered Resume Screener"
    )
    
    st.divider()

    resume = st.file_uploader("**Upload Resume:**", type=["txt", "pdf"])
    
    if resume and st.button("Screen"):

            # utf-8 and latin decoder
            try:
                resume_bytes = resume.read()
                resume_text = resume_bytes.decode("utf-8")
            except UnicodeDecodeError:
                resume_text = resume_bytes.decode("latin-1")
            
            # cleaniong and vectorizing resumes
            cleaned_resume = clean_resume(resume_text)
            vectorized_resume = vectorizer.transform([cleaned_resume])

            # predictions
            prediction_idx = model.predict(vectorized_resume)[0]
            st.write("message")



if __name__ == "__main__":
    main()