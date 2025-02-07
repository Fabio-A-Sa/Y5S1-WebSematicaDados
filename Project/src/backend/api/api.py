from sources import DBPediaSource, WikidataSource
from graph import GraphCreator, GraphQueryHandler

class API:

    @staticmethod
    def get_definition(data: list, lang: str) -> str:
        if not lang:
            return None
        else:
            for element in data.values():
                for definition in element:
                    if definition['lang'] == lang:
                        return definition['description']
        return None

    @staticmethod
    def search(query: str, lang: str, source: str) -> dict:

        if query:

            lang = lang.lower() if lang else None
            source = source.lower() if source else None

            # Getting data from the selected sources
            if source == 'wikidata':
                wikidata_data = WikidataSource.search(query, lang)
                dbpedia_data = {}
            elif source == 'dbpedia':
                dbpedia_data = DBPediaSource.search(query, lang)
                wikidata_data = {}
            else:
                wikidata_data = WikidataSource.search(query, lang)
                dbpedia_data = DBPediaSource.search(query, lang)

            # Creating the graph
            graph_creator = GraphCreator()
            data = graph_creator.merge_results(wikidata_data, dbpedia_data)
            graph = graph_creator.create(query, data)

            # Creating the handler
            query_handler = GraphQueryHandler(graph)

            # Extract main definition
            definition = API.get_definition(data, lang)

            # Results format
            return {
                'user_input': query,
                'definition': definition,
                'false_friends': query_handler.get_false_friends(), 
                'ambiguities': query_handler.get_ambiguities(),
                'language_guess_probabilities': query_handler.get_language_probabilities(),
                'raw_results': data,
            }

        # Avoiding frontend crashes
        else:
            return {
                'user_input': query,
                'definition': None,
                'false_friends': [], 
                'ambiguities': [],
                'language_guess_probabilities': [],
            }
