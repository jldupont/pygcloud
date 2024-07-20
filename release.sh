#!/bin/bash

set -e

VERSION=`./extract_version.py`

git add .
git commit -m "${VERSION}"
git push
git tag $VERSION HEAD
git push --tags
