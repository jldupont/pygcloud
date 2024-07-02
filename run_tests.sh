#!/bin/bash
# @author: jldupont
#
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest
