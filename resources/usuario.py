from models.usuario import UserModel
from flask_restful import Resource, reqparse

class User(Resource):
  # /usuarios/{user_id}
  def get(self, user_id):
    user = UserModel.find_user(user_id)
    if user:
      return user.json()
    return {'message': 'User not found.'}, 404

  def delete(self, user_id): # Recebe o hotel_id da url /hoteis/hotel_id
    user = UserModel.find_user(user_id)
    if user: 
      try:
        user.delete_user()
      except:
        return {'message': 'An error ocurred trying to delete user.'}, 500
      return {'message': 'User deleted.'}
    return {'message': 'User not found.'}, 404
     
class UserRegister(Resource):
  # /cadastro

  def post(self):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('login', type=str, required=True, help="The field 'login' cammpt be left blank")
    argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' cammpt be left blank")
    dados = argumentos.parse_args()

    if UserModel.find_by_login(dados['login']):
      return {"message": "The Login '{}' already exists.".format(dados['login'])}, 409 

    user = UserModel(**dados)
    user.save_user()
    return {"message": "User created successfully."}, 201