import sys
import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    src_path = "ppt/MC400-Minor Project Presentation format-BTech CSE MO26.pptx"
    out_path = "ppt/MC400-Minor Project Presentation format-BTech CSE MO26.pptx"
    copy_path = "ppt/SchemeSaathi_70_Percent_Minor_Project_Presentation.pptx"
    root_copy_path = "SchemeSaathi_70_Percent_Minor_Project_Presentation.pptx"

    prs = pptx.Presentation(src_path)

    # Palette
    C_NAVY = RGBColor(0, 32, 96)         # #002060
    C_CRIMSON = RGBColor(192, 0, 0)      # #C00000
    C_GOLD = RGBColor(180, 115, 0)       # #B47300
    C_DARK = RGBColor(30, 41, 59)        # #1E293B
    C_SLATE = RGBColor(100, 116, 139)    # #64748B
    C_LIGHT_BG = RGBColor(248, 250, 252) # #F8FAFC
    C_CARD_BG = RGBColor(241, 245, 249)  # #F1F5F9
    C_BORDER = RGBColor(203, 213, 225)   # #CBD5E1
    C_GREEN = RGBColor(16, 140, 75)      # #108C4B
    C_WHITE = RGBColor(255, 255, 255)
    C_BLUE = RGBColor(14, 116, 144)      # #0E7490

    # Helper to format footer & date
    for i in range(1, len(prs.slides) - 1):
        slide = prs.slides[i]
        for sh in slide.shapes:
            if sh.name == "Date Placeholder 3" and sh.has_text_frame:
                sh.text_frame.text = "November 2026"
                for p in sh.text_frame.paragraphs:
                    p.font.name = "Lora"
                    p.font.size = Pt(10)
                    p.font.color.rgb = C_DARK
            elif sh.name == "Footer Placeholder 2" and sh.has_text_frame:
                sh.text_frame.text = "              B.TECH. (CSE)-VII  MO2026                 |                     MC400 – Minor Project Presentation (70% Work)	               |"
                for p in sh.text_frame.paragraphs:
                    p.font.name = "Lora"
                    p.font.size = Pt(10)
                    p.font.color.rgb = C_DARK

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides[0]
    for sh in s1.shapes:
        if sh.name == "Title 1" and sh.has_text_frame:
            sh.top = Inches(2.7)
            sh.height = Inches(1.2)
            tf = sh.text_frame
            tf.word_wrap = True
            tf.clear()
            p1 = tf.paragraphs[0]
            p1.text = "SchemeSaathi (योजना साथी)"
            p1.font.name = "Lora"
            p1.font.size = Pt(26)
            p1.font.bold = True
            p1.font.color.rgb = C_CRIMSON
            p1.alignment = PP_ALIGN.CENTER
            
            p2 = tf.add_paragraph()
            p2.text = "AI-Driven Government Benefits Discovery Platform"
            p2.font.name = "Lora"
            p2.font.size = Pt(17)
            p2.font.bold = True
            p2.font.color.rgb = C_NAVY
            p2.alignment = PP_ALIGN.CENTER

        elif sh.name == "Title 5" and sh.has_text_frame:
            sh.top = Inches(1.55)
            sh.height = Inches(1.0)
            tf = sh.text_frame
            tf.word_wrap = True
            tf.clear()
            p1 = tf.paragraphs[0]
            p1.text = "B.Tech. (CSE) - VII Monsoon 2026"
            p1.font.name = "Lora"
            p1.font.size = Pt(15)
            p1.font.bold = True
            p1.font.color.rgb = C_NAVY
            p1.alignment = PP_ALIGN.CENTER

            p2 = tf.add_paragraph()
            p2.text = "MC400 – Minor Project Progress Evaluation (70% Work Completed)"
            p2.font.name = "Lora"
            p2.font.size = Pt(16)
            p2.font.bold = True
            p2.font.color.rgb = C_NAVY
            p2.alignment = PP_ALIGN.CENTER

        elif sh.name == "TextBox 2" and sh.has_text_frame:
            tf = sh.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.text = "Presented by:"
            p0.font.name = "Lora"
            p0.font.size = Pt(14)
            p0.font.color.rgb = C_DARK

            p1 = tf.add_paragraph()
            p1.text = "Shivani"
            p1.font.name = "Lora"
            p1.font.size = Pt(16)
            p1.font.bold = True
            p1.font.color.rgb = C_NAVY

            p2 = tf.add_paragraph()
            p2.text = "Roll No.: ____________________"
            p2.font.name = "Lora"
            p2.font.size = Pt(14)
            p2.font.color.rgb = C_DARK

        elif sh.name == "TextBox 1" and sh.has_text_frame:
            tf = sh.text_frame
            tf.clear()
            p0 = tf.paragraphs[0]
            p0.text = "Under Guidance of:"
            p0.font.name = "Lora"
            p0.font.size = Pt(14)
            p0.font.color.rgb = C_DARK

            p1 = tf.add_paragraph()
            p1.text = "Name of Guide"
            p1.font.name = "Lora"
            p1.font.size = Pt(16)
            p1.font.bold = True
            p1.font.color.rgb = C_NAVY

            p2 = tf.add_paragraph()
            p2.text = "Assistant Professor"
            p2.font.name = "Lora"
            p2.font.size = Pt(14)
            p2.font.color.rgb = C_DARK

    print("Slide 1 configured.")

    prs.save(out_path)
    print("Test save successful.")

build_presentation()
