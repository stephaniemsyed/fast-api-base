# fast-api-base
A basic skeleton for Rest APIs. 

Uses: 
* https://python-poetry.org/ for dependency management
* https://fastapi.tiangolo.com/ framework
* https://www.dynaconf.com/ for config 

## Local Dev
1. Activate virtual env: `eval $(poetry env activate)`
1. Install dependencies: `poetry install`
1. To run the server in dev mode: `poetry run uvicorn app.main:app --reload`
1. Run tests with `pytest` [full docs](https://docs.pytest.org/en/stable/getting-started.html)