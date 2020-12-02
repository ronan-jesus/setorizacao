# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:23:36 2020

@author: User
"""
from app import db
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER, VARCHAR
from sqlalchemy import select, join

class tab_consumidoresPorDistrito(db.Model):
        __tablename__ = 'tab_consumidoresPorDistrito'
        matricula = db.Column(db.Integer, primary_key=True, nullable=False)
        idZona = db.Column(db.String, nullable=False)
        idDmc = db.Column(db.String, nullable=False)
   
class tab_consumidores(db.Model):
        __tablename__ = 'tab_consumidores'
        id = db.Column(db.Integer, nullable=False)
        matricula = db.Column(db.Integer, primary_key=True, nullable=False)
        categoria = db.Column(db.String, nullable=False)
        nome = db.Column(db.String, nullable=False)
        endereco = db.Column(db.String, nullable=False)        
        bairro = db.Column(db.String, nullable=False)        
        latitude = db.Column(db.REAL, nullable=True)
        longitude = db.Column(db.REAL, nullable=True)
        UTMx = db.Column(db.REAL, nullable=True)
        UTMy = db.Column(db.REAL, nullable=True)
        
class tab_pontosDmcs(db.Model):
        __tablename__ = 'tab_pontosDmcs'
        id = db.Column(db.Integer, primary_key=True, nullable=False)
        idDmc = db.Column(db.String, nullable=False)
        numVertice = db.Column(db.Integer, nullable=False)
        latitude = db.Column(db.REAL, nullable=True)
        longitude = db.Column(db.REAL, nullable=True)
        UTMx = db.Column(db.REAL, nullable=True)
        UTMy = db.Column(db.REAL, nullable=True)

class tab_dmcs(db.Model):
        __tablename__ = 'tab_dmcs'        
        id_dmc = db.Column(db.String, primary_key=True, nullable=False)
        numero_dmc = db.Column(db.Integer, nullable=False)
        nome = db.Column(db.String, primary_key=True, nullable=False)
        zona = db.Column(db.Integer, nullable=False)

        def __init__(self, id_dmc, numero_dmc, nome, zona):
            self.id_dmc = id_dmc
            self.numero_dmc = numero_dmc
            self.nome = nome
            self.zona = zona

        @property
        def serialize(self):
            """Return object data in easily serializable format"""
            return {
               'id_dmc'         : self.id_dmc,
               'numero_dmc': self.numero_dmc,
               'nome': self.nome,
               'zona': self.zona,               
            }
        

#tab_consumidores = Table('tab_consumidores',
#                         metadata,
#                         Column('matricula', Integer, primary_key=True,
#                                nullable=False),
#                         Column('nome', String, nullable=False),
#                         Column('endereco', String, nullable=False),
#                         Column('bairro', String, nullable=False),
#                         Column('latitude', REAL, nullable=True),
#                         Column('longitude', REAL, nullable=True),
#                         Column('UTMx', REAL, nullable=True),
#                         Column('UTMy', REAL, nullable=True),
#                         )
#
#tab_consumos = Table('tab_consumos',
#                     metadata,
#                     Column('matricula', Integer, nullable=False),
#                     Column('volume', REAL, nullable=False),
#                     Column('mes', Integer, nullable=False),
#                     Column('ano', Integer, nullable=False),
#                     )
#

class tab_nos(db.Model):
        __tablename__ = 'tab_nos'
        idNo = db.Column(db.String, primary_key=True, nullable=False)
        numeroNo = db.Column(db.Integer, nullable=False)
        coord_x = db.Column(db.REAL, nullable=False)
        coord_y = db.Column(db.REAL, nullable=False)
        latitude = db.Column(db.REAL, nullable=True)
        longitude = db.Column(db.REAL, nullable=True)
        descricao = db.Column(db.String, nullable=False)
        zona = db.Column(db.Integer, nullable=False)
        cota = db.Column(db.REAL, nullable=False)

class tab_trechos(db.Model):
        __tablename__ = 'tab_trechos'
        idTrecho = db.Column(db.String, primary_key=True, nullable=False)
        numTrecho = db.Column(db.String, nullable=False)
        noInicial = db.Column(db.String, nullable=False)
        noFinal = db.Column(db.String, nullable=False)
        diametro = db.Column(db.Integer, nullable=True)
        rugosidade = db.Column(db.Integer, nullable=True)
        coefPerCarSingular = db.Column(db.Integer, nullable=True)
        estadoInicial = db.Column(db.String, nullable=True)        
        coefReacEscoamento = db.Column(db.Integer, nullable=True)        
        coefReacParede = db.Column(db.Integer, nullable=True)
        descricao = db.Column(db.String, nullable=True)
        zona = db.Column(db.String, nullable=False)
        
db.create_all()

#SELECIONAR COORDENADAS POR DISTRITO
#users = db.session.query(tab_consumidores).join(tab_consumidoresPorDistrito, tab_consumidoresPorDistrito.matricula == tab_consumidores.matricula).filter(tab_consumidoresPorDistrito.idDmc == '15.001')
#for i in users:
#    print(i.latitude, i.longitude)

#SELECIONAR 'NOS' NO BANCO DE DADOS
#nos = db.session.query(tab_nos).filter(tab_nos.idNo.like('20.001.%'))
#for no in nos:
#    print(no.idNo, no.latitude, no.longitude)

#SELECIONAR PONTOS DE DELIMITACAO DOS DISTRITOS BANCO DE DADOS
#vertices = db.session.query(tab_pontosDmcs).all()
#for v in vertices:
#    print(v.idDmc, v.numVertice, v.latitude, v.longitude)

#matriculas = [consumidor.matricula for consumidor in tab_consumidoresPorDistrito.query.filter_by(idDmc='15.001').all()]
#composicao = tab_composicoes.query.filter_by(codigo='5632').all()
#insumos = tab_insumos.query.filter_by(mes=3, ano=2020, uf='AC').all()
#insumos = tab_insumos.query.filter((tab_insumos.id=='AC.01.2019.039840')).first()
