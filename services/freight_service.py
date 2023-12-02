from models.freight_options import FREIGHT_OPTIONS


class FreightService:
    def calculate_freight(self, data):
        dimension = data.get("dimensao")
        weight = data.get("peso")
        response = []

        for name, option in FREIGHT_OPTIONS.items():
            if self._validate_dimensions(dimension, option) and weight > 0:
                freight_cost = (weight * option["const"]) / 10
                response.append({
                    "nome": name,
                    "valor_frete": round(freight_cost, 2),
                    "prazo_dias": option["delivery_days"]
                })
        
        return response
    
    def _validate_dimensions(self, dimension, option):
        return option["min_height"] <= dimension["altura"] <= option["max_height"] and \
            option["min_width"] <= dimension["largura"] <= option["max_width"]

