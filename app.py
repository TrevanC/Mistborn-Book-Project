import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
import os

# Set page config
st.set_page_config(
    page_title="Mistborn Character Network Analysis",
    page_icon="📚",
    layout="wide"
)

# Title and description
st.title("Mistborn Character Network Analysis")
st.markdown("""
This interactive dashboard showcases the character relationships and communities in Brandon Sanderson's Mistborn series.
Explore the networks to understand how characters are connected and their importance in the story.
""")

# Create tabs for different visualizations
tab1, tab2 = st.tabs(["Character Network", "Community Analysis"])

# Function to load and display HTML file
def load_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    return html

# Tab 1: Character Network
with tab1:
    st.header("Character Relationship Network")
    st.markdown("""
    This network visualization shows the relationships between characters in the Mistborn series.
    The size of the nodes represents character importance, and the edges show relationships between characters.
    """)
    
    # Load and display the character network
    html_content = load_html_file('mistborn.html')
    components.html(html_content, height=800, scrolling=True)

# Tab 2: Community Analysis
with tab2:
    st.header("Character Communities")
    st.markdown("""
    This visualization shows how characters form natural communities or groups within the Mistborn series.
    Colors represent different communities, helping to identify character clusters and their relationships.
    """)
    
    # Load and display the community network
    html_content = load_html_file('mistborn_communities.html')
    components.html(html_content, height=800, scrolling=True)

# Add sidebar with information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This dashboard visualizes character relationships in the Mistborn series by Brandon Sanderson.
    
    **Features:**
    - Interactive network visualization
    - Community detection analysis
    - Character importance metrics
    
    Use the tabs above to explore different aspects of the character network.
    """)
    
    st.header("How to Use")
    st.markdown("""
    - **Zoom**: Use mouse wheel or pinch gestures
    - **Pan**: Click and drag
    - **Select**: Click on nodes to see details
    - **Reset View**: Double click
    """) 