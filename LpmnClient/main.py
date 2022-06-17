from lpmn_client import download_file, upload_file
from lpmn_client import Task
import sys

def main(argv):
    source_file = argv[0]
    dest_folder = argv[1]

    task = Task(lpmn='any2txt|wcrft2|fextor2({"features":"base noun_count bigrams","base_modification":"startlist","orth_modification":"startlist","lang":"pl","filters":{"base":[{"type":"lemma_stoplist","args":{"stoplist":"@resources/fextor/ml/polish_base_startlist.txt"}}]}})|dir|featfilt2({"weighting":"all:sm-mi_simple","filter":"min_tf-2 min_df-2","similarity":"cosine"})|cluto({"no_clusters":2,"analysis_type":"plottree"})')

    file_id = upload_file(source_file)
    output_file_id_tm = task.run(file_id)
    download_file(output_file_id_tm, dest_folder)

if __name__ == '__main__':
    main(sys.argv[1:])
    