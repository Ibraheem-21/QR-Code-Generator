# QR Code Generator

A simple QR code generator with a graphical user interface (GUI) built using Python and Tkinter. This application allows users to generate QR codes from any text input and save them as PNG files.

## Features

- Easy-to-use graphical user interface
- Generates QR codes from text input
- Saves QR codes as PNG images

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` library
- `tkinter` (comes pre-installed with Python)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/qr-code-generator.git
    cd qr-code-generator
    ```

2. Install the required libraries:
    ```sh
    pip install qrcode[pil] pillow
    ```

## Usage

1. Run the application:
    ```sh
    python qr_code_generator.py
    ```

2. Enter the data you want to convert to a QR code in the text entry field.

3. Click the "Generate QR Code" button.

4. Choose the location to save the generated QR code image.



root.mainloop()
