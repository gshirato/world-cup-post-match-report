from PdfParser import PdfParser
def get_pressure_data(pdf_path, page):
    res = []
    parser = PdfParser(pdf_path)
    text = parser.extract_text(page)
    lines = text.split('\n')
    for l in lines[2: 11]:
        res.append(parse_pressure_line(l))
    return res

def parse_pressure_line(line):
    elems = line.split(' ')
    return {"home": elems[0], "away": elems[-1], "type": ' '.join(elems[1:-1])}