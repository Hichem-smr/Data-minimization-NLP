from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans
from PyInstaller.utils.hooks import collect_data_files
import spacy
import json

print("status of GPU", spacy.prefer_gpu())

with open("Annotations0.json", "r") as f:
    data = json.load(f)

trainning = data["annotations"]
trainning = [tuple(i) for i in trainning]

for entry in trainning:
        entry[1]["entities"][0] = tuple(entry[1]["entities"][0])

# nlp = spacy.blank('en')
# datas = collect_data_files("en_core_web_lg")
# nlp = spacy.load("en_core_web_lg")
nlp = spacy.blank('en')



doc_bin = DocBin()
for text, annot in tqdm(trainning):
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annot["entities"]: 
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    filtered_ents = filter_spans(ents)
    doc.ents = filtered_ents
    doc_bin.add(doc)




gpu = spacy.prefer_gpu()
# print(gpu)
    
doc_bin.to_disk("train.spacy")
