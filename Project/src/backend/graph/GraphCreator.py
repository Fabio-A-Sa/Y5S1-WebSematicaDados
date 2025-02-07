from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, SKOS, OWL

ENTITY = Namespace("http://example.org/entity#")

class GraphCreator:
    
    def __init__(self): return
    
    def create_skos_owl_graph(self, input: str, results: list) -> list:

        g = Graph()

        # Namespace definition
        g.bind("skos", SKOS)
        g.bind("owl", OWL)
        g.bind("entity", ENTITY)

        # Create a new SKOS 
        g.add((ENTITY.source, RDF.type, OWL.Ontology))

        # The root is the main concept
        root = URIRef(f"http://wordify.com/search/{input}")
        g.add((root, RDF.type, SKOS.Concept))

        # For each entity, create an edge
        for entity_uri in results.keys():
            
            # Associating the entity with the root concept
            entity = URIRef(entity_uri)
            g.add((entity, SKOS.related, root))
            
            # For each possible definition, create an edge
            for definition in results[entity_uri]:

                lang = definition['lang']
                description = definition['description']
                description_literal = Literal(description, lang=lang)
                source = Literal(definition['source'])
                
                # Associating the definition@language with the entity
                g.add((description_literal, SKOS.definition, entity)) 

                # Associating the source with the entity
                g.add((source, ENTITY.source, entity))

        return g

    def define_false_friend_axioms(self, graph: Graph) -> Graph:
        
        # Axiom OWL to define False Friends
        graph.add((ENTITY.falseFriend, RDF.type, OWL.Class))

        # Getting all entities
        entities = list(graph.subjects(predicate=SKOS.related))

        for x in range(0, len(entities) - 1):
            for y in range(x + 1, len(entities)):

                entity1 = entities[x]
                entity2 = entities[y]
                
                definitions1 = list(graph.objects(subject=entity1, predicate=SKOS.definition))
                definitions2 = list(graph.objects(subject=entity2, predicate=SKOS.definition))

                langs_1 = [definition.language for definition in definitions1]
                langs_2 = [definition.language for definition in definitions2]
                
                # If there is at least two different definitions in the the different languages
                # This two entities are false friends
                if not (len(langs_1) == 1 and len(langs_2) == 1 and langs_1[0] == langs_2[0]):
                    graph.add((entity1, ENTITY.falseFriend, entity2))
        
        return graph

    def merge_results(self, wikidata_data: dict, dbpedia_data: dict) -> dict:       
        return {**wikidata_data, **dbpedia_data}
    
    def create(self, input: str, data: dict) -> list:
        graph = self.create_skos_owl_graph(input, data)
        return self.define_false_friend_axioms(graph)