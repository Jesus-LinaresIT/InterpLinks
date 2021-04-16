"""
    main.appointments
    ~~~~~~~~~~~~~~
    main appointments package
"""
import flask_praetorian
from .services import company
from ..router import route
from ..core import guard
from flask import Blueprint, request


bp = Blueprint('company', __name__, url_prefix='/company')


@route(bp, '/', methods = ['GET'])
@flask_praetorian.roles_accepted('admin')
def get_all():
  return company.all()


@route(bp, '/', methods = ['POST'])
@flask_praetorian.roles_accepted('admin')
def create():
  req = request.get_json()
  return company.add_new(req)



@route(bp, '/<id>', methods = ['PUT'])
@flask_praetorian.roles_accepted('admin')
def update(id):
  req = request.get_json()
  return company.update_by_id(req, id)


@route(bp, '/<id>', methods = ['DELETE'])
@flask_praetorian.roles_accepted('admin')
def delete(id):
  return company.delete_by_id(id)