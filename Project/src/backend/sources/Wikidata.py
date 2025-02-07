from .Source import Source
import requests

URL = "https://query.wikidata.org/sparql"

QUERY = """
    SELECT ?entity ?description ?lang
    WHERE {{
        ?entity rdfs:label "{entity}"@{lang} .
        ?entity schema:description ?description .
        BIND(LANG(?description) AS ?lang)
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE]" . }}
    }}
    LIMIT 25
"""

class WikidataSource(Source):

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
                            'lang': result['lang'],
                            'source': 'wikidata'
                        })
                        seen.add(key)

        return all
    
    def format_output(entity: str, data: list) -> list:

        results = []
        seen = set()

        for item in data['results']['bindings']:
            entity = item['entity']['value']
            description = Source.sanitize_text(item['description']['value'])
            lang = item['lang']['value']
            
            key = (entity, description, lang)

            if key not in seen:
                results.append({'entity': entity, 'description': description, 'lang': lang, 'source': 'wikidata'})
                seen.add(key)

        return results

    def search_entity(entity: str, lang: str) -> list:
        
        if lang is None:
            
            results = []
            for language in Source.LANGUAGES:
                results.extend(WikidataSource.search_entity(entity, language))

            return results

        elif lang in Source.LANGUAGES:
            query = QUERY.format(entity = entity, lang = lang)
        
        else: 
            return []
    
        params = {
            'format': 'json',
            'query': query
        }
        
        response = requests.get(URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return WikidataSource.format_output(entity, data)

        else:
            return []

    @staticmethod
    def search(entity: str, lang: str) -> list:
        results = WikidataSource.search_entity(entity, lang)
        return WikidataSource.group(results)