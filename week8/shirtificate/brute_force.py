import fpdf

# base shirt
pdf = fpdf.FPDF(orientation='portrait', format="A5")
pdf.set_font('Helvetica', size=32)
pdf.add_page()
pdf.ln(20)  # Move down 20 units
pdf.cell(0, 0, txt="CS50 Shirtificate", align='C')
image_width = pdf.w * 0.75
image_x = (pdf.w - image_width) / 2
pdf.image("shirtificate.png", x=image_x, y=55, w=image_width)

# text name
name = 'John Harvard'
tookCS50 = f'{name} took CS50'
pdf.set_xy(image_x, 100)  
pdf.set_font('Helvetica', size=16)
pdf.set_text_color(255, 255, 255)  
pdf.cell(image_width, 10, tookCS50, align='C')


pdf.output("as.pdf")  