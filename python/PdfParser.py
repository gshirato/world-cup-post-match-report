from PyPDF2 import PdfReader

class PdfParser:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.pdf = PdfReader(pdf_path)

    def extract_text(self, page_num):
        return self.pdf.pages[page_num].extractText()

    @property
    def num_pages(self):
        return len(self.pdf.pages)
