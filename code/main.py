import cv2
import pytesseract

# Load image
image = cv2.imread('sample.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# OCR
text = pytesseract.image_to_string(thresh)

print("Extracted Text:")
print(text)
