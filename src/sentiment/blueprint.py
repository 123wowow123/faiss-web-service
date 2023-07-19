from jsonschema import validate, ValidationError
from werkzeug.exceptions import BadRequest
from flask import Blueprint, jsonify, request
from sentiment.sentiment import Sentiment
from bs4 import BeautifulSoup

blueprint = Blueprint('sentiment', __name__)

@blueprint.record_once
def record(setup_state):
    blueprint.Sentiment = Sentiment()
    score = blueprint.Sentiment.getSentiment("T'estimo!")
    print(score)

@blueprint.route('/sentiment', methods=['POST'])
def getSentiment():
    try:
        mediaHtmlContent = ''
        json = request.get_json(force=True)
        title = json.get('title', '')
        description = BeautifulSoup(json.get('description', ''), 'html.parser').get_text()
        media = json['media']
        if bool(media):
            mediaHtmlContent = next(iter(media), {}).get('html', '')
            mediaHtmlContent = BeautifulSoup(mediaHtmlContent, 'html.parser').get_text()

        sentence = f"{title} {description} {mediaHtmlContent}" 
        score = blueprint.Sentiment.getSentiment(sentence)
        return jsonify({'score': score})

    except (BadRequest, ValidationError) as e:
        print('Bad request', e)
        return 'Bad request', 400

    except Exception as e:
        print('Server error', e)
        return 'Server error', 500
