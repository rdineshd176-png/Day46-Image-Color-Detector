# 🎨 Image Color Detector

## 📘 Overview
**Day 46 of 100 Days of Code** — In this project, I built an **Image Color Detector** using Python.  
It extracts the **top 3 dominant colors** from any image and shows them visually along with their RGB values.  

This project helps in identifying the main color palette of an image — useful for designers, developers, and artists who want to analyze or recreate a color scheme.

---

## ⚙️ Requirements
Make sure you have Python installed, then install these libraries:
```bash
pip install opencv-python numpy matplotlib
🚀 How to Run
Save your image (e.g., download.png) inside the project folder.

Open your terminal in the project directory.

Run the script:

bash
Copy code
python generate.py
You’ll see:

The top 3 colors printed in the console with RGB values.

A color palette displayed using Matplotlib.

💻 Example Output
css
Copy code
🎨 Top Colors:
1. RGB(251, 204, 71) → 43.21%
2. RGB(125, 200, 255) → 36.89%
3. RGB(95, 142, 60) → 19.90%

🧠 How It Works

The image is resized to reduce pixel count.

Each pixel’s color is read and counted using collections.Counter.

The top 3 most frequent RGB colors are extracted and visualized.