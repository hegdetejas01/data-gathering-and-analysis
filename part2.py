##### USING API's #####


import pandas as pd
import requests

import time
import random


url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

headers = {
    "accept": "application/json",

    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNTFlOTI4MzlmZjhmMTM4MmRhN2E3ZmJjYjhlYTYyNiIsIm5iZiI6MTc4NDIwOTI0MS44MzgsInN1YiI6IjZhNThkZjU5NmM0NmFjZGQ5OGQ2NDIyNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5FylF7yBngBJ2wBW2DoOBpM_mULrXVSsWQW7bjYfipU",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

df = pd.DataFrame()

for i in range(1,500): # there are 551 pages

    print(i)

    try:
        url = "http://api.themoviedb.org/3/movie/top_rated?language=en-US&page={}".format(i)
        response = requests.get(url, headers=headers, timeout=10, verify=False)

    except:
        print("Lost connection at", i)

    else:
        temp = pd.DataFrame(response.json()['results'])
        temp = temp[['id','title','popularity','vote_average','vote_count','overview']]
        df = pd.concat([df, temp], ignore_index=True)

df.to_csv('tmdb.csv', index=False)
print(df)