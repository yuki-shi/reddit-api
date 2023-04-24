import requests
from requests.auth import HTTPBasicAuth
import json
import datetime as dt
from utils import timestamp_to_datetime, str_to_datetime
from settings import CLIENT_ID, CLIENT_SECRET, USERNAME, PASSWORD, USER_AGENT


class Reddit():
    def __init__(self):
        self.client_id = CLIENT_ID
        self.client_secret = CLIENT_SECRET
        self.username = USERNAME
        self.password = PASSWORD
        self.user_agent = USER_AGENT
        self.token = self.get_token()
        self.headers = {'Authorization': f'bearer {self.token["access_token"]}',
                         'User-Agent': self.user_agent}

    def get_token(self):
        client_auth = HTTPBasicAuth(self.client_id, self.client_secret)
        post_data = {'grant_type': 'password',
                    'username': self.username,
                    'password': self.password}
        headers = {'User-Agent': self.user_agent}

        response = requests.post("https://www.reddit.com/api/v1/access_token", 
                                 auth=client_auth, 
                                 data=post_data,
                                 headers=headers)
        print('Token ok!')
        return response.json()

    def get_posts_data(self, data_limite: str, subreddit: str) -> list:
        params = {
           'limit': 100 #limite é 100
        }

        url = f'https://oauth.reddit.com/{subreddit}/new'
        after = ''
        data_final = dt.datetime.now() # valor dummy
        data_limite = str_to_datetime(data_limite)
        posts = []

        # O limite da API para sua listagem é 1k, mesmo com paginação
        #TODO: agora a lógica de limite de datas vai ocorrer no processamento.
        while len(posts) <= 1000:
            response = json.loads(requests.get(f'{url}?after={after}', 
                                               params=params, 
                                               headers=self.headers).text)

            for post in response['data']['children']:
                post = post['data']
                posts.append([post['title'],
                              post['author'], 
                              post['link_flair_text'],
                              post['ups'],
                              #post['downs'],
                              post['url'],
                              timestamp_to_datetime(post['created']),
                              post['selftext']])

            #data_final = timestamp_to_datetime(post['created']) #time delta (-3)
            after = response['data']['after']


        print('Extação ok!')
        return posts

