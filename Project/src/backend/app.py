from flask import Flask, request, jsonify
from api import API

app = Flask(__name__)

@app.route('/search/definition', methods=['GET'])
def definition():
    
    query = request.args.get('query')
    lang = request.args.get('lang')
    source = request.args.get('source')

    results = API.search(query, lang, source)
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True, port=8081)