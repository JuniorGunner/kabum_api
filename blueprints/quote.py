from flask import Blueprint, request, jsonify
from services.freight_service import FreightService
import logging

quote_blueprint = Blueprint('quote_blueprint', __name__)


@quote_blueprint.route('/quote', methods=['POST'])
def quote():
    try:
        data = request.json
        freight_service = FreightService()
        response = freight_service.calculate_freight(data)
        return jsonify(response)
    except Exception as e:
        logging.error(f"Error processing the request: {e}")
        return jsonify({"error": str(e)}), 500
