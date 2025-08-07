from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from /..KnjigaEdit import KnjigaEdit
from ...KnjigaEdit import KnjigaEdit


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #alert(anvil.server.call("uzmi_knjige"))
    #self.repeating_panel_1.items = anvil.server.call("uzmi_knjige")
    #self.refresh_knjige()
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Get the user to confirm if they wish to delete the article
        # If yes, raise the 'x-delete-article' event on the parent
        # (which is the articles_panel on Homepage)

        result = alert(
            content=f"Jeste li sigurni da želite da izbrišete  {self.item['Наслов']} {self.item['Аутори']} ?",
            buttons=[("Da", True), ("Ne", False)],
            #role="alert-greska",
        )
        if result:
            #self.parent.raise_event("x-delete-article", article=self.item)
            #alert("ааааааа")
            anvil.server.call(
                        "brisi_knjiga", knjiga=self.item
                    )
            #self.refresh_knjige()
            self.parent.raise_event("x-osvjezi")
      
  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Create a copy of the existing article from the Data Table        
        knjiga_copy = dict(self.item)        
        #if article_copy["tecaj"] is None:
           # article_copy["tecaj"] = []
        upis_traje = True
        while upis_traje:
            save_clicked = alert(
                content=KnjigaEdit(item=knjiga_copy),
                title="Izmjena podataka",
                large=True,
                buttons=[("Čuvanje", True), ("Odustajanje", False)],
            )
            if save_clicked:
                anvil.server.call(
                        "izmjena_knjiga", self.item, knjiga_copy
                    )
                upis_traje = False
                self.refresh_data_bindings()
               
            else:
                upis_traje = False



