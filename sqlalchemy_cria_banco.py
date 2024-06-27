from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, DateTime
from datetime import datetime


engine = create_engine('sqlite:///banco_novo.db', echo=True)
metadata = MetaData(bind=engine)

Tab = Table('codigo_resposta', 
            metadata,
            Column('url_pagina', String(1024), index=True),
            Column('codigo_de_historico', Integer),
            Column('codigo_de_resposta', Integer),
            Column('imagens', String(200000)),
            Column('links', String(200000)),
            Column('data_criacao', DateTime, default=datetime.now))

metadata.create_all()
