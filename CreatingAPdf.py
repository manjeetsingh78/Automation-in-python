from fpdf import FPDF

# To Set Orientation of the pdf
pdf = FPDF(orientation='P',unit='pt',format='A4')

pdf.add_page()

# TO insert image in the pdf
# w,h are the size of the image and x, y are the orientation of the image in the pdf
pdf.image('./image.jpg',w=53,h=55)

# Note: First We should define font then we can write text
pdf.set_font(family="Times",style="B",size = 24)

#To add text
pdf.cell(w=0,h = 50,txt = "Malayan Tiger",align="C",ln=1,border=1)

pdf.set_font(family='Times',style='B',size=14)
pdf.cell(w=0,h=15,txt='Description',ln=1,border=1)


# Note: If there is any dash in the string either convert the string into latin1 or remove dash becasuse dash is not supported in latin1
pdf.set_font(family='Times',size=12)
txt1 = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia. This population inhabits the southern and central parts of the Malay Peninsula, and has been classified as critically endangered. As of April 2014, the population was estimated at 80 120 mature individuals, with a continuing downward trend."""

# cell gives content in the sigle line if you want to in the another line you should use multi_cell
pdf.multi_cell(w=0,h=15,txt=txt1)

pdf.set_font(family="Times",style='B',size=14)
pdf.cell(w=100,h=25,txt='Kingdom:')

pdf.set_font(family="Times",size=14)
pdf.cell(w=100,h=25,txt='Animalia',ln=1)

pdf.set_font(family="Times",style='B',size=14)
pdf.cell(w=100,h=25,txt='Phylum:')

pdf.set_font(family="Times",size=14)
pdf.cell(w=100,h=25,txt='Chordata',ln=1)

# To get the pdf
pdf.output('output.pdf')
