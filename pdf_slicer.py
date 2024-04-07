from pathlib import Path
import sys
from PyPDF2 import PdfReader, PdfWriter
import os
import pdfplumber


def analyze_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        page_numbers = []
        sections = {}
        current_section = None
        current_page_start = 1
        
        for i, page in enumerate(pdf.pages):
            page_numbers.append(i + 1)
            text = page.extract_text()
            lines = text.split('\n')
            # print(lines)
            for line in lines:
                print(line)
                if line.startswith('Problem'):
                    section_name = line.split(':')[0].strip()
                    if current_section:
                        sections[current_section] = (current_page_start, i)
                    current_section = section_name
                    current_page_start = i + 1
                    break 
            
    
    if current_section:
        sections[current_section] = (current_page_start, len(page_numbers))
    return page_numbers, sections

# python pdf_slicer.py /3B/PHYS334/A2/ 1 3 4 5 6 7 (except the last page)

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

pdf_path = "/Users/ms" + sys.argv[1]
output_path = os.path.dirname(pdf_path)
print(output_path)
#1 - 3 4 - 5 6 -7
arr = []
for i in range(2,len(sys.argv)):
    arr.append(sys.argv[i])


input_pdf = PdfReader(str(pdf_path))

# pdf_writer = PdfWriter()

for n in range(0,len(arr)):
    pdf_writer = PdfWriter()
    page_num = "q" + str(n + 1) + ".pdf"
    path_to_write = output_path + "/" + page_num
    print(path_to_write)
    last_page = int(arr[n+1]) if n <= len(arr) - 2 else len(input_pdf.pages) + 1
    for k in range(int(arr[n]),last_page): # 1-2-3
        page = input_pdf.pages[k-1] #0-1-2
        pdf_writer.add_page(page)
    print("Printing page number from " + arr[n] + " to " + str(last_page - 1))
    with Path(path_to_write).open(mode="wb") as output_file:
        pdf_writer.write(output_file)

