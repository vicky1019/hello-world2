# encoding:utf-8
# @date:
# @author: vicky
# @environment:
# @brief:



texts = [
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
]
import spacy

# from collections import defaultdict
nlp = spacy.load('en_core_web_sm')
for doc in nlp.pipe(texts, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):
    # Do something with the doc here
    print([(ent.text, ent.label_) for ent in doc.ents])