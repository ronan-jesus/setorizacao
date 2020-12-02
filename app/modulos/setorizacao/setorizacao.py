import os, tempfile, shutil
from flask import Blueprint

from app import app
from flask import render_template, request, jsonify
from app.models.tables import (tab_consumidores, tab_consumidoresPorDistrito, tab_nos,
                               tab_trechos, tab_pontosDmcs, tab_dmcs, db)
from flask_googlemaps import Map

import ezdxf

setorizacao_bp = Blueprint('setorizacao', __name__, url_prefix='/setorizacao', 
							template_folder='templates', static_folder='static',
							static_url_path='/static/setorizacao')

@setorizacao_bp.route('/')
def index():
	#Faz o select dos distritos no banco de dados 
	dists = tab_dmcs.query.all()
	#Transforma o select dos distritos em um dicionario tendo o id_dmc como chave
	dmcs_dict = {}
	for dmc in dists:
		dmcs_dict[dmc.id_dmc]= dmc.__dict__
	
	return render_template('setorizacao/index.html', dmcs=dists)

@setorizacao_bp.route("/distritos", methods=["GET", "POST"])
def distritos():
    ######## SELECAO DOS VERTICES DOS POLIGOS DOS DISTRITOS ##########
    vertices = db.session.query(tab_pontosDmcs).all()
    DMCs_aux = {}
    DMCs = {}
    for v in vertices:
        if v.idDmc in DMCs_aux:
            DMCs_aux[v.idDmc].append({'lat':v.latitude, 'lng':v.longitude})
        else:
            DMCs_aux[v.idDmc] = []
            DMCs_aux[v.idDmc].append({'lat':v.latitude, 'lng':v.longitude})

    for key, value in DMCs_aux.items():
        nkey = str(key).replace(".","")        
        DMCs[nkey] = DMCs_aux[key]   
    
    ######## SELECAO DOS CONSUMIDORES POR DISTRITO ##########
    consDistrito = db.session.query(tab_consumidores).join(tab_consumidoresPorDistrito, tab_consumidoresPorDistrito.matricula == tab_consumidores.matricula).filter(tab_consumidoresPorDistrito.idDmc == '15.001')
    
    ######## SELECAO DOS TRECHOS POR DISTRITO ##########
    trechos = db.session.query(tab_trechos).filter(tab_trechos.idTrecho.like('20.001.%'))
        
    ######## SELECAO DOS NOS POR DISTRITO ##########
    nos = db.session.query(tab_nos).filter(tab_nos.idNo.like('20.001.%'))
    NOS = {}
    for no in nos:
       NOS[no.idNo] = {'lat': no.latitude, 'lng': no.longitude}
    
    #print(NOS)
    return render_template('distritosView.html', DMCs=DMCs, consDistrito=consDistrito, trechos=trechos, NOS=NOS)

@setorizacao_bp.route("/dmc", methods=['GET','POST'])
def dmc():
    return render_template('uploadPoligonosDMCs.html')   


@setorizacao_bp.route('/getfile', methods=['GET','POST'])
def getfile():    
    if request.method == 'POST':
        result = request.files["myfile"]
        dirpath = tempfile.mkdtemp()
        result.save(os.path.join(dirpath, result.filename))
        layers = ExtractPoligonsDMCs(os.path.join(dirpath, result.filename))
        shutil.rmtree(dirpath)        
    else:
        result = request.args.get['myfile']    
    
    dados = {}
    dados["lyrs"] = layers
    return jsonify(dados)


def ExtractPoligonsDMCs(filePath):
    dwg = ezdxf.readfile(filePath)
    msp = dwg.modelspace()

    listLayers = {}
    ptsTrechos = []
    poligonosDeConsumos = []

    #get all POLYLINES intities from model space
    polylines = msp.query('LWPOLYLINE')
    for polyline in polylines:
        lyr = polyline.dxf.layer    #Nome da layer da polyline
        if lyr not in listLayers:
            listLayers[lyr] = {}
        else:
            pass
        pts = []

    return listLayers

@setorizacao_bp.route("/administrar/<id_dmc>")
def administrar(id_dmc):

    return render_template('setorizacao/administarDmc.html', id_dmc=id_dmc)

@setorizacao_bp.route('/api/', methods=["POST"])
def main_interface():
    response = request.get_json()
    print(response)
    return jsonify(response)

@setorizacao_bp.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response