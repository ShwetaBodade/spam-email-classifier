# spam-email-classifier
Machine Learning project to classify emails as spam or not spam
📌 Project Description

This project is a Spam Email Classification system built using Python and Machine Learning.
It classifies email/SMS messages as Spam or Ham (Not Spam) using text processing and a Naive Bayes model.

🧠 Machine Learning Approach

Text preprocessing (lowercasing, removing punctuation & stopwords)

Feature extraction using TF-IDF Vectorizer

Model training using Multinomial Naive Bayes

Model evaluation using accuracy, precision, recall, and F1-score

🛠️ Technologies Used

Python

Pandas

Scikit-learn

TF-IDF Vectorizer

Multinomial Naive Bayes

Jupyter Notebook

📊 Model Performance

Accuracy: ~96.86%

Precision (Spam): 1.00

Recall (Spam): 0.77

🚀 How to Run the Project

Clone the repository

Install dependencies

Run the Jupyter Notebook

pip install -r requirements.txt
jupyter notebook

📂 Project Structure
spam-email-classifier/
│
├── data/
│   └── spam.csv
├── eda.ipynb
├── README.md
└── requirements.txt

✨ Future Improvements

Improve recall for spam messages

Add a GUI using Streamlit

Try other ML models like Logistic Regression

👩‍💻 Author

Shweta Bodade