from ._anvil_designer import PocetnaTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
#from anvil.google.drive import app_files
from random import choice
import custom_signup.login_flow

import anvil.email
import anvil.users
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.http
from datetime import datetime


#openpyxl

class Pocetna(PocetnaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    # Any code you write here will run when the form opens.

    self.init_components(**properties)
    custom_signup.login_flow.login_with_form()
    kor=anvil.users.get_user()['email']
    
    if kor=="" :
       self.button_2.visible=False
    else:
      self.button_2.visible=True
    self.loading_image.visible = False
    self.cover_image.visible = False
    #lib_file = app_files.my_library
    #lib_file = app_files.rume
    #lib_file_row=app_tables.podaci.get(naziv="Biblioteka")
  
    #lib_file = app_tables.podaci.get(ExcelFile=row)
    #lib_file = app_files.bibliotekaradnaverzija
    #lib_file = app_files.biblioteka
    #self.refresh_articles()
    #print("File is called: " + lib_file.title)
    #print("File is called: " + lib_file.naziv)
    #print("File is called: " + lib_file.name)
    #self.worksheet = lib_file[0]
    #print(self.worksheet.fields)
    #print(self.worksheet)

    #r=app_tables.knjige.search()
    #for rr in r:
         #rr["ISBN"]="0192817299"
         #rr["ISBN"]=""
    
    


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.cover_image.visible = False
    self.loading_image.visible = True
    self.book_title.visible = True
    self.button_1_copy.text = "Druga slučajna knjiga?"
    #print(self.worksheet.rows)
    #r = choice(list(app_tables.knjige.search(tables.order_by("Креирано", ascending=False))))
    r = choice(anvil.server.call('uzmi_knjige'))
    print(r)
    #alert(self.worksheet.rows)
    self.book_title.text = f" {r['Наслов']}"
    self.book_author.text = f" {r['Аутори']}"
    self.repeating_panel_1.visible = False
    if r['ISBN'] and r['ISBN']!=" "  and r['ISBN']!="":
      self.cover_image.source = anvil.server.call('lookup_cover', r['ISBN'])
      self.loading_image.visible = False
      self.cover_image.visible = True
    
  def button_pretraga_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.repeating_panel_1.visible = True
    lista_pret=[]
    lista_pret=anvil.server.call("search_records",self.drop_down_1.selected_value,self.text_box_1.text)
    print(lista_pret)
    self.repeating_panel_1.items=lista_pret    
    self.book_title.visible = False
    self.cover_image.visible=False
    self.loading_image.visible=False

  def error_handler(self):
        r = alert(
            str(self), title="Greška", buttons=["U redu", True], role="alert-greska"
        )
  set_default_error_handling(error_handler)  

  def link_2_click(self, **event_args):
          """This method is called when the link is clicked"""
          self.text_box_1.text=''
          self.text_box_1.focus()

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    #anvil.users.login_with_form()
    #custom_signup.login_flow.login_with_form()
    #login_flow.login_with_form()
    #open_form('LoginDialog')
    #open_form('Form1')
    open_form('Edit',items=anvil.server.call("uzmi_knjige"))
    

