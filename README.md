# Resume Screener Web Application

An NLP-powered resume screening web application built with **Streamlit**.
The system processes uploaded resumes, cleans the text, vectorizes it, and predicts the most relevant job category using a pre-trained machine learning model.

---

## Overview

This application is designed to automate the initial resume screening process using classical Natural Language Processing techniques. It loads pre-trained artifacts (model, label encoder, and vectorizer) and exposes an interactive web interface for inference.

Core capabilities:

* Resume upload (`.txt` and `.pdf`)
* Text cleaning and normalization
* Vectorization using a saved NLP pipeline
* Classification into predefined job categories
* Lightweight, fast inference via Streamlit

---

## Project Structure

```
.
├── app/
│   └── main.py
├── resources/
│   ├── model.pkl
│   ├── encoder.pkl
|   ├── resume.csv
│   └── vectorizer.pkl
├── notebooks
|    └── main.ipynb
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## How It Works

1. **Artifact Loading**
   The application loads the trained model, label encoder, and vectorizer using cached resources for efficiency.

2. **Resume Ingestion**
   Users upload a resume file through the Streamlit UI. The app supports UTF-8 and Latin-1 decoding.

3. **Text Cleaning**
   The resume text is normalized by removing:

   * URLs, mentions, hashtags
   * Special characters and non-ASCII symbols
   * Extra whitespace

4. **Vectorization & Prediction**
   The cleaned text is transformed using the saved vectorizer and passed to the trained model.
   The predicted class index is mapped back to a human-readable label using the encoder.

---

## Installation

Create and activate your environment (example using conda):

```bash
conda create -n resume-screener python=3.10
conda activate resume-screener
```

Install dependencies :

```bash
pip install streamlit nltk scikit-learn
```

Download required NLTK resources (handled automatically on first run):

* `punkt`
* `stopwords`

---

## Running the Application

From the project root:

```bash
streamlit run app/main.py
```

Open the provided local URL in your browser, upload a resume, and click **Screen** to get a prediction.

---

## Dependencies

* Python 3.9+
* Streamlit
* scikit-learn
* NLTK
* pickle (standard library)
* regex (standard library)

---

## Notes & Limitations

* The application performs **inference only**; training is not included in the Streamlit app.
* Model performance depends entirely on the quality and balance of the training data used to generate the `.pkl` artifacts.
* PDF files must be text-readable; scanned PDFs are not supported without OCR.
* This is a screening aid, not a decision-making system.

---

## Future Improvements

* Add OCR support for scanned PDFs
* Display prediction confidence scores
* Multi-label classification support
* Resume keyword highlighting
* Model versioning and monitoring

---

## License

This project is intended for educational and experimental use.
Add a license file if redistribution or commercial use is planned.

---