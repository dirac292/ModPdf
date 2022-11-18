from pathlib import Path
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

#python pdf_slicer.py filepath q1page q2page q3page .... append
dir = "2B"
split_list = sys.argv[1].split('/')
file_init = split_list[0] + '/' + split_list[1]
# print(type(file_init))

pdf_path = ( 
    Path.home()
    / dir
    / str(sys.argv[1])
)

is_int = True

try: 
    int(sys.argv[len(sys.argv) - 1])
except:
    is_int = False
    print("appending with" + sys.argv[len(sys.argv) - 1])


if(is_int):
    ap = ""
    size = len(sys.argv)
else:
    ap = sys.argv[len(sys.argv) - 1]
    size = len(sys.argv) - 1
arr = []

for i in range(2,size):
    arr.append(int(sys.argv[i]))

arr.append(arr[len(arr) - 1] + 1)
print(arr)
input_pdf = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()

for n in range(0,len(arr) - 1):
    page_num = file_init + "/" + ap + "q" + str(n + 1) + ".pdf"
    for k in range(arr[n],arr[n + 1]): # 0-4 4-5 5-6
        page = input_pdf.getPage(k - 1) #0-1-2
        pdf_writer.addPage(page)
    print("Printing page number from " + str(arr[n]) + " to " + str(arr[n + 1] -1))
    with Path(page_num).open(mode="wb") as output_file:
        pdf_writer.write(output_file)
    pdf_writer = PdfFileWriter()
