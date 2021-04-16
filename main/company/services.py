from flask import current_app
from ..core import Service, db, guard
from .models import Company
from ..auth.services import auth
import json



class CompanyServices(Service):
  __model__ = Company

  def add_new(self, req):
    """
    """
    try:
      company = self.create(**req)  
      ret = {'message': 'successfully create company and saving data'}, 200 

    except:
      ret = {'message': 'Something went wrong, please try again later'}, 400  

    return ret


  def update_by_id(self, req, id):
    """
      Update an appointment by appointment id.  
    """  
    company = self.get(id)   
    
    try:
      self.update(company, **req)
      ret = {'message': 'successfully changes data'}, 200 
    except:
      ret = {'message': 'Something went wrong update this company, please try again later'}, 400  
    
    return ret
  

  def delete_by_id(self, id): 
    """
      Delete an appointment by appointment id.  
    """
    company = self.get(id)

    try:   
      self.delete(company)
      ret = {'message': 'Company successfully deleted.'}, 200
    except:
      ret = {'message': 'Something went wrong deleting this company, please try again later'}, 400  

    return ret


company = CompanyServices()