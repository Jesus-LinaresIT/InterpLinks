# -*- coding: utf-8 -*-
"""
    main.interpreters
    ~~~~~~~~~~~~~~
    main interpreters package
"""
import flask_praetorian
from .services import interpreter
from ..router import route
from ..core import guard
from flask import Blueprint, request


bp = Blueprint('interpreters', __name__, url_prefix='/interpreters')

@route(bp, '/', methods = ['POST'])
@flask_praetorian.roles_accepted('interpreters')
def create():
  req = request.get_json()
  return interpreter.add_new(req)


@route(bp, '/<user_id>', methods = ['POST'])
@flask_praetorian.roles_accepted('interpreters')
def update(user_id):
  req = request.get_json()
  return interpreter.update_by_user_id(req, user_id)


@route(bp, '/', methods = ['GET'])
def get_all():
  return interpreter.get_interpreters()


@route(bp, '/<user_id>', methods = ['GET'])
def get_by_id(user_id):
  return interpreter.get_by_user_id(user_id)
