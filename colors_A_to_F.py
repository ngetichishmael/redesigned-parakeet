import requests
from bs4 import BeautifulSoup
import json
import random

# Function to generate random 
def generate_id():
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-';
  idLength = 22;
  id = '';
  
  for i in range(idLength):
    randomIndex = random.randint(0, len(characters) - 1)
    id += characters[randomIndex];
  
  return id;

url = "https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F"
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; ColorExtractor/1.0; +https://example.org/bot)"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

colors = []

# Try to find the correct table by looking for one that has "Name" and "Hex" in the header
tables = soup.find_all('table', {'class': 'wikitable'})

if not tables:
    raise ValueError("No wikitable found on the page.")

target_table = None
for table in tables:
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    if any("name" in h.lower() for h in headers) and any("hex" in h.lower() for h in headers):
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
            colors.append({"id": generate_id(), "name": name, "value": hex_code})

# Save to JSON
with open('data/colors_A_to_F.json', 'w') as f:
    json.dump(colors, f, indent=2)

print(f"✅ Successfully extracted {len(colors)} colors to 'colors_A_to_F.json'")