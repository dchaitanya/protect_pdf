from PyPDF2 import PdfFileReader, PdfFileWriter

def add_password(filename, password):
    pdfFileReader = PdfFileReader(filename)
    
    protect_pdf = PdfFileWriter()
    
    filename = filename.replace('.pdf', '_protected.pdf')

    protect_pdf_stream = open(filename, 'wb')
    print ("Total Pages = ", pdfFileReader.getNumPages())

    for page in pdfFileReader.pages:
        # print page
        protect_pdf.addPage(page)
        
    protect_pdf.write(protect_pdf_stream)
    protect_pdf_stream.close()

    return True
