from preprocess import preprocess_image
from ocr import extract_text

image_path = "../Dataset/sample.png"

processed_image = preprocess_image(
    image_path
)

text = extract_text(
    processed_image
)

print("\n===== EXTRACTED TEXT =====\n")
print(text)

with open(
    "../Output/extracted_text.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(text)

print("\nText saved successfully.")
