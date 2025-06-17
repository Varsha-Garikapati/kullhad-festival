import streamlit as st

# Set page config
st.set_page_config(page_title="Kullhad Economy Festival", layout="wide")

# Extract URL query parameters
query_params = st.query_params
section = query_params.get("section", ["home"])[0]
scroll = query_params.get("scroll", [""])[0]

# ---------------- STYLES ----------------
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
.feature-grid {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 2rem;
    margin-top: 2rem;
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
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="top-nav">
    <div class="nav-logo">KULLHAD FESTIVAL</div>
    <div class="nav-links">
        <a href="/?section=home&scroll=overview">About</a>
        <a href="/?section=organising">Organising Structure</a>
        <a href="/?section=features">Key Features</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- HOME PAGE ----------------
if section == "home":

    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🌾 KULLHAD ECONOMY FESTIVAL</div>
        <div class="hero-subtitle">Reclaiming Roots, Reinventing Futures</div>
    </div>
    """, unsafe_allow_html=True)

    # Overview Section as Cards
    st.markdown("<h2 id='overview' style='text-align: center; margin-top:4rem;'>📖 Festival Overview</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🧱</div>
            <div class="feature-title">Model in Motion</div>
            <div class="feature-text">KEF is not just a festival — it is a living ecosystem of local innovation and dignity-first economy.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🌍</div>
            <div class="feature-title">Think Glocal</div>
            <div class="feature-text">Celebrating local roots while embracing global consciousness — the glocal dharma of development.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤝</div>
            <div class="feature-title">Inclusive Participation</div>
            <div class="feature-text">Involving artisans, students, farmers, teachers, innovators, and policy-makers in one immersive experience.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔥</div>
            <div class="feature-title">Cultural Spark</div>
            <div class="feature-text">Begins with the sacred Maha Chandi Homa on Vijaya Dashami to ground the festival in spiritual energy.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Objectives Section
    st.markdown("<div class='section-spacer'></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>🌟 Festival Objectives</h2>", unsafe_allow_html=True)

    st.markdown("""
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

    # ---------------- FOOTER (Only on Home Page) ----------------
    st.markdown("---")
    st.subheader("Why IIT Mandi?")
    st.write("""
    IIT Mandi lies at a unique confluence of culture, consciousness, and capability...
    """)

    st.subheader("💬 Share your thoughts")
    review = st.text_area("Leave a review or message:")
    if st.button("Submit Review"):
        st.success("✅ Thank you for your feedback!")

# ---------------- ORGANISING STRUCTURE ----------------
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

# ---------------- KEY FEATURES ----------------
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
