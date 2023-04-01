from flask import Flask
import os

from internal.blueprint import blueprint as InternalBlueprint
from faiss_index.blueprint import blueprint as FaissIndexBlueprint

app = Flask(__name__)

app.register_blueprint(InternalBlueprint)
app.register_blueprint(FaissIndexBlueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
