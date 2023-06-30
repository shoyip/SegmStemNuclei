#!/bin/bash

# Create data and raw data folder
mkdir -p ./data/raw
mkdir -p ./data/interim/{cutouts,tagged_cutouts,gt}
mkdir -p ./data/preprocessed/{img,gt}
mkdir -p ./data/dataset/train/{img,gt}
mkdir -p ./data/dataset/test/{img,gt}
