from models.usuario import UserModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import safe_str_cmp

argumentos = reqparse.RequestParser()
argumentos.add_argument('login', type=str, required=True, help="The field 'login' cammpt be left blank")
argumentos.add_argument('senha', type=str, required=True, help="The field 'senha' cammpt be left blank")

class User(Resource):
  # /usuarios/{user_id}
  def get(self, user_id):
    user = UserModel.find_user(user_id)
    if user:
      return user.json()
    return {'message': 'User not found.'}, 404

  @jwt_required()
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
    dados = argumentos.parse_args()

    if UserModel.find_by_login(dados['login']):
      return {"message": "The Login '{}' already exists.".format(dados['login'])}, 409 

    user = UserModel(**dados)
    user.save_user()
    return {"message": "User created successfully."}, 201

class UserLogin(Resource):

  @classmethod
  def post(cls):
    dados = argumentos.parse_args()

    user = UserModel.find_by_login(dados['login'])
    if user and safe_str_cmp(user.senha, dados['senha']):
      token = create_access_token(identity=user.user_id)
      return {"acess_token": token}, 200
    return {"message": "The username or password is incorrect."}, 401