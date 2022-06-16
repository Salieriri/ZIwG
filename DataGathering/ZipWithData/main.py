import ZipFile
import json
import sys

def main(argv):
    source_path = argv[0]
    dest_path = argv[1]
    pages = argv[2:]
    json_objects = []

    for page in pages:
        try:
            with open(source_path + "/" + page + ".json") as json_file:
                json_objects.append({page: json.loads(json_file.read())})
        except FileNotFoundError:
            print("error")
            pass

    zipanator = ZipFile.Zipanator(json_objects)
    zipanator.make_files_from_data()
    zipanator.zip_files(dest_path + '/' + '_'.join(pages) + '.zip')

if __name__ == '__main__':
    main(sys.argv[1:])
