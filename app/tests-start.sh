#! /usr/bin/env bash
set -x

python app/tests_pre_start.py

bash ./scripts/test.sh "$@"