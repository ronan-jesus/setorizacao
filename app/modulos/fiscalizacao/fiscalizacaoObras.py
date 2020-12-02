from flask import Blueprint

fiscalizacaoObras_bp = Blueprint('fiscalizacaoObras', __name__)

@fiscalizacaoObras_bp.route('/fiscalizacaoObras')
def index():
	return '<h1>Modulo de fiscalização de Obras</h1>'