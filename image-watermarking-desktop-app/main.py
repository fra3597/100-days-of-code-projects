import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageDraw, ImageTk, ImageFont
import os

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

def drop(event):
    file_path = event.data
    add_watermark(file_path)

def add_watermark(file_path):
    original_image = Image.open(file_path)

    watermark_text = "Fra was here"
    watermark_font = ImageFont.load_default()
    draw = ImageDraw.Draw(original_image)
    text_height = draw.textlength(watermark_text, font=watermark_font)
    margin = 10
    position = (margin, original_image.height - text_height - margin)
    draw.text(position, watermark_text, font=watermark_font, fill=(0, 0, 0, 128))

    img_with_watermark = ImageTk.PhotoImage(original_image)

    original_image.save(file_path)

    canvas.delete(0, tk.END)
    canvas.insert(0, file_path)

    image_label.configure(image=img_with_watermark)
    image_label.image = img_with_watermark

app = TkinterDnD.Tk()
app.configure(bg="lightblue")

label = tk.Label(app, text="Drag and drop an image:")
label.pack(pady=10)

canvas = tk.Canvas(app, width=300, height=300)
image_path = f"{CURRENT_PATH}/images/drag_and_drop.png"
img = tk.PhotoImage(file=image_path)
canvas_width = 300
canvas_height = 300
width, height = img.width(), img.height()
x_scale = canvas_width / width
y_scale = canvas_height / height
scale_factor = min(x_scale, y_scale)
resized_image = img.subsample(int(scale_factor), int(scale_factor))
canvas.create_image(10, 10, anchor=tk.CENTER, image=resized_image)
canvas.pack()

canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', drop)

image_label = tk.Label(app)
image_label.pack(pady=10)

app.mainloop()
