#!/usr/bin/env python3
"""
task2_solution.py

A Python solution for Task 2. 
- Loads an RDF graph G (with classes, properties, etc.).
- Computes RDFS entailments using `owlrl`.
- Saves the entailed graph to T2Entailed.ttl.
- Verifies that our 4 new inferred triples (Task 2.A) appear.
"""

from rdflib import Graph, Namespace, RDF, RDFS
import owlrl  # for RDFS reasoning

def load_graph(file_path: str, file_format: str = "turtle") -> Graph:
    """
    loads an RDF file into an rdflib Graph. 
    Prints how many triples were loaded.
    """
    g = Graph()
    g.parse(file_path, format=file_format)
    print(f"Loaded '{len(g)}' triples from '{file_path}'.")
    return g

def compute_rdfs_entailment(g: Graph) -> Graph:
    """
    Applies RDFS closure to 'g' using owlrl's RDFS_Semantics,
    returns a new Graph containing all entailed triples.
    """
    closure_g = Graph()
    closure_g += g

    # Perform RDFS reasoning (including axiomatic RDFS triple rules)
    owlrl.DeductiveClosure(
        owlrl.RDFS_Semantics, 
        axiomatic_triples=True, 
        datatype_axioms=False
    ).expand(closure_g)

    print(f"After RDFS reasoning, we have '{len(closure_g)}' triples.")
    return closure_g

def add_subclass_is_class_rule(g: Graph):
    """
    If X rdfs:subClassOf Y, then X is recognised as (rdf:type rdfs:Class).
    Adding the extra statements manually
    """
    new_triples = []
    for (x, _, _) in g.triples((None, RDFS.subClassOf, None)):
        new_triples.append((x, RDF.type, RDFS.Class))
    for t in new_triples:
        g.add(t)
    if new_triples:
        print(f"Added {len(new_triples)} new statements for 'subclass => class' rule.")

def save_graph(g: Graph, out_file: str):
    """
    Saves the entailed graph to a Turtle file.
    Also prints how many total triples there are.
    """
    g.serialize(destination=out_file, format='turtle')
    print(f"Entailed graph saved to '{out_file}' with {len(g)} triples.")

# Part 2 C - Verifying the 4 dervived triples
def verify_inferred_triples(g: Graph, triples_to_check):
    """
    For each triple in 'triples_to_check' (list of (s,p,o)),
    check if it's in 'g'. Print True/False results.
    """
    print("\nVerifying the 4 inferred triples from Task 2.A:")
    for (s, p, o) in triples_to_check:
        is_present = (s, p, o) in g
        print(f"  {s} {p} {o} => {is_present}")

if __name__ == "__main__":
    # 1) Load the original Graph G.
    G_FILE = "task2_data.ttl"
    base_graph = load_graph(G_FILE, file_format="turtle")

    # 2) Compute RDFS entailment
    entailed_graph = compute_rdfs_entailment(base_graph)

    # 3) Apply the 'subclasses are classes' extension
    add_subclass_is_class_rule(entailed_graph)
    print(f"After extension, graph has {len(entailed_graph)} triples.\n")

    # 4) Save final entailed graph as T2Entailed.ttl
    save_graph(entailed_graph, "T2Entailed.ttl")

    # 5) Verify the 4 new inferred triples from Task 2.A
    EX = Namespace("http://example.org/")
    # check exactly these four:
    check_these = [
        (EX.MilesDavis, RDF.type, EX.Person),
        (EX.BlueNoteRecords, RDF.type, EX.Label),
        (EX.CoolJazz, RDF.type, EX.Genre),
        (EX.CoolJazz, RDF.type, RDFS.Class),
    ]
    verify_inferred_triples(entailed_graph, check_these)
