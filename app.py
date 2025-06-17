import streamlit as st

# Page config
st.set_page_config(page_title="Kullhad Economy Festival", layout="wide")

# Custom styling for top navbar
st.markdown("""
<style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .top-nav {
        background-color: #111827;
        padding: 1rem 2rem;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 8px;
        margin-bottom: 2rem;
    }
    .nav-logo {
        font-size: 1.5rem;
        font-weight: bold;
    }
    .nav-links a {
        margin: 0 1.2rem;
        color: #fbbf24;
        text-decoration: none;
        font-weight: 500;
        font-size: 1rem;
    }
    .nav-links a:hover {
        text-decoration: underline;
    }
</style>

<div class="top-nav">
    <div class="nav-logo">KULLHAD FESTIVAL</div>
    <div class="nav-links">
        <a href="?section=about">About</a>
        <a href="?section=organising">Organising Structure</a>
        <a href="?section=features">Key Features</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Detect which section to show based on URL param
query_params = st.query_params
section = query_params.get("section", ["home"])[0]

# ----------- HERO SECTION (Centered) -----------
st.markdown("""
<style>
.hero-container {
    text-align: center;
    padding-top: 4rem;
    padding-bottom: 3rem;
}
.hero-title {
    font-size: 3.5rem;
    font-weight: 800;
    color: #1f2937;
    margin-bottom: 0.5rem;
}
.hero-subtitle {
    font-size: 1.5rem;
    font-weight: 400;
    color: #4b5563;
}
.section-spacer {
    margin-top: 4rem;
    margin-bottom: 2rem;
}
</style>

<div class="hero-container">
    <div class="hero-title">🌾 KULLHAD ECONOMY FESTIVAL</div>
    <div class="hero-subtitle">Reclaiming Roots, Reinventing Futures</div>
</div>

<div class="section-spacer"></div>
""", unsafe_allow_html=True)


# ------------------- OBJECTIVES GRID -------------------
st.markdown("""
    <style>
    .feature-grid {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 2rem;
        margin-top: 3rem;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #1f2937;
        color: white;
        padding: 2rem;
        border-radius: 12px;
        width: 250px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.25);
        text-align: center;
        transition: transform 0.2s ease-in-out;
    }
    .feature-card:hover {
        transform: scale(1.05);
    }
    .feature-icon {
        font-size: 2.5rem;
        color: #fbbf24;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .feature-text {
        font-size: 0.95rem;
        color: #d1d5db;
    }
    </style>

    <h2 style='text-align: center;'>🌟 Festival Objectives</h2>

    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🌿</div>
            <div class="feature-title">Promote Philosophy</div>
            <div class="feature-text">Celebrate the core spirit and practice of the Kullhad Economy.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <div class="feature-title">Empower Communities</div>
            <div class="feature-text">Showcase entrepreneurs, SHGs, and artisans driving local change.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Connect Tradition & Tech</div>
            <div class="feature-text">Inspire innovation rooted in Indic values and sustainability.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📢</div>
            <div class="feature-title">Amplify Voices</div>
            <div class="feature-text">Highlight regional changemakers and place-based impact stories.</div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ABOUT SECTION
if section == "about":
    st.header("📖 Overview")
    st.write("""
    The Kullhad Economy Festival (KEF) is envisioned as a landmark 1.5-day event celebrating grassroots entrepreneurship, indigenous innovation, sustainable production, and cultural heritage in alignment with the philosophy of the Kullhad Economy.

    Rooted in the spirit of **ātmanirbharta (self-reliance)** and drawing inspiration from timeless Indic civilisational values, KEF marks a conscious transition from marketing-driven, consumption-heavy models to **production-centric, dignity-first economic systems**.

    KEF is not just a festival — it is a **model in motion**. Focused on a 10 km radius around the Kamand Valley, the festival will bring together **artisans, farmers, innovators, students, teachers, performers, and policymakers** to create an immersive, participatory experience that celebrates being local while thinking cosmic — or what we call the **glocal dharma of development**.

    The event will begin with an auspicious **Maha Chandi Homa** on **Vijaya Dashami (Oct 2nd, 2025)** and continue through Oct 4–5, 2025.
    """)


# ORGANISING STRUCTURE
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

# KEY FEATURES
elif section == "features":
    st.header("Festival Highlights")
    with st.expander("🎪 Marketplace Stalls"):
        st.write("50+ curated stalls featuring artisans, farmers, SHGs, and local food innovators.")
    with st.expander("🎭 Cultural Performances"):
        st.write("Folk and classical fusion acts from Himachal and beyond.")
    with st.expander("🗣️ KFN Talks"):
        st.write("'Real Stories, Real Voices' — inspiring TED-style talks from the Kamand Valley.")
    with st.expander("🤝 Community Participation"):
        st.write("Thousands of local students, women groups, and leaders expected.")
    with st.expander("🎤 Dignitaries and Guests"):
        st.write("National icons from ecology, innovation, and culture.")

# Footer
st.markdown("---")
st.subheader("Why IIT Mandi?")
st.write("""
IIT Mandi lies at a unique confluence of culture, consciousness, and capability...
""")

st.subheader("💬 Share your thoughts")
review = st.text_area("Leave a review or message:")
if st.button("Submit Review"):
    st.success("✅ Thank you for your feedback!")
