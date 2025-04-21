import os
from PIL import Image
import base64

icon_dir = os.path.dirname(__file__)
script_dir = os.path.dirname(icon_dir)
docs_dir = os.path.dirname(script_dir)
root_dir = os.path.dirname(docs_dir)
image_dir = os.path.join(docs_dir, "image")

# Path to the generated PNG icon from the previous step
src_path = os.path.join(icon_dir, "tkeasygui-org.png")
dest_path = os.path.join(icon_dir, "icon.ico")
png_path = os.path.join(image_dir, "icon64.png")
png256_path = os.path.join(image_dir, "icon256.png")
py_path = os.path.join(root_dir, "TkEasyGUI", "icon.py")

# Open the source image
img = Image.open(src_path)
# Save as ICO with the requested sizes
img.save(dest_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

# Resize to 256x256
img256 = img.resize((256, 256), Image.LANCZOS)
img256.save(png256_path, format="PNG")

# Resize to 64x64
img = img.resize((64, 64), Image.LANCZOS)
img.save(png_path, format="PNG")

# Read the ICO file and encode it to base64
with open(png_path, "rb") as ico_path:
    # Read the ICO file and encode it to base64
    # The result is a string that can be used in a data URI
    # Example: "data:image/x-icon;base64,BASE64_ENCODED_STRING"
    b64_string = base64.b64encode(ico_path.read()).decode("ascii")
    src = f"""
\"\"\"TkEasyGUI icon\"\"\"
ICON = b"{b64_string}"
"""
    with open(py_path, "w", encoding="utf-8") as fp:
        fp.write(src)
    print(src)
