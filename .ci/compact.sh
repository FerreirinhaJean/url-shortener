#!/bin/bash


ZIP_NAME="url_shortener.zip"


BASE_DIR=$(dirname "$0")


zip -r "$ZIP_NAME" . \
    -x "*.pyc" \
    -x "__pycache__/*" \
    -x "**/__pycache__/*" \
    -x ".venv/*" \
    -x ".venv/**" \
    -x "$ZIP_NAME"
