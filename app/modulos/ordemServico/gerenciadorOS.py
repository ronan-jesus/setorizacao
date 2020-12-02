from flask import Blueprint

gerenciadorOS_bp = Blueprint('gerenciadorOS', __name__)

@gerenciadorOS_bp.route('/ordemServico')
def index():
	return '<h1>Modulo de Gerenciamento de Ordem de Serviços</h1>'