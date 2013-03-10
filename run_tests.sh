#!/bin/bash
# Run all tests in project

cd `dirname $0`

python -m unittest discover -s . -p '*_test.py'
