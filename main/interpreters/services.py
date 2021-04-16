from flask import current_app
from flask.json import jsonify
from .models import Interpreter
from ..core import Service, db
from ..models import User
from ..users.services import users
from ..auth.services import auth


class InterpreterServices(Service):
  __model__ = Interpreter

  def add_new(self, req):
    """
      Save a new interpreter detail
    """ 
    req["user_id"] = users.get_authenticated_user_id()
    return self.create(**req)


  def update_by_user_id(self, req, user_id):
    """
      Update existing interpreter by id
    """ 
    
    interpreter_info = self.first(user_id = user_id)
    auth.check_permissions(interpreter_info)  
    
    try:       
      self.update(interpreter_info, **req)
      ret = ({'message': 'Interpreter detail successfully updated'}, 200)
    
    except Exception as e:
      ret = ({'message': 'Something went wrong updating interpreter detail, please try again later'}, 500)

    return ret


  def get_by_user_id(self, user_id):
    """
      Get interpreters detail by interpreter id
    """ 
    user = self.first(user_id=user_id)
    
    if not user:
        return {'Error': 'The interpreter id doesn\'t exist'}, 400 
        
    interpreter = db.session.query(User.first_name, User.last_name, Interpreter.native_language, \
                                  Interpreter.target_languages, Interpreter.field_of_expertise) \
                                  .filter(User.id == Interpreter.user_id) \
                                  .filter_by(id = user_id).first()              
    
    return interpreter._asdict(), 200


  def get_interpreters(self):
    """
      Get list of interpreters
      TODO: check this method to return right information
    """ 
    interpreter = db.session.query(User.first_name, User.last_name, Interpreter.native_language, \
                                  Interpreter.target_languages, Interpreter.field_of_expertise) \
                                  .filter(User.id == Interpreter.user_id).all()            
      
    return interpreter, 200
                                                                                  

interpreter = InterpreterServices()
