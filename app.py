
import streamlit as st

st.set_page_config(
    page_title="TextilePro AI",
    page_icon="🧵",
    layout="wide"
)

# ---------- Custom Design ----------
st.markdown("""
<style>
.stApp {
    background-color: #f5f7f6;
}
[data-testid="stSidebar"] {
    background-color: #123b35;
}
[data-testid="stSidebar"] * {
    color: white;
}
.hero {
    padding: 30px;
    border-radius: 18px;
    background: linear-gradient(120deg, #123b35, #27816d);
    color: white;
}
.hero h1 {
    color: white;
}
.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #dce6e1;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Fibre Database ----------
fibres = {
    "Cotton": {
        "Type": "Natural plant fibre",
        "Source": "Cotton plant seed hairs",
        "Properties": "Soft, breathable, absorbent and comfortable.",
        "Uses": "Shirts, T-shirts, towels, denim and bedsheets."
    },
    "Wool": {
        "Type": "Natural animal fibre",
        "Source": "Sheep fleece",
        "Properties": "Warm, elastic, crimped and insulating.",
        "Uses": "Sweaters, blankets, carpets and suits."
    },
    "Silk": {
        "Type": "Natural animal fibre",
        "Source": "Silkworm filament",
        "Properties": "Smooth, lustrous, lightweight and strong.",
        "Uses": "Scarves, luxury clothes and decorative fabrics."
    },
    "Polyester": {
        "Type": "Synthetic fibre",
        "Source": "Polymer manufacturing",
        "Properties": "Durable, quick-drying and crease-resistant.",
        "Uses": "Sportswear, uniforms, curtains and sewing threads."
    },
    "Nylon": {
        "Type": "Synthetic polyamide fibre",
        "Source": "Polyamide polymer",
        "Properties": "Strong, tough and abrasion-resistant.",
        "Uses": "Hosiery, ropes, carpets and sportswear."
    },
    "Viscose": {
        "Type": "Regenerated cellulosic fibre",
        "Source": "Regenerated cellulose",
        "Properties": "Soft, absorbent and good drape.",
        "Uses": "Dresses, shirts, linings and scarves."
    },
    "Acrylic": {
        "Type": "Synthetic fibre",
        "Source": "Acrylonitrile-based polymer",
        "Properties": "Lightweight, warm and wool-like.",
        "Uses": "Sweaters, blankets and knitted garments."
    },
    "Linen": {
        "Type": "Natural plant fibre",
        "Source": "Flax plant stem",
        "Properties": "Strong, absorbent and breathable.",
        "Uses": "Summer clothes, table linen and home textiles."
    }
}

# ---------- Process Database ----------
processes = {
    "Ginning":
        "Separates cotton fibres from cotton seeds.",

    "Blow Room":
        "Opens, blends and cleans cotton fibre tufts.",

    "Carding":
        "Separates fibres, removes impurities and produces sliver.",

    "Drawing":
        "Combines and drafts slivers to improve uniformity.",

    "Combing":
        "Removes short fibres and improves fibre uniformity.",

    "Roving":
        "Reduces sliver thickness and adds a small amount of twist.",

    "Ring Spinning":
        "Drafts roving and inserts twist to produce yarn.",

    "Rotor Spinning":
        "Uses a rotor system to form yarn from fibres.",

    "Weaving":
        "Interlaces warp and weft yarns to produce fabric.",

    "Knitting":
        "Forms fabric by interlooping yarns.",

    "Dyeing":
        "Adds colour to fibres, yarns or fabrics.",

    "Finishing":
        "Improves fabric appearance, handle or performance."
}

# ---------- Sidebar ----------
with st.sidebar:
    st.title("🧵 TextilePro AI")
    st.caption("Textile Engineering Hub")

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Fibre Library",
            "Textile Processes",
            "Yarn Calculator",
            "Fabric GSM Calculator",
            "Quiz",
            "Glossary",
            "About"
        ]
    )

    st.divider()
    st.caption("Learn • Calculate • Explore")

# ---------- Home ----------
if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>🧵 TextilePro AI</h1>
        <p>Textile Engineering Learning and Calculation Hub</p>
        <p>Explore fibres, spinning, weaving, yarn calculations
        and important textile manufacturing processes.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)
    c1.metric("Fibres", len(fibres))
    c2.metric("Processes", len(processes))
    c3.metric("Learning Tools", 4)

    st.subheader("Explore the application")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🧬 Fibre Library</h3>
        Learn about natural and synthetic fibres.
        </div>
        <div class="card">
        <h3>🏭 Textile Processes</h3>
        Understand spinning, weaving, dyeing and more.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🧮 Yarn Calculator</h3>
        Convert yarn counts between Ne, Tex and Denier.
        </div>
        <div class="card">
        <h3>📊 Fabric GSM</h3>
        Calculate fabric mass per square metre.
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "Designed for textile engineering students "
        "and textile manufacturing learners."
    )

# ---------- Fibre Library ----------
elif page == "Fibre Library":
    st.title("🧬 Fibre Knowledge Center")

    selected = st.selectbox(
        "Select a fibre",
        list(fibres.keys())
    )

    data = fibres[selected]

    st.subheader(selected)
    st.write("**Classification:**", data["Type"])
    st.write("**Source:**", data["Source"])
    st.write("**Properties:**", data["Properties"])
    st.write("**Common uses:**", data["Uses"])

    st.divider()
    st.subheader("Compare Fibres")

    selected_fibres = st.multiselect(
        "Choose fibres to compare",
        list(fibres.keys()),
        default=["Cotton", "Polyester"]
    )

    for name in selected_fibres:
        with st.expander(name):
            for key, value in fibres[name].items():
                st.write(f"**{key}:** {value}")

# ---------- Textile Processes ----------
elif page == "Textile Processes":
    st.title("🏭 Textile Manufacturing Processes")

    search = st.text_input("Search a process")

    results = {
        name: description
        for name, description in processes.items()
        if search.lower() in name.lower()
    }

    if not results:
        st.warning("No matching process found.")
    else:
        selected = st.selectbox(
            "Select process",
            list(results.keys())
        )

        st.subheader(selected)
        st.write(results[selected])

        st.markdown("### Simplified Process Flow")

        if selected == "Ginning":
            st.code("Seed Cotton → Ginning → Cotton Lint")
        elif selected == "Blow Room":
            st.code("Bales → Opening → Cleaning → Blending")
        elif selected == "Carding":
            st.code("Fibre Tufts → Carding → Sliver")
        elif selected == "Drawing":
            st.code("Slivers → Doubling → Drafting → Drawn Sliver")
        elif selected == "Combing":
            st.code("Lap → Combing → Combed Sliver")
        elif selected == "Roving":
            st.code("Drawn Sliver → Drafting → Light Twist → Roving")
        elif selected in ["Ring Spinning", "Rotor Spinning"]:
            st.code("Fibre Preparation → Spinning → Yarn")
        elif selected == "Weaving":
            st.code("Warp Preparation + Weft Insertion → Fabric")
        elif selected == "Knitting":
            st.code("Yarn Feeding → Loop Formation → Fabric")
        elif selected == "Dyeing":
            st.code("Preparation → Dyeing → Washing → Drying")
        elif selected == "Finishing":
            st.code("Preparation → Treatment → Drying → Inspection")

        st.caption(
            "Actual process sequences vary with machinery, "
            "fibre type and product specifications."
        )

# ---------- Yarn Calculator ----------
elif page == "Yarn Calculator":
    st.title("🧮 Yarn Count Calculator")

    conversion = st.selectbox(
        "Choose conversion",
        [
            "Ne to Tex",
            "Tex to Ne",
            "Tex to Denier",
            "Denier to Tex"
        ]
    )

    value = st.number_input(
        "Enter yarn count",
        min_value=0.001,
        value=20.0,
        step=1.0
    )

    if conversion == "Ne to Tex":
        result = 590.5 / value
        unit = "Tex"
        formula = "Tex = 590.5 / Ne"

    elif conversion == "Tex to Ne":
        result = 590.5 / value
        unit = "Ne"
        formula = "Ne = 590.5 / Tex"

    elif conversion == "Tex to Denier":
        result = value * 9
        unit = "Denier"
        formula = "Denier = Tex × 9"

    else:
        result = value / 9
        unit = "Tex"
        formula = "Tex = Denier / 9"

    st.metric("Calculated Result", f"{result:.3f} {unit}")
    st.info(f"Formula: {formula}")

    st.caption(
        "The Ne/Tex conversion uses the approximate "
        "conventional constant 590.5."
    )

    st.divider()
    st.subheader("Yarn Mass Calculator")

    tex = st.number_input(
        "Yarn linear density (Tex)",
        min_value=0.001,
        value=25.0
    )

    length = st.number_input(
        "Yarn length (metres)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    mass = tex * length / 1000

    st.metric("Estimated Yarn Mass", f"{mass:.3f} grams")

# ---------- Fabric GSM ----------
elif page == "Fabric GSM Calculator":
    st.title("📊 Fabric GSM Calculator")

    st.write(
        "GSM means grams per square metre. "
        "It measures fabric mass per unit area."
    )

    mass = st.number_input(
        "Fabric sample mass (grams)",
        min_value=0.001,
        value=5.0
    )

    width = st.number_input(
        "Sample width (cm)",
        min_value=0.1,
        value=10.0
    )

    length = st.number_input(
        "Sample length (cm)",
        min_value=0.1,
        value=10.0
    )

    area = (width / 100) * (length / 100)
    gsm = mass / area

    st.metric("Fabric GSM", f"{gsm:.2f} g/m²")

    st.info("Formula: GSM = Sample Mass (g) / Sample Area (m²)")

# ---------- Quiz ----------
elif page == "Quiz":
    st.title("📝 Textile Knowledge Quiz")

    questions = [
        {
            "question": "Which fibre comes from a plant?",
            "options": ["Nylon", "Cotton", "Polyester", "Acrylic"],
            "answer": "Cotton"
        },
        {
            "question": "Which process produces sliver?",
            "options": ["Dyeing", "Weaving", "Carding", "Finishing"],
            "answer": "Carding"
        },
        {
            "question": "Tex represents grams per:",
            "options": ["100 metres", "1,000 metres", "9,000 metres", "1 metre"],
            "answer": "1,000 metres"
        },
        {
            "question": "Which process interlaces warp and weft?",
            "options": ["Knitting", "Weaving", "Ginning", "Combing"],
            "answer": "Weaving"
        }
    ]

    with st.form("quiz_form"):
        answers = []

        for i, question in enumerate(questions):
            st.markdown(f"**Q{i+1}. {question['question']}**")

            answer = st.radio(
                "Select answer",
                question["options"],
                index=None,
                key=f"q{i}"
            )

            answers.append(answer)

        submitted = st.form_submit_button("Check Score")

    if submitted:
        score = sum(
            answers[i] == question["answer"]
            for i, question in enumerate(questions)
        )

        st.success(f"Your score: {score}/{len(questions)}")

        for i, question in enumerate(questions):
            if answers[i] == question["answer"]:
                st.write(f"✅ Question {i+1}: Correct")
            else:
                st.write(
                    f"❌ Question {i+1}: "
                    f"Correct answer: {question['answer']}"
                )

# ---------- Glossary ----------
elif page == "Glossary":
    st.title("📘 Textile Glossary")

    glossary = {
        "Absorbency": "Ability to take up moisture.",
        "Crimp": "Waviness in a fibre.",
        "Drafting": "Reducing strand thickness by drawing fibres out.",
        "Denier": "Grams per 9,000 metres.",
        "GSM": "Grams per square metre.",
        "Ne": "English cotton yarn count system.",
        "Sliver": "A loose strand of fibres produced by carding or drawing.",
        "Tex": "Grams per 1,000 metres.",
        "Warp": "Lengthwise yarns in woven fabric.",
        "Weft": "Crosswise yarns in woven fabric."
    }

    search = st.text_input("Search a textile term")

    for term, meaning in glossary.items():
        if (
            search.lower() in term.lower()
            or search.lower() in meaning.lower()
        ):
            with st.expander(term):
                st.write(meaning)

# ---------- About ----------
elif page == "About":
    st.title("ℹ️ About TextilePro AI")

    st.write("""
    TextilePro AI is a Textile Engineering learning application.

    It provides:
    - Fibre information
    - Textile manufacturing process explanations
    - Yarn count conversions
    - Fabric GSM calculations
    - Practice quizzes
    - Textile terminology

    This version is an educational application. It does not yet
    connect to an external AI model.

    Always verify industrial calculations against the applicable
    laboratory standards and mill specifications.
    """)

st.divider()
st.caption("TextilePro AI | Textile Engineering Learning Hub")
