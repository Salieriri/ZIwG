import json
import os
import time
import datetime
import sys

class UpdateDates:
    def update(self, file):
        if 'PPE' in file:
            self.update_ppe(file)
        elif 'GryOnline' in file:
            self.update_gry_online(file)

    def update_ppe(self, file):
        with open(file, 'r+', encoding="utf8") as a_file:
            json_object = json.load(a_file)

        lista = []
        for element in json_object:
            if element['date'] != None:
                data = element['date'].split(" ")
                if data[1] != 'Dzisiaj,' and data[1] !='Wczoraj,':
                    godzina = data[-1].split(":")
                    dzien = data[1].split(".")
                    a=datetime.datetime(2022, int(dzien[1][:-1]), int(dzien[0]), int(godzina[0]), int(godzina[1]))
                    # print(a)
                    element['date'] = a.strftime("%Y-%m-%dT%H:%M:%S+02:00")
                    lista.append(element)
        with open(file, 'w', encoding='utf8') as f:
            f.write(json.dumps(lista, ensure_ascii=False))

    def update_gry_online(self, file):
        with open(file, 'r+', encoding="utf8") as a_file:
            json_object = json.load(a_file)
        miesiace = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia']

        for element in json_object:
            if element['date'] != None:
                data = element['date'].split(" ")
                index = miesiace.index(data[1])+1
                # print(index)
                godzina = data[-1].split(":")
                a=datetime.datetime(int(data[2][:-1]), int(index), int(data[0]), int(godzina[0]), int(godzina[1]))
                # print(a)
                element['date'] = a.strftime("%Y-%m-%dT%H:%M:%S+02:00")
        with open(file, 'w', encoding='utf8') as f:
            f.write(json.dumps(json_object, ensure_ascii=False))

# python UpdateDates.py #source_path# GryOnline PPE
def main(argv):
    source_path = argv[0]
    pages = argv[1:]
    json_objects = []

    update_dates = UpdateDates()
    for page in pages:
        update_dates.update(source_path + "/" + page + ".json")

if __name__ == '__main__':
    main(sys.argv[1:])
