from sqlalchemy import create_engine, text, Connection, MetaData, Table, Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
metadata = MetaData()

user_table = Table(
    "Users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", BigInteger, unique=True),
    Column("fullname", String)
)

addresses = Table(
    "Addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("Users.user_id")),
    Column("email", String, nullable=False)
)

metadata.create_all(engine)
metadata.drop_all(engine)
