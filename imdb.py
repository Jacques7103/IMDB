from bs4 import BeautifulSoup
import requests
import pandas as pd

list = []

for season in range(5):
    num_season = season + 1
    
    s_url = f'https://www.imdb.com/title/tt6468322/episodes?season={num_season}'
    print(f"Season link : {s_url}")
    response = requests.get(s_url)
    soup = BeautifulSoup(response.content)
    title = soup.find_all('div', class_ = 'info')
    
    for episode_no, episode in enumerate(title):
        episode_name = episode.strong.a.text
        episode_no = episode_no + 1
        
        airdate = episode.find('div', class_ = 'airdate')
        airdates = airdate.text.strip().replace('.', '')
        
        rating = episode.find('span', class_ = 'ipl-rating-star__rating').get_text()
        
        vote = episode.find('span', class_ = 'ipl-rating-star__total-votes').get_text()
        
        description = episode.find('div', class_ = 'item_description').get_text().strip().replace(',', '')
        
        data = {"Season":num_season,
                "Episode":episode_no,
                "Title":episode_name,
                "Airdate":airdates,
                "Rating":rating,
                "Votes":vote,
                "Description":description}
        list.append(data)

        print(f"Season : {num_season}")
        print(f"Episode : {episode_no}")
        print(f"Title : {episode_name}")
        print(f"Airdate : {airdates}")
        print(f"Rating : {rating}")
        print(f"Number of vote : {vote}")
        print(f"Description : {description}\n")
        
df = pd.DataFrame(list, columns = ['Season', 'Episode', 'Title', 'Airdate', 'Rating', 'Votes', 'Description'])
print(list[0])
print(df.head())

df.to_csv('money_heist.csv', index=False)