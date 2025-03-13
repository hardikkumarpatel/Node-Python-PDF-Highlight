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
#                     "x1": area.x1, "y1": area.y1, # Bottom-right corner
#                 })
            
#             highlight_data.append({
#                 "page": int(page_num),
#                 "text": text,
#                 "areas": area_coords
#             })

#     doc.save(output_path)
#     print(json.dumps({"status": "success", "message": "PDF highlighted successfully",  "highlights": highlight_data }))

# if __name__ == "__main__":
#     data = json.loads(sys.stdin.read())
#     pdf_path = data["pdf_path"]
#     output_path = data["output_path"]
#     highlights = data["highlights"]
#     highlight_text(pdf_path, output_path, highlights)


import fitz  # PyMuPDF
import sys
import json

def highlight_text(pdf_path, output_path, search_texts):
    doc = fitz.open(pdf_path)
    highlight_data = []  # Store highlight areas with text

    for page_num in range(len(doc)):  # Iterate through all pages
        page = doc[page_num]
        for text in search_texts:
            areas = page.search_for(text)
            area_coords = []  # Store coordinates for each text occurrence

            if areas:  # If text is found on the page
                for area in areas:
                    page.add_highlight_annot(area)
                    area_coords.append({
                        "x0": area.x0, "y0": area.y0,
                        "x1": area.x1, "y1": area.y1,
                    })

                highlight_data.append({
                    "page": page_num,
                    "text": text,
                    "areas": area_coords
                })

    doc.save(output_path)
    print(json.dumps({"status": "success", "message": "PDF highlighted successfully", "highlights": highlight_data}))

if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    pdf_path = data["pdf_path"]
    output_path = data["output_path"]
    search_texts = data["highlights"]  # Now expecting a list of texts instead of a dict
    highlight_text(pdf_path, output_path, search_texts)
