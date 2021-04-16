"""
    main.appointments.models
    ~~~~~~~~~~~~~~~~~~~~~
    Company models
"""

from ..core import db
from ..helpers import JsonSerializer


class CompanyJsonSerializer(JsonSerializer):
  __json_public__ = ['name', 'code', 'email', 'industry', 'phone']


class Company(CompanyJsonSerializer, db.Model):
  __tablename__ = 'company'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), index=True, unique=True, nullable=False)
  code = db.Column(db.String(100), nullable=False)
  phone = db.Column(db.String(20))
  tax_number = db.Column(db.String(20))
  email = db.Column(db.String(75), index=True, unique=True)
  industry = db.Column(db.String(25), nullable=False)
  address_1 = db.Column(db.String(100))
  address_2 = db.Column(db.String(100))
  address_3 = db.Column(db.String(100))
  city = db.Column(db.String(25))
  country = db.Column(db.String(25))
  state = db.Column(db.String(25))
  zipcode = db.Column(db.String(10))
  is_active = db.Column(db.Boolean, nullable=False, default=False, server_default='false') 


