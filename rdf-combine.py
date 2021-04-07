#!/usr/bin/env python3
#+author: Harshvardhan J. Pandit

from rdflib import Graph

G = Graph()
DATAFILES = (
    'datasets/alpha.ttl',
    'datasets/marketing.ttl',
    'datasets/customer_service.ttl',
    'datasets/hr.ttl',
    )

for data in DATAFILES:
    g = Graph()
    g.load(data, format='ttl')
    G += g

G.serialize('data-combined.ttl', format='ttl')
