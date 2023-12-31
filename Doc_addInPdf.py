from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj

input_file = "my_file.pdf"
output_file = "my_file_with_footer.pdf"

# Get pages
reader = PdfReader(input_file)
pages = [pagexobj(p) for p in reader.pages]

# Compose new pdf
canvas = Canvas(output_file)

for page_num, page in enumerate(pages, start=1):

    # Add page
    canvas.setPageSize((page.BBox[2], page.BBox[3]))
    canvas.doForm(makerl(canvas, page))

    # Draw footer
    footer_text = "Page %s of %s" % (page_num, len(pages))
    x = 128
    canvas.saveState()
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setLineWidth(0.5)
    canvas.line(66, 78, page.BBox[2] - 66, 78)
    canvas.setFont('Times-Roman', 10)
    canvas.drawString(page.BBox[2]-x, 65, footer_text)
    canvas.restoreState()

    canvas.showPage()

canvas.save()
