from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///receitas.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Receitas(Base):
    __tablename__ = "receitas"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(80), index=True)
    ingredientes = Column(String(500))
    preparo = Column(String(1500))

    def __repr__(self):
        return '<Receita {}'.format(self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)


init_db()