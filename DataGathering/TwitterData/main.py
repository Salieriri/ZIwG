from TwitterApi import TwitterApi
from ZipWithData import ZipFile

if __name__ == '__main__':
    api = TwitterApi()
    api.load_data_from_files()
    api.get_data_from_twitter()
    api.save_data_to_txt_files()
    api.summary()
    zipanator = ZipFile.Zipanator(api.data)
    zipanator.make_files_from_data()
    zipanator.zip_files('data/all_twitter_data.zip')
