"""
    main.appointments
    ~~~~~~~~~~~~~~
    main appointments package
"""
import flask_praetorian
from .services import appointments, assignedS
from ..router import route
from ..core import guard
from ..users.services import users
from ..zoom.services import zoom
from flask import Blueprint, request


bp = Blueprint('appointments', __name__, url_prefix='/appointments')


@route(bp, '/', methods = ['GET'])
@flask_praetorian.roles_accepted('admin')
def get_all():
  return appointments.get_all()

 
@route(bp, '/<user_id>', methods = ['GET'])
@flask_praetorian.roles_accepted('company', 'admin')
def get_by_company_id(user_id):
  return appointments.get_by_company_id(user_id)


@route(bp, '/', methods = ['POST'])
@flask_praetorian.roles_accepted('company', 'admin')
def create():
  req = request.get_json()
  return appointments.add_new(req)

  
@route(bp, '/assigned', methods = ['POST'])
@flask_praetorian.roles_accepted('company', 'admin')
def createAssign():
  req = request.get_json()
  return assignedS.add_assigned(req)

@route(bp, '/assigned/<id>', methods = ['DELETE'])
@flask_praetorian.roles_accepted('company', 'admin')
def deleteAssign(id):
  return assignedS.delete_by_id(id)



@route(bp, '/<id>', methods = ['PUT'])
@flask_praetorian.roles_accepted('company', 'admin')
def update(id):
  req = request.get_json()
  return appointments.update_by_id(req, id)


@route(bp, '/<id>', methods = ['DELETE'])
@flask_praetorian.roles_accepted('company' 'admin')
def delete(id):
  return appointments.delete_by_id(id)