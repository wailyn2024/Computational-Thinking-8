import requests
from bs4 import BeautifulSoup

def fetch_live_scores():
    url = 'https://www.espncricinfo.com/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the live scores section
        live_scores_section = soup.find('section', class_='live-scores')
        if live_scores_section:
            matches = live_scores_section.find_all('div', class_='match-info')
            for match in matches:
                teams = match.find_all('span', class_='team-name')
                scores = match.find_all('span', class_='score')

                if teams and scores:
                    print(f"{teams[0].text.strip()} vs {teams[1].text.strip()}")
                    print(f"Score: {scores[0].text.strip()} - {scores[1].text.strip()}")
                    print()
        else:
            print("No live scores available at the moment.")
    else:
        print("Failed to fetch data. Status code:", response.status_code)

if __name__ == '__main__':
    fetch_live_scores()