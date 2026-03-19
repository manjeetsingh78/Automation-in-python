import pandas as pd
from fpdf import FPDF


df = pd.read_excel('animal.xlsx')

print(df)

for index,row in df.iterrows():
    pdf = FPDF(orientation='P',unit='pt',format='A4')
    pdf.add_page()
    
    pdf.set_font(family='Times',style='B',size=24)
    pdf.cell(w=0,h=50,txt=row['Name'],align='C',ln=1)
    
    for column in df.columns:
        if column != 'Name':
            pdf.set_font(family='Times',style='B',size=14)
            pdf.cell(w=100,h=25,txt=f"{column}:",ln=0)
            
            pdf.set_font(family='Times',size=14)
            pdf.cell(w=100,h=25,txt=str(row[column]),ln=1)
    
    
    pdf.output(f"{row['Name']}.pdf")