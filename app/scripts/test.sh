#!/usr/bin/env bash

pytest --cov=app --cov-report=term-missing app/tests "${@}"
