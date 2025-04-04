"""
Contents:
1. Loads two RDF datasets ("NobelLaureatesKG.ttl" and "scientistsBio.ttl")
   containing Nobel laureate information and scientists’ biographical details.
2. Merges the two datasets by identifying common individuals (using owl:sameAs linking
   to Wikidata URIs) so that each individual present in both datasets gets enriched with
   all available details. The merged graph is saved in Turtle format as "updatedKG.ttl".
3. Executes the following SPARQL queries against the merged graph:
   a. Query 1: List individuals present in both datasets.
   b. Query 2: List Nobel Laureates born in France who won the Chemistry prize with exactly one co-laureate.
   c. Query 3: List Nobel Laureates who won more than one Nobel Prize (with years and categories).
   d. Query 4: List Nobel Laureates (Physics) affiliated with universities in Germany.
4. Prints all query results in a clear, structured format.
"""

import rdflib
from rdflib.namespace import OWL

def main():
    # ---------------------------
    # Step 1: Load RDF Datasets
    # ---------------------------
    print("Loading RDF datasets...")
    nobel_graph = rdflib.Graph()
    bio_graph = rdflib.Graph()
    
    try:
        nobel_graph.parse("NobelLaureatesKG.ttl", format="turtle")
        bio_graph.parse("scientistsBio.ttl", format="turtle")
    except Exception as e:
        print("Error loading files:", e)
        exit(1)
    
    # ---------------------------
    # Step 2: Merge Data
    # ---------------------------
    # The merge is performed by identifying common individuals using owl:sameAs links.
    # In the Nobel KG, laureate resources have owl:sameAs links pointing to Wikidata URIs
    # that are used as subjects in scientistsBio.
    bio_subjects = set(bio_graph.subjects())
    common_uris = set()
    for subj, obj in nobel_graph.subject_objects(predicate=OWL.sameAs):
        if isinstance(obj, rdflib.URIRef) and obj in bio_subjects:
            common_uris.add(obj)
    
    print("Individuals present in both datasets (by Wikidata URI):")
    for uri in sorted(common_uris):
        print(" -", uri)
    
    # Create a new merged graph
    merged_graph = rdflib.Graph()
    
    # Merge data for each common individual:
    # Use the Wikidata URI as the unified subject for biographical details.
    for wd_uri in common_uris:
        # Add all triples from scientistsBio about the individual
        for p, o in bio_graph.predicate_objects(subject=wd_uri):
            merged_graph.add((wd_uri, p, o))
        # Add Nobel KG information for corresponding laureate nodes (linked via owl:sameAs)
        for laureate in nobel_graph.subjects(predicate=OWL.sameAs, object=wd_uri):
            for p, o in nobel_graph.predicate_objects(subject=laureate):
                merged_graph.add((laureate, p, o))
            # Preserve the linking via owl:sameAs
            merged_graph.add((laureate, OWL.sameAs, wd_uri))
    
    # Also, include any remaining triples from the Nobel KG to ensure no prize info is lost
    for triple in nobel_graph:
        merged_graph.add(triple)
    
    # Save the merged knowledge graph to 'updatedKG.ttl'
    merged_graph.serialize("updatedKG.ttl", format="turtle")
    print(f"Merged knowledge graph saved as 'updatedKG.ttl' with {len(common_uris)} common individuals.\n")
    
    # ---------------------------
    # Step 3: Execute SPARQL Queries
    # ---------------------------
    
    # Query 1: Individuals present in both datasets (using owl:sameAs links)
    query1 = """
    PREFIX ns1: <http://data.nobelprize.org/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    SELECT DISTINCT ?name WHERE {
      ?laur a ns1:Laureate ;
            owl:sameAs ?wd .
      ?wd foaf:name ?name .
    }
    ORDER BY ?name
    """
    results1 = merged_graph.query(query1)
    print("Query 1: Individuals present in both datasets:")
    for row in results1:
        print(f" - {row.name}")
    print()
    
    # Query 2: Nobel Laureates born in France who won the Chemistry prize with exactly one co-laureate
    query2 = """
    PREFIX ns1: <http://data.nobelprize.org/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    SELECT DISTINCT ?name WHERE {
      ?laur a ns1:Laureate ;
            foaf:name ?name ;
            dbo:birthPlace <http://data.nobelprize.org/resource/country/France> ;
            ns1:nobelPrize ?np .
      ?np ns1:category ns1:Chemistry .
      ?co a ns1:Laureate ;
          ns1:nobelPrize ?np .
      FILTER(?co != ?laur)
      FILTER NOT EXISTS {
          ?other a ns1:Laureate ;
                 ns1:nobelPrize ?np .
          FILTER(?other != ?laur && ?other != ?co)
      }
    }
    ORDER BY ?name
    """
    results2 = merged_graph.query(query2)
    print("Query 2: Nobel Laureates born in France who won the Chemistry prize with exactly one co-laureate:")
    for row in results2:
        print(f" - {row.name}")
    print()
    
    # Query 3: Nobel Laureates who won more than one Nobel Prize (with years and categories)
    query3 = """
    PREFIX ns1: <http://data.nobelprize.org/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?name (GROUP_CONCAT(CONCAT(?categoryName, " (", STR(?year), ")"); separator=", ") AS ?prizes)
    WHERE {
      ?laureate a ns1:Laureate ;
                foaf:name ?name ;
                ns1:nobelPrize ?prize .
      ?prize ns1:category ?cat ;
             ns1:year ?year .
      # Convert the category URI into a readable name
      BIND( REPLACE(REPLACE(STR(?cat), "^.*/", ""), "_", " ") AS ?categoryName )
    }
    GROUP BY ?laureate ?name
    HAVING (COUNT(DISTINCT ?prize) > 1)
    ORDER BY ?name
    """
    results3 = merged_graph.query(query3)
    print("Query 3: Nobel Laureates who won more than one Nobel Prize (with years and categories):")
    for row in results3:
        print(f" - {row.name}: {row.prizes}")
    print()
    
    # Query 4: Nobel Laureates (Physics) affiliated with universities in Germany
    query4 = """
    PREFIX ns1: <http://data.nobelprize.org/terms/>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    SELECT DISTINCT ?name WHERE {
      ?laureate a ns1:Laureate ;
                foaf:name ?name ;
                ns1:nobelPrize ?np ;
                dbo:affiliation ?univ .
      ?np ns1:category ns1:Physics .
      ?univ dbo:country <http://data.nobelprize.org/resource/country/Germany> .
    }
    ORDER BY ?name
    """
    results4 = merged_graph.query(query4)
    print("Query 4: Nobel Laureates (Physics) affiliated with universities in Germany:")
    for row in results4:
        print(f" - {row.name}")
    print()
    
    print("All queries executed and merged graph saved.")

if __name__ == "__main__":
    main()