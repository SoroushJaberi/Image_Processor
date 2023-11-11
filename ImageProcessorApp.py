import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

def open_image():
    """Open an image file and display it in the application."""
    global original_img, img

    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        h, w, _ = img.shape
        if h > w:
            scale_factor = canvas.winfo_height() / h
        else:
            scale_factor = canvas.winfo_width() / w
        img = cv2.resize(img, (int(w * scale_factor), int(h * scale_factor)))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        original_img = img.copy()
        display_image()


def display_image():
    """Display the current image in the Tkinter canvas."""
    global img, photo
    photo = ImageTk.PhotoImage(image=Image.fromarray(img))
    canvas.create_image(canvas.winfo_width() // 2, canvas.winfo_height() // 2,
                        image=photo, anchor='center')
    canvas.photo = photo


def clear_canvas():
    """Clear the canvas and display the original image."""
    global img
    img = original_img.copy()  # Reset to the original image
    display_image()


def grayscale():
    """Convert the image to grayscale and display it."""
    global img
    img = cv2.cvtColor(original_img.copy(), cv2.COLOR_RGB2GRAY)
    display_image()


def hist():
    """Display the histogram of the current image."""
    if img.ndim == 3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray_img = img
    hist_val = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
    plt.figure("Histogram")
    plt.plot(hist_val)
    plt.title('Histogram')
    plt.xlabel('Pixel value')
    plt.ylabel('Frequency')
    plt.show()


def hist_equalization():
    """Apply histogram equalization to the image and display the result."""
    global img
    img_gray = cv2.cvtColor(original_img.copy(), cv2.COLOR_RGB2GRAY)
    img_eq = cv2.equalizeHist(img_gray)
    img = img_eq
    display_image()


def edge_detection():
    """Detect edges in the image using a simple kernel and display the result."""
    global img
    img_gray = cv2.cvtColor(original_img.copy(), cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(img_gray, 100, 200)
    img = edges
    display_image()


root = tk.Tk()
root.title('Image Processing Tool by Soroush Jaberi')
root.config(bg="#37474F")

left_frame = tk.Frame(root, width=200, height=400, bg="#455A64")
left_frame.pack(side="left", fill="y", padx=5)

canvas = tk.Canvas(root, width=700, height=500, bg="white")
canvas.pack(pady=5, expand=True, fill="both")

# Buttons
image_button = tk.Button(left_frame, text="Open Image", command=open_image, bg="#546E7A", fg="white", width=20)
image_button.pack(pady=5)

clear_button = tk.Button(left_frame, text="Clear", command=clear_canvas, bg="#546E7A", fg="white", width=20)
clear_button.pack(pady=5)

grayscale_button = tk.Button(left_frame, text="Grayscale", command=grayscale, bg="#78909C", fg="white", width=20)
grayscale_button.pack(pady=5)

hist_button = tk.Button(left_frame, text="Histogram", command=hist, bg="#78909C", fg="white", width=20)
hist_button.pack(pady=5)

hist_eq_button = tk.Button(left_frame, text="Equalize Histogram", command=hist_equalization, bg="#78909C", fg="white", width=20)
hist_eq_button.pack(pady=5)

edge_button = tk.Button(left_frame, text="Edge Detection", command=edge_detection, bg="#78909C", fg="white", width=20)
edge_button.pack(pady=5)

root.mainloop()