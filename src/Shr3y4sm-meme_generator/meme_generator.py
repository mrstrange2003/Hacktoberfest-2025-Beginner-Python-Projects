import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os

class MemeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Meme Generator")
        self.root.geometry("600x400")
        
        # Variables
        self.image_path = None
        self.top_text = tk.StringVar()
        self.bottom_text = tk.StringVar()
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Image selection button
        select_btn = tk.Button(self.root, text="Select Image", command=self.select_image)
        select_btn.pack(pady=10)
        
        # Top text entry
        tk.Label(self.root, text="Top Text:").pack(pady=5)
        top_entry = tk.Entry(self.root, textvariable=self.top_text, width=50)
        top_entry.pack()
        
        # Bottom text entry
        tk.Label(self.root, text="Bottom Text:").pack(pady=5)
        bottom_entry = tk.Entry(self.root, textvariable=self.bottom_text, width=50)
        bottom_entry.pack()
        
        # Generate button
        generate_btn = tk.Button(self.root, text="Generate Meme", command=self.generate_meme)
        generate_btn.pack(pady=20)
    
    def select_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
        )
        if self.image_path:
            messagebox.showinfo("Success", "Image selected successfully!")
    
    def generate_meme(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first!")
            return
        
        try:
            # Open the image
            img = Image.open(self.image_path)
            
            # Create a drawing object
            draw = ImageDraw.Draw(img)
            
            # Calculate font size based on image size
            font_size = int(img.width / 15)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                # Fallback to default font if arial is not available
                font = ImageFont.load_default()
            
            # Add top text
            if self.top_text.get():
                top_text = self.top_text.get().upper()
                text_width = draw.textlength(top_text, font=font)
                x = (img.width - text_width) / 2
                draw.text((x, 10), top_text, font=font, fill='white', stroke_width=2, stroke_fill='black')
            
            # Add bottom text
            if self.bottom_text.get():
                bottom_text = self.bottom_text.get().upper()
                text_width = draw.textlength(bottom_text, font=font)
                x = (img.width - text_width) / 2
                draw.text((x, img.height - font_size - 10), bottom_text, font=font, fill='white', stroke_width=2, stroke_fill='black')
            
            # Save the meme
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
            
            if save_path:
                img.save(save_path)
                messagebox.showinfo("Success", "Meme generated successfully!")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemeGenerator(root)
    root.mainloop()