#!/usr/bin/env bash

echo "collect all vocab files into a single file"
riot ../dpcat.ttl vocab/* > vocab.ttl

echo "run RDFS inference over data using vocab"
riot --rdfs vocab.ttl EDPS/*.ttl > data.ttl
riot vocab.ttl data.ttl > data_combined.ttl

echo "validate data file using DCAT-AP shacl shapes"
shaclvalidate.sh -shapesfile ../shapes/dcat-ap_2.0.1_shacl_shapes.ttl -datafile data_combined.ttl
echo "validate data file using DPCat shacl shapes"
shaclvalidate.sh -shapesfile ../shapes/dpcat_shapes_mandatory.ttl -datafile data_combined.ttl