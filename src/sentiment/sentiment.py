from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

class Sentiment:

    def __init__(self):
        # https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment
        MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL)
        self.config = AutoConfig.from_pretrained(MODEL)

        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL)
        self.tokenizer.save_pretrained(MODEL)
        self.model.save_pretrained(MODEL)

    def getSentiment(self, sentence):
        result = 0
        text = self.__preprocess__(sentence)
        encoded_input = self.tokenizer(text, return_tensors='pt')
        output = self.model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        for i in range(scores.shape[0]):
            l = self.config.id2label[ranking[i]]
            s = scores[ranking[i]]

            if l == "positive":
                result += float(s) * 1
            elif l == "neutral":
                result += float(s) * 0
            elif l == "negative":
                result += float(s) * -1

        return result

    def __preprocess__(self,text):
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)
