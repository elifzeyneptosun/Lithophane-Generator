from PIL import Image
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_stl(height_map):
    rows, cols = height_map.shape
    vertices = []
    faces = []

    for i in range(rows - 1):
        for j in range(cols - 1):
            v0 = [i, j, height_map[i, j]]
            v1 = [i + 1, j, height_map[i + 1, j]]
            v2 = [i + 1, j + 1, height_map[i + 1, j + 1]]
            v3 = [i, j + 1, height_map[i, j + 1]]

            idx = len(vertices)
            vertices.extend([v0, v1, v2, v3])

            faces.append([idx, idx + 1, idx + 2])
            faces.append([idx, idx + 2, idx + 3])

    vertices = np.array(vertices)
    faces = np.array(faces)

    model = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            model.vectors[i][j] = vertices[f[j], :]

    return model

def main():
    root = tk.Tk()
    root.withdraw()

    img_path = filedialog.askopenfilename(
        title="Görüntü dosyasını seçin",
        filetypes=[
            ("PNG dosyaları", "*.png"),
            ("JPEG dosyaları", "*.jpg;*.jpeg"),
            ("Tüm dosyalar", "*.*")
        ]
    )

    if not img_path:
        messagebox.showerror("Hata", "Görsel seçilmedi.")
        return

    img = Image.open(img_path).convert("L")
    data = np.array(img)
    max_height = 10
    height_map = data / 255.0 * max_height

    plt.imshow(height_map, cmap='gray')
    plt.title("Yükseklik Haritası")
    plt.colorbar()
    plt.show()

    answer = messagebox.askyesno("STL Kaydet", "Bu yükseklik haritasına göre STL kaydedilsin mi?")
    if answer:
        model = generate_stl(height_map)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".stl",
            filetypes=[("STL files", "*.stl")],
            title="STL dosyasını kaydet"
        )

        if save_path:
            model.save(save_path)
            messagebox.showinfo("Başarılı", f"STL dosyası kaydedildi:\n{save_path}")
        else:
            messagebox.showwarning("İptal", "STL kaydedilmedi.")
    else:
        messagebox.showinfo("İptal", "STL oluşturma iptal edildi.")

if __name__ == "__main__":
    main()
