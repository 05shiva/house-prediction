from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    ans=anvil.server.call("predicting_function",self.land_size.text,self.house_size.text,self.Number_of_rooms.text,self.Number_of_bathrooms.text,self.large_living_room.text ,
                                               self.parking.text,self.house_age.text,self.front_garden.text,self.Swimming_pool.text,self.distance_to_school.text,
                                               self.wall_fence.text,self.water_front.text,self.distance_from_market.text,self.crime_rate_index.text,self.room_size.text)
    self.label_2.text=ans





