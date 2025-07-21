from PIL import Image, ImageDraw, ImageFont
import sys
import textwrap

# Constants
GRID_SIZE = int(sys.argv[2])
WIDTH, HEIGHT = 32*GRID_SIZE, 32*GRID_SIZE
FONT_SIZE = 20
LINE_SPACING = 2  # extra pixels between lines
FONT_PATH = "/System/Library/Fonts/Menlo.ttc"  # macOS monospaced font

def get_text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt")
        return

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        text = f.read()

    img = Image.new("L", (WIDTH, HEIGHT), color=255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    char_width, char_height = get_text_size(draw, "A", font)
    max_chars = WIDTH // char_width
    line_height = char_height + LINE_SPACING

    y = LINE_SPACING  # top padding
    for paragraph in text.splitlines():
        wrapped = textwrap.wrap(paragraph, width=max_chars)
        for line in wrapped:
            if y + line_height > HEIGHT:
                break
            draw.text((0, y), line, fill=0, font=font)
            y += line_height
        y += line_height // 2  # extra space after paragraphs

    img.save("output1.png")
    img.save("output2.png")
    print(f"Saved as output1.png and output2.png as {32*GRID_SIZE}x{32*GRID_SIZE} px ({GRID_SIZE*GRID_SIZE} tokens)")

if __name__ == "__main__":
    main()