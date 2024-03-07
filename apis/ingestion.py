import tempfile
from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
from langchain.document_loaders.git import GitLoader

app = Flask(__name__)
CORS(app)

ingestion_blueprint = Blueprint('ingestion', __name__, url_prefix='/codebits')


@ingestion_blueprint.route('/api/v1/ingest', methods=['POST'])
def ingest_repo():
    args = request.json
    repo_url = args['repo_url']
    branch = args['branch']
    print(f"GitLoader called with repo_url: {repo_url}\nand branch: {branch}")
    temp_dir_path = tempfile.mkdtemp()
    data = GitLoader(
        repo_path=temp_dir_path,
        branch=branch,
        clone_url=repo_url
    ).load()
    print("-"*80)
    for d in data:
        print(d.metadata['file_name'])
    print("-"*80)
    print(f"Repo cloned at {temp_dir_path}")

    return jsonify({"result": "success", "count": len(data)})
