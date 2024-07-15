import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import qrcode 

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)

def on_generate():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data to generate the QR code.")
        return 
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        generate_qr(data, file_path)
        messagebox.showinfo("Success", f"QR code saved as {file_path}")

root = tk.Tk()
root.title("QR Code Generator")

label = tk.Label(root, text="Enter data:")
label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

button = tk.Button(root, text="Generate QR Code", command=on_generate)
button.pack(padx=10, pady=20)

root.mainloop()
