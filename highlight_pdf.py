import fitz  # PyMuPDF
import sys
import json

def highlight_text(pdf_path, output_path, highlights):
    doc = fitz.open(pdf_path)
    for page_num, text_list in highlights.items():
        page = doc[int(page_num)]
        for text in text_list:
            areas = page.search_for(text)
            # print(areas)
            for area in areas:
                page.add_highlight_annot(area)
    doc.save(output_path)
    print(json.dumps({"status": "success", "message": "PDF highlighted successfully"}))

if __name__ == "__main__":
    data = json.loads(sys.stdin.read())
    pdf_path = data["pdf_path"]
    output_path = data["output_path"]
    highlights = data["highlights"]
    highlight_text(pdf_path, output_path, highlights)
