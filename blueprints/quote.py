from flask import Blueprint, request, jsonify
from services.freight_service import FreightService
import logging

quote_blueprint = Blueprint('quote_blueprint', __name__)


@quote_blueprint.route('/quote', methods=['POST'])
def quote():
    """
    Endpoint para cálculo de frete. Recebe as dimensões e o peso via JSON e retorna as opções de frete.

    Retorna:
        JSON: Resposta contendo as opções de frete ou mensagem de erro.
    """
    try:
        data = request.json
        freight_service = FreightService()
        response = freight_service.calculate_freight(data)
        return jsonify(response)
    except Exception as e:
        logging.error(f"Error processing the request: {e}")
        return jsonify({"error": str(e)}), 500
