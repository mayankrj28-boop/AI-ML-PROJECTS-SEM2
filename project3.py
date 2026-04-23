# spam_detector.py

import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------------------
# LOAD DATASET
# ---------------------------
try:
    df = pd.read_csv("spam_final.csv", encoding='latin-1')
except:
    print("Error: spam.csv file not found!")
    exit()

# Keep only useful columns
df = df[['v1', 'v2']]
df.columns = ['label', 'text']

# ---------------------------
# PREPROCESSING
# ---------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# ---------------------------
# TRAIN TEST SPLIT
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------
# TRAIN MODEL
# ---------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# ---------------------------
# EVALUATION
# ---------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# ---------------------------
# GUI FUNCTION
# ---------------------------
def check_spam():
    msg = entry.get()

    if msg.strip() == "":
        messagebox.showwarning("Warning", "Please enter a message!")
        return

    msg_vec = vectorizer.transform([msg])
    result = model.predict(msg_vec)[0]

    if result == "spam":
        output_label.config(text="SPAM 🛑", fg="red")
    else:
        output_label.config(text="NOT SPAM ✅", fg="green")

# ---------------------------
# GUI SETUP
# ---------------------------
root = tk.Tk()
root.title("AI Spam Detector 📩")
root.geometry("400x300")
root.resizable(False, False)

title = tk.Label(root, text="Spam Message Detector", font=("Arial", 14, "bold"))
title.pack(pady=10)

label = tk.Label(root, text="Enter your message:")
label.pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Message", command=check_spam)
check_btn.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
output_label.pack(pady=10)

root.mainloop()
