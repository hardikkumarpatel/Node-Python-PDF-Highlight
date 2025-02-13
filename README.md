# node-python-pdf-highlight

A simple Node.js and Python integration to highlight text in PDF files. The Node.js script executes a Python script (using PyMuPDF or Spire.PDF) to search for specific words and highlight them with customizable colors. Ideal for document processing and automated text markup workflows.

## 🚀 Features
- Highlight specific words or phrases in PDF files.
- Customizable highlight colors (RGB format).
- Supports both PyMuPDF and Spire.PDF for PDF processing.
- Cross-platform compatibility (macOS, Linux, Windows).

## 🛠️ Requirements
- Node.js (v16 or higher)
- Python 3.9 or higher
- PyMuPDF (`pip install pymupdf`)
- Spire.PDF (`pip install spire.pdf`)

## 📂 Project Structure
```
📂 node-python-pdf-highlight
├── highlightPdf.js            # Node.js script to execute Python script
├── highlight_pdf.py           # Python script using PyMuPDF
├── highlight_pdf_spire.py     # Python script using Spire.PDF
└── README.md
```

## 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/node-python-pdf-highlight.git
   cd node-python-pdf-highlight
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Install Python dependencies:
   ```bash
   pip install pymupdf spire.pdf
   ```

## 🚀 Usage
### 1️⃣ Using PyMuPDF:
```javascript
const { highlightPdf } = require('./highlightPdf');

const highlights = {
  "0": ["example", "highlight"],
  "1": ["important"]
};

highlightPdf('input.pdf', 'output.pdf', highlights, [1, 1, 0])
  .then(response => console.log(response))
  .catch(error => console.error(error));
```

### 2️⃣ Using Spire.PDF:
```javascript
const { highlightPdf } = require('./highlightPdfSpire');

const highlights = {
  "0": ["example", "highlight"],
  "1": ["important"]
};

highlightPdf('input.pdf', 'output.pdf', highlights, [0, 1, 0])
  .then(response => console.log(response))
  .catch(error => console.error(error));
```

## 🎨 Color Format
- Use RGB values in the range `[0, 1]`.
  - Red: `[1, 0, 0]`
  - Green: `[0, 1, 0]`
  - Blue: `[0, 0, 1]`
  - Yellow: `[1, 1, 0]` (default)

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
This project is licensed under the MIT License.

---
**Author:** Your Name  
**GitHub:** [yourusername](https://github.com/yourusername)

