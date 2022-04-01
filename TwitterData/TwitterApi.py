from pytwitter import Api
import json
import os


class TwitterApi:
    def __init__(self):
        self._BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAACSZWwEAAAAAJZ3QT42UEu5R37mzwc6FAPL1%2Bdk%3DSPoWTeez7GtI1YhetxbkHaFlI4g32exGVnnpdGy56QGa9KMgE6'
        self.api = Api(bearer_token=self._BEARER_TOKEN)
        self.data = {}
        self.twitter_pages = [
            'golpl', 'EurogamerPL', 'cdaction',
            'PPE_pl', 'pzt_tenis', 'WPSportoweFakty',
            'TMagazyn', 'sportpl', 'przeglad'
        ]
        self.dir_name = 'Data_from_twitter'

    def get_data_from_twitter(self):
        max_results = 100
        max_tweets = 3300
        tweet_field = 'created_at'
        query = {
            'max_results': max_results,
            'return_json': True,
            'tweet_fields': tweet_field
        }
        for page in self.twitter_pages:
            user_id = self.api.get_user(username=page, return_json=True)['data']['id']
            current_tweets_data = []
            query.update({'pagination_token': None})
            while len(current_tweets_data) <= max_tweets:
                current_tweets = self.api.get_timelines(user_id, **query)
                print('Pobrano {} tweetów z {}'.format(len(current_tweets), page))
                current_tweets_data.extend(current_tweets['data'])
                if 'next_token' not in current_tweets['meta'].keys():
                    break
                query.update({'pagination_token': current_tweets['meta']['next_token']})
            self.data.update({page: current_tweets_data})

    def save_data_to_txt_files(self):
        try:
            os.mkdir(self.dir_name)
        except FileExistsError:
            pass
        for key, data in self.data.items():
            with open('{}/{}.txt'.format(self.dir_name, key), 'w') as f:
                f.write(json.dumps(data))

    def load_data_from_files(self):
        for page in self.twitter_pages:
            with open('{}/{}.txt'.format(self.dir_name, page), 'r') as f:
                self.data.update({page: json.loads(f.read())})

    def summary(self):
        for key, values in self.data.items():
            print('{:<15} -> {} tweetów'.format(key, len(values)))
