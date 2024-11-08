# SPARQL

Usado para interrogar RDFs (triples). É usado para:

- Retirar dados de forma estruturada ou semi-estruturada;
- Explorar relações;
- Complex joins;
- Update da base de dados existente;

## Structure

A seleção e a pesquisa é feita sempre com base em triplos (?subject ?property ?name):

```s
PREFIX rov: <definition of prefixes>

SELECT ?name                        // ?subject ?property ?name

WHERE { ?x rov:legalName ?name }    // ?subject ?property ?name
```

A question mark (?) pode dar match com um resource ou literal. `a` é a abreviatura de `rdf:type`. Exemplos usando o `tutle`:

```sql
SELECT ?name ?fname
WHERE  {
    ?x a ex:Person;
    ex:name ?name ;
    ex:firstname ?fname ;
    ex:author ?y . 
}

PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?x 
WHERE {
    ?x foaf:name "Nuno"@pt ;
    foaf:age "21"^^xsd:integer .
}

PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?person ?name
WHERE {
    ?person foaf:name ?name .
}
VALUES ?name { "Peter" "Pedro" "Pierre" }

PREFIX ex: <http://fe.up.pt/schema#>
SELECT ?person ?name
WHERE {
    ?person rdf:type ex:Person ;
    ex:name ?name ;
    ex:age ?age .
    FILTER (xsd:integer(?age) >= 18)
}
```