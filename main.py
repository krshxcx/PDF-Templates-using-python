from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(False)
df = pd.read_csv('topics.csv')

#set header
for index,items in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=12)
    pdf.cell(w=0,h=12,txt=items['Topic'],align='L',ln=1)
    
    for y in range(20,288,10):
        pdf.line(10,y,200,y)
    #set footer
    pdf.ln(262)
    
    pdf.set_font(family='Times',style='B',size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=12,txt=items['Topic'],align='R',ln=1)    
    
    for i in range(items['Pages']-1):
        pdf.add_page()
        pdf.ln(275)
    
        pdf.set_font(family='Times',style='B',size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=12,txt=items['Topic'],align='R',ln=1)   
        for y in range(20,288,10):
            pdf.line(10,y,200,y)

        
    
pdf.output('output.pdf')