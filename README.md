# Resume Screening App

A simple and modern web-based application for automatic resume screening using machine learning. Upload a resume to get its predicted job category, with a clean and responsive UI.

## Features
- Upload resumes in PDF, DOCX, or TXT format
- Automatic extraction of resume text
- Predicts the job category using a trained ML model
- Responsive and modern design
- Easy-to-use web interface

## Technologies Used
- Python
- Streamlit
- scikit-learn
- pandas
- NumPy
- PyPDF2
- python-docx
- pickle

## How to Use
1. Install dependencies:
   ```powershell
   pip install -r requirements.txt

   Or manually:
   pip install streamlit scikit-learn python-docx PyPDF2 pandas numpy
2.(Optional) Train the model if not already present:
   python train_model.py
3.Start the app:
   streamlit run app.py
4.Upload a resume file and view the predicted job category.

Screenshot

https://github.com/user-attachments/assets/0eca52af-b98b-4d86-a885-e18efb1366c5


License
This project is for educational purposes. Feel free to modify and use it as you like.

