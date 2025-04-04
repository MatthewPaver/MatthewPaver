from rdflib import Graph, Namespace, Literal, URIRef, BNode
from rdflib.namespace import RDF, RDFS, XSD, DCTERMS
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the output file path
output_file = os.path.join(script_dir, "lab2_rdflib.ttl")


# create the specific namespaces to use
ex = Namespace("http://www.liverpool.ac.uk/examples/beatles#")
dbo = Namespace("https://dbpedia.org/ontology/")
dbpedia = Namespace("http://dbpedia.org/resource/")

g = Graph()

# declare prefixes through bind
g.bind("DCTERMS", DCTERMS)  # Dublin core is declared as a new namespace
g.bind("ex", ex)  # ex is declared as a new namespace
g.bind("dbo", dbo)  # dbo is declared as a new namespace
g.bind("dbpedia", dbpedia) # dbpedia is declared as a new namespace

ex = Namespace("http://www.liverpool.ac.uk/examples/beatles#")
dbo = Namespace("https://dbpedia.org/ontology/")
dbpedia = Namespace("http://dbpedia.org/resource/")

# Bind namespaces to graph
g.bind("DCTERMS", DCTERMS)  
g.bind("ex", ex)
g.bind("dbo", dbo)
g.bind("dbpedia", dbpedia)

# Creating The Beatles group as an entity
beatles = URIRef(ex.Beatles)
g.add((beatles, RDF.type, dbo.Group))

# Creating the album 'With the Beatles'
with_the_beatles = URIRef(ex.With_The_Beatles)
g.add((with_the_beatles, RDF.type, dbo.Studio_Album))

# Adding the name (title) of the album
title = Literal("With the Beatles", datatype=XSD.string)
g.add((with_the_beatles, DCTERMS.title, title))

# Creating George Martin as a producer
george_martin = URIRef(ex.GeorgeMartin)
g.add((george_martin, RDF.type, ex.Producer))

# Defining the artist-property relationship
g.add((with_the_beatles, ex.has_artist, beatles))

# Defining the producer relationship
g.add((with_the_beatles, ex.has_Producer, george_martin))

# Creating a song "It Won't Be Long"
song = URIRef(ex.It_Wont_Be_Long)
g.add((song, RDF.type, ex.Song))
g.add((song, DCTERMS.title, Literal("It Won't Be Long", datatype=XSD.string)))
g.add((song, ex.duration, Literal("2:13", datatype=XSD.string)))
g.add((song, ex.performed_by, beatles))
g.add((song, ex.composed_by, URIRef(ex.JohnLennon)))

# Linking the song to the album
g.add((with_the_beatles, ex.has_track, song))

# Defining Album as a superclass
g.add((ex.Album, RDF.type, RDFS.Class))

# Defining Studio_Album and Live_Album as subclasses of Album
g.add((dbo.Studio_Album, RDFS.subClassOf, ex.Album))
g.add((ex.Live_Album, RDFS.subClassOf, ex.Album))

# Creating band members as individuals
ringo = URIRef(ex.Ringo)
paul = URIRef(ex.PaulMcCartney)
john = URIRef(ex.JohnLennon)
george = URIRef(ex.GeorgeHarrison)

# Assigning them as members of The Beatles
g.add((ringo, RDF.type, ex.BandMember))
g.add((paul, RDF.type, ex.BandMember))
g.add((john, RDF.type, ex.BandMember))
g.add((george, RDF.type, ex.BandMember))

g.add((beatles, ex.has_member, ringo))
g.add((beatles, ex.has_member, paul))
g.add((beatles, ex.has_member, john))
g.add((beatles, ex.has_member, george))


g.serialize(destination=output_file, format="turtle")
print(f"Graph saved to {output_file}")
