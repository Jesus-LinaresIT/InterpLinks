"""
    main.interpreters.models
    ~~~~~~~~~~~~~~~~~~~~~
    Interpreter models
"""

from ..core import db
from ..helpers import JsonSerializer
from ..models import User


class InterpreterJsonSerializer(JsonSerializer):
 
  __json_public__ = ['headline', 'native_language', 'target_languages', 'years_of_experience', 'field_of_expertise', 'certifications', 'interpreting_service']


class Interpreter(InterpreterJsonSerializer, db.Model):
  __tablename__ = 'interpreters'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  headline =  db.Column(db.String(150))
  native_language =  db.Column(db.String(150))
  target_languages =  db.Column(db.Text, nullable=False) 
  years_of_experience = db.Column(db.Integer, nullable=False)
  education =  db.Column(db.String((150)))
  field_of_expertise =  db.Column(db.Text)
  certifications =  db.Column(db.Text)
  interpreting_service =  db.Column(db.Text)

  interpreters_assigned = db.relationship('Assigned', cascade = 'all,delete', backref = 'interpreter', uselist = False)

  @property
  def target_languages_prop(self):
      try:
          return self.target_languages.split(',')
      except Exception:
          return []

  @property        
  def field_of_expertise_prop(self):
    try:
        return self.field_of_expertise.split(',')
    except Exception:
        return []

  @property
  def certifications_select_prop(self):
    try:
        return self.certifications.split(',')
    except Exception:
        return []

  @property
  def select_interpreting_prop(self):
    try:
        return self.interpreting_service.split(',')
    except Exception:
        return []
