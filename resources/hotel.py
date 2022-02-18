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

class Hoteis(Resource): # Referente ao GET de todos os Hoteis
  def get(self):
    return {'hoteis': hoteis}

class Hotel(Resource):
  
  def get(self, hotel_id): # Recebe o hotel_id da url /hoteis/hotel_id
    for hotel in hoteis:
      if hotel['hotel_id'] == hotel_id:
        return hotel
    return {'message': 'Hotel not found.'}, 404

  def post(self, hotel_id): # Recebe o hotel_id da url /hoteis/hotel_id
    pass

  def put(self, hotel_id): # Recebe o hotel_id da url /hoteis/hotel_id
    pass

  def delete(self, hotel_id): # Recebe o hotel_id da url /hoteis/hotel_id
    pass
