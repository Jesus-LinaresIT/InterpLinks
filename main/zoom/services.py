from flask import current_app, jsonify
from ..core import Service, zoom_client
from ..users.services import users
from ..appointments.models import Appointments



class ZoomServices(Service):
  __model__ = Appointments

  def create_meeting(self, req):
    """
    """ 
    response = current_app.zoom_client.meeting.create(**req) 
    return response.content

  def update_meeting(self, req):
    """
    """
    response = current_app.zoom_client.meeting.update(**req)
    return response.content

  def delete_meeting(self, req):
    """
    """
    response = current_app.zoom_client.meeting.delete(**req)

zoom = ZoomServices()