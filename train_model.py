import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("ai_impact_student_performance_dataset.csv")

print("Dataset Shape:", df.shape)
print("Columns:", df.columns)

# -----------------------------
# DROP UNNECESSARY COLUMNS
# -----------------------------
df = df.drop(["student_id", "final_score", "performance_category"], axis=1)

# -----------------------------
# HANDLE MISSING VALUES
# -----------------------------
df = df.dropna()

# -----------------------------
# SELECT ONLY REQUIRED FEATURES
# -----------------------------
features = [
    "study_hours_per_day",
    "attendance_percentage",
    "last_exam_score",
    "assignment_scores_avg",
    "sleep_hours"
]

X = df[features]
y = df["passed"]

# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# FEATURE SCALING
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# MODEL
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# -----------------------------
# EVALUATION
# -----------------------------
y_pred = model.predict(X_test_scaled)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -----------------------------
# SAVE MODEL
# -----------------------------
os.makedirs("model", exist_ok=True)

with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("\nModel and scaler saved successfully!")