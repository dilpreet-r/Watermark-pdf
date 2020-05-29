import PyPDF2
import sys

resultPdf=sys.argv[1]
inputPdf=sys.argv[2]
watermarkPdf=sys.argv[3]
template=PyPDF2.PdfFileReader(open(inputPdf,'rb'))
watermark=PyPDF2.PdfFileReader(open(watermarkPdf,'rb'))

output=PyPDF2.PdfFileWriter()
for i in range(template.getNumPages()):
	page=template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)
	with open(resultPdf,'wb')as file:
		output.write(file)
