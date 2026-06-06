#!/bin/bash
set -e

PACKAGE=$(basename "$(pwd)")
PACKAGE="${PACKAGE#anki-}"

zip -r -Z deflate "${PACKAGE}.ankiaddon" *.json *.py

echo "Created ${PACKAGE}.ankiaddon"
