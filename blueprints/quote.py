from flask import Blueprint, request, jsonify
from services.freight_service import FreightService

quote_blueprint = Blueprint('quote_blueprint', __name__)


@quote_blueprint.route('/quote', methods=['POST'])
def quote():
    data = request.json()
    freight_service = FreightService()
    response = freight_service.calculate_freight(data)
    return jsonify(response)
