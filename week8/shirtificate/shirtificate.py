import fpdf 
import sys

class Shirt:
    
    def __init__(self, orientation='portrait', format='A4',image=None, name=''):
        self._orientation = orientation
        self._format = format
        if image == None:
            raise ValueError('empty image')
        self._image = image

        if name == '':
            raise ValueError('empty None')
        self._name = name

    @property # setter
    def orientation(self):
        return self._orientation
    
    @property # setter
    def format(self):
        return self._format

    @property
    def image(self):
        return self._image

    @property
    def name(self):
        return self._name

    def pdf(self):
        try:
            pdf = fpdf.FPDF(orientation=self._orientation, format=self._format)
            pdf.set_font('Helvetica', size=32)
            pdf.add_page()
            pdf.ln(20)  
            pdf.cell(0, 0, txt="CS50 Shirtificate", align='C')
            image_width = pdf.w * 0.75
            image_x = (pdf.w - image_width) / 2
            pdf.image(self._image, x=image_x, y=55, w=image_width)
            self.add_shirt_name(pdf)
            pdf.output('shirtificate.pdf')
            # pdf.output(f'shirtificate-{self._name.replace(' ', ' ')}.pdf')
        except RuntimeError:
            sys.exit(1)

    def add_shirt_name(self, pdf):
        tookCS50 = f'{self._name} took CS50'
        image_width = pdf.w * 0.75
        image_x = (pdf.w - image_width) / 2
        pdf.set_xy(image_x, 100)  
        pdf.set_font('Helvetica', size=16)
        pdf.set_text_color(255, 255, 255)  
        pdf.cell(image_width, 10, tookCS50, align='C')

def main():
    john = Shirt(image='shirtificate.png', name='John Harvard')    
    john.pdf()
    

if __name__ == "__main__":
    main()