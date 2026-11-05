import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(filename="SchemeSaathi_Presentation.pptx"):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    C_NAVY = RGBColor(18, 48, 74)         # #12304A
    C_DARK_BG = RGBColor(14, 36, 56)      # #0E2438
    C_CARD_BG = RGBColor(24, 58, 88)      # #183A58
    C_PRIMARY = RGBColor(23, 105, 170)    # #1769AA
    C_PRIMARY_LIGHT = RGBColor(56, 189, 248) # #38BDF8
    C_GOLD = RGBColor(245, 158, 11)       # #F59E0B
    C_GREEN = RGBColor(16, 185, 129)      # #10B981
    C_RED = RGBColor(225, 29, 72)         # #E11D48
    C_WHITE = RGBColor(255, 255, 255)
    C_SLATE = RGBColor(148, 163, 184)     # #94A3B8
    C_LIGHT_BG = RGBColor(247, 249, 252)  # #F7F9FC
    C_CARD_LIGHT = RGBColor(255, 255, 255)
    C_BORDER_LIGHT = RGBColor(226, 232, 240)
    C_TEXT_DARK = RGBColor(23, 43, 58)
    C_TEXT_MUTED = RGBColor(100, 116, 139)

    def draw_bg(slide, dark=True):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_DARK_BG if dark else C_LIGHT_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, tag, title, dark=True):
        # Category Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(0.4))
        tf = tag_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = tag.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_GOLD if dark else C_PRIMARY
        p.font.name = "Arial"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.7))
        tf2 = title_box.text_frame
        tf2.word_wrap = True
        tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0
        p2 = tf2.paragraphs[0]
        p2.text = title
        p2.font.size = Pt(26)
        p2.font.bold = True
        p2.font.color.rgb = C_WHITE if dark else C_TEXT_DARK
        p2.font.name = "Arial"

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    draw_bg(s1, dark=True)

    # Accent decorative shape
    accent = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.2), Inches(3.2), Inches(0.45))
    accent.fill.solid()
    accent.fill.fore_color.rgb = C_PRIMARY
    accent.line.fill.background()
    p_acc = accent.text_frame.paragraphs[0]
    p_acc.text = "🏛️ CIVIC-TECH INNOVATION"
    p_acc.font.size = Pt(11)
    p_acc.font.bold = True
    p_acc.font.color.rgb = C_WHITE
    p_acc.alignment = PP_ALIGN.CENTER

    # Big Title
    title_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(11.7), Inches(1.8))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "SchemeSaathi (योजना साथी)"
    p.font.size = Pt(46)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    p.font.name = "Arial"

    p2 = tf.add_paragraph()
    p2.text = "AI-Driven Government Benefits Discovery Platform"
    p2.font.size = Pt(24)
    p2.font.color.rgb = C_PRIMARY_LIGHT
    p2.font.name = "Arial"

    # Subtitle Description Box
    desc_box = s1.shapes.add_textbox(Inches(0.8), Inches(3.9), Inches(10.5), Inches(1.2))
    tf_desc = desc_box.text_frame
    tf_desc.word_wrap = True
    p3 = tf_desc.paragraphs[0]
    p3.text = "Empowering Indian citizens to discover Central & State welfare initiatives through zero-knowledge client-side eligibility matching, offline-first PWA architecture, and direct official portal redirection."
    p3.font.size = Pt(15)
    p3.font.color.rgb = C_SLATE
    p3.font.name = "Arial"

    # Metadata & Links Card
    meta_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.5))
    meta_card.fill.solid()
    meta_card.fill.fore_color.rgb = C_CARD_BG
    meta_card.line.color.rgb = C_PRIMARY
    meta_card.line.width = Pt(1.5)
    tf_meta = meta_card.text_frame
    tf_meta.word_wrap = True
    tf_meta.margin_left = Inches(0.4)
    tf_meta.margin_top = Inches(0.25)
    
    p_m1 = tf_meta.paragraphs[0]
    p_m1.text = "👩‍💻 Developer: Shivani | Creator & Full-Stack Architect"
    p_m1.font.size = Pt(13)
    p_m1.font.bold = True
    p_m1.font.color.rgb = C_WHITE

    p_m2 = tf_meta.add_paragraph()
    p_m2.text = "🌐 Live URL: https://sathischeme.netlify.app/    |    📂 Repository: https://github.com/Shivaniroy09/SchemeSathi-Ai-Project"
    p_m2.font.size = Pt(12)
    p_m2.font.color.rgb = C_GOLD

    p_m3 = tf_meta.add_paragraph()
    p_m3.text = "⚙️ Stack: Next.js 16 (Turbopack) • React 19 • Tailwind CSS v4 • PWA Service Worker • Netlify Edge CDN"
    p_m3.font.size = Pt(11)
    p_m3.font.color.rgb = C_SLATE

    # ==========================================
    # SLIDE 2: Executive Summary & The Vision
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    draw_bg(s2, dark=True)
    add_header(s2, "Executive Overview", "Vision & Core Value Proposition")

    cards_data = [
        ("🔒 Zero-Document Privacy", 
         "No Citizen Papers Uploaded", 
         "Eliminates fear of identity theft and data leaks. SchemeSaathi never collects or stores Aadhaar, PAN, phone numbers, OTPs, or financial records.",
         C_GOLD),
        ("⚡ Instant Client Matching", 
         "Deterministic Rules Engine", 
         "Evaluates 15+ multi-factor parameters (state, occupation, income, category, gender) directly in the user's browser in sub-10 milliseconds.",
         C_PRIMARY_LIGHT),
        ("🔗 Direct Portal Routing", 
         "Unblockable Official Links", 
         "Bypasses predatory middleman websites and guides citizens directly to official .gov.in and .nic.in portals with native unblockable navigation.",
         C_GREEN),
        ("📱 Offline-First PWA", 
         "Installable App Experience", 
         "Native WebAPK installation on Android and iOS home screens with service worker offline caching for low-connectivity rural environments.",
         C_WHITE),
    ]

    for i, (title, subtitle, desc, accent_col) in enumerate(cards_data):
        left = Inches(0.8 + i * 2.95)
        top = Inches(1.8)
        width = Inches(2.8)
        height = Inches(4.8)

        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = accent_col
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = accent_col

        p_sub = tf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.size = Pt(11)
        p_sub.font.bold = True
        p_sub.font.color.rgb = C_SLATE
        p_sub.space_before = Pt(4)

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = C_WHITE
        p_desc.space_before = Pt(14)

    # ==========================================
    # SLIDE 3: Problem Background in India
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    draw_bg(s3, dark=True)
    add_header(s3, "Problem Statement", "The Last-Mile Welfare Delivery Crisis in India")

    # Left Column: The Problem Reality
    c1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_CARD_BG
    c1.line.color.rgb = C_RED
    c1.line.width = Pt(1.5)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.35)

    p = tf1.paragraphs[0]
    p.text = "🚨 The Ground Reality"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = C_RED

    points1 = [
        ("₹3+ Lakh Crore Earmarked Annually: ", "Massive budget allocations exist across Central & State ministries, but a large percentage of rightful beneficiaries remain unreached."),
        ("Information Asymmetry: ", "Citizens cannot find clear criteria; guidelines are buried across dozens of disparate ministerial websites in confusing bureaucratic jargon."),
        ("Predatory Middlemen (Dalals): ", "Uninformed rural citizens are often charged ₹500 - ₹2,000 simply to fill out free government welfare application forms."),
        ("Privacy & Scam Phishing: ", "Fake government clone websites harvest sensitive Aadhaar, PAN, and bank account credentials for financial cyber fraud.")
    ]
    for bold_txt, norm_txt in points1:
        p_pt = tf1.add_paragraph()
        p_pt.space_before = Pt(10)
        run1 = p_pt.add_run()
        run1.text = bold_txt
        run1.font.bold = True
        run1.font.size = Pt(12)
        run1.font.color.rgb = C_GOLD
        run2 = p_pt.add_run()
        run2.text = norm_txt
        run2.font.size = Pt(11)
        run2.font.color.rgb = C_WHITE

    # Right Column: The SchemeSaathi Breakthrough
    c2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_CARD_BG
    c2.line.color.rgb = C_GREEN
    c2.line.width = Pt(1.5)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.35)

    p2 = tf2.paragraphs[0]
    p2.text = "✅ The SchemeSaathi Solution"
    p2.font.size = Pt(18)
    p2.font.bold = True
    p2.font.color.rgb = C_GREEN

    points2 = [
        ("Zero KYC Barrier: ", "Zero document uploads. Zero mandatory logins. Citizens discover benefits completely anonymously without fear of data leakage."),
        ("Bilingual Algorithmic Wizard: ", "4-step intuitive questionnaire in English and Hindi that translates complex legal criteria into simple dropdown choices."),
        ("Direct Verified Portal Routing: ", "Provides verified direct links to authentic .gov.in and .nic.in portals with built-in departure verification notices."),
        ("Transparent Scoring: ", "Clearly displays 'Why this matches you' with exact matched rules (e.g., Landholding <= 2 hectares, Family Income < ₹2.5L).")
    ]
    for bold_txt, norm_txt in points2:
        p_pt = tf2.add_paragraph()
        p_pt.space_before = Pt(10)
        run1 = p_pt.add_run()
        run1.text = bold_txt
        run1.font.bold = True
        run1.font.size = Pt(12)
        run1.font.color.rgb = C_PRIMARY_LIGHT
        run2 = p_pt.add_run()
        run2.text = norm_txt
        run2.font.size = Pt(11)
        run2.font.color.rgb = C_WHITE

    # ==========================================
    # SLIDE 4: High-Level System Architecture
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    draw_bg(s4, dark=True)
    add_header(s4, "System Architecture", "Dual-Mode Execution & Edge Delivery Model")

    arch_layers = [
        ("Layer 1: Citizen Interface (Client)", 
         "PWA / Next.js React 19 Frontend",
         [
             "• Progressive Web App installable on Android / iOS / Desktop",
             "• Service Worker (sw.js) for app shell & offline asset caching",
             "• Bilingual state engine (English & Hindi) with instant toggle",
             "• Client-side reactive filtering and multi-step Wizard forms"
         ], C_PRIMARY_LIGHT),
        ("Layer 2: Edge CDN & Hosting Gateway", 
         "Netlify Global Edge Network",
         [
             "• Sub-50ms TTFB static asset delivery across global edge nodes",
             "• Pre-compiled SSG static HTML files (output: 'export')",
             "• Custom security headers (CSP, X-Frame-Options, nosniff)",
             "• Optimized cache-control policies for SW and Manifest"
         ], C_GOLD),
        ("Layer 3: Algorithmic Logic & Data", 
         "Zero-Knowledge Matching Engine",
         [
             "• lib/eligibility.ts deterministic multi-factor rules evaluator",
             "• In-memory structured civic dataset (15+ verified schemes)",
             "• Dynamic query synchronization (?state=Bihar&age=20)",
             "• Local execution: 0 bytes of sensitive data leave the device"
         ], C_GREEN),
        ("Layer 4: Destination Ecosystem", 
         "Official Government Portals (.gov.in)",
         [
             "• Unblockable native anchor links (target='_blank')",
             "• NSP, PM-KISAN, Ayushman Bharat, PMAY-G, Skill India, Mudra",
             "• Verified authentic domain validation (.gov.in / .nic.in)",
             "• Complete safety departure notices and anti-phishing safeguards"
         ], C_WHITE)
    ]

    for i, (layer_title, layer_sub, bullets, col) in enumerate(arch_layers):
        top = Inches(1.8 + i * 1.25)
        box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.7), Inches(1.1))
        box.fill.solid()
        box.fill.fore_color.rgb = C_CARD_BG
        box.line.color.rgb = col
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = layer_title + " — "
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = col
        r2 = p.add_run()
        r2.text = layer_sub
        r2.font.bold = True
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_SLATE

        p_b = tf.add_paragraph()
        p_b.text = "   |   ".join(bullets)
        p_b.font.size = Pt(10.5)
        p_b.font.color.rgb = C_WHITE
        p_b.space_before = Pt(3)

    # ==========================================
    # SLIDE 5: Architecture Flow Diagram
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    draw_bg(s5, dark=True)
    add_header(s5, "Architecture Flowchart", "High-Level Execution & Redirection Pipeline")

    flow_boxes = [
        ("1. Citizen Browser / PWA", "HTTPS Request / PWA Launch", Inches(0.8), Inches(2.2), Inches(3.2), Inches(1.2), C_PRIMARY),
        ("2. Netlify Edge Gateway", "Sub-50ms Pre-rendered SSG Shell", Inches(4.8), Inches(2.2), Inches(3.7), Inches(1.2), C_CARD_BG),
        ("3. Service Worker (sw.js)", "Offline Assets & Manifest Cached", Inches(9.3), Inches(2.2), Inches(3.2), Inches(1.2), C_CARD_BG),

        ("4. Eligibility Wizard Input", "State, Age, Income, Occupation", Inches(0.8), Inches(4.0), Inches(3.2), Inches(1.2), C_CARD_BG),
        ("5. Local Rules Engine", "Zero-Knowledge Local Evaluation", Inches(4.8), Inches(4.0), Inches(3.7), Inches(1.2), C_GOLD),
        ("6. Decision & Scoring", "Strong (>=80%) vs Potential", Inches(9.3), Inches(4.0), Inches(3.2), Inches(1.2), C_CARD_BG),

        ("7. Interactive Results UI", "Ranked Scheme Cards + Criteria", Inches(0.8), Inches(5.6), Inches(4.5), Inches(1.2), C_GREEN),
        ("8. Native Direct Outbound Link", "Safe Navigation (target='_blank')", Inches(5.8), Inches(5.6), Inches(3.5), Inches(1.2), C_CARD_BG),
        ("9. Official Govt Portal", "Verified .gov.in / .nic.in Application", Inches(9.7), Inches(5.6), Inches(2.8), Inches(1.2), C_PRIMARY_LIGHT),
    ]

    for title, desc, left, top, w, h, border_col in flow_boxes:
        shape = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h)
        shape.fill.solid()
        shape.fill.fore_color.rgb = C_CARD_BG
        shape.line.color.rgb = border_col
        shape.line.width = Pt(2)

        tf = shape.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.18)
        tf.margin_left = tf.margin_right = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = border_col
        p.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_WHITE
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(3)

    # ==========================================
    # SLIDE 6: Component & Execution Sequence Flow
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    draw_bg(s6, dark=True)
    add_header(s6, "Component Sequence Flow", "Step-by-Step Citizen Lifecycle & System Interactions")

    seq_steps = [
        ("Step 1: Edge Delivery", "Citizen requests sathischeme.netlify.app. Netlify Edge CDN returns pre-rendered static HTML, CSS & Turbopack JS bundle in under 50ms."),
        ("Step 2: PWA Activation", "Browser fires 'load' event; PwaRegister component activates Service Worker (sw.js) and caches offline shell and manifest.json."),
        ("Step 3: Wizard Assessment", "Citizen answers 4 profile prompts: State, Occupation, Income Range, Social Category. No PII is transmitted to any backend."),
        ("Step 4: Heuristic Scoring", "lib/eligibility.ts evaluates schemes dataset in memory. Applies weighted scoring formula across demographics, bounds, and exclusions."),
        ("Step 5: Ranked Results", "UI performs client-side transition to /results. Displays MatchBadges (Strong Match 90%, Potential Match 65%) with matched rule pills."),
        ("Step 6: Official Dispatch", "Citizen clicks 'Official Portal'. Native unblockable anchor navigates directly to authentic .gov.in domain (NHA, NSP, PM-KISAN, Mudra).")
    ]

    for i, (title, desc) in enumerate(seq_steps):
        left = Inches(0.8 + (i % 2) * 5.95)
        top = Inches(1.8 + (i // 2) * 1.65)
        box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.7), Inches(1.4))
        box.fill.solid()
        box.fill.fore_color.rgb = C_CARD_BG
        box.line.color.rgb = C_PRIMARY
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_GOLD

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = C_WHITE
        p_desc.space_before = Pt(3)

    # ==========================================
    # SLIDE 7: AI & Algorithmic Intelligence
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    draw_bg(s7, dark=True)
    add_header(s7, "AI & Algorithmic Logic", "Where AI & Rules-Based Scoring Are Deployed")

    c1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_CARD_BG
    c1.line.color.rgb = C_PRIMARY_LIGHT
    c1.line.width = Pt(1.5)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.3)

    p1 = tf1.paragraphs[0]
    p1.text = "🧠 Algorithmic Scoring Engine (lib/eligibility.ts)"
    p1.font.size = Pt(16)
    p1.font.bold = True
    p1.font.color.rgb = C_PRIMARY_LIGHT

    rules = [
        ("Multi-Factor Weighted Matrix: ", "Occupation (35%), Geography/State (25%), Social Category (15%), Income Tier (15%), and Special Criteria/Age (10%)."),
        ("Deterministic Match Categorization: ", "Score >= 80% yields 'Strong Match'; Score 60-79% yields 'Potential Match'; Score < 60% yields 'Basic Eligibility'."),
        ("Strict Exclusion Hard-Filters: ", "Taxpayer exclusion rules (PM-KISAN), institutional landholder disqualifiers, age limits (<18 or >60 for pensions)."),
        ("Explainable AI (XAI): ", "Every recommendation generates an array of human-readable matched signals ('Why this matches you') so citizens understand the exact basis.")
    ]
    for bold_txt, norm_txt in rules:
        p_r = tf1.add_paragraph()
        p_r.space_before = Pt(8)
        run1 = p_r.add_run()
        run1.text = bold_txt
        run1.font.bold = True
        run1.font.size = Pt(11.5)
        run1.font.color.rgb = C_GOLD
        run2 = p_r.add_run()
        run2.text = norm_txt
        run2.font.size = Pt(11)
        run2.font.color.rgb = C_WHITE

    c2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_CARD_BG
    c2.line.color.rgb = C_GOLD
    c2.line.width = Pt(1.5)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.3)

    p2 = tf2.paragraphs[0]
    p2.text = "🤖 Semantic AI & Future Conversational Roadmap"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = C_GOLD

    future_ai = [
        ("Bilingual Taxonomy Normalization: ", "Heuristic token search mapping colloquial Hindi terms (e.g. 'किसान', 'छात्रवृत्ति', 'ऋण') to formal government categories."),
        ("Zero-Knowledge AI Principle: ", "Unlike external LLMs that harvest personal data, SchemeSaathi executes all criteria matching entirely in-browser without sending prompt data to remote servers."),
        ("Phase 2 Roadmap — Voice AI Bot: ", "Integration of Indic-Whisper & Gemini Flash models to allow illiterate or elderly citizens to discover schemes by voice in regional dialects."),
        ("Document OCR Assistance (Future): ", "Client-side WebAssembly OCR to help citizens verify if their Aadhaar/Ration card is eligible without storing images on the server.")
    ]
    for bold_txt, norm_txt in future_ai:
        p_r = tf2.add_paragraph()
        p_r.space_before = Pt(8)
        run1 = p_r.add_run()
        run1.text = bold_txt
        run1.font.bold = True
        run1.font.size = Pt(11.5)
        run1.font.color.rgb = C_PRIMARY_LIGHT
        run2 = p_r.add_run()
        run2.text = norm_txt
        run2.font.size = Pt(11)
        run2.font.color.rgb = C_WHITE

    # ==========================================
    # SLIDE 8: Frontend Architecture & Engineering
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    draw_bg(s8, dark=True)
    add_header(s8, "Frontend Engineering", "Next.js 16 App Router & Modular UI Architecture")

    front_cards = [
        ("Next.js 16 (App Router)", "Turbopack Compiling", [
            "• Turbopack bundler for instantaneous compilation",
            "• Server Component & Client Component boundary separation",
            "• Pre-rendering 42 static HTML routes with generateStaticParams()",
            "• Automated SEO metadata and open-graph generation"
        ], C_PRIMARY_LIGHT),
        ("React 19 & State Architecture", "Reactive Lifecycle", [
            "• React 19 use() hook and async Promise param unwrap",
            "• LanguageContext with zero-re-render bilingual strings (EN/HI)",
            "• Suspense boundaries on search query param pages",
            "• Memory-safe event listener teardowns for PWA events"
        ], C_GOLD),
        ("Tailwind CSS v4 Design System", "High-Contrast Civic UI", [
            "• Bespoke government civic palette: Navy #12304A, Sky #1769AA",
            "• High contrast typography for outdoor mobile readability",
            "• Fully responsive layouts for 320px mobile up to 4K displays",
            "• Print-ready CSS for generating offline document checklists"
        ], C_GREEN),
        ("Key Modular Components", "Component Hierarchy", [
            "• EligibilityWizard: 4-step interactive civic criteria form",
            "• SchemeCard: Verified badge, benefits list & direct link",
            "• CompareBar: Floating side-by-side scheme comparison",
            "• PwaRegister: Install trigger banner & SW lifecycle manager"
        ], C_WHITE)
    ]

    for i, (title, sub, bullets, col) in enumerate(front_cards):
        left = Inches(0.8 + (i % 2) * 5.95)
        top = Inches(1.8 + (i // 2) * 2.5)
        box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(5.7), Inches(2.25))
        box.fill.solid()
        box.fill.fore_color.rgb = C_CARD_BG
        box.line.color.rgb = col
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = col

        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(10)
        p_sub.font.bold = True
        p_sub.font.color.rgb = C_SLATE

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = b
            p_b.font.size = Pt(10.5)
            p_b.font.color.rgb = C_WHITE
            p_b.space_before = Pt(2)

    # ==========================================
    # SLIDE 9: Backend, Edge & Static Infrastructure
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    draw_bg(s9, dark=True)
    add_header(s9, "Backend & Infrastructure", "Serverless Edge Delivery & Netlify Hosting Configuration")

    infra_points = [
        ("Static Site Generation (SSG) with output: 'export'", 
         "Compiled into pure static HTML, CSS, JavaScript, and assets. Zero runtime Node.js dependency eliminates server crash risks, scalability bottlenecks, and server maintenance costs.",
         C_PRIMARY_LIGHT),
        ("Netlify Edge CDN Infrastructure", 
         "Hosted on Netlify's globally distributed Edge Network with sub-50ms latency. Configured with dual netlify.toml files at root and subfolder levels for automated monorepo base routing.",
         C_GOLD),
        ("Granular HTTP Headers & Security", 
         "Includes strict security headers: X-Frame-Options: DENY, X-Content-Type-Options: nosniff, Referrer-Policy: strict-origin-when-cross-origin. Implements 1-year immutable caching for static assets.",
         C_GREEN),
        ("Service Worker & Manifest Caching Policies", 
         "sw.js is strictly configured with Cache-Control: no-cache, no-store, must-revalidate to ensure instant updates. manifest.json served with application/manifest+json MIME type.",
         C_WHITE),
        ("Universal SPA & 404 Routing", 
         "trailingSlash: true creates clean directory structures (/about/index.html). Integrated _redirects file provides seamless client-side routing fallback and custom 404 pages.",
         C_PRIMARY)
    ]

    for i, (title, desc, col) in enumerate(infra_points):
        top = Inches(1.8 + i * 1.0)
        box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.7), Inches(0.88))
        box.fill.solid()
        box.fill.fore_color.rgb = C_CARD_BG
        box.line.color.rgb = col
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.12)

        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = title + ": "
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = col

        r2 = p.add_run()
        r2.text = desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = C_WHITE

    # ==========================================
    # SLIDE 10: Progressive Web App (PWA) Implementation
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    draw_bg(s10, dark=True)
    add_header(s10, "PWA & Mobile Installation", "Enabling Native WebAPK Installation on Android & iOS")

    pwa_boxes = [
        ("Web App Manifest (manifest.json)", 
         "Standalone Experience",
         "Configured with display: 'standalone', background_color: '#12304A', theme_color: '#12304A', and orientation: 'portrait-primary' to launch full-screen without Chrome browser address bar.",
         C_PRIMARY_LIGHT),
        ("Production Service Worker (sw.js)", 
         "Dual Caching Strategy",
         "Pre-caches core app shell on installation. Implements Network-First strategy for dynamic pages and Cache-First strategy for static JS, CSS, and icons with offline fallback.",
         C_GOLD),
        ("Multi-Resolution Adaptive Icons", 
         "Standard & Maskable Icons",
         "Generated 192x192 and 512x512 PNG icons plus safe-zone Android maskable icons (icon-maskable-192.png, icon-maskable-512.png) and 180x180 apple-touch-icon.png.",
         C_GREEN),
        ("In-App Install Prompt Banner", 
         "PwaRegister Component",
         "Intercepts Chrome beforeinstallprompt event. Displays a sleek floating install banner with a 1-tap 'Install SchemeSaathi' button that triggers the native WebAPK install sheet.",
         C_WHITE),
    ]

    for i, (title, sub, desc, col) in enumerate(pwa_boxes):
        left = Inches(0.8 + i * 2.95)
        top = Inches(1.8)
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.8), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.3)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = col

        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(11)
        p_sub.font.bold = True
        p_sub.font.color.rgb = C_SLATE
        p_sub.space_before = Pt(4)

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(11.5)
        p_desc.font.color.rgb = C_WHITE
        p_desc.space_before = Pt(14)

    # ==========================================
    # SLIDE 11: Portal Redirection & Safety Architecture
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    draw_bg(s11, dark=True)
    add_header(s11, "Redirection Engineering", "Solving Mobile Popup Blocking & Live Government Endpoints")

    c1 = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c1.fill.solid()
    c1.fill.fore_color.rgb = C_CARD_BG
    c1.line.color.rgb = C_RED
    c1.line.width = Pt(1.5)
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.3)

    p1 = tf1.paragraphs[0]
    p1.text = "🔧 The Redirection Challenge & Fix"
    p1.font.size = Pt(16)
    p1.font.bold = True
    p1.font.color.rgb = C_GOLD

    fixes = [
        ("The Popup Blocker Issue: ", "Previously, clicking 'Official Portal' opened a React modal that executed window.open(). Mobile Chrome aggressively blocks window.open() as an untrusted popup, causing zero redirection."),
        ("The Native Anchor Solution: ", "Converted all portal actions into direct HTML <a> tags with target='_blank' and rel='noopener noreferrer'. Browser-native link clicks are 100% unblockable on all mobile OS."),
        ("ExternalLinkModal Enhancement: ", "Replaced modal buttons with direct clickable anchors, ensuring even secondary warning confirmation links navigate smoothly without blocker traps.")
    ]
    for b_txt, n_txt in fixes:
        p_f = tf1.add_paragraph()
        p_f.space_before = Pt(10)
        r1 = p_f.add_run()
        r1.text = b_txt
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = C_PRIMARY_LIGHT
        r2 = p_f.add_run()
        r2.text = n_txt
        r2.font.size = Pt(11)
        r2.font.color.rgb = C_WHITE

    c2 = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    c2.fill.solid()
    c2.fill.fore_color.rgb = C_CARD_BG
    c2.line.color.rgb = C_GREEN
    c2.line.width = Pt(1.5)
    tf2 = c2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.3)

    p2 = tf2.paragraphs[0]
    p2.text = "✅ 15 Verified Live Government Endpoints (200 OK)"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = C_GREEN

    endpoints = [
        ("PM-KISAN Samman Nidhi: ", "https://pmkisan.gov.in/"),
        ("Ayushman Bharat (PM-JAY): ", "https://beneficiary.nha.gov.in/"),
        ("Pradhan Mantri Awas Yojana (PMAY-G): ", "https://pmayg.dord.gov.in/"),
        ("National Scholarship Portal (NSP): ", "https://scholarships.gov.in/"),
        ("PM MUDRA Yojana: ", "https://www.mudra.org.in/"),
        ("Sukanya Samriddhi Yojana: ", "https://www.myscheme.gov.in/schemes/ssa"),
        ("PMKVY Skill India: ", "https://www.skillindiadigital.gov.in/"),
        ("Bihar Student Credit Card (MNSSBY): ", "https://www.7nishchay-yuvaupmission.bihar.gov.in/"),
        ("Bihar Kanya Utthan Yojana: ", "https://www.myscheme.gov.in/schemes/mkuy"),
        ("e-Shram National Database: ", "https://eshram.gov.in/")
    ]
    for b_txt, n_txt in endpoints:
        p_e = tf2.add_paragraph()
        p_e.space_before = Pt(4)
        r1 = p_e.add_run()
        r1.text = "• " + b_txt
        r1.font.bold = True
        r1.font.size = Pt(10.5)
        r1.font.color.rgb = C_WHITE
        r2 = p_e.add_run()
        r2.text = n_txt
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = C_SLATE

    # ==========================================
    # SLIDE 12: Technology Stack & Language Metrics
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    draw_bg(s12, dark=True)
    add_header(s12, "Technology Stack", "Languages, Frameworks, Libraries & DevOps")

    tech_grid = [
        ("Language: TypeScript 5.x", "98.4% of Codebase", "Strict static typing, custom domain interfaces (Scheme, UserProfile, MatchResult), eliminating runtime errors and ensuring type-safe civic algorithms.", C_PRIMARY_LIGHT),
        ("Framework: Next.js 16.3", "App Router Architecture", "Next.js 16 with Turbopack, static site export (output: 'export'), and generateStaticParams() for pre-compiling all scheme and category routes.", C_GOLD),
        ("UI Library: React 19.2", "Modern Concurrency", "React 19 Server & Client components, Context API (LanguageContext), useMemo optimization, and native Suspense boundaries for search params.", C_GREEN),
        ("CSS: Tailwind CSS v4", "High-Performance CSS", "Tailwind CSS v4 with custom HSL theme tokens, native responsive utilities, micro-animations, and custom print styling for document checklists.", C_WHITE),
        ("Icons: Lucide React", "Lightweight SVG Icons", "Tree-shaken SVG icon library providing crisp civic, government, navigation, and validation icons across all responsive breakpoints.", C_PRIMARY_LIGHT),
        ("Cloud & CI/CD: Netlify", "Edge Hosting & PWA", "Continuous deployment from GitHub (SchemeSathi-Ai-Project), edge CDN routing, custom headers, and automated static export publishing.", C_GOLD)
    ]

    for i, (title, sub, desc, col) in enumerate(tech_grid):
        left = Inches(0.8 + (i % 3) * 3.95)
        top = Inches(1.8 + (i // 3) * 2.5)
        box = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.75), Inches(2.3))
        box.fill.solid()
        box.fill.fore_color.rgb = C_CARD_BG
        box.line.color.rgb = col
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col

        p_s = tf.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(10)
        p_s.font.bold = True
        p_s.font.color.rgb = C_SLATE

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = C_WHITE
        p_d.space_before = Pt(6)

    # ==========================================
    # SLIDE 13: Civic Impact & Performance Metrics
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    draw_bg(s13, dark=True)
    add_header(s13, "Performance & Impact", "Key Metrics, Lighthouse Scores & User Experience")

    metrics = [
        ("0 Bytes", "Sensitive Data Uploaded", "Zero Aadhaar, PAN, phone numbers or bank details ever leave the user's device. 100% privacy preserved.", C_GREEN),
        ("< 50ms", "Time to First Byte (TTFB)", "Pre-rendered static HTML delivered globally via Netlify Edge CDN with zero server-side processing delays.", C_PRIMARY_LIGHT),
        ("98+", "Google Lighthouse Score", "Optimized performance, accessibility, SEO metadata tags, and PWA best practices.", C_GOLD),
        ("15+", "Verified National Schemes", "Covering Agriculture, Healthcare, Higher Education, MSME Business Loans, Women Welfare, and Senior Pensions.", C_WHITE),
    ]

    for i, (big_num, lbl, sub, col) in enumerate(metrics):
        left = Inches(0.8 + i * 2.95)
        top = Inches(1.8)
        card = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.8), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.4)

        p = tf.paragraphs[0]
        p.text = big_num
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = col
        p.alignment = PP_ALIGN.CENTER

        p_lbl = tf.add_paragraph()
        p_lbl.text = lbl
        p_lbl.font.size = Pt(13)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = C_WHITE
        p_lbl.alignment = PP_ALIGN.CENTER
        p_lbl.space_before = Pt(10)

        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_SLATE
        p_sub.alignment = PP_ALIGN.CENTER
        p_sub.space_before = Pt(12)

    # ==========================================
    # SLIDE 14: Future Roadmap & Scalability
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    draw_bg(s14, dark=True)
    add_header(s14, "Future Roadmap", "Strategic Expansion & Technological Horizons")

    roadmap_items = [
        ("Phase 1: Dataset Expansion", "Scale to 100+ Schemes Across All 36 States & UTs", 
         "Expand structured dataset to include state-specific flagship initiatives (e.g., Kanyashree, Rythu Bandhu, Ladli Behna, Kalaignar Magalir Urimai).", C_PRIMARY_LIGHT),
        ("Phase 2: Multilingual Expansion", "8 Major Indian Regional Languages", 
         "Broaden beyond English & Hindi to include Bengali, Telugu, Tamil, Marathi, Gujarati, Kannada, and Punjabi with automated locale detection.", C_GOLD),
        ("Phase 3: Conversational Voice AI Bot", "Indic-LLM & Voice Assistant", 
         "Deploy a speech-to-speech voice assistant powered by Gemini / Indic-LLMs to assist illiterate, elderly, and rural citizens through voice conversations.", C_GREEN),
        ("Phase 4: WhatsApp & SMS Micro-Gateway", "Accessibility for Non-Smartphone Citizens", 
         "Introduce an automated WhatsApp Bot and SMS/USSD inquiry numbers for rural citizens with feature phones to check eligibility without Internet.", C_WHITE)
    ]

    for i, (phase, title, desc, col) in enumerate(roadmap_items):
        top = Inches(1.8 + i * 1.25)
        box = s14.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top, Inches(11.7), Inches(1.1))
        box.fill.solid()
        box.fill.fore_color.rgb = C_CARD_BG
        box.line.color.rgb = col
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.14)

        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = phase + " — "
        r1.font.bold = True
        r1.font.size = Pt(13)
        r1.font.color.rgb = col

        r2 = p.add_run()
        r2.text = title
        r2.font.bold = True
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_WHITE

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = C_SLATE
        p_desc.space_before = Pt(4)

    # ==========================================
    # SLIDE 15: Conclusion, Q&A & Developer Info
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    draw_bg(s15, dark=True)
    add_header(s15, "Project Summary", "Empowering Civic Technology for 1.4 Billion Citizens")

    # Conclusion Card
    c_left = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(6.8), Inches(4.8))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = C_CARD_BG
    c_left.line.color.rgb = C_GOLD
    c_left.line.width = Pt(1.5)
    tf_l = c_left.text_frame
    tf_l.word_wrap = True
    tf_l.margin_left = tf_l.margin_right = tf_l.margin_top = Inches(0.35)

    p_l = tf_l.paragraphs[0]
    p_l.text = "🎯 Summary & Core Takeaway"
    p_l.font.size = Pt(18)
    p_l.font.bold = True
    p_l.font.color.rgb = C_GOLD

    summary_bullets = [
        "SchemeSaathi proves that civic welfare discovery does not require sacrificing citizen privacy or building expensive centralized databases.",
        "By leveraging static edge generation (Next.js 16 SSG on Netlify) and client-side deterministic evaluation, the platform delivers instantaneous, zero-cost, and fraud-resistant welfare navigation.",
        "Direct verified routing guarantees that citizens reach authentic .gov.in application portals without intermediary exploitation.",
        "Fully installable as an offline-first PWA for universal accessibility across all devices."
    ]
    for b in summary_bullets:
        p_b = tf_l.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = C_WHITE
        p_b.space_before = Pt(10)

    # Contact & Project Links Card
    c_right = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.9), Inches(1.8), Inches(4.6), Inches(4.8))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = C_CARD_BG
    c_right.line.color.rgb = C_PRIMARY_LIGHT
    c_right.line.width = Pt(1.5)
    tf_r = c_right.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = Inches(0.35)

    p_r = tf_r.paragraphs[0]
    p_r.text = "👩‍💻 Developer & Project Links"
    p_r.font.size = Pt(18)
    p_r.font.bold = True
    p_r.font.color.rgb = C_PRIMARY_LIGHT

    links = [
        ("Creator: ", "Shivani"),
        ("Live Website: ", "https://sathischeme.netlify.app/"),
        ("GitHub Repo: ", "Shivaniroy09/SchemeSathi-Ai-Project"),
        ("LinkedIn: ", "linkedin.com/in/shivani2302/"),
        ("Email: ", "shivaniroy2309@gmail.com"),
        ("Status: ", "Active & Deployed on Netlify")
    ]
    for lbl, val in links:
        p_item = tf_r.add_paragraph()
        p_item.space_before = Pt(10)
        r1 = p_item.add_run()
        r1.text = lbl
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = C_GOLD
        r2 = p_item.add_run()
        r2.text = val
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = C_WHITE

    p_end = tf_r.add_paragraph()
    p_end.space_before = Pt(20)
    p_end.text = "Thank You! Questions & Discussion Welcome."
    p_end.font.size = Pt(13)
    p_end.font.bold = True
    p_end.font.color.rgb = C_GREEN
    p_end.alignment = PP_ALIGN.CENTER

    prs.save(filename)
    print(f"Presentation saved successfully to: {filename}")

if __name__ == "__main__":
    create_deck("/Users/shivani/Desktop/My file/SchemeSaathi_Presentation.pptx")
