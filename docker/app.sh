#!/bin/bash

alembic upgrade head

pytest tests/

python src/main.py