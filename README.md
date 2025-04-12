# Mistborn Character Network Analysis

This project visualizes character relationships and networks in Brandon Sanderson's Mistborn series using network analysis and interactive visualizations.

## Interactive Dashboard

Explore the character relationships and communities through our interactive Streamlit dashboard:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mistborn-book-project-ganlxgtgottzmkxbq3qzsa.streamlit.app/)


The dashboard features:
- Interactive character relationship network
- Community detection analysis
- Zoom and pan capabilities
- Node selection for detailed information


## Visualizations

### Character Relationship Network
![](pictures/Book1Relationships.png)

### Community Analysis
![](pictures/Book1Community.png)

### Character Relevance
![](pictures/SeriesRelevance.png)

## Project Structure

- `app.py`: Streamlit application for hosting the visualizations
- `mistborn.html`: Interactive character network visualization
- `mistborn_communities.html`: Interactive community analysis visualization
- `Relationship.ipynb`: Jupyter notebook containing the original analysis code
- `Characters.txt`: Character data and relationships
- `pictures/`: Directory containing static visualizations

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Mistborn-Book-Project.git
cd Mistborn-Book-Project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app locally:
```bash
streamlit run app.py
```

## Tools Used

- Python
- Jupyter Lab for initial analysis
- NetworkX for network analysis
- Pyvis for interactive network visualization
- Streamlit for web interface
- Pandas for data manipulation

## Features

- Interactive network visualization of character relationships
- Community detection analysis
- Responsive web interface
- Detailed character information on selection

## TODO
- Character relationship charts of the 2nd and 3rd books
- A more detailed analysis into character importance across the series
- Character locations throughout the books

## License

This project is licensed under the MIT License - see the LICENSE file for details.
