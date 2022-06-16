from zipfile import ZipFile
import os


class Zipanator:
    zip_file_path = os.path.curdir

    def __init__(self, twitter_data):
        self.twitter_data = twitter_data
        self.files_path = []

    def make_files_from_data(self):
        try:
            os.mkdir(self.zip_file_path)
        except FileExistsError:
            pass
        for key, values in self.twitter_data.items():
            for i, value in enumerate(values):
                print('{} plik z {}'.format(i + 1, key))
                self.files_path.append('{}/{}_{}.txt'.format(self.zip_file_path,
                                                             key, i + 1))
                with open(self.files_path[-1], 'w', encoding='utf8') as f:
                    if isinstance(value['text'], list):
                        value =' '.join(value['text'])
                    else:
                        value = value['text']
                    f.write(value)

    def zip_files(self, filename):
        with ZipFile(filename, 'w') as zip:
            for file in self.files_path:
                if os.stat(file).st_size > 0:
                    zip.write(file)
                    print('Skompresowano plik {}'.format(file))
                os.remove(file)
