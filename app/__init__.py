# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:43:32 2020

@author: User
"""
from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_googlemaps import GoogleMaps

app = Flask(__name__)
db = SQLAlchemy(app)

#Importacao dos Modulos Blueprints
from app.modulos.ordemServico.gerenciadorOS import gerenciadorOS_bp
from app.modulos.aprovacao.aprovacaoProjetos import aprovacaoProjetos_bp
from app.modulos.fiscalizacao.fiscalizacaoObras import fiscalizacaoObras_bp
from app.modulos.setorizacao.setorizacao import setorizacao_bp
from app.modulos.projetosCustos.projetosCustos import projetosCustos_bp




#Registro dos modulos Blueprints
app.register_blueprint(gerenciadorOS_bp)
app.register_blueprint(aprovacaoProjetos_bp)
app.register_blueprint(fiscalizacaoObras_bp)
app.register_blueprint(setorizacao_bp)
app.register_blueprint(projetosCustos_bp)



app.config.from_object('config')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/User/Google Drive/SETORIZAPY/app/database/db_setorizapy.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_setorizapy'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
