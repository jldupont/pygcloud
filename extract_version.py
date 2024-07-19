#!/usr/bin/env python3
"""
@author: jldupont
"""
try:
    import toml
except Exception:
    print("\033[0;31mThe package 'toml' is required")
    import sys
    sys.exit(1)

pyproject_toml = toml.load("pyproject.toml")

print(pyproject_toml["project"]["version"])
