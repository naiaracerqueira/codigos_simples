from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, Column, String, MetaData, Integer
import pymysql


url = "mysql+pymysql://user:pass@host/database"

engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

metadata = MetaData(bind=engine)

class CreateTable(Base):
    __tablename__ = "outro_teste"
    cadastro = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(20))
    cpf = Column(String(11), unique=True)
    idade = Column(Integer)
    estado = Column(String(2))

    def __repr__(self):
        return self.nome

    def cria_tabela(self):
        Base.metadata.create_all(engine)

    def le_tabela(self):
        dados_da_tabela = session.query(CreateTable).all()
        return dados_da_tabela
    
    def escreve_tabela(self):
        entrada = CreateTable(nome = "Maria",
                              cpf = "12345678900",
                              idade = 12,
                              estado = "MG")
        session.add(entrada)
        session.commit()


if __name__ == "__main__":
    pass
