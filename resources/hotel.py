from flask_restful import Resource

hoteis = [
  {
    'hotel_id': 'alpha',
    'nome': 'Alpha Hotel',
    'estrelas': 4.3,
    'diaria': 420.34,
    'cidade': 'Rio de Janeiro'
  },
  {
    'hotel_id': 'bravo',
    'nome': 'Bravo Hotel',
    'estrelas': 4.4,
    'diaria': 380.90,
    'cidade': 'Pelotas'
  },
  {
    'hotel_id': 'charlie',
    'nome': 'Charlie Hotel',
    'estrelas': 3.9,
    'diaria': 320.24,
    'cidade': 'Balneario Camboriu'
  }
]

class Hoteis(Resource):
  def get(self):
    return {'hoteis': hoteis}
