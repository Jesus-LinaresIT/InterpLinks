"""
    main.appointments.models
    ~~~~~~~~~~~~~~~~~~~~~
    Appointments models
"""
import datetime
from ..core import db
from ..models import User, Interpreter
from ..helpers import JsonSerializer


class AppointmentsJsonSerializer(JsonSerializer):
  __json_public__ = ['source_language', 'target_languages', 'industry', 'date', 'time', 'duration', 'meeting_type', 'order_id', 'status']


class Appointments(AppointmentsJsonSerializer, db.Model):
  __tablename__ = 'appointments'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  source_language = db.Column(db.String(100))
  target_languages =  db.Column(db.Text, nullable=False) 
  industry = db.Column(db.String(150))
  date = db.Column(db.DATE)
  time = db.Column(db.TIME)
  duration = db.Column(db.Integer)
  meeting_type = db.Column(db.String(50))
  category_type = db.Column(db.Text)
  order_id  = db.Column(db.String(50))
  status = db.Column(db.String(20))

  join_url = db.Column(db.String(256))
  start_url = db.Column(db.String(550))
  meeting_id = db.Column(db.String(15))
  meeting_password = db.Column(db.String(256))

  appointments_assigned = db.relationship('Assigned', cascade = 'all,delete', backref = 'appointments', uselist = False)


class Assigned(db.Model):
  __tablename__ = 'assigned'

  id = db.Column(db.Integer, primary_key=True)
  interpreter_id = db.Column(db.Integer, db.ForeignKey('interpreters.id'))
  appoinment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))

