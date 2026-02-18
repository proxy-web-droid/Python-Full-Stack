#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
TXT = os.path.join(ROOT, 'reports', 'progress_report.txt')
OUT = os.path.join(ROOT, 'reports', 'project1_progress_report.pdf')

def build_pdf():
    with open(TXT, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    heading = styles['Heading1']

    story = []

    # Title (first line)
    if lines:
        story.append(Paragraph(lines[0], heading))
        story.append(Spacer(1, 12))

    # Add rest of content preserving blank lines as spacing
    for line in lines[1:]:
        if line.strip() == '':
            story.append(Spacer(1, 6))
        else:
            story.append(Paragraph(line.replace('`', ''), normal))
    
    doc.build(story)
    print('PDF written to', OUT)

if __name__ == '__main__':
    build_pdf()
