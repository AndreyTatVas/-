from sqlalchemy import create_engine, ForeignKey, BigInteger, select
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column, Mapped, Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class UserModel(AbstractModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()


class AddressesModel(AbstractModel):
    __tablename__ = "addresses"

    email: Mapped[str] = mapped_column(nullable=False)
    user_id = mapped_column(ForeignKey('users.id'))


with Session(engine) as session:
    with session.begin():
        AbstractModel.metadata.create_all(engine)

        user = UserModel(
            user_id=1,
            name='Jack',
            fullname='Jack Cow'
        )
        session.add(user)

    with session.begin():
        res = session.execute(select(UserModel).where(UserModel.user_id == 1))
        user = res.scalar_one_or_none()
        print(user)

    with session.begin():
        AddressesModel.metadata.drop_all(engine)
