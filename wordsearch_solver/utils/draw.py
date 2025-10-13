import cv2
import numpy as np
import os

def draw_words(img_path, found):
    img = cv2.imread(img_path)
    os.makedirs("output", exist_ok=True)

    if not found:
        print("\n⚠️ No words found — check OCR or spelling.")
        cv2.imwrite("output/solved.png", img)
        return

    h, w, _ = img.shape
    max_row = max(max(y for _, path in found for y, _ in path), 10)
    max_col = max(max(x for _, path in found for _, x in path), 10)
    cell_h, cell_w = h / max_row, w / max_col

    for word, path in found:
        color = tuple(np.random.randint(0, 255, 3).tolist())

        # Convert grid positions to pixel positions
        pixel_path = [(int(x * cell_w + cell_w / 2), int(y * cell_h + cell_h / 2)) for y, x in path]

        # Compute center of the word
        xs, ys = zip(*pixel_path)
        center = (int(np.mean(xs)), int(np.mean(ys)))

        # Compute axis lengths based on path spread
        axis_x = int((max(xs) - min(xs)) / 2 + cell_w * 0.4)
        axis_y = int((max(ys) - min(ys)) / 2 + cell_h * 0.4)

        # Draw a clean ellipse
        cv2.ellipse(img, center, (axis_x, axis_y), 0, 0, 360, color, 3)

    output_path = "output/solved.png"
    cv2.imwrite(output_path, img)
    print(f"✅ Saved output with clean oval highlights to {output_path}")
