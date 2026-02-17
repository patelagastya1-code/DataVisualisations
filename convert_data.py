"""
Convert EMISSIONSVSGDP Excel or CSV data to JSON for the visualization.
"""
import pandas as pd
import json
import os

# Country to continent mapping (7 continents)
COUNTRY_TO_CONTINENT = {
    'Afghanistan': 'Asia', 'Albania': 'Europe', 'Algeria': 'Africa', 'Angola': 'Africa',
    'Argentina': 'South America', 'Armenia': 'Asia', 'Australia': 'Oceania', 'Austria': 'Europe',
    'Azerbaijan': 'Asia', 'Bahrain': 'Asia', 'Bangladesh': 'Asia', 'Barbados': 'North America',
    'Belarus': 'Europe', 'Belgium': 'Europe', 'Benin': 'Africa', 'Bolivia': 'South America',
    'Bosnia and Herzegovina': 'Europe', 'Botswana': 'Africa', 'Brazil': 'South America',
    'Bulgaria': 'Europe', 'Burkina Faso': 'Africa', 'Burundi': 'Africa', 'Cambodia': 'Asia',
    'Cameroon': 'Africa', 'Canada': 'North America', 'Cape Verde': 'Africa',
    'Central African Republic': 'Africa', 'Chad': 'Africa', 'Chile': 'South America',
    'China': 'Asia', 'Colombia': 'South America', 'Comoros': 'Africa', 'Congo': 'Africa',
    'Costa Rica': 'North America', "Cote d'Ivoire": 'Africa', 'Croatia': 'Europe',
    'Cuba': 'North America', 'Cyprus': 'Asia', 'Czechia': 'Europe',
    'Democratic Republic of Congo': 'Africa', 'Denmark': 'Europe', 'Djibouti': 'Africa',
    'Dominica': 'North America', 'Dominican Republic': 'North America', 'Ecuador': 'South America',
    'Egypt': 'Africa', 'El Salvador': 'North America', 'Equatorial Guinea': 'Africa',
    'Estonia': 'Europe', 'Eswatini': 'Africa', 'Ethiopia': 'Africa', 'Finland': 'Europe',
    'France': 'Europe', 'Gabon': 'Africa', 'Gambia': 'Africa', 'Georgia': 'Asia',
    'Germany': 'Europe', 'Ghana': 'Africa', 'Greece': 'Europe', 'Guatemala': 'North America',
    'Guinea': 'Africa', 'Guinea-Bissau': 'Africa', 'Haiti': 'North America',
    'Honduras': 'North America', 'Hong Kong': 'Asia', 'Hungary': 'Europe', 'Iceland': 'Europe',
    'India': 'Asia', 'Indonesia': 'Asia', 'Iran': 'Asia', 'Iraq': 'Asia', 'Ireland': 'Europe',
    'Israel': 'Asia', 'Italy': 'Europe', 'Jamaica': 'North America', 'Japan': 'Asia',
    'Jordan': 'Asia', 'Kazakhstan': 'Asia', 'Kenya': 'Africa', 'Kuwait': 'Asia',
    'Kyrgyzstan': 'Asia', 'Laos': 'Asia', 'Latvia': 'Europe', 'Lebanon': 'Asia',
    'Lesotho': 'Africa', 'Liberia': 'Africa', 'Libya': 'Africa', 'Lithuania': 'Europe',
    'Luxembourg': 'Europe', 'Madagascar': 'Africa', 'Malawi': 'Africa', 'Malaysia': 'Asia',
    'Mali': 'Africa', 'Malta': 'Europe', 'Mauritania': 'Africa', 'Mauritius': 'Africa',
    'Mexico': 'North America', 'Moldova': 'Europe', 'Mongolia': 'Asia', 'Montenegro': 'Europe',
    'Morocco': 'Africa', 'Mozambique': 'Africa', 'Myanmar': 'Asia', 'Namibia': 'Africa',
    'Nepal': 'Asia', 'Netherlands': 'Europe', 'New Zealand': 'Oceania', 'Nicaragua': 'North America',
    'Niger': 'Africa', 'Nigeria': 'Africa', 'North Korea': 'Asia', 'North Macedonia': 'Europe',
    'Norway': 'Europe', 'Oman': 'Asia', 'Pakistan': 'Asia', 'Palestine': 'Asia',
    'Panama': 'North America', 'Paraguay': 'South America', 'Peru': 'South America',
    'Philippines': 'Asia', 'Poland': 'Europe', 'Portugal': 'Europe', 'Qatar': 'Asia',
    'Romania': 'Europe', 'Russia': 'Europe', 'Rwanda': 'Africa', 'Saint Lucia': 'North America',
    'Sao Tome and Principe': 'Africa', 'Saudi Arabia': 'Asia', 'Senegal': 'Africa',
    'Serbia': 'Europe', 'Seychelles': 'Africa', 'Sierra Leone': 'Africa', 'Singapore': 'Asia',
    'Slovakia': 'Europe', 'Slovenia': 'Europe', 'South Africa': 'Africa', 'South Korea': 'Asia',
    'Spain': 'Europe', 'Sri Lanka': 'Asia', 'Sweden': 'Europe', 'Switzerland': 'Europe',
    'Syria': 'Asia', 'Taiwan': 'Asia', 'Tajikistan': 'Asia', 'Tanzania': 'Africa',
    'Thailand': 'Asia', 'Togo': 'Africa', 'Trinidad and Tobago': 'North America',
    'Tunisia': 'Africa', 'Turkey': 'Asia', 'Turkmenistan': 'Asia', 'Uganda': 'Africa',
    'Ukraine': 'Europe', 'United Arab Emirates': 'Asia', 'United Kingdom': 'Europe',
    'United States': 'North America', 'Uruguay': 'South America', 'Uzbekistan': 'Asia',
    'Venezuela': 'South America', 'Vietnam': 'Asia', 'World': 'World', 'Yemen': 'Asia',
    'Zambia': 'Africa', 'Zimbabwe': 'Africa',
}

def convert_to_json():
    if os.path.exists('EMISSIONSVSGDP.csv'):
        df = pd.read_csv('EMISSIONSVSGDP.csv')
    elif os.path.exists('EMISSIONSVSGDP .xlsx'):
        df = pd.read_excel('EMISSIONSVSGDP .xlsx')
    else:
        raise FileNotFoundError('No EMISSIONSVSGDP.csv or EMISSIONSVSGDP .xlsx found')
    
    # Clean column names for JSON
    df = df.rename(columns={
        'Entity': 'country',
        'Year': 'year',
        'Per capita emissions': 'emissions_per_capita',
        'GDP per capita': 'gdp_per_capita',
        'Population': 'population'
    })
    
    # Drop rows with missing critical values
    df = df.dropna(subset=['gdp_per_capita', 'emissions_per_capita', 'population'])
    
    # Add continent to each record
    df['continent'] = df['country'].map(COUNTRY_TO_CONTINENT).fillna('Other')
    
    # Convert to list of records
    data = df.to_dict(orient='records')
    
    # Get unique countries and years for quick reference
    countries = sorted(df['country'].unique().tolist())
    years = sorted(df['year'].unique().tolist())
    
    output = {
        'countries': countries,
        'years': years,
        'data': data
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"Converted {len(data)} records for {len(countries)} countries, years {min(years)}-{max(years)}")
    print("Saved to data.json")

if __name__ == '__main__':
    convert_to_json()
