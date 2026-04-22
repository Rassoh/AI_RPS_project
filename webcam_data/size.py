from pathlib import Path
from PIL import Image

src = Path("webcam_data")          # change if needed
dst = Path("webcam_data_small")
dst.mkdir(exist_ok=True)

for class_dir in src.iterdir():
    if not class_dir.is_dir():
        continue
    out_dir = dst / class_dir.name
    out_dir.mkdir(exist_ok=True)

    for img_path in class_dir.iterdir():
        if img_path.suffix.lower() not in [".png", ".jpg", ".jpeg"]:
            continue

        img = Image.open(img_path).convert("RGB")
        img.thumbnail((800, 800))   # shrink max size
        out_path = out_dir / (img_path.stem + ".jpg")
        img.save(out_path, "JPEG", quality=75, optimize=True)

print("Done. Compressed images saved to:", dst)