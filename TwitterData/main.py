from TwitterApi import TwitterApi


if __name__ == '__main__':
    api = TwitterApi()
    api.load_data_from_files()
    # api.get_data_from_twitter()
    # api.save_data_to_txt_files()
    api.summary()
