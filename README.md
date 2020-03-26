Maintains a listing of managed sites and the resources they depend on.

Requires a Python 3.7 environment. Dependencies can be installed via:

`pip install -r requirements.txt`

The required environment variables are defined in api/settings.py (DATABASE_URL at the very least). Once defined, the
database tables can be set up by running `api/migrate.py`

The application can be started with e.g. `uvicorn main:api --host 0.0.0.0 --port 8000`

Once it's running, th documentation for the API will be available at the following URLs:

* http://DATABASE_URL:LISTEN_PORT/docs (Swagger UI)
* http://DATABASE_URL:LISTEN_PORT/redoc (ReDoc)

The Swagger UI documentation allows you to make API calls via its web interface.
