#!/usr/bin/env python3
#+author: Harshvardhan J. Pandit

from rdflib import Graph

G = Graph()
DATAFILES = (
    'alpha.ttl',
    'marketing.ttl'
    )

for data in DATAFILES:
    g = Graph()
    g.load(data, format='ttl')
    G += g

G.serialize('data.ttl', format='ttl')
