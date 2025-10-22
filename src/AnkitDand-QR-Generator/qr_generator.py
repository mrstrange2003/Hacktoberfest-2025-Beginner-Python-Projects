"""
Usage:
    python qr_generator.py -t "https://www.instagram.com"
"""

import argparse
import qrcode


def generate_qr(text: str, filename: str = "qrcode.png"):
    """Generate and save a QR code image for the given text."""
    qr = qrcode.QRCode(
        version=None,  # auto size
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code saved as '{filename}'")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a QR code from text or URL.")
    parser.add_argument("-t", "--text", required=True,
                        help="Text or URL to encode into the QR code.")
    parser.add_argument("-o", "--output", default="qrcode.png",
                        help="Output file name (default: qrcode.png)")
    args = parser.parse_args()

    generate_qr(args.text, args.output)


if __name__ == "__main__":
    main()
