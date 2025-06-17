import streamlit as st

# Page setup
st.set_page_config(page_title="Kullhad Economy Festival", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["About", "Organising Structure", "Key Features"])

# Hero Section (always visible)
st.markdown("# 🌾 KULLHAD ECONOMY FESTIVAL")
st.markdown("### Reclaiming Roots, Reinventing Futures")

# Content based on selection
if page == "About":
    st.subheader("About the Festival")
    st.write("""
    The Kullhad Economy Festival (KEF) is envisioned as a landmark 1.5-day event celebrating grassroots entrepreneurship, indigenous innovation, sustainable production, and cultural heritage...
    """)
    st.subheader("Objectives")
    st.markdown("""
    - To promote the core philosophy and practice of the Kullhad Economy  
    - To provide a platform for community entrepreneurship, rural innovation  
    - To inspire students to reconnect technology with tradition  
    - To amplify rural voices and place-based models  
    """)

elif page == "Organising Structure":
    st.subheader("Organising Committee")
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

elif page == "Key Features":
    st.subheader("Festival Highlights")
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
