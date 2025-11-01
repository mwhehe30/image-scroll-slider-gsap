import os
from PIL import Image

# folder tempat script ini berada
current_folder = os.path.dirname(os.path.abspath(__file__))

# Ekstensi gambar yang didukung
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".heic", ".webp")

for root, dirs, files in os.walk(current_folder):
    for filename in files:
        if filename.lower().endswith(IMAGE_EXTENSIONS):
            img_path = os.path.join(root, filename)

            try:
                img = Image.open(img_path).convert("RGB")
            except Exception as e:
                print(f"❌ Gagal membuka {img_path}: {e}")
                continue

            new_filename = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(root, new_filename)

            # Simpan sebagai WebP Lossless
            try:
                img.save(output_path, "WEBP", quality=70, lossless=True)
                print(f"✅ Converted (lossless): {img_path} → {output_path}")

                # Hapus file asli jika beda nama (hindari delete diri sendiri)
                if img_path != output_path:
                    os.remove(img_path)
                    print(f"🗑️ Deleted original: {img_path}")

            except Exception as e:
                print(f"❌ Gagal convert {img_path}: {e}")

print("🎯 Semua gambar berhasil dipaksa menjadi WebP Lossless!")
