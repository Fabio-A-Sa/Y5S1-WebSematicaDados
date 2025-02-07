# Wordify - WSDL Project - Checkpoint 1

## Group Members

- Fábio Araújo de Sá (up202007658@up.pt)
- Marcos Rafael Peixoto Aires (up202006888@up.pt)
- Pedro Pereira Ferreira (up202004986@up.pt)

## Description

The group has proposed to develop a system that disambiguate existent entities in knowledge bases (that can be represented in different languages), using Web Semantic and Linked data principles, concepts, and technologies. This will be useful as it will help a computer (and humans) to precisely perceives what entity is being referred, in a certain context.

## Motivation

Humans always tried to communicate in a clear and simple way with others, as well as with computers. However, it is a critical, inherent problem of the languages used by humans to communicate, is that there are ambiguous.

It is easy to think of a word, or something that can have different meanings, for different contexts: for instance, when someone is talking about a "balance", this word can mean the state in which opposing forces, or can also mean the object used to measure weights. So, when a person is looking on the web the meaning or a representation of the entity "balance", what content should appear?

Another problem faced with natural languages is the fact that the same word can also have divergent meanings in different languages: for instance the word "vela" in italian is the same as "sail", but means "candle" in Spanish. As a consequence, it becomes difficult to connect the same words in different languages, if we are using the words to represent entities on web.

Finally, another motivating example is the regionalisms that exist in languages, which makes words vary its meaning accross the location: for instance, a "garoto" in Porto is the same word for "kid", but in Lisbon can mean a coffee. If this word were search on Web, what content should appear in different portuguese locations?

With the exposure of this problems, it is clear that if it was a system that manipulates a knowledge base in a way that could clarify the entities search, according to the multilanguages charactheristics, contexts, and locations of where it is being used. To fulfill this purpose, Wordify was built.

## Data and Resources

Wordify would be sustained with the following knwoledge databases:

- Wikidata, as it is vast and complete knowledge bases, used in various purposes;

- DBpedia, to obtain multilingual linked data from Wikipedia;

- Wikipedia, to obtain the entities;

## Challenges

The development of this system presents a number of challenges. Firstly, the vast number of potential entities that could be ambiguous could present a challenge, as it may hinder the system from automatically and consistently disambiguating entities. While having significant amounts of data to work with is advantageous, it can also present a challenge when compared to having restricted access to them. This can impede the automation of linking similar entities, which is crucial for clarifying the meaning of the same entity across different content. It can also affect the system's overall performance.

Finally, there are instances where a word may exist in one language but cannot be automatically associated with another representation in another entity in a different language. The word "saudade," for instance, means missing someone. This presents a challenge to achieving the proposed objectives.

Despite these challenges, the project can still be completed successfully and achieve the proposed objectives.

## Development Roadmap

The group planned to develop Wordify in the following milestones:

- Milestone 1 (due to 6/11/2024) : at this point, the system must be able to retrieve the entity(ies) searched;

- Milestone 2 (due to 20/11/2024) : at this point, the system should be capable of linking the various entities according to the following aspects:

 - Meaning / context (to be done until 20/11/2024);
 - Different languages (to be done until 20/11/2024);
 - Regionalisms (to be done until 20/11/2024);

- Milestone 3 (4/12/2024) : at this point, Wordify must follow the 4 Tim Berners-Lee Linking Data principles (RDF e OWL).
Note: it is quite probable that this milestone is achieved in parallel with Milestone 1 and/or 2.

- Milestone 4 (18/12/2024) : at this point, Wordify has a simple and user-friendly GUI. Documentation and presentation should also be ready.