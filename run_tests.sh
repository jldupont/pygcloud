#!/bin/bash
# @author: jldupont
#
export PYTEST_ADDOPTS="--color=yes"
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest $1
