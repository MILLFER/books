print("Hola mundo")

def get_db():
    db =getattr(g, "_database", None)
    if db is None:
        db= psycopg2.connect


@app.teardown_appconnect: