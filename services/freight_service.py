from models.freight_options import FREIGHT_OPTIONS


class FreightService:
    """
    Serviço para cálculo do frete baseado nas dimensões e peso do produto.
    """
    def calculate_freight(self, data):
        """
        Calcula o frete com base nas dimensões e peso fornecidos.

        Parâmetros:
            data (dict): Dicionário contendo 'dimensao' e 'peso'.

        Retorna:
            list: Lista de opções de frete disponíveis e seus respectivos custos.
        """
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
        """
        Valida se as dimensões do produto estão dentro dos limites permitidos pela opção de frete.

        Parâmetros:
            dimension (dict): Dicionário contendo 'altura' e 'largura'.
            option (dict): Dicionário contendo as opções de frete.

        Retorna:
            bool: Verdadeiro se as dimensões estão dentro dos limites, falso caso contrário.
        """
        return option["min_height"] <= dimension["altura"] <= option["max_height"] and \
            option["min_width"] <= dimension["largura"] <= option["max_width"]

