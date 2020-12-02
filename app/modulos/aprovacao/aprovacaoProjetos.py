from flask import Blueprint

aprovacaoProjetos_bp = Blueprint('aprovacaoProjetos', __name__)

@aprovacaoProjetos_bp.route('/aprovacao')
def index():
	return '<h1>Modulo de Aprovacao de Projetos</h1>'