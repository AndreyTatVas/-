from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("select 'Hello, World!' union select 'Hello' union select 'World'"))
    print(result.scalars().all())
