import requests

base_url = "https://graphql.anilist.co"

#
# The function is meant to take in 
#
#
def get_anime_info(anime_id):
    query = '''
    query ($id: Int) {
      Media(id: $id, type: ANIME) {
        id
        title {
          romaji
          english
          native
          }
        UserScoreStatistic {
          score
        }
    }
}


variables = { # Testing the query
    'id': 15125
}

response = requests.post(url, json={'query': query, 'variables': variables})

print(response.status_code)
print(response.json())