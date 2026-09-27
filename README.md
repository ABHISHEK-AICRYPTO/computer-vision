# 👁️ Computer Vision Portfolio

Welcome to my OpenCV projects! Click on any topic below to jump directly to its documentation:

- [1. Basic Fixed Thresholding](#1-basic-fixed-thresholding)
- [2. Otsu's Automatic Thresholding](#2-otsus-automatic-thresholding)



---

## 1. Basic Fixed Thresholding
### File: `1_thresh_binary.py`
# 🌸 Iris Flower Classification using Bagging Ensemble Method

This project demonstrates the implementation of an **Ensemble Learning** technique using Scikit-Learn. It utilizes a **Bagging Classifier** with a **Decision Tree** as the base estimator to classify the famous Iris flower dataset.
- [1. Basic Fixed Thresholding](./1_thresh_binary.py)
## 🚀 Features
- Uses the classic **Iris Dataset** (150 samples, 4 features, 3 classes).
- Implements **Bagging (Bootstrap Aggregating)** to reduce variance and prevent overfitting.
- Evaluates model performance using **Accuracy Score** on both training and testing subsets.
- Maps numerical predictions back to actual biological class names (`setosa`, `versicolor`, `virginica`).

## 📊 Model Performance
The model achieves perfect classification scores due to the clean boundary separations of the Iris dataset:
- **Training Accuracy:** 100% (`1.0`)
- **Testing Accuracy:** 100% (`1.0`)

## 🛠️ Prerequisites
To run this machine learning script or Jupyter notebook, you need Python installed along with the **scikit-learn** library. You can install it via pip:

```bash
pip install scikit-learn
```

## 💻 Code Overview & Implementation
The core script splits the dataset into an 80/20 train-test ratio and fits 10 ensemble Decision Trees:

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load and split dataset
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Initialize Bagging Classifier
base_classifier = DecisionTreeClassifier()
bagging_classifier = BaggingClassifier(base_classifier, n_estimators=10, random_state=42)

# Train the model
bagging_classifier.fit(X_train, y_train)

# Predictions
y_pred = bagging_classifier.predict(X_test)
```

## 🔍 Sample Prediction Output
When mapping the predicted target arrays to actual species names, the model outputs:
`['versicolor', 'setosa', 'virginica', 'versicolor', ...]`

---

## 2. Otsu's Automatic Thresholding
### File: `2_otsu_binary.py`
# 🧤 Otsu's Automatic Image Thresholding

This project implements **Otsu's Binarization** method using **OpenCV** in Python. Unlike standard thresholding where you have to manually guess a threshold value, Otsu's algorithm automatically calculates the optimal threshold limit from the image's pixel histogram.
- [2. Otsu's Automatic Thresholding](./2_otsu_binary.py)
## 🚀 Features
- Converts a standard colored image into **Grayscale**.
- Automatically determines the ideal threshold value using `cv2.THRESH_OTSU`.
- Highly effective for bimodal images (images with clear background and foreground separation, such as text documents or hand outlines).
- Prints the automatically calculated Otsu threshold value directly in the console.

## 🛠️ Prerequisites
Make sure you have Python installed along with the **OpenCV** library:

```bash
pip install opencv-python
```

## 💻 Code Overview
The script automatically reads the image locally and applies the dual flags (`cv2.THRESH_BINARY + cv2.THRESH_OTSU`):

```python
import cv2

# Load image and convert to grayscale
img = cv2.imread("hands.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu's automatic thresholding
thresh_val, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(f"Otsu's calculated threshold: {thresh_val}")
```

## 📊 Visual Windows
When executed, the program renders two real-time visual outputs:
1. **original**: The raw, untouched input image.
2. **Otsu's_binary**: The cleanly separated high-contrast black-and-white output.

*Note: Focus on any of the active output windows and press any key to close them safely.*
