import cv2
import sys
from utils.ocr import extract_grid
from solver import find_words
from utils.draw import draw_words

# usage: python main.py images/puzzle.png
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_image>")
        return

    img_path = sys.argv[1]
    print(f"📷 Reading puzzle from {img_path} ...")

    grid = extract_grid(img_path)
    print("\n🧩 Extracted Grid:")
    for row in grid:
        print(" ".join(row))

    # Define words to search for
    # words = ["CAT", "DOG", "APPLE", "BANANA"]
    words = [
    "HARDSHIP", "STEWARDSHIP", "LEADER", "EXAM", "FORGIVENESS", "SATAN", "OBEY", 
    "TEMPTATION", "RESPONSIBLE", "CREATION", "PRIDE", "GOD", "THANK", "BLAME", "END", 
    "HANDS", "PRAYER", "POSSESSIONS", "SUFFER", "CIRCUMSTANCES", "GUILTY", "HATE", 
    "CITIZENSHIP", "FAVOUR", "TIME", "FUTURE", "EXAM", "TALENT", "SUCCESS", "FALL", 
    "LOSE", "SIN", "FAME", "MOUTH", "LIFE", "LION", "SEED", "ADD", "AIR", "ALIVE", 
    "DEAD", "BABY", "EYE", "SEE", "O.I.C", "HONEST", "SEA", "GIVE", "BUS"
]

    print("\n🔍 Searching for words:", words)

    found = find_words(grid, words)

    # Draw on original image
    draw_words(img_path, found)

    print("\n✅ Done! Solved image saved to output/solved.png")

if __name__ == "__main__":
    main()
