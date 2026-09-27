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
python 1_thresh_binary.py
```

## 📊 Visual Outputs
When you run the code, three distinct windows will pop up:
1. **original**: The untouched colored input image.
2. **gray**: The image converted to a single-channel grayscale layout.
3. **binary**: A stark, high-contrast black-and-white output based on your thresholding limit.

*Note: Press any key on your keyboard while focusing on the windows to safely close them.*
