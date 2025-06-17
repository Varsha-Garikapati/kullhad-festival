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
query_params = st.experimental_get_query_params()
section = query_params.get("section", ["home"])[0]

# Hero section (still at top)
if section == "home":
    st.markdown("# 🌾 KULLHAD ECONOMY FESTIVAL")
    st.markdown("### Reclaiming Roots, Reinventing Futures")

# ABOUT SECTION
if section == "about":
    st.header("About the Festival")
    st.write("""
    The Kullhad Economy Festival (KEF) is envisioned as a landmark 1.5-day event celebrating grassroots entrepreneurship, indigenous innovation, sustainable production, and cultural heritage...
    """)
    st.subheader("Objectives")
    st.markdown("""
    - Promote the core philosophy of the Kullhad Economy  
    - Provide a platform for community entrepreneurship  
    - Reconnect students with tradition and sustainability  
    - Amplify rural voices and craft-based models  
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
