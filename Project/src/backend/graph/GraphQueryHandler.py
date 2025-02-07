from rdflib import Graph
from rdflib.plugins.sparql import prepareQuery

class GraphQueryHandler:
    
    def __init__(self, graph: Graph):
        self.graph = graph
    
    def get_false_friends(self) -> list:
       
        query = prepareQuery(
            """
            PREFIX entity: <http://example.org/entity#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            
            SELECT DISTINCT ?entity1 ?definition1 ?lang1 ?source1 ?entity2 ?definition2 ?lang2 ?source2
            WHERE {
                ?entity1 entity:falseFriend ?entity2 .
                ?definition1 skos:definition ?entity1 .
                ?definition2 skos:definition ?entity2 .
                ?source1 entity:source ?entity1 .
                ?source2 entity:source ?entity2 .
                BIND(LANG(?definition1) AS ?lang1)
                BIND(LANG(?definition2) AS ?lang2)
                FILTER (?lang1 != ?lang2)
            }
            """
        )

        false_friends = []
        results = self.graph.query(query)
        
        for row in results:
            false_friends.append({
                "entity1": str(row.entity1),
                "definition1": str(row.definition1),
                "lang1": row.definition1.language if row.definition1.language else None,
                "source1": str(row.source1),
                "entity2": str(row.entity2),
                "definition2": str(row.definition2),
                "lang2": row.definition2.language if row.definition2.language else None,
                "source2": str(row.source2),
            })

        return false_friends

    def get_ambiguities(self) -> list:

        query = prepareQuery(
            """
            PREFIX entity: <http://example.org/entity#>
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            
            SELECT DISTINCT ?lang1 ?entity1 ?definition1 ?source1 ?entity2 ?definition2 ?source2
            WHERE {
                ?definition1 skos:definition ?entity1 .
                ?definition2 skos:definition ?entity2 .
                ?source1 entity:source ?entity1 .
                ?source2 entity:source ?entity2 .
                BIND(LANG(?definition1) AS ?lang1)
                BIND(LANG(?definition2) AS ?lang2)
                FILTER (?lang1 = ?lang2)
                FILTER (?entity1 != ?entity2)
                FILTER (STR(?entity1) < STR(?entity2))
            }
            """
        )

        ambiguities = []
        results = list(self.graph.query(query))

        for row in results:
            ambiguities.append({
                "lang": row.definition1.language if row.definition1.language else None,
                "entity1": str(row.entity1),
                "source1": str(row.source1),
                "definition1": str(row.definition1),
                "entity2": str(row.entity2),
                "definition2": str(row.definition2),
                "source2": str(row.source2),
            })

        return ambiguities
    
    def get_language_probabilities(self) -> list:

        query = prepareQuery(
            """
            PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

            SELECT (LANG(?definition) AS ?lang) (COUNT(?definition) AS ?occurrences)
            WHERE {
                ?definition skos:definition ?entity .
            }
            GROUP BY LANG(?definition)
            """
        )

        results = self.graph.query(query)

        languages = [
            {"language": str(row.lang), "occurrences": int(row.occurrences)}
            for row in results
            if row.lang is not None
        ]

        total = sum([int(occ['occurrences']) for occ in languages])
        probabilities = [
            {"language": language['language'], "occurrences": language['occurrences'], "probability": round((language['occurrences'] / total) * 100, 2)}
            for language in languages
        ]
        
        return sorted(probabilities, key=lambda x: x['occurrences'], reverse=True)
