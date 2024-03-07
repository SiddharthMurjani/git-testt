from flask import Flask
from flask_cors import CORS
from apis.ingestion import ingestion_blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(ingestion_blueprint)
app.run(threaded=True, port=5001)
