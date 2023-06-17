import faiss
import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

class FaissIndex:

    def __init__(self, df):
        # https://www.sbert.net/docs/pretrained_models.html#model-overview
        
        # self.model = SentenceTransformer('bert-base-nli-mean-tokens')
        # self.model = SentenceTransformer('flax-sentence-embeddings/all_datasets_v3_mpnet-base')
        self.model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

        
        df['searchColumn'] = df['title'] + " " + df['description'] + " " + df['mediaHtmlContent']
        sentences = df['searchColumn'].tolist()
        ids = df["id"].tolist()
        sentence_embeddings = self.__get_embeddings__(sentences)

        d = sentence_embeddings.shape[1] # 768
        nlist = 8 # need to add more later
        bits = 4 # number of bits in each centroid
        m = 8 # number of centroid IDs in final compressed vectors
        quantizer = faiss.IndexFlatL2(d)  # this remains the same
        self.index = faiss.IndexIVFPQ(quantizer, d, nlist, m, bits)
                                        # 8 specifies that each sub-vector is encoded as 8 bits

        if not self.index.is_trained:
            print('Training needed')
            self.index.train(sentence_embeddings)
            
        self.index.add_with_ids(sentence_embeddings, ids)

        ### sanity check
        ntotal = self.index.ntotal
        print(f'{ntotal} indexed')

        test_search = "street fighter"
        print(f'Test search term: {test_search}')
        D, I = self.search_by_sentence(test_search, 10) 
        tupleList = list(zip(I[0], D[0]))
        results = sorted(
            [{"index": i, "match": d, "text": f'{df.loc[df["id"] == i]["searchColumn"]}'} for i, d in tupleList if i != -1],
            key=lambda x: x["match"]
        )
        print(results)
        
    def search_by_sentence(self, sentence, k = 5):
        embedding = self.__get_embeddings__([sentence])
        return self.index.search(embedding, k)

    def add_with_id(self, id, sentence):
        sentence_embeddings = self.__get_embeddings__([sentence])
        self.remove_by_id(id)
        return self.index.add_with_ids(sentence_embeddings, [id])

    def remove_by_id(self, id):
        return self.index.remove_ids(np.array([id]))

    def __get_embeddings__(self, sentences):
        sentence_embeddings = self.model.encode(sentences)
        return sentence_embeddings
        
    # def __json_batch_add__():