import requests
from bs4 import BeautifulSoup
import json
import random

# Function to generate random ID
def generate_id(used_ids):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-'
    id_length = 22
    while True:
        id = ''.join(random.choice(characters) for _ in range(id_length))
        if id not in used_ids:
            used_ids.add(id)
            return id

# Load existing data.json
try:
    with open('data.json', 'r') as f:
        existing_data = json.load(f)
except FileNotFoundError:
    existing_data = {"cascadeColors": true, "colorBackground": false, "palette": [], "fileColors": []}

# Extract existing IDs and color mappings
used_ids = set(color['id'] for color in existing_data['palette'])
existing_colors = {color['name'].lower(): color for color in existing_data['palette'] if color['name']}
existing_hex = {color['value'].lower(): color for color in existing_data['palette']}

# Scrape colors from Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; ColorExtractor/1.0; +https://example.org/bot)"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

colors = existing_data['palette']  # Start with existing palette

# Find the color table
tables = soup.find_all('table', {'class': 'wikitable'})
target_table = None
for table in tables:
    headers = [th.get_text(strip=True).lower() for th in table.find_all('th')]
    if any("name" in h for h in headers) and any("hex" in h for h in headers):
        target_table = table
        break

if not target_table:
    raise ValueError("Could not find the color table with 'Name' and 'Hex' columns.")

# Extract rows
rows = target_table.find_all('tr')
for row in rows[1:]:  # Skip header row
    cols = row.find_all('td')
    if len(cols) >= 2:
        name = cols[0].get_text(strip=True)
        hex_code = cols[1].get_text(strip=True).upper()
        if hex_code.startswith('#') and len(hex_code) == 7:  # Valid hex code
            # Check if color name or hex already exists
            name_lower = name.lower()
            hex_lower = hex_code.lower()
            if name_lower in existing_colors:
                # Reuse existing ID for same name
                color_entry = existing_colors[name_lower]
            elif hex_lower in existing_hex:
                # Reuse existing ID for same hex
                color_entry = existing_hex[hex_lower]
            else:
                # New color, generate unique ID
                color_entry = {
                    "id": generate_id(used_ids),
                    "name": name,
                    "value": hex_code
                }
                colors.append(color_entry)
                # Update tracking dictionaries
                existing_colors[name_lower] = color_entry
                existing_hex[hex_lower] = color_entry

# Update data.json with new palette, preserving fileColors and other settings
existing_data['palette'] = colors

# Save to data.json
with open('data.json', 'w') as f:
    json.dump(existing_data, f, indent=2)

print(f"✅ Successfully updated data.json with {len(colors)} colors")