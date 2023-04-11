setup_venv:
    poetry install

activate_venv:
    source $(poetry env info --path)/bin/activate

test: activate_venv
    pytest --cov
