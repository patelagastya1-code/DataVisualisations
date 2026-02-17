# CO₂ Emissions vs GDP per Capita Visualization

An interactive data visualization exploring the relationship between CO₂ emissions per capita and GDP per capita by country, from 1850 to 2022.

## Features

- **Bubble chart**: GDP per capita (x-axis) vs emissions per capita (y-axis), with bubble size representing population
- **Timeline slider**: Scrub through years 1850–2022
- **Play button**: Animate through the timeline automatically
- **Country filter**: Multi-select dropdown with search to focus on specific countries
- **Responsive design**: Dark theme with clean typography

## Quick Start

1. **Convert data** (if using Excel):
   ```bash
   python convert_data.py
   ```

2. **Build the visualization**:
   ```bash
   python build_html.py
   ```

3. **Open** `index.html` in your browser (double-click or drag into browser).

## Data

- **Source**: Place your data file as `EMISSIONSVSGDP .xlsx` or `EMISSIONSVSGDP.csv`
- **Required columns**: Entity (country), Year, Per capita emissions, GDP per capita, Population
- **Note**: GDP per capita is expressed in international-$ at 2011 prices.
