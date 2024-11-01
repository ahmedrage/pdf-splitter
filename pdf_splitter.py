from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import io
import fitz  # PyMuPDF
import argparse
import sys
import os

def split_pdf_pages(input_path, output_path):
    """
    Split a PDF where each page contains two side-by-side pages into separate pages.
    
    Args:
        input_path (str): Path to input PDF file
        output_path (str): Path for output PDF file
    """
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)
        
    # Check if input file is a PDF
    if not input_path.lower().endswith('.pdf'):
        print(f"Error: Input file '{input_path}' is not a PDF.")
        sys.exit(1)
        
    try:
        # Open the PDF
        pdf_document = fitz.open(input_path)
        output = PdfWriter()
        
        # Show progress
        total_pages = pdf_document.page_count
        print(f"Processing {total_pages} pages...")
        
        for page_num in range(total_pages):
            # Get the page
            page = pdf_document[page_num]
            
            # Get page dimensions
            width = page.rect.width
            height = page.rect.height
            
            # Create crops for left and right sides
            left_rect = fitz.Rect(0, 0, width/2, height)
            right_rect = fitz.Rect(width/2, 0, width, height)
            
            # Crop and add each half
            for rect in [left_rect, right_rect]:
                # Get the cropped page as an image
                pix = page.get_pixmap(clip=rect)
                
                # Convert to PIL Image
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                
                # Convert PIL image to PDF page
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format='PDF')
                img_byte_arr.seek(0)
                
                # Add the new page to output PDF
                temp_reader = PdfReader(img_byte_arr)
                output.add_page(temp_reader.pages[0])
            
            # Show progress
            print(f"Processed page {page_num + 1}/{total_pages}")
        
        # Save the output PDF
        with open(output_path, 'wb') as output_file:
            output.write(output_file)
        
        pdf_document.close()
        print(f"\nSuccess! Split PDF saved as '{output_path}'")
        print(f"Original pages: {total_pages}")
        print(f"New pages: {total_pages * 2}")
        
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        sys.exit(1)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Split a PDF with two pages per sheet into individual pages.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python pdf_splitter.py input.pdf output.pdf
  python pdf_splitter.py "My Book.pdf" "My Book - Split.pdf"
        """
    )
    
    parser.add_argument('input_file', help='Input PDF file')
    parser.add_argument('output_file', help='Output PDF file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the splitter
    split_pdf_pages(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
