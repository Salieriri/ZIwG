from zipfile import ZipFile
import os
from datetime import datetime

class Zipanator:
    zip_file_path = os.path.curdir

    def __init__(self, json_data):
        self.json_data = json_data
        self.files_path = []

    def make_files_from_data(self):
        try:
            os.mkdir(self.zip_file_path)
        except FileExistsError:
            pass
        for item in self.json_data:
            for key, values in item.items():
                for i, value in enumerate(values):
                    if i%3==0 and value['date'] is not None:
                        print('{} plik z {}'.format(i + 1, key))
                        self.files_path.append('{}/{}_{}_{}.txt'.format(self.zip_file_path,
                                                                    key, i + 1, datetime.strptime(value['date'], "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%dT%H-%M-%S%z")))
                        with open(self.files_path[-1], 'w', encoding='utf8') as f:
                            text = value['title'] + '\n'
                            if isinstance(value['text'], list):
                                text += ' '.join(value['text'])
                            else:
                                text += value['text']
                            f.write(text)

    def zip_files(self, filename):
        with ZipFile(filename, 'a') as zip:
            for file in self.files_path:
                zip.write(file)
                print('Skompresowano plik {}'.format(file))
                os.remove(file)
