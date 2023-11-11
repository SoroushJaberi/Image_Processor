# Image_Processor
Image_Processor is an intuitive GUI application for basic image processing, developed with Python and Tkinter and leveraging OpenCV for image manipulation and Matplotlib for displaying histograms. The application is designed with simplicity in mind, making it easy for users to perform common image processing tasks without requiring in-depth knowledge of the underlying libraries.

# Features
Open and dynamically scale images to fit within the application's canvas.
Convert color images to grayscale.
Display the histogram to analyze the intensity distribution of pixels.
Apply histogram equalization to improve image contrast.
Highlight edges within an image using edge detection.

# Getting Started
To use Image_Processor, follow the below instructions:

1. Launch the Application:
Execute the Python script to start the GUI.

2. Load an Image:
Use the "Open Image" button to load an image into the application.

3. Image Processing Options:
Grayscale: Click "Grayscale" to convert the image to grayscale.
Histogram: Click "Histogram" to plot and view the image's histogram.
Equalize Histogram: Click "Equalize Histogram" to perform histogram equalization on the image.
Edge Detection: Click "Edge Detection" to perform edge detection and view the results.

4. Reset the Image:
Click "Clear" to discard any changes and revert to the original image.

# Prerequisites
Ensure you have the following prerequisites installed:

.Python
.Tkinter
.OpenCV (cv2)
.Pillow (PIL)
.Matplotlib

# You can install the necessary Python libraries using pip:
pip install opencv-python
pip install Pillow
pip install matplotlib

(Tkinter typically comes bundled with Python. If for some reason it's not included in your installation, you may need to install it separately.)

# Installation
Clone this repository to get started:
git clone https://github.com/[Your_GitHub_Username]/Image_Processor.git

After cloning, navigate to the cloned directory and run the script:
python image_processor.py


# Contribute
Contributions to Image_Processor are welcome! You can contribute by submitting issues, providing fixes/improvements, or by suggesting new features.

# License
This project is made available under the MIT License.
