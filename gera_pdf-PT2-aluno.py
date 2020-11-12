import os
import PyPDF2
# from PyPDF2 import PdfFileReader, PdfFileMerger

files_dir = r"M:\MÉTODOS TROMPA PDF\mozart-12duos"


# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()

def pdf_num_pages(reader):

    for page_cont in range(reader.numPages):
        pageObj = reader.getPage(page_cont)
        pdfWriter.addPage(pageObj)


# Create the reader instance

# pdfiles = [open(f'{files_dir}\\duo1.pdf', 'rb'), open(f'{files_dir}\\duo2.pdf', 'rb')]

pdfiles = []
test = []

for file in sorted(os.listdir(files_dir), key=lambda s: s[4]):
    # input(file)

    test.append(file)
    pdfiles.append(open(f'{files_dir}\\{file}', 'rb'))
input(test)
for file in pdfiles:
    pdf_reader = PyPDF2.PdfFileReader(file)
    pdf_num_pages(pdf_reader)


# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open(f'{files_dir}\\Margett_chesque_dale.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

# Close all the files - Created as well as opened
pdfOutputFile.close()
