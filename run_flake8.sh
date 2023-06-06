#!/bin/bash

SRC_DIR=./

python3 -m flake8 --ignore=D203 ${SRC_DIR}/substitute/substitute.py
