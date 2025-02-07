from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

DEFINITION_API_BASE_URL = "http://backend:8081"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    language = request.form.get('language')
    entity = request.form.get('entity')

    if entity and language:
        return redirect(url_for('search_results', entity=entity, language=language))
    
    return redirect(url_for('index'))

@app.route('/search/<entity>/<language>')
def search_results(entity, language):

    # Check for "clear" button action
    if request.args.get('clear') == "true":
        return redirect(url_for('search_results', entity=entity, language=language))

    # Get optional query parameters
    source = request.args.get('source', None)

    # Build API request parameters
    params = {"query": entity, "lang": language, "source": source}

    try:
        response = requests.get(f'{DEFINITION_API_BASE_URL}/search/definition', params=params)
        response.raise_for_status()
        results = response.json()

        return render_template('results.html', entity=entity, language=language, results=results)
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching definition for '{entity}': {e}. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True, port=8082)
