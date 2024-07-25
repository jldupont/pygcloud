#!/bin/bash
# @author: jldupont
#

export PYTEST_ADDOPTS="--color=yes"
export PYTHONPATH=$PYTHONPATH:$(pwd)/src

watch --color -n 4 pytest
