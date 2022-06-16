import ZipFile
import json
import sys

# run:
# python3 main.py GryOnline Dataflow/data/GryOnline.json
def main(argv):
    try:
        with open(argv[1]) as jsonFile:
            jsonObject = {argv[0]: json.loads(jsonFile.read())}
    except FileNotFoundError:
        pass

    zipanator = ZipFile.Zipanator(jsonObject)
    zipanator.make_files_from_data()
    zipanator.zip_files(argv[0] + '.zip')

if __name__ == '__main__':
    main(sys.argv[1:])
