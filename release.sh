#!/bin/bash

VERSION=`extract_version.py`

git add .
git commit -m "$1"
git push
git tag $VERSION HEAD
git push --tags
