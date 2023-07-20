from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
from bs4 import BeautifulSoup

class Sentiment:

    def __init__(self):
        # https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment
        MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
        # MODEL = f"mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL)
        self.config = AutoConfig.from_pretrained(MODEL)

        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL)

        ensure_tokenizer_max_length(self.tokenizer, self.model)
        # self.tokenizer.save_pretrained(MODEL)
        # self.model.save_pretrained(MODEL)

    def cleanAndGetSentiment(self, json):
        mediaHtmlContent = ''
        title = json.get('title', '')
        description = BeautifulSoup(json.get('description', ''), 'html.parser').get_text()
        media = json.get('media')
        if bool(media):
            mediaHtmlContent = next(iter(media), {}).get('html', '')
            mediaHtmlContent = BeautifulSoup(mediaHtmlContent, 'html.parser').get_text()

        sentence = f"{title} {description} {mediaHtmlContent}" 
        score = self.getSentiment(sentence)
        return score

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
        maxWords = 300
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text[:maxWords])
    


MAX_SEQUENCE_LENGTH = 512
"""For now we don't need texts longer than this, ever."""

def ensure_tokenizer_max_length(tokenizer, model):
    """Ensure tokenizer has a max. length defined (#tokens) at which to truncate.

    Unfortunately many tokenizers don't seem to have this defined by default, which will
    lead to failure when using their resulting non-truncated outputs in a model which does
    have a maximum size.
    """
    max_length = getattr(tokenizer, "model_max_length", None)
    if max_length is None or max_length > MAX_SEQUENCE_LENGTH:
        print(f"Tokenizer's model_max_length={max_length} probably wasn't set correctly.")

        default_lengths = getattr(tokenizer, "max_model_input_sizes", {})
        if default_lengths:
            k, v = next(iter(default_lengths.items()))
            print(f"Found and will use default max length for model {k}={v}.")
            max_length = v
        else:
            model_len = model.config.to_dict().get("max_position_embeddings")
            if model_len is not None:
                print(f"Found no default max length but model defines max_position_embeddings={model_len}")
                if model_len in (514, 130):
                    model_len -= 2
                    print(f"Corrected max length to be {model_len}.")
                max_length = model_len
            else:
                print(f"Couldn't determine appropriate max length. Will use default of {MAX_SEQUENCE_LENGTH}.")
                max_length = MAX_SEQUENCE_LENGTH

    tokenizer.model_max_length = max_length
