# 🛡️ eKYC System

An end-to-end eKYC (Electronic Know Your Customer) system built with Python, DeepFace, OpenCV, and Streamlit to automate identity verification using face recognition and OCR.

## 🚀 Features

- 🔍 **Face Verification**: Uses DeepFace to compare user-submitted selfies with ID documents.
- 📄 **OCR Engine**: Extracts textual data from uploaded identity documents.
- 🗃️ **Database Integration**: Stores user data and verification results securely using MySQL.
- 🌐 **Web Interface**: Interactive front-end built with Streamlit for user onboarding and admin monitoring.
- ⚙️ **Modular Codebase**: Structured components for preprocessing, face verification, OCR, and DB operations.

## 🛠️ Tech Stack

- **Languages**: Python
- **Libraries**: DeepFace, OpenCV, Tesseract OCR
- **Backend**: MySQL
- **Web Framework**: Streamlit

├── app.py                      # Streamlit front-end
├── db_operations.py           # Custom DB handling
├── face_verification.py       # DeepFace face matching
├── ocr_engine.py              # OCR module
├── preprocess.py              # Image preprocessing
├── utils.py                   # Utility functions
├── config.yaml                # Configuration file
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation


<img src="asset/output.png" alt="Registration UI" width="800"/>



## 📁 Project Structure

```bash
├── app.py                      # Streamlit front-end
├── db_operations.py           # Custom DB handling
├── face_verification.py       # DeepFace face matching
├── ocr_engine.py              # OCR module
├── preprocess.py              # Image preprocessing
├── utils.py                   # Utility functions
├── config.yaml                # Configuration file
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation


![Registration UI](asset/output.png)

