# Development Guide

## Keystroke Recognition Using Machine Learning

### 1. Project Setup

Create the project folder and open it in VS Code.

```bash
mkdir Keystroke_Recognition_Using_Machine_Learning
cd Keystroke_Recognition_Using_Machine_Learning
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib
```

### 4. Development Process

```text
Data Collection
      ↓
Feature Extraction
      ↓
Dataset Preparation
      ↓
Random Forest Training
      ↓
Model Testing
      ↓
GUI Development
      ↓
System Integration
```

### 5. Main Features

* Collects keystroke data
* Calculates dwell time and flight time
* Creates the dataset
* Trains Random Forest model
* Predicts the user
* Displays the result through GUI

### 6. Run the Project

```bash
python main.py
```

### 7. Save Dependencies

```bash
pip freeze > requirements.txt
```

Install them later using:

```bash
pip install -r requirements.txt
```

### 8. GitHub Commands

```bash
git init
git add .
git commit -m "Initial project development"
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

### 9. Development Checklist

* [ ] Dataset prepared
* [ ] Features extracted
* [ ] Random Forest model trained
* [ ] GUI developed
* [ ] Model tested
* [ ] Application integrated
* [ ] Dependencies saved
* [ ] Project uploaded to GitHub
