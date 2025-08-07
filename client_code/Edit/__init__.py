from ._anvil_designer import EditTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..KnjigaEdit import KnjigaEdit

class Edit(EditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #alert(anvil.server.call("uzmi_knjige"))
    self.refresh_knjige()
    #self.repeating_panel_1.items = anvil.server.call("uzmi_knjige")
    # Any code you write here will run when the form opens.
    self.repeating_panel_1.set_event_handler("x-osvjezi",self.osvjezi)

  def refresh_knjige(self):
        # Load existing articles from the Data Table,
        # and display them in the RepeatingPanel
        self.repeating_panel_1.items = anvil.server.call("uzmi_knjige_odDo",broj1=1,broj2=11)
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Pocetna')

  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        new_knjiga = {
            "Наслов": "",
            "Аутори": "",
            "Издавач": "",
            "ISBN": "",
            "Година": "",
            "Количина": "",
            "Рбр": "",
            "Задужење": "",
            "Полица": "",
            "Напомена1": "",
            "Напомена2": ""
        }
        # Open an alert displaying the 'ArticleEdit' Form
        upis_traje = True
        while upis_traje:
            save_clicked = alert(
                content=KnjigaEdit(item=new_knjiga),
                title="Dodavanje podataka",
                large=True,
                buttons=[("Čuvanje", True), ("Odustajanje", False)],
            )
            # If the alert returned 'True', the save button was clicked.
            
            if save_clicked:
                    #alert(new_knjiga)
                    upis_traje = False
                    anvil.server.call(
                        "dodaj_knjigu", new_knjiga
                    )
                    #if self.text_box_pret.text ==""  :  
                         #self.refresh_articles()
                    #else:
                          #lista_pret=[]
                          #lista_pret=anvil.server.call("search_records",self.text_box_pret.text)
                          #self.articles_panel.items=lista_pret*/
        
            else:
                upis_traje = False
        self.refresh_knjige()
  def pretraga_broj_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_broj1.text=="" or self.text_broj2.text=="":
        self.repeating_panel_1.items = anvil.server.call("uzmi_knjige_odDo",broj1=1,broj2=11)
    else:  
        self.repeating_panel_1.items = anvil.server.call("uzmi_knjige_odDo",broj1=self.text_broj1.text,broj2=self.text_broj2.text)

  def text_broj1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.text_broj2.focus()

  #def osvjezi(self, article, **event_args):
  def osvjezi(self,  **event_args):
        self.refresh_knjige()
        