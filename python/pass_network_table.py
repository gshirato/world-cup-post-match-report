import tabula

def parse_network_table(pdf_path, page):
    df = tabula.read_pdf(pdf_path, pages=page, stream=True)[0].reset_index(drop=True).iloc[5:, :-2]
    df = df.dropna(subset=['Unnamed: 0'])
    df = df.drop('Unnamed: 2', axis=1)
    players = df['Unnamed: 1'].tolist()
    df.columns = ['#', 'name', *players]
    return df.reset_index(drop=True)
