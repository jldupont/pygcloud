#!/bin/bash

git add .
git commit -m "$1"
git push
git tag $1 HEAD
git push --tags
