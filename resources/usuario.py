from models.usuario import UserModel
from flask_restful import Resource, reqparse

class User(Resource):

  def get(self, user_id):
    user = UserModel.find_user(user_id)
    if user:
      return user.json()
    return {'message': 'Hotel not found.'}, 404

  def delete(self, user_id): # Recebe o hotel_id da url /hoteis/hotel_id
    user = UserModel.find_user(user_id)
    if user: 
      try:
        user.delete_user()
      except:
        return {'message': 'An error ocurred trying to delete user3.'}, 500
      return {'message': 'User deleted.'}
    return {'message': 'User not found.'}, 404
     

