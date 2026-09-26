

## Deployment Guide

### Local Deployment

#### Project Setup

Navigate to the project folder.

```bash
cd Keystroke_Recognition_Using_Machine_Learning
```

Create a Python virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

Install the required dependencies.

```bash
pip install pandas scikit-learn numpy matplotlib
```

#### Run the Application

Run the main Python file.

```bash
python main.py
```

The application will open the **Keystroke Recognition** interface.

---

### Dataset and Model Deployment

The keystroke dataset is collected from users by recording their typing behaviour. The system extracts features such as **dwell time and flight time** from the collected data.

The extracted data is used to train the **Random Forest machine learning model**. After training, the model is saved and loaded by the application for recognizing users.

```text
User Typing
     ↓
Keystroke Data Collection
     ↓
Feature Extraction
     ↓
Trained Random Forest Model
     ↓
User Prediction
     ↓
Recognition Result
```

---

### Application Deployment

The application can be deployed on a Windows computer or laptop with Python installed. The user opens the application, enters the required text, and the system records the typing pattern.

The collected keystroke features are processed and passed to the trained machine learning model. The predicted user identity is then displayed on the application interface.

---

### Executable Deployment

For easier deployment, the Python project can be converted into a Windows executable using **PyInstaller**.

Install PyInstaller:

```bash
pip install pyinstaller
```

Create the executable:

```bash
pyinstaller --onefile --windowed main.py
```

The executable will be generated inside the:

```text
dist
```

folder.

The generated `.exe` file can then be used to run the project without opening the Python development environment.

---

### Deployment Requirements

```text
Python 3.x
Pandas
NumPy
Scikit-learn
Tkinter
PyInstaller
Windows OS
```

---

### Deployment Checklist

* Python installed
* Required Python libraries installed
* Keystroke dataset prepared
* Dwell-time and flight-time features extracted
* Random Forest model trained
* Trained model saved
* Main application configured
* Application tested
* Executable generated using PyInstaller
* Final project successfully deployed
