import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="Mistborn Character Network",
    layout="wide"
)

# Title
st.title("Mistborn Character Network Analysis")

# Function to load and display HTML file
def load_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    return html

# Create tabs
tab1, tab2 = st.tabs(["Character Network", "Community Analysis"])

# Tab 1: Character Network
with tab1:
    st.header("Character Relationship Network")
    html_content = load_html_file('mistborn.html')
    components.html(html_content, height=800)

# Tab 2: Community Analysis
with tab2:
    st.header("Character Communities")
    html_content = load_html_file('mistborn_communities.html')
    components.html(html_content, height=800) 