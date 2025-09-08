# 🧑‍⚕️ Obesity Classification Using Classic ML

## 📖 Overview
This project predicts **obesity categories** (Normal Weight, Obese, Overweight, Underweight) using a **Random Forest Classifier**.  
The model takes user inputs such as **Age, Gender, Height, Weight, and BMI** and provides a classification in real-time through an interactive **Streamlit web application**.  

---

## ✨ Features
- User-friendly **Streamlit interface** for entering health metrics.  
- **Automatic preprocessing** of categorical (Gender) and numerical features.  
- **Real-time predictions** of obesity class.  
- Lightweight design for easy deployment.  

---

## 🧠 Model Explanation
- **Algorithm**: Random Forest Classifier (an ensemble method combining multiple decision trees to improve accuracy and reduce overfitting).  
- **Input Features**: Age, Gender, Height, Weight, BMI.  
- **Preprocessing**:  
  - Gender encoded using LabelEncoder.  
  - BMI included as an important predictive feature.  
- **Model Storage**: The trained model is saved as `model.pkl` and loaded into the Streamlit app for inference.  

---

## 📊 Evaluation
The model was trained and evaluated in `Classic_ML.ipynb` with the following steps:
- Train-test split applied to ensure generalization.  
- Performance metrics (Accuracy, Precision, Recall, and F1-score) were computed.  
- The Random Forest model achieved **high accuracy** in classifying obesity categories, showing robustness compared to single decision trees.  

*(You can add exact metrics here once finalized.)*  

---

## 🚀 Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/obesity-classification.git
   cd obesity-classification
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the app:
   ```bash
   streamlit run App.py
   ```
4. Open your browser at **http://localhost:8501**.

---

## 📜 License
This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software with proper attribution.  
