from lpmn_client import download_file, upload_file
from lpmn_client import Task


fast_text = Task(lpmn='doc2vec({"lang": "polish"})|dir|feature2({"type":"word2vec"})')
topic_modeling = Task(lpmn='wcrft2|fextor2({"features":"base","lang":"ud","filters":{"base":[{"type":"pos_stoplist","args":{"stoplist"🙁"NOUN"]},"excluding":false}]}})|dir|feature2({"filter":{"base":{"min_df":2,"max_df":1,"keep_n":1000}}})|topic3({"no_topics":8,"no_passes":500,"method":"lda_mallet", "distance_map":false})')
stylometry = Task(lpmn='wcrft2|fextor2({"features":"base interp_signs bigrams","base_modification":"startlist","orth_modification":"startlist","lang":"ud","filters":{"base":[{"type":"lemma_stoplist","args":{"stoplist":"@resources/fextor/ml/polish_base_startlist.txt"}}]}})|dir|feature2')

file_id = upload_file("./all_twitter_data.zip")  # zip file with some documents (for example docx files)

output_file_id_ft = fast_text.run(file_id)
download_file(output_file_id_ft, "./out/ft")

# output_file_id_sm = stylometry.run(file_id)
# download_file(output_file_id_sm, "./out/sm")

output_file_id_tm = topic_modeling.run(file_id)
download_file(output_file_id_tm, "./out/tm")
