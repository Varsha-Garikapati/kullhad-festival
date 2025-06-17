import streamlit as st

# Custom page config
st.set_page_config(
    page_title="Kullhad Economy Festival",
    layout="wide"
)

# Custom CSS for clean styling (like margamai.com)
st.markdown("""
    <style>
        body {
            background-color: #fff;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            font-size: 4em;
            font-weight: 700;
            margin-top: 1.5em;
            margin-bottom: 0.2em;
            text-align: center;
        }
        .subtitle {
            font-size: 1.5em;
            font-weight: 400;
            text-align: center;
            margin-bottom: 3em;
            color: #444;
        }
        .nav-buttons {
            display: flex;
            justify-content: center;
            gap: 1.5em;
            margin-top: 1em;
        }
        .footer {
            margin-top: 4em;
            padding-top: 2em;
            border-top: 1px solid #ccc;
            text-align: center;
            font-size: 0.9em;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

# ---- HERO SECTION ----
st.markdown('<div class="main-title">KULLHAD ECONOMY FESTIVAL</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Reclaiming Roots, Reinventing Futures</div>', unsafe_allow_html=True)

# Navigation (simulated nav buttons)
nav = st.columns(3)
if nav[0].button("About"):
    section = "about"
elif nav[1].button("Organising Structure"):
    section = "organising"
elif nav[2].button("Key Features"):
    section = "features"
else:
    section = "home"

# ---- SECTION: ABOUT ----
if section == "about":
    st.header("About the Festival")
    st.write("""
    The Kullhad Economy Festival (KEF) is envisioned as a landmark 1.5-day event celebrating grassroots entrepreneurship, indigenous innovation, sustainable production, and cultural heritage...
    """)
    st.subheader("Objectives")
    st.markdown("""
    - To promote the core philosophy of the Kullhad Economy  
    - To provide a platform for community entrepreneurship  
    - To inspire students to reconnect technology with tradition  
    - To amplify rural voices and place-based models  
    """)

# ---- SECTION: ORGANISING STRUCTURE ----
elif section == "organising":
    st.header("Organising Committee")
    st.markdown("""
    - Prof. Ajay Chaturvedi  
    - Dr. Surya Prakash Upadhyaya  
    - Dr. Arnav Bhavsar  
    - Dr. Shyam Masakapalli  
    """)
    st.subheader("Advisory Board")
    st.markdown("""
    - Ms. Kangana Ranaut  
    - Prof. Lakshmidhar Behera  
    - Prof. Gautam Desiraju  
    """)

# ---- SECTION: KEY FEATURES ----
elif section == "features":
    st.header("Festival Highlights")
    with st.expander("🎪 Marketplace Stalls"):
        st.write("50+ curated stalls featuring artisans, farmers, SHGs, local food producers, and innovators.")
    with st.expander("🎭 Cultural Performances"):
        st.write("Folk and classical fusion performances by regional artists and renowned contributors.")
    with st.expander("🗣️ KFN Talks"):
        st.write("TED-style talks by local entrepreneurs and cultural figures: 'Real Stories, Real Voices'")
    with st.expander("🤝 Community Participation"):
        st.write("5,000+ locals, including students, SHGs, panchayats, and more.")
    with st.expander("🎤 Dignitaries and Special Guests"):
        st.write("Notable figures from sustainability, traditional knowledge, and policy.")

# ---- FOOTER ----
st.markdown('<div class="footer">Made with ❤️ at IIT Mandi | Why IIT Mandi? See below.</div>', unsafe_allow_html=True)

st.subheader("Why IIT Mandi?")
st.write("""
IIT Mandi lies at a unique confluence of culture, consciousness, and capability...
""")

st.subheader("💬 Share your thoughts")
review = st.text_area("Leave a review or message:")

if st.button("Submit Review"):
    st.success("✅ Thank you for your feedback!")
