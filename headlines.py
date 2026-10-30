import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

page = requests.get(URL, headers=headers, timeout=10)
if page.status_code != 200:
    print(f"Error: received status code {page.status_code}")
    exit(1)

soup = BeautifulSoup(page.text, "html.parser")

# BBC News uses data-testid="card-headline" on h2 elements for article headlines
items = soup.find_all(attrs={"data-testid": "card-headline"})

seen = set()
headlines = []
for item in items:
    text = item.get_text(strip=True)
    if text and text not in seen:
        seen.add(text)
        headlines.append(text)
    if len(headlines) == 5:
        break

if not headlines:
    print("No headlines found.")
else:
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")
