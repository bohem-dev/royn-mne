# Makefile

dev:
	source .venv/bin/activate && npm run tauri dev

install:
	python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && npm install

# run-python:
# 	source .venv/bin/activate && python backend/core.py '{"path": "data/sample_raw.fif"}'
