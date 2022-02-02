
# coding: utf-8

# In[10]:


class Personaje:
    
    def __init__(self, nombre, vida, tiempo, puntos, destreza, resistencia, inteligencia, suerte):
        self.nombre = nombre
        self.vida = vida
        self.tiempo = tiempo
        self.puntos = puntos
        self.destreza = destreza
        self.resistencia = resistencia
        self.inteligencia = inteligencia
        self.suerte = suerte
        
        self.stats_vida = int(self.vida)
        self.stats_tiempo = int(self.tiempo)
        self.stats_puntos = int(self.puntos)
        self.stats_destreza = 0
        self.stats_resistencia = 0
        self.stats_inteligencia = 0
        self.stats_suerte = 0
        
    def __str__(self):
        return "V {}  D {}  R {}  I {}  S {}".format(int(self.stats_vida),int(self.stats_destreza),int(self.stats_resistencia),int(self.stats_inteligencia),int(self.stats_suerte))
     
    def agregar_consumible(self, consumible,parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte ):
        if consumible.atributo == "vida":
            parche1_vida += consumible.beneficio
            self.stats_vida += consumible.beneficio
        elif consumible.atributo == "destreza":
            parche1_destreza += consumible.beneficio
            self.stats_destreza += consumible.beneficio
        elif consumible.atributo == "resistencia":
            parche1_resistencia +=consumible.beneficio
            self.stats_resistencia += consumible.beneficio 
        elif consumible.atributo == "inteligencia":
            parche1_inteligencia+=consumible.beneficio
            self.stats_inteligencia += consumible.beneficio
        elif consumible.atributo == "suerte":
            parche1_suerte+=consumible.beneficio
            self.stats_suerte += consumible.beneficio
        self.stats_tiempo -= consumible.costo
        
        return parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte
    
    def quitar_consumible(self, consumible,parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte):
        self.stats_vida -= parche1_vida
        self.stats_destreza -= parche1_destreza
        self.stats_resistencia -= parche1_resistencia 
        self.stats_inteligencia -= parche1_inteligencia
        self.stats_suerte -= parche1_suerte
        parche1_vida = 0
        parche1_destreza = 0
        parche1_resistencia = 0
        parche1_inteligencia = 0
        parche1_suerte = 0
        
        return parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte
    
    def agregar_equipamiento(self, equipamiento):
        if equipamiento.atributo == "vida":
            self.stats_vida *= equipamiento.multiplicador
        elif equipamiento.atributo == "destreza":
            self.stats_destreza *= equipamiento.multiplicador
        elif equipamiento.atributo == "resistencia":
            self.stats_resistencia *= equipamiento.multiplicador
        elif equipamiento.atributo == "inteligencia":
            self.stats_inteligencia *= equipamiento.multiplicador
        elif equipamiento.atributo == "suerte":
            self.stats_suerte *= equipamiento.multiplicador
            
        return True
         
    def agregar_stats_inicial(self):
        print("Como quieres repartir tus {} puntos?".format(self.stats_puntos))
        final = False
        while not final:
            valido = False
            while not valido:
                agregar_vida = int(input("Vida: \n>>"))
                if self.stats_puntos >= agregar_vida:
                    self.stats_puntos -= agregar_vida
                    self.stats_vida += agregar_vida
                    
                elif self.stats_puntos < agregar_vida:
                    print("Lo siento, no tienes suficientes puntos para asignar a este atributo \nEmpezaremos otra vez por si te equivocaste al repartir")
                    break
                agregar_destreza = int(input("Destreza: \n>>"))
                if self.stats_puntos >= agregar_destreza:
                    self.stats_puntos -= agregar_destreza
                    self.stats_destreza += agregar_destreza
                    
                elif self.stats_puntos < agregar_destreza:
                    self.stats_puntos += agregar_vida
                    print("Lo siento, no tienes suficientes puntos para asignar a este atributo \nEmpezaremos otra vez por si te equivocaste al repartir")
                    break
                agregar_resistencia = int(input("Resistencia: \n>>"))
                if self.stats_puntos >= agregar_resistencia:
                    self.stats_puntos -= agregar_resistencia
                    self.stats_resistencia += agregar_resistencia
                    
                elif self.stats_puntos < agregar_resistencia:
                    self.stats_puntos += agregar_destreza
                    self.stats_puntos += agregar_vida
                    print("Lo siento, no tienes suficientes puntos para asignar a este atributo \nEmpezaremos otra vez por si te equivocaste al repartir")
                    break
                agregar_inteligencia = int(input("Inteligencia: \n>>"))
                if self.stats_puntos >= agregar_inteligencia:
                    self.stats_puntos -= agregar_inteligencia
                    self.stats_inteligencia += agregar_inteligencia
                    
                elif self.stats_puntos < agregar_inteligencia:
                    self.stats_puntos += agregar_resistencia
                    self.stats_puntos += agregar_destreza
                    self.stats_puntos += agregar_vida
                    print("Lo siento, no tienes suficientes puntos para asignar a este atributo \nEmpezaremos otra vez por si te equivocaste al repartir")
                    break
                agregar_suerte = int(input("Suerte: \n>>"))
                if self.stats_puntos >= agregar_suerte:
                    self.stats_puntos -= agregar_suerte
                    self.stats_suerte += agregar_suerte
                    
                elif self.stats_puntos < agregar_suerte:
                    self.stats_puntos += agregar_inteligencia
                    self.stats_puntos += agregar_resistencia
                    self.stats_puntos += agregar_destreza
                    self.stats_puntos += agregar_vida
                    print("Lo siento, no tienes suficientes puntos para asignar a este atributo \nEmpezaremos otra vez por si te equivocaste al repartir")
                    break
                if self.stats_puntos > 0:
                    print("¡Aún te sobran puntos! Debido a tus malas matemáticas los asignaremos a Suerte (la necesitarás)\n")
                    self.stats_suerte += self.stats_puntos
                    self.stats_puntos = 0
                    final = True
                    valido = True
                elif self.stats_puntos == 0:
                    final = True
                    valido = True
    
        
        
class Equipamiento:
    
    def __init__(self, nombre , atributo, multiplicador):
        self.nombre = nombre
        self.atributo = atributo
        self.multiplicador = multiplicador
    def __str__(self):
        return "{}: Bonificador {} a {}".format(self.nombre,float(self.multiplicador),self.atributo)
       
        
  
        
class Consumible:
    
    def __init__(self, nombre, cantidad, atributo, beneficio, costo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.atributo = atributo
        self.beneficio = beneficio
        self.costo = costo
    def __str__(self):
        return "{}: {} de tiempo, {} de {}".format(self.nombre,self.costo,self.beneficio,self.atributo)
    
class Interrogacion:
    
    def __init__(self, nombre, vida, destreza, resistencia, inteligencia, suerte, debilidad):
        self.nombre = nombre
        self.vida = int(vida)
        self.destreza = int(destreza)
        self.resistencia = int(resistencia)
        self.inteligencia = int(inteligencia)
        self.suerte = int(suerte)
        self.debilidad = debilidad
        if debilidad == "vida":
            self.debilidad = int(vida)
        elif debilidad == "destreza":
            self.debilidad = int(destreza)
        elif debilidad == "resistencia":
            self.debilidad = int(resistencia)
        elif debilidad== "inteligencia":
            self.debilidad = int(inteligencia)
        elif debilidad == "suerte":
            self.debilidad = int(suerte)
            
    def __str__(self):
        return "V {}  D {}  R {}  I {}  S {}".format(int(self.vida),int(self.destreza),int(self.resistencia),int(self.inteligencia),int(self.suerte))
            
class Simulacion:
    
    
    def __init__(self):
        self = self
        
    
    def simular(self, personaje, interrogacion):
        resultado = ((personaje.stats_destreza - interrogacion.destreza) + (personaje.stats_resistencia - interrogacion.resistencia) + (personaje.stats_inteligencia - interrogacion.inteligencia) + (personaje.stats_suerte - interrogacion.suerte))*(interrogacion.vida//interrogacion.debilidad)     
        if resultado >= 0:
            return 0
        elif resultado < 0:
            personaje.stats_vida += resultado
            return int(-resultado)
    
    
    
    
    
with open('base.txt') as file:
    jugadas = 0
    parche1_vida = 0
    parche1_destreza = 0
    parche1_resistencia = 0
    parche1_inteligencia = 0
    parche1_suerte = 0
    stats_iniciales = ""
    
    equipamientos_utilizados = []
    consumibles_utilizados = []
    lista_equipamientos= []
    lista_consumibles = []
    lista_interrogaciones = []
    vida, tiempo, puntos = file.readline().split(",")
    variedad_consumibles, variedad_equipamientos = file.readline().split(",")
    print("Bienvenido a la simulación de pruebas")
    nombre_personaje = input("El nombre de tu personaje será: \n>> ")
    print("Bienvenido {}, te informo que comenzarás esta partida con: \n{} puntos de Vida base \n{} puntos de Tiempo \n{} puntos para gastar en stats iniciales\n".format(nombre_personaje, vida, tiempo, puntos.replace("\n","")))
    jugador = Personaje(nombre_personaje,vida,tiempo,puntos,0,0,0,0)
    jugador.agregar_stats_inicial()
    print("Tus stats iniciales son: \nVida: {}, Destreza: {}, Resistencia: {}, Inteligencia: {}, Suerte: {}\n".format(jugador.stats_vida, jugador.stats_destreza,jugador.stats_resistencia,jugador.stats_inteligencia,jugador.stats_suerte))
    stats_iniciales += "{}".format(jugador)
    print("Aquí hay un listado con los equipamientos que tenemos para tí, elige un número para equiparlo\nEn caso de que ya no quieras equiparte más ingresa -1\n")
    i = 1
    for line in file:
        line_list = line.split(",")
        if "Interrogacion" in line_list[0]:
            lista_interrogaciones.append(line)
        if len(line_list[0])>3 and ("Interrogacion" not in line_list[0]) and line_list[1].isdigit():
            lista_consumibles.append(line)
        if (len(line_list[1]) > 2) and ("Interrogacion" not in line_list[0]):  
            lista_equipamientos.append(line)
            print("{}.- {}: Bonificador {} a {}".format(i,line_list[0],float(line_list[2]),line_list[1]))
            i+=1
    respuesta_equipamientos = int(input(">> "))       
    while respuesta_equipamientos != -1:
        i= 1
        e_list = lista_equipamientos[respuesta_equipamientos-1].split(",")
        equipamiento = Equipamiento(e_list[0],e_list[1],float(e_list[2].replace("\n","")))
        jugador.agregar_equipamiento(equipamiento)
        del lista_equipamientos[respuesta_equipamientos-1]
        for elemento in lista_equipamientos:
            lista_elemento = elemento.split(",")
            print("{}.- {}: Bonificador {} a {}".format(i,lista_elemento[0],float(lista_elemento[2]),lista_elemento[1]))
            i+=1
        equipamientos_utilizados.append("{}".format(equipamiento))
        respuesta_equipamientos = int(input(">> "))
        if lista_equipamientos == []:
            print("Ya utilizaste todo el equipamiento disponible! Pasemos a los consumibles")
            break
    vida_inicial = jugador.stats_vida
    tiempo_inicial = jugador.stats_tiempo
    for prueba in lista_interrogaciones:
        lista_prueba = prueba.split(",")
        interrogacion = Interrogacion(lista_prueba[0],lista_prueba[1],lista_prueba[2],lista_prueba[3],lista_prueba[4],lista_prueba[5],lista_prueba[6].replace("\n",""))
        
        print("\nAquí están los consumibles, selecciona el número del objeto que deseas\nPara comenzar la evaluación ingresa -1\nStats actuales: {}\nTiempo disponible: {}\n".format(jugador,jugador.stats_tiempo))
        i = 1
        for elemento_consumible in lista_consumibles:
            c_list = elemento_consumible.split(",")
            print("{}.- ({}) {}: {} de tiempo, {} de {}".format(i,c_list[1],c_list[0],c_list[4].replace("\n",""),c_list[3],c_list[2]))
            i+=1

        respuesta_consumibles = int(input(">> "))
        while respuesta_consumibles != -1:
            i=1
            c_list_final = lista_consumibles[respuesta_consumibles-1].split(",")
            
            c_list_final[1] = int(c_list_final[1])-1
            c_list[1]= int(c_list[1])-1
           
            consumible = Consumible(c_list_final[0],c_list_final[1],c_list_final[2],int(c_list_final[3]),int(c_list[4].replace("\n","")))
            parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte = jugador.agregar_consumible(consumible,parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte )
            if c_list_final[1] == 0:
                del lista_consumibles[respuesta_consumibles-1]
            print("\nStats actuales: {}\nTiempo disponible: {}\n".format(jugador,jugador.stats_tiempo))
            for elemento_consumible_final in lista_consumibles:
                c_list_2 = elemento_consumible_final.split(",")
                print("{}.- ({}) {}: {} de tiempo, {} de {}".format(i,c_list_2[1],c_list_2[0],c_list_2[4].replace("\n",""),c_list_2[3],c_list_2[2]))
                i+=1
                
            consumibles_utilizados.append("{}".format(consumible))
            respuesta_consumibles = int(input(">> "))

        print("\nLlegó la hora de la evaluación!\nPrepárate {} para enfrentar a la {}\nEsta prueba posee {} y es débil contra la {}\nPodrás superarla?\n".format(jugador.nombre, interrogacion.nombre, interrogacion, lista_prueba[6].replace("\n","")))
        print("2 horas, 2 minutos, 2 segundos... y 2 semanas después...\n")
        resultado = Simulacion().simular(jugador, interrogacion)
        if jugador.stats_vida <= 0:
            print("Lamentablemente esta interrogación fue mucho para ti, te quedaste sin puntos de vida :( suerte la próxima!")
            break
        elif jugador.stats_vida > 0:
            if resultado !=0:
                print("¡Lograste superar la interrogación! Sin embargo, perdiste {} puntos de vida en ella, te quedan {} puntos de vida actualmente\n".format(resultado,jugador.stats_vida))
                             
            if resultado == 0:
                print("Lograste superar la interrogación con honores, esta vez no pierdes puntos de vida ¡Felicitaciones!")
            parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte=jugador.quitar_consumible(consumible,parche1_vida,parche1_destreza,parche1_resistencia,parche1_inteligencia,parche1_suerte)
            
            jugadas +=1
            if jugadas <3:
                print("¿Estás listo para el siguiente combate? Comienza a preparate!")
            elif jugadas ==3:
                print("Acabas de aprobar las 3 interrogaciones, eso quiere decir que pasaste el curso! Felicitaciones! ")
                guardar = input("Deseas guardar los datos de la partida? (Si/No)\n>>")
                if guardar == "No":
                    print("Tus stats finales son: {}".format(jugador))
                    print("El juego ha terminado! Gracias por jugar")
                    pass
                elif guardar == "Si":
                    archivo = input("Que nombre deseas poner a tu archivo? (El \".txt\" lo ponemos nosotros ;))\n>>")
                    with open("{}.txt".format(archivo),"w") as archivo:
                        delta_vida = vida_inicial-jugador.stats_vida 
                        delta_tiempo = tiempo_inicial- jugador.stats_tiempo
                        archivo.write(jugador.nombre+ "\n")
                        archivo.write("{}".format(stats_iniciales+"\n"))
                        archivo.write("{}\n".format(jugador))
                        archivo.write("{}\n".format(delta_vida))
                        for b in consumibles_utilizados:
                            archivo.write("{}\n".format(b))
                        for a in equipamientos_utilizados:
                            archivo.write("{}\n".format(a))
                        for c in lista_interrogaciones:
                            cc = c.split(",")
                            archivo.write("{},".format(cc[0].replace("\n","")))
                        archivo.write("\n{}".format(delta_tiempo))
                    print("Tu archivo se ha guardado correctamente")


    

    
    
    


# In[ ]:




