from flask import Blueprint

projetosCustos_bp = Blueprint('projetosCustos', __name__)

@projetosCustos_bp.route('/projetosCustos')
def index():
	return '<h1>Modulo de Gerenciamento de Projetos e Custos</h1>'