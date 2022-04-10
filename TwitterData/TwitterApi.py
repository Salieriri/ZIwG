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
        tweet_field = 'created_at,context_annotations,entities'
        query = {
            'max_results': max_results,
            'return_json': True,
            'tweet_fields': tweet_field
        }
        for page in self.twitter_pages:
            user_id = self.api.get_user(username=page, return_json=True)['data']['id']
            if page in list(self.data.keys()):
                query.update({
                    'since_id': max(self.data[page], key=lambda x: int(x['id']))['id']
                })
            else:
                query.update({
                    'since_id': None
                })
            current_tweets_data = []
            query.update({'pagination_token': None})
            while len(current_tweets_data) <= max_tweets:
                current_tweets = self.api.get_timelines(user_id, **query)
                print('Pobrano {} tweetów z {}'.format(current_tweets['meta']['result_count'], page))
                if 'data' in list(current_tweets.keys()):
                    current_tweets_data.extend(current_tweets['data'])
                if 'next_token' not in current_tweets['meta'].keys():
                    break
                query.update({'pagination_token': current_tweets['meta']['next_token']})
            if page in list(self.data.keys()):
                self.data[page].extend(current_tweets_data)
            else:
                self.data.update({page: current_tweets_data})

    def save_data_to_txt_files(self):
        try:
            os.mkdir(self.dir_name)
        except FileExistsError:
            pass
        for key, data in self.data.items():
            with open('{}/{}.txt'.format(self.dir_name, key), 'w', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))

    def load_data_from_files(self):
        for page in self.twitter_pages:
            try:
                with open('{}/{}.txt'.format(self.dir_name, page), 'r', encoding='utf8') as f:
                    self.data.update({page: json.loads(f.read())})
            except FileNotFoundError:
                pass

    def summary(self):
        for key, values in self.data.items():
            print('{:<15} -> {} tweetów'.format(key, len(values)))
