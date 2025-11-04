from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "FAIRPRESS Bias Analysis Report", ln=True, align="C")
        self.ln(10)

def generate_pdf(text, bias, confidence, polarity, subjectivity, explanation, filename="output/report.pdf"):
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 10, f"Bias: {bias} ({confidence})\nPolarity: {polarity}, Subjectivity: {subjectivity}\n\nExplanation:\n{explanation}")
    pdf.image("bias_chart.png", x=10, w=180)
    pdf.image("sentiment_chart.png", x=40, w=120)
    pdf.output(filename)
    return filename
