import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns


DATA_FILE = "keystroke_data.csv"
MODEL_FILE = "keystroke_model.pkl"


# Load dataset
data = pd.read_csv(DATA_FILE)

print("\nDataset:")
print(data)

# Features
X = data[
    [
        "avg_dwell_time",
        "avg_flight_time",
        "typing_speed"
    ]
]

# Target
y = data["user"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train
model.fit(X_train, y_train)


# Prediction
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n------------------------------")
print("MODEL TRAINING RESULT")
print("------------------------------")

print(
    f"Accuracy: {accuracy * 100:.2f}%"
)


# Classification report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# Save model
joblib.dump(
    model,
    MODEL_FILE
)

print(
    f"\nModel saved as {MODEL_FILE}"
)


# Confusion matrix
cm = confusion_matrix(
    y_test,
    y_pred,
    labels=model.classes_
)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=model.classes_,
    yticklabels=model.classes_
)

plt.xlabel("Predicted User")
plt.ylabel("Actual User")
plt.title("Keystroke Recognition Confusion Matrix")

plt.tight_layout()
plt.show()