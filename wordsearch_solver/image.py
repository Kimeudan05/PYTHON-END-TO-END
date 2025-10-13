from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Define the grid manually based on the image you uploaded
grid = [
    "TALENTHARDSHIP",
    "DLSTEWARDSHIPO",
    "AOEHEXAMISHIPO",
    "LEADERCERCHIAS",
    "CDDIYETSAHAYEY",
    "AAIKAMUNUOONES",
    "SNFSECTNTBSOSD",
    "UFORGIVENESSDO",
    "MFDBZNKTMBUSTA",
    "SELECTAUTOSOYR",
    "SELECTBAYDEADR",
    "BABYQUIETEUEEC",
    "CREATIONEPVFIN",
    "TEMPTATIONPDFF",
    "RESPONSIBILITY",
    "EXEMPTEMPTATION",
    "EXAMTEMPTATION",
    "RESPONSIBILITY"
]

# Image settings
cell_size = 60
rows = len(grid)
cols = len(grid[0])
img_width = cols * cell_size
img_height = rows * cell_size
bg_color = "white"
text_color = "black"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Change if needed

# Create image
image = Image.new("RGB", (img_width, img_height), color=bg_color)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, size=int(cell_size * 0.6))

# Draw letters centered in each cell
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        w, h = draw.textsize(char, font=font)
        pos_x = x * cell_size + (cell_size - w) / 2
        pos_y = y * cell_size + (cell_size - h) / 2 - 4  # Adjust if needed
        draw.text((pos_x, pos_y), char, fill=text_color, font=font)

# Save or display
image.save("clean_wordsearch.png")
image.show()  # Optional

