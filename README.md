# 👁️ Computer Vision Portfolio

Welcome to my OpenCV projects! Click on any topic below to jump directly to its documentation:

- [1. Basic Fixed Thresholding](#1-basic-fixed-thresholding)
- [2. Otsu's Automatic Thresholding](#2-otsus-automatic-thresholding)
  

## 1. Basic Fixed Thresholding
### File: `1_thresh_binary.py`
# 👁️ Computer Vision - Image Thresholding using OpenCV

This is a beginner-friendly **Computer Vision** project that demonstrates how to load a colored image and convert it into Grayscale and Binary (Black & White) formats using **OpenCV** in Python.

## 🚀 Features
- Loads and processes local images.
- Converts colored BGR images to **Grayscale**.
- Applies **Binary Thresholding** (Threshold value: 127) to separate the foreground from the background.
- Displays all three versions (Original, Grayscale, and Binary) simultaneously in separate interactive windows.

## 🛠️ Prerequisites
Before running the script, make sure you have Python installed, and then install the **OpenCV** library using pip:

```bash
pip install opencv-python
```

## 💻 How to Run
1. Clone or download this repository to your local machine.
2. Open the script (`1_thresh_binary.py`) and update the image path (`C:\Users\Lenovo\...`) to point to an image on your computer.
3. Run the script via your terminal or command prompt:

```bash
python 1_thresh_binary.py.py
```

## 📊 Visual Outputs
When you run the code, three distinct windows will pop up:
1. **original**: The untouched colored input image.
2. **gray**: The image converted to a single-channel grayscale layout.
3. **binary**: A stark, high-contrast black-and-white output based on your thresholding limit.
4. #original image
<img width="670" height="350" alt="image" src="https://github.com/user-attachments/assets/32f6c757-ff5a-43ce-873b-96c969495bac" />
5.#output image
<img width="670" height="350" alt="image" src="https://github.com/user-attachments/assets/257c3147-9666-4798-9443-1e1b43195e78" />

*Note: Press any key on your keyboard while focusing on the windows to safely close them.*


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
3. original image
<img width="488" height="350" alt="image" src="https://github.com/user-attachments/assets/75d43fdc-7f56-4e75-8c4a-b58fbda256df" />

4.output image
<img width="488" height="350" alt="image" src="https://github.com/user-attachments/assets/09aa2c51-894b-46ad-b294-20b14e1bfd74" />


*Note: Focus on any of the active output windows and press any key to close them safely.*
