import requests
from .Source import Source

SPARQL_URL = "https://dbpedia.org/sparql"

DBPEDIA_QUERY = """
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?entity ?abstract ?abstractLang WHERE {{
        ?entity rdfs:label "{entity}"@{lang} .
        ?entity dbo:abstract ?abstract .
        BIND(LANG(?abstract) AS ?abstractLang) .
    }} LIMIT 25
"""

class DBPediaSource(Source):
    
    @staticmethod
    def group(results):
        all = {}
        entities = list(set([r['entity'] for r in results]))

        for entity in entities:
            all[entity] = []
            seen = set()

            for result in results:

                if result['entity'] == entity:
                    key = (result['description'], result['lang'])
                    if key not in seen:
                        all[entity].append({
                            'description': result['description'],
                            'lang': result.get('lang'),
                            'source': 'dbpedia'
                        })
                        seen.add(key)

        return all

    @staticmethod
    def formatOutput(data: list) -> list:
        results = []
        seen = set()

        for item in data['results']['bindings']:
            entity = item['entity']['value']

            abstract = item.get('abstract', {}).get('value', None)
            abstract_lang = item.get('abstractLang', {}).get('value', None)

            key = (entity, abstract, abstract_lang)

            if key not in seen:
                results.append({
                    'entity': entity,
                    'description': abstract,
                    'lang': abstract_lang,
                    'source': 'dbpedia'
                })
                seen.add(key)

        return results

    @staticmethod
    def consultEntity(entity: str, lang: str) -> list:

        if lang is None:
            results = []
            for language in Source.LANGUAGES:
                results.extend(DBPediaSource.consultEntity(entity, language))
            return results

        elif lang in Source.LANGUAGES:
            query = DBPEDIA_QUERY.format(entity = entity.capitalize(), lang = lang)
        
        else:
            return []

        query = DBPEDIA_QUERY.format(entity=entity.capitalize(), lang=lang)

        params = {
            'format': 'json',
            "query": query
        }

        response = requests.get(SPARQL_URL, params=params)

        if response.status_code == 200:
            try:
                data = response.json()
                return DBPediaSource.formatOutput(data)
            except Exception as e:
                print(f"Error parsing JSON response: {e}")
                print(response.text)
                return []
        else:
            print(f"SPARQL query failed with status code {response.status_code}")
            print(response.text)
            return []

    @staticmethod
    def search(entity: str, lang: str) -> dict:
        results = DBPediaSource.consultEntity(entity, lang)
        return DBPediaSource.group(results)
