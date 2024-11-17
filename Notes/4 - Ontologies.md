# Ontologies

RDF é muito fraca a nível de restrições. Não dá para explicitar, por exemplo:

- Que uma pessoa tem exatamente dois pais (cardinalidade).
- Reuniões, interseções ou complementos de classes.
- Propriedades transitivas, simétricas, ou inversas.
- Restrições específicas de domínio (e.g., `person -> person` ou `elephant -> elephant`).

Ontologias fornecem as regras e o conhecimento sobre que relações fazem sentido dentro de um sistema.

- **Definição:** são formais (*machine readable*), especificações explícitas e partilhadas:

- Descrevem o que existe num domínio e como as entidades podem ou não se relacionar.
- Facilitam a partilha e reutilização de conhecimento.
- Permitem separar o conhecimento do domínio do conhecimento operacional.

### Importância de Ontologias

1. Melhoram a definição de recursos, tornando-os mais processáveis por máquinas.
2. Facilitam a troca de suposições sobre um domínio.
3. Ajudam na separação entre conhecimento de domínio e conhecimento operacional.
4. Fornecem uma referência comum para definir conceitos, relações e axiomas.
5. Permitem um entendimento consistente de um domínio.

### Passos para Partilha de Conhecimento

- **Símbolos comuns (sintaxe):** Definir como os dados serão expressos.
- **Acordo semântico:** Estabelecer significados claros para conceitos.
- **Classificação:** Organizar conceitos (e.g., taxonomias).
- **Associações:** Relacionar conceitos usando tesauros.
- **Regras:** Definir relações válidas entre conceitos.

### Tipos de Ontologias

1. **Ontologias de Domínio:** Focam em áreas específicas (e.g., medicina, mecânica).
2. **Ontologias de Meta-dados:** Descrevem conteúdos de fontes na web.
3. **Ontologias Genéricas:** Abrangem conhecimento válido em múltiplos domínios.
4. **Ontologias de Métodos/Tarefas:** Suportam tarefas ou métodos específicos.

### Elementos das Ontologias

- **Conceitos (classes):** Representam entidades ou objetos do domínio.
- **Propriedades (slots):** Caracterizam os conceitos.
- **Restrições:** Limitam cardinalidade, tipo ou domínio.
- **Relações:** Definem como os conceitos estão conectados.
- **Instâncias:** Exemplos concretos dos conceitos.

## Web Ontology Language (OWL)

OWL é uma recomendação do W3C para representação de ontologias na web. É uma extensão do RDF(S) e possui mais funcionalidades:

- Restrições de cardinalidade.
- Propriedades inversas, simétricas e transitivas.
- Definições de igualdade e disjunção de conceitos.

### Características do OWL

- Possui semântica formal e suporte eficiente para raciocínio.
- Baseado em lógica descritiva (*Description Logic*).
- É organizado em três sub-linguagens:

  1. **OWL Full:** Mais expressiva, mas menos eficiente.
  2. **OWL DL:** Balanceia expressividade e decidibilidade.
  3. **OWL Lite:** Focada em aplicações simples.

### Principais Conceitos do OWL

- **Propriedades Transitiva, Simétrica e Inversa:**
  - `transitive`: Se \( P(x, y) \) e \( P(y, z) \), então \( P(x, z) \).
  - `symmetric`: Se \( P(x, y) \), então \( P(y, x) \).
  - `inverseOf`: Se \( P1(x, y) \), então \( P2(y, x) \).
- **Cardinalidade:**
  - `cardinality`: Restrições exatas.
  - `minCardinality` e `maxCardinality`: Limites mínimo e máximo.
- **Classes Compostas:**
  - `intersectionOf`, `unionOf`, `complementOf`: Operações entre classes.
- **Equivalência e Disjunção:**
  - `equivalentClass`, `disjointWith`: Definições de igualdade ou exclusividade.

### Exemplo de Ontologia

#### African Wildlife Ontology (AWO)

- Representa conhecimento sobre vida selvagem.
  - Giraffes são herbívoros.
  - Herbívoros são animais.
- Pode ser descrita em lógica descritiva ou implementada com ferramentas como `Protégé`.

#### Código OWL Exemplo

```xml
<owl:Class rdf:ID="Person" />
<owl:Class rdf:ID="Woman">
    <rdfs:subClassOf rdf:resource="#Person"/>
</owl:Class>

<owl:ObjectProperty rdf:ID="hasChild">
    <rdfs:domain rdf:resource="#Person"/>
    <rdfs:range rdf:resource="#Person"/>
</owl:ObjectProperty>

<owl:Class rdf:ID="Mother">
    <rdfs:subClassOf>
        <owl:Restriction>
            <owl:onProperty rdf:resource="#hasChild"/>
            <owl:someValuesFrom rdf:resource="#Person"/>
        </owl:Restriction>
    </rdfs:subClassOf>
</owl:Class>
```