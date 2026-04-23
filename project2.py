import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load CSV
df = pd.read_csv("student.csv")

# Convert Pass/Fail to 1/0
df['final_result'] = df['final_result'].map({'Fail': 0, 'Pass': 1})

X = df[['hours_studied', 'attendance', 'previous_marks', 'sleep_hours']]
y = df['final_result']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
prediction = model.predict([[6, 80, 60, 7]])
print("Prediction:", "Pass" if prediction[0] == 1 else "Fail")
