# import fitz  # PyMuPDF
# import sys
# import json

# def highlight_text(pdf_path, output_path, highlights):
#     doc = fitz.open(pdf_path)
#     highlight_data = []  # Store highlight areas with text

#     for page_num, text_list in highlights.items():
#         page = doc[int(page_num)]
#         for text in text_list:
#             areas = page.search_for(text)
#             area_coords = []  # Store coordinates for each text

#             # print(areas)
#             for area in areas:
#                 page.add_highlight_annot(area)
#                 area_coords.append({
#                     "x0": area.x0, "y0": area.y0,  # Top-left corner
#                     "x1": area.x1, "y1": area.y1   # Bottom-right corner
#                 })
            
#             highlight_data.append({
#                 "page": int(page_num),
#                 "text": text,
#                 "areas": area_coords
#             })
#     doc.save(output_path)
#     print(json.dumps({"status": "success", "message": "PDF highlighted successfully",  "highlights": highlight_data}))

# if __name__ == "__main__":
#     data = json.loads(sys.stdin.read())
#     pdf_path = data["pdf_path"]
#     output_path = data["output_path"]
#     highlights = data["highlights"]
#     highlight_text(pdf_path, output_path, highlights)


# import fitz  # PyMuPDF
# import pytesseract
# from pdf2image import convert_from_path
# import json
# import sys
# import numpy as np

# def extract_text_with_coordinates(image):
#     """Extract text and coordinates using pytesseract."""
#     data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
#     text_data = []

#     for i in range(len(data["text"])):
#         if data["text"][i].strip():  # Ignore empty text
#             text_data.append({
#                 "text": data["text"][i],
#                 "x": data["left"][i],
#                 "y": data["top"][i],
#                 "w": data["width"][i],
#                 "h": data["height"][i]
#             })
#     return text_data

# def highlight_text(pdf_path, output_path, highlights):
#     doc = fitz.open(pdf_path)
#     images = convert_from_path(pdf_path, dpi=300)  # Convert PDF pages to high-resolution images

#     highlight_data = []  # Store highlight areas with text

#     for page_num, text_list in highlights.items():
#         page_idx = int(page_num)
#         page = doc[page_idx]
#         image = images[page_idx]

#         img_width, img_height = image.size  # Get image dimensions
#         pdf_width, pdf_height = page.rect.width, page.rect.height  # Get PDF page dimensions

#         # Get OCR extracted text and coordinates
#         text_data = extract_text_with_coordinates(image)

#         for text in text_list:
#             for entry in text_data:
#                 if text.lower() in entry["text"].lower():  # Match text

#                     # Convert OCR coordinates to PDF coordinates
#                     x0 = (entry["x"] / img_width) * pdf_width
#                     y0 = (entry["y"] / img_height) * pdf_height
#                     x1 = ((entry["x"] + entry["w"]) / img_width) * pdf_width
#                     y1 = ((entry["y"] + entry["h"]) / img_height) * pdf_height
#                     w = (entry['w'])
#                     h = (entry['h'])

#                     rect = fitz.Rect(x0, y0, x1, y1)
#                     page.add_highlight_annot(rect)

#                     highlight_data.append({
#                         "page": page_idx,
#                         "text": text,
#                         "areas": [{"x0": x0, "y0": y0, "x1": x1, "y1": y1, "w": w, "h": h}]
#                     })

#     doc.save(output_path)
#     print(json.dumps({"status": "success", "message": "PDF highlighted successfully", "highlights": highlight_data}))

# if __name__ == "__main__":
#     data = json.loads(sys.stdin.read())
#     pdf_path = data["pdf_path"]
#     output_path = data["output_path"]
#     highlights = data["highlights"]
#     highlight_text(pdf_path, output_path, highlights)






import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
import json
import sys
import re

def extract_text_with_coordinates(image):
    """Extract text and coordinates using pytesseract."""
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    text_data = []

    for i in range(len(data["text"])):
        if data["text"][i].strip():  # Ignore empty text
            text_data.append({
                "text": data["text"][i],
                "x": data["left"][i],
                "y": data["top"][i],
                "w": data["width"][i],
                "h": data["height"][i]
            })
    return text_data

def highlight_text(pdf_path, output_path, highlights):
    doc = fitz.open(pdf_path)
    images = convert_from_path(pdf_path, dpi=300)  # Convert PDF pages to high-resolution images

    highlight_data = []  # Store highlight areas with text

    for page_num, text_list in highlights.items():
        page_idx = int(page_num)
        page = doc[page_idx]
        image = images[page_idx]

        img_width, img_height = image.size  # Get image dimensions
        pdf_width, pdf_height = page.rect.width, page.rect.height  # Get PDF page dimensions

        # Get OCR extracted text and coordinates
        text_data = extract_text_with_coordinates(image)

        for text in text_list:
            for entry in text_data:
                word_pattern = r"\b" + re.escape(text) + r"\b"  # Ensure exact match

                if re.search(word_pattern, entry["text"], re.IGNORECASE):  # Match full word only
                    # Convert OCR coordinates to PDF coordinates
                    x0 = (entry["x"] / img_width) * pdf_width
                    y0 = (entry["y"] / img_height) * pdf_height
                    x1 = ((entry["x"] + entry["w"]) / img_width) * pdf_width
                    y1 = ((entry["y"] + entry["h"]) / img_height) * pdf_height
                    w = entry['w']
                    h = entry['h']

                    rect = fitz.Rect(x0, y0, x1, y1)
                    page.add_highlight_annot(rect)

                    highlight_data.append({
                        "page": page_idx,
                        "text": text,
                        "areas": [{"x0": x0, "y0": y0, "x1": x1, "y1": y1, "w": w, "h": h}]
                    })

    doc.save(output_path)
    print(json.dumps({"status": "success", "message": "PDF highlighted successfully", "highlights": highlight_data}))

if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    pdf_path = data["pdf_path"]
    output_path = data["output_path"]
    highlights = data["highlights"]
    highlight_text(pdf_path, output_path, highlights)
