from flask import current_app
from ..core import Service, db, guard, mail
from flask_mail import Message
from ..templates import get_template
from .models import Appointments, Assigned
from ..users.models import User
from ..interpreters.models import Interpreter
from ..users.services import users
from ..zoom.services import zoom
from ..auth.services import auth
import json
import flask_praetorian as flaskP
from _datetime import datetime


class AppointmentsServices(Service):
  __model__ = Appointments

  def add_new(self, req):
    """
    """
    get_rolename = flaskP.current_rolenames()
    object_rolename = {
      'company'
    }

    if get_rolename == object_rolename:
      req["user_id"] = users.get_authenticated_user_id()

    req["status"] = "schedule"

    try:
      appointment = self.create(**req)

      if appointment.meeting_type == 'Video remote interpreting':  

        start_time = datetime.combine(appointment.date, appointment.time)
        
        metting = {
          "start_time": start_time,
          "duration": appointment.duration,
          "topic": "API Test",
          "type": 2,
          "user_id" : 'raul.escamilla@asesoriait.com'
        }
        
        json_meeting = zoom.create_meeting(metting)
        created_meeting = json.loads(json_meeting.decode())

        if created_meeting:
          args = {
            "join_url": created_meeting['join_url'],
            "start_url": created_meeting['start_url'], 
            "meeting_id": str(created_meeting['id']), 
            "meeting_password": created_meeting['password']          
          }

          self.update(appointment, **args)

      return self.send_appointment_email(appointment, start_time)

    except:
      ret = {'message': 'Something went wrong creating this appointment, please try again later'}, 400  

      return ret


  def send_appointment_email(self, appointment, start_time):
    """
    """
    msg = Message('Appointment create', recipients = [current_app.config['MAIL_USERNAME']])
    msg.html = '<span><b>Source Languages: </b></span>' + appointment.source_language + "<br>";
    msg.html += '<span><b>Target Languages: </b></span>' + appointment.target_languages + "<br>";
    msg.html += '<span><b>Industry: </b></span>' + appointment.industry + "<br>";
    msg.html += '<span><b>Date: </b></span>' + str(start_time) + "<br>";
    msg.html += '<span><b>Duration: </b></span>' + str(appointment.duration) + "<br>";
    msg.html += '<span><b>Meeting Type: </b></span>' + appointment.meeting_type + "<br>";
    msg.html += '<span><b>Category Type: </b></span>' + appointment.category_type + "<br>";
    msg.html += '<span><b>Status: </b></span>' + appointment.status + "<br>";
    mail.send(msg)

    ret = {'message': 'Email has been sent to, please confirm your email to see information of appointments'}, 201

    return ret


  def update_by_id(self, req, id):
    """
      Update an appointment by appointment id.  
    """  
    appointment = self.get(id)   
    auth.check_permissions(appointment)
    
    try:
      self.update(appointment, **req)

      start_time = datetime.combine(appointment.date, appointment.time)
      metting = {
        "topic": "API Test4",
        "start_time": start_time,
        "duration": appointment.duration,
        "id" : appointment.meeting_id
      }
      
      zoom.update_meeting(metting)
      ret = {'message': 'successfully changes data'}, 200
    
    except:
      ret = {'message': 'Something went wrong deleting this appointment, please try again later'}, 400  
    
    return ret
  

  def delete_by_id(self, id): 
    """
      Delete an appointment by appointment id.  
    """
    appointment = self.get(id)
    auth.check_permissions(appointment)

    try:
      metting = {"id": appointment.meeting_id}

      zoom.delete_meeting(metting)
      
      self.delete(appointment)
      ret = {'message': 'Appointment successfully deleted.'}, 200

    except:
      ret = {'message': 'Something went wrong deleting this appointment, please try again later'}, 400  

    return ret


  def get_by_company_id(self, user_id):
    """
      Get all appointments by company user_id  
    """
    if int(user_id) != users.get_authenticated_user_id():  
      return ({'message': 'Access denied'}, 401)
    
    result = db.session.query(User.first_name, User.last_name, Appointments.source_language, \
                                  Appointments.target_languages, Appointments.date, Appointments.join_url, \
                                  Appointments.start_url, Appointments.meeting_id, Appointments.meeting_password,\
                                  Appointments.meeting_type, Appointments.order_id, Appointments.status) \
                                  .filter(User.id == Appointments.user_id) \
                                  .filter_by(id = user_id).first()  
                                   
    return result._asdict(), 200


  def get_status(self, req):
    """
    """
    get_instances = self.first(id = req['appoinment_id'])
    if get_instances:
      return get_instances.status


class AssignedServices(Service):
  __model__= Assigned

  def add_assigned(self, req):
    """
    """
    status_appointment = appointments.get_status(req)

    if status_appointment == "schedule":
      try:
        assign = self.create(**req)      
        ret = {'message': 'Success assigned added'}, 201
      except:
        ret = {'message': 'Something went wrong creating this assign, please verify your appointment is schedule'}, 400

    return ret

  def delete_by_id(self, id):
    """
    """
    assign_delete = self.get(id) 
    
    if not assign_delete:
      ret = {'message': 'Something went wrong find this assigned it may have already been removed, please try again later'}, 404
    else:
      status_appointment = appointments.first(id = assign_delete.appoinment_id) 
      
      if status_appointment.status == "schedule":      
        self.delete(assign_delete)
        ret = {'message': 'Assigned successfully deleted.'}, 200   
  
    return ret


appointments = AppointmentsServices()
assignedS = AssignedServices()

