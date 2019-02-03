import PyPDF2
pdfObject = open(r'C:\Users\ayanori.ohashi\Downloads\meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfObject)
#print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
print(pageObj.extractText())