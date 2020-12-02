# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 02:42:19 2020

@author: User
"""
import os, tempfile, shutil
from app import app
from flask import render_template, request, jsonify
from app.models.tables import (tab_consumidores, tab_consumidoresPorDistrito, tab_nos,
                               tab_trechos, tab_pontosDmcs, db)

from flask_googlemaps import Map

import ezdxf


@app.route("/")
def index():
    return render_template("index.html")
