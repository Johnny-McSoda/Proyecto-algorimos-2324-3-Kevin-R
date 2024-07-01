import requests
import json

class cliente:
    def __init__(self,nombre,cedulad,edad,partido,entrada):
        self.nombre = nombre
        self.cedulad = cedulad
        self.edad = edad
        self.partido = partido
        self.entrada = entrada

class squad:
    def __init__(self,full_country,fifa_code,group):
        self.full_country = full_country
        self.fifa_code = fifa_code
        self.group = group

class local(squad):
    def __init__(self,full_country,fifa_code,group):
        squad.__init__(self,full_country,fifa_code,group)

    def __str__(self):
        return f'el equipo del pais {self.full_country} con con el id {self.fifa_code} son locales'
    
class visitor(squad):
     def __init__(self,full_country,fifa_code,group):
        squad.__init__(self,full_country,fifa_code,group)

     def __str__(self):
        return f'el equipo del pais {self.full_country} con con el id {self.fifa_code} son visitantes'

class stadium:
    def __init__(self,Sname,location,StaCode):
        self.Sname = Sname
        self.location = location
        #En el instructivo no se pide el id del estadio pero lo agrego a la clase ya que mas adelante lo voy a usar
        self.Stacode = StaCode

class match(local,visitor,stadium):
    #el 1 reepresenta 'home' y el 2 'away', lo pongo junto al nombre para recordarlos y diferernciarlos
    def __init__(self,full_country1,fifa_code1,group1,full_country2,fifa_code2,group2,time,number,Sname,location,Stacode):
        local.__init__(self,full_country1,fifa_code1,group1)
        visitor.__init__(self,full_country2,fifa_code2,group2)
        self.time = time
        self.number = number
        stadium.__init__(self,Sname,location,Stacode)
    
    def __str__(self):
        return f'El partido de {self.full_country1} contra {self.full_country2} llevado acabo el {self.time} en el estadio {self.Sname} de {self.location}'
    
    def __repr__(self):
        if int(self.number) < 10:
            return f'Nº0{self.number}.  {self.full_country1} vs {self.full_country2} / {self.Sname} - {self.location} / {self.time}'
        else:
            return f'Nº{self.number}.  {self.full_country1} vs {self.full_country2} / {self.Sname} - {self.location} / {self.time}'

#x = match(full_country1="EquipoA", fifa_code1="A123", group1="GrupoX",full_country2="EquipoB", fifa_code2="B456", group2="GrupoY",time="14:00", Sname="Estadio ABC", location="CiudadXYZ")

URLsquads = ('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json')
URLstadiums = ('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json')
URLmatches = ('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json')

stadium_list = []
date_list = []
country_list =  []

responce_list_complete = []
filter_list = ['paese','stadio','data']
filter_base = {'paese':{},'stadio':{},'data':{}}


def colador(cambio, tipo):
    j = filter_base[tipo]
    j.update({cambio : []})
    for i in responce_list_complete:
        julian = str(i).rfind(cambio)
        if julian != -1:
            j[cambio] += [i]    
        else:
            pass 



    



decodificador3 = requests.get(URLmatches)
foobaz = decodificador3.json()
for i in foobaz:
    #el 1 reepresenta 'home' y el 2 'away', lo pongo junto al nombre para diferenciarlo y recordarlos
    home1 = i['home']
    away2 = i ['away']
    #definiendo al pais local (home)
    match.full_country1 = home1['name']
    match.fifa_code1 = home1['id']
    match.group1 = home1['group']
    #definiendo al pais visitante
    match.full_country2 = away2['name']
    match.fifa_code2 = away2['id']
    match.group2 = away2['group']
    #definiendo el resto de la la clase "match"
    match.time = i['date']
    match.number = i['number']

    date_list.append(match.time)   #Aqui se guarda la fecha en una lista para luego facilitar su busqueda
    match.Stacode = i['stadium_id']
    #en este ciclo se compara el id del estadio con el id del match para determinar el nombre del estadio donde se lleva acabo el parido 
    decodificador2 = requests.get(URLstadiums)
    barbaz = decodificador2.json()
    for n in barbaz:
        stadium.Stacode = n['id']
        stadium.Sname = n['name']
        stadium.location = n['city']
        match.Stacode = i['stadium_id']
        if match.Stacode == stadium.Stacode:
            match.Sname = stadium.Sname
            match.location = stadium.location
            #print('El ID es igual por lo tanto el id del partido '+match.Stacode+' pertenecea al estadio '+match.Sname+'!!!!!!!!!!! \n')
        else:
            continue
    
    
    molde = match(match.full_country1,match.fifa_code1,match.group1,match.full_country2,match.fifa_code2,match.group2,match.time,match.number,match.Sname,match.location,match.Stacode)
        
    responce_list_complete.append(repr(molde))
    responce_list_complete.sort()

    colador(match.time,'data')


decodificador1 = requests.get(URLsquads)
foobar = decodificador1.json()
for i in foobar:
    squad.full_country = i['name']
    country_list.append(squad.full_country) #Aqui se guarda el pais en una lista para luego facilitar su busqueda
    squad.fifa_code = i['id']
    squad.group = i['group']
    

    colador(squad.full_country,'paese') # filtra paises


decodificador2 = requests.get(URLstadiums)
barbaz = decodificador2.json()
for i in barbaz:
    stadium.Sname = i['name']
    stadium_list.append(stadium.Sname) #Aqui se guarda el estadio en una lista para luego facilitar su busqueda
    stadium.location = i["city"]
    stadium.StaCode = i['id']

    colador(stadium.Sname,'stadio')
    
'''for key, value in filter_base['data'].items():
    print(f"{key}: \n{'\n'.join(value)} \n")'''
#print(filter_base)
   





def filtrador():
    while True:
        a = input('Desea filtrar los partidos? \n')
        if a.lower() == 'si':
            while True:
                print('Elija por cual opcion quiere filtrar los partidos en su busqueda: \n1. Filtrar por Pais \n2. Filtrar por Estadio \n3. Filtrar por Fecha') 
                obj = (input('Introduzca el numero del filtro que desee: \n'))
                if obj == '1':
                    for key, value in filter_base['Paese'].items():
                        print(f"{key}: \n{'\n'.join(value)} \n")
                    break
                elif obj == '2':
                    for key, value in filter_base['stadio'].items():
                        print(f"{key}: \n{'\n'.join(value)} \n")
                    break
                elif obj == '3':
                    for key, value in filter_base['data'].items():
                        print(f"{key}: \n{'\n'.join(value)} \n")
                    break
                else:
                    input('Introduzca un valor valido')
                    continue
            break
        elif a.lower() == 'no':
            print('\n'.join(responce_list_complete))
            break
        else:
            input('Introduzca un valor valido')
            continue




