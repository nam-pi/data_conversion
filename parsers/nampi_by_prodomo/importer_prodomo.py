from classes.time import Time
from lxml import etree
import glob
import sys
import os
import requests
import xmltodict
from classes.person import Person
from classes.date import Dates
from classes.place import Place
from classes.placename import PlaceName

# prepare dicts
ns = dict(
    aodl="http://pdr.bbaw.de/namespaces/aodl/",
    exist="http://exist.sourceforge.net/NS/exist",
    mods="http://www.loc.gov/mods/v3",
    podl="http://pdr.bbaw.de/namespaces/podl/",
)

selector = dict(
    persName="surname forename",
    time="",
    placeName="",
    date="",
    spatialStm="",
    place="",
    timeStm="",
    semanticStm=""
)




# init variables and URLs
baseURL = "https://prodomo.icar-us.eu/rest/db?_wrap=yes&_howmany=1000&_query="
personQuery = "xquery version '3.1';declare namespace podl = 'http://pdr.bbaw.de/namespaces/podl/';declare namespace aodl = 'http://pdr.bbaw.de/namespaces/aodl/'; collection('/db/apps/prodomo/data/pdr/person')//podl:person/data(@id)"

url = baseURL + personQuery
response = requests.get(url)
dict_data = xmltodict.parse(response.content)

# iterate over persons
for person in dict_data.get("exist:result").get("exist:value"):
    personID = str(person.get("#text"))

    # prepare query for aspects
    query = "xquery version '3.1';declare namespace podl = 'http://pdr.bbaw.de/namespaces/podl/';declare namespace aodl = 'http://pdr.bbaw.de/namespaces/aodl/'; let $cols := collection('/db/apps/prodomo/data/pdr/aspect')//aodl:relation[data(@object)='" + personID +"'] return for $col in $cols let $root := root($col) return $root//.[@type][@type != 'undefined']" 
    url = baseURL + query
    response = requests.get(url)
    dict_data = xmltodict.parse(response.content)

    tagName = ""

    # iterate over result set
    for key in dict_data.get("exist:result").keys():

        # prepare Tag without Namespace
        tagName = ""
        if str(key).index(":") > 0:
            arrKey = key.split(":")
            tagName = arrKey[1]

        # check if Tag is allowed; if not, continue else do build strings
        if not tagName in selector :
             continue 
        else:
            
            # PERSON
            if tagName == "persName":
                
                persName = dict_data.get("exist:result").get(key)
                for entry in persName:
                    singlePerson = Person()
                    singlePerson.Id = personID 
                    typ = entry.get("@type")
                    text = entry.get("#text")
                    if typ == "surname":
                        singlePerson.Surname = text
                    elif typ == "forename":
                        singlePerson.Forename = text
                
                break
            # ASPEKT Date
            elif tagName == "date":
                date = dict_data.get("exist:result").get(key)

                for entry in date:
                    personDate = Dates()
                    personDate.persId = personID 
                    typ = entry.get("@type")
                    if entry.get("@subtype"):
                        subtype = (entry.get("@subtype"))
                    else:
                        subtype = ""
                    text = entry.get("#text")
                    when = entry.get("@when")
                   
                    personDate.Text = text
                    personDate.Type = typ
                    personDate.Subtype = subtype
                    personDate.When = when
                
                    print(personDate)
                break

            # ASPEKT place
            elif tagName == "place":
                place = dict_data.get("exist:result").get(key)

                for entry in place:
                    placeObject = Place()
                    placeObject.persId = personID 
                    typ = entry.get("@type")
                    if entry.get("@subtype"):
                        subtype = (entry.get("@subtype"))
                    else:
                        subtype = ""
                    
                    if entry.get("@key"):
                        key = (entry.get("@key"))
                    else:
                        key = ""

                    text = entry.get("#text")
                    when = entry.get("@when")
                   
                    placeObject.Text = text
                    placeObject.Type = typ
                    placeObject.Key = key
                    placeObject.Subtype = subtype
                    placeObject.When = when
                
                    print(placeObject)
                break

            # ASPEKT placeName
            elif tagName == "placename":
                placename = dict_data.get("exist:result").get(key)

                for entry in placename:
                    placenameObject = PlaceName()
                    placenameObject.persId = personID 
                    typ = entry.get("@type")
                    if entry.get("@subtype"):
                        subtype = (entry.get("@subtype"))
                    else:
                        subtype = ""
                    ana = entry.get("@ana")
                    when = entry.get("@when")
                   
                    placenameObject.Ana = ana
                    placenameObject.Type = typ
                    placenameObject.Subtype = subtype
                    placenameObject.When = when
                
                    print(placenameObject)
                break

            # ASPEKT Time
            elif tagName == "time":
                time = dict_data.get("exist:result").get(key)

                for entry in time:
                    personTime = Time()
                    personTime.persId = personID 
                    typ = entry.get("@type")
                    if entry.get("@subtype"):
                        subtype = (entry.get("@subtype"))
                    else:
                        subtype = ""
                    text = entry.get("#text")
                    when = entry.get("@when")
                   
                    personTime.Text = text
                    personTime.Type = typ
                    personTime.Subtype = subtype
                    personTime.When = when
                
                    print(personTime)
                break

    break
    