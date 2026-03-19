import tabula

table = tabula.read_pdf('Table+and+Text.pdf')

table[0].to_excel('intoExcel.xlsx',index=None)