# PDF Page Splitter

A Python script to split PDFs where each page contains two side-by-side pages (like scanned books) into individual pages. This tool is particularly useful for:
- Converting scanned book PDFs into a more readable format
- Preparing PDFs for e-readers
- Processing academic papers or documents that were scanned two pages at a time

## Features

- Splits each PDF page into left and right halves
- Maintains original page quality
- Preserves page order (left page followed by right page)
- Command-line interface
- Progress tracking during processing
- Error handling and validation

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - PyPDF2
  - PyMuPDF (fitz)
  - Pillow (PIL)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pdf-splitter.git
cd pdf-splitter
```

2. Install the required packages:
```bash
pip install PyPDF2 PyMuPDF Pillow
```

## Usage

Basic usage:
```bash
python pdf_splitter.py input.pdf output.pdf
```

For files with spaces in their names:
```bash
python pdf_splitter.py "My Book.pdf" "My Book - Split.pdf"
```

Show help message:
```bash
python pdf_splitter.py -h
```

## Example

Input: A PDF where each page contains two pages of a book side by side
```
[Page 1 | Page 2]
[Page 3 | Page 4]
...
```

Output: A new PDF where each page is separate
```
[Page 1]
[Page 2]
[Page 3]
[Page 4]
...
```

## Error Handling

The script includes error handling for common issues:
- Non-existent input files
- Invalid file formats
- Processing errors
- File permission issues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PyPDF2](https://github.com/py-pdf/pypdf) for PDF processing
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) for PDF manipulation
- [Pillow](https://python-pillow.org/) for image processing

## Support

If you encounter any problems or have suggestions, please open an issue on GitHub.
