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

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.

@anvil.server.callable
def lookup_cover(isbn):
  request = f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg"
  print(request)
  try:
    resp = anvil.http.request(request)
    return resp
  except anvil.http.HttpError as e:
    print(f"Error: {e.status}")

@anvil.server.callable
def search_records(tip_string,search_string):
  search_string = search_string.lower()
  if tip_string=="naslov":
    return [r for r in app_tables.knjige.search(tables.order_by("Креирано", ascending=False))
    #return [r for r in list
            if search_string in r['Наслов'].lower()]
  elif  tip_string=="autor": 
       return [r for r in app_tables.knjige.search(tables.order_by("Креирано", ascending=False))
            if search_string in r['Аутори'].lower()]
  elif  tip_string=="ISBN": 
       return [r for r in app_tables.knjige.search(tables.order_by("Креирано", ascending=False))
            if search_string in r['ISBN'].lower()]   
  elif  tip_string=="izdavač": 
       return [r for r in app_tables.knjige.search(tables.order_by("Креирано", ascending=False))
            if search_string in r['Издавач'].lower()]     
  elif  tip_string=="godina": 
       return [r for r in app_tables.knjige.search(tables.order_by("Креирано", ascending=False))
            if search_string in r['Година'].lower()]  
  elif  tip_string=="polica": 
       return [r for r in app_tables.knjige.search(tables.order_by("Креирано", ascending=False))
            if search_string in r['Полица'].lower()] 
  elif  tip_string=="početno slovo": 
       return [r for r in app_tables.knjige.search(tables.order_by("Креирано", ascending=False))            
            if  r['Наслов'].lower().startswith(search_string)] 
@anvil.server.callable
def uzmi_knjige():
    # Get a list of articles from the Data Table, sorted by 'created' column, in descending order
    #return list(app_tables.knjige.search(tables.order_by("Created", ascending=False)))
    return list(app_tables.knjige.search(tables.order_by("Креирано", ascending=False)))



@anvil.server.callable
def import_podataka(art_dict):

    #org_jed_za_dave = app_tables.categories.get(
                #name=art_dict["category"]
            #) 
    #art_dict["category"]=org_jed_za_dave    
    art_dict["Креирано"]=datetime.now()
    app_tables.knjige.add_row(**art_dict) 

@anvil.server.callable
def dodaj_knjigu(knjiga_dict):         
         app_tables.knjige.add_row(Креирано=datetime.now(), **knjiga_dict)

@anvil.server.callable
def izmjena_knjiga(knjiga, knjiga_dict):
 
  # check that the article given is really a row in the ‘articles’ table
  if app_tables.knjige.has_row(knjiga):
    #knjiga_dict['updated'] = datetime.now()        
    knjiga.update(**knjiga_dict)     
  else:
    raise Exception("Knjiga ne postoji")

@anvil.server.callable
def uzmi_knjige_odDo(broj1,broj2):
    # Get a list of articles from the Data Table, sorted by 'created' column, in descending order
    lista_а=list(app_tables.knjige.search(tables.order_by("Креирано", ascending=False)))
    #print(list(lista_а))
    lista_а_p=[]
    br=1
    for art in lista_а  :
      if br>=int(broj1) and br<=int(broj2):
         lista_а_p.append(art)
      br=br+1
        
    print(lista_а_p)    
    return lista_а_p 


@anvil.server.callable
def brisi_knjiga(knjiga):  
    # check that the article being deleted exists in the Data Table  
    if app_tables.knjige.has_row(knjiga):
       knjiga.delete()        
    else:
        raise Exception("Knjiga ne postoji")
   
