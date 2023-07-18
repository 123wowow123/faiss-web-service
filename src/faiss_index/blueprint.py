from jsonschema import validate, ValidationError
from flask import Blueprint, jsonify, request
from sqlalchemy import true
from werkzeug.exceptions import BadRequest
from faiss_index.faiss_index import FaissIndex
import requests
import pandas as pd
from bs4 import BeautifulSoup

blueprint = Blueprint('faiss_index', __name__)

@blueprint.record_once
def record(setup_state):
    df = pd.DataFrame(columns = ['id', 'title', 'description'])

    count = 0
    next_url = 'https://www.chronopin.com/api/main?from_date_time=0001-01-01T00:00:00.000Z'
    while (next_url):
        count = count + 1

        # Making a GET request
        r = requests.get(next_url)

        if r.links.get('next'):
            next_url = r.links['next']['url']
            print(f'Loading pin on page: {count}')
        else:
            print(f'Loaded all pin from total page: {count}')
            next_url = None

        data = r.json()
        for pin in data['pins']:
            # test = next(iter(pin.get('media', [])), {}).get('html', '')
            # if bool(test):
            #     print(test)

            df = pd.concat([df, pd.DataFrame.from_records([
                        {
                            'id' : pin.get('id', ''), 
                            'title' : pin.get('title', ''), 
                            'description' : BeautifulSoup(pin.get('description', ''), 'html.parser').get_text(),
                            'mediaHtmlContent' : BeautifulSoup(next(iter(pin.get('media', [])), {}).get('html', ''), 'html.parser').get_text()
                        }
                    ])
                ])

    blueprint.faiss_index = FaissIndex(
        df
    )

@blueprint.route('/faiss/search')
def search():
    try:
        q = request.args.get('q')
        k = request.args.get('k', type=int)

        D, I = blueprint.faiss_index.search_by_sentence(q, k)
        tupleList = list(zip(I[0], D[0]))
        res = sorted(
            [{"index": int(i), "match": float(d)} for i, d in tupleList if i != -1],
            key=lambda x: x["match"]
        )
        return jsonify({'res': res})

    except (BadRequest, ValidationError) as e:
        print('Bad request', e)
        return 'Bad request', 400

    except Exception as e:
        print('Server error', e)
        return 'Server error', 500


@blueprint.route('/faiss/add', methods=['POST'])
def add():
    try:
        mediaHtmlContent = ''
        json = request.get_json(force=True)
        id = json['id']
        title = json['title']
        description = BeautifulSoup(json.get('description', ''), 'html.parser').get_text()
        media = json['media']
        if bool(media):
            mediaHtmlContent = next(iter(media), {}).get('html', '')
            mediaHtmlContent = BeautifulSoup(mediaHtmlContent, 'html.parser').get_text()

        sentence = f"{title} {description} {mediaHtmlContent}" 
        res = blueprint.faiss_index.add_with_id(id, sentence)
        return jsonify({'res': "success"})

    except (BadRequest, ValidationError) as e:
        print('Bad request', e)
        return 'Bad request', 400

    except Exception as e:
        print('Server error', e)
        return 'Server error', 500


@blueprint.route('/faiss/remove', methods=['DELETE'])
def remove():
    try:
        json = request.get_json(force=True)
        id = json['id']
        res = blueprint.faiss_index.remove_by_id(id)
        return jsonify({'res': "success"})

    except (BadRequest, ValidationError) as e:
        print('Bad request', e)
        return 'Bad request', 400

    except Exception as e:
        print('Server error', e)
        return 'Server error', 500