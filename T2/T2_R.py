
# coding: utf-8

# In[1]:


def generar_nuevo_tablero():
    Inter1 = ["|","\\","|","/","|","\\","|","/","|"]
    Inter2 = ["|","/","|","\\","|","/","|","\\","|"]
    F1 = ["G","-","G","-","G","-","G","-","G"]
    F2 = ["G","-","G","-","G","-","G","-","G"]
    F3 = ["G","-","N","-","C","-","N","-","G"]
    F4 = ["N","-","N","-","N","-","N","-","N"]
    F5 = ["N","-","N","-","N","-","N","-","N"]
    lista_tablero = [F1,Inter1,F2,Inter2,F3,Inter1,F4,Inter2,F5 ]
    
    return lista_tablero

def mostrar_tablero(lista_tablero):
    for elemento in lista_tablero:
        print(" ".join(elemento))
    return lista_tablero

def guardar(Nombre_Gallinas, Nombre_Coyote,movimientos,lista_tablero):
    nombre_archivo = input("Con que nombre quieres guardar tu partida?")
    file = open(nombre_archivo+'.txt', 'a')
    file.write("{},{} \n".format(Nombre_Coyote, Nombre_Gallinas))
    file.write(movimientos + "\n")
    tablero = open("tablero.txt", 'w')
    tablero.write(lista_tablero + "\n")
    file.close()

def archivo_tablero(lista_tablero):
    guardar_tablero = ""
    for fila in lista_tablero:
        final_tablero = " ".join(fila) + "\n"
        guardar_tablero += final_tablero 
    return guardar_tablero    
        
def archivo_movimientos(movimientos):
    guardar_movimientos = ""
    for elemento in movimientos:
        final_movimientos = ",".join(elemento) + "\n"
        guardar_movimientos += final_movimientos 
    return guardar_movimientos

def C_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero,gallinas):
    gallinas_obligatorias = 0
    if not C_confirmar_fila_final(columna_final,fila_final,lista_tablero):
        return False
    if C_confirmar_fila_final(columna_final,fila_final,lista_tablero):
        gallinas_obligatorias = 0
        fila_inicial = (1/2)*fila_inicial
        fila_final = (1/2)*fila_final
        columna_inicial = (1/2)*columna_inicial
        columna_final = (1/2)*columna_final
        
        if (fila_inicial + columna_inicial)%2 ==0: # Movimiento validos cuando la posicion es par
            fila_inicial = (2)*fila_inicial
            fila_final = (2)*fila_final
            columna_inicial = (2)*columna_inicial
            columna_final = (2)*columna_final
            
            if gallinas <= 11:
            
            #######
            
                if (str(lista_tablero[int(fila_inicial)][int(columna_inicial+2)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial)][int(columna_inicial+4)]) == "N"):
                        gallinas_obligatorias +=1
                if (str(lista_tablero[int(fila_inicial)][int(columna_inicial-2)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial)][int(columna_inicial-4)]) == "N"):
                        gallinas_obligatorias +=1
                if (str(lista_tablero[int(fila_inicial+2)][int(columna_inicial)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial+4)][int(columna_inicial)]) == "N"):
                        gallinas_obligatorias +=1
                if (str(lista_tablero[int(fila_inicial-2)][int(columna_inicial)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial-4)][int(columna_inicial)]) == "N"):
                        gallinas_obligatorias +=1
                
                if (str(lista_tablero[int(fila_inicial+2)][int(columna_inicial+2)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial+4)][int(columna_inicial+4)]) == "N"):
                        gallinas_obligatorias +=1      
                if (str(lista_tablero[int(fila_inicial+2)][int(columna_inicial-2)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial+4)][int(columna_inicial-4)]) == "N"):
                        gallinas_obligatorias +=1        
                if (str(lista_tablero[int(fila_inicial-2)][int(columna_inicial+2)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial-4)][int(columna_inicial+4)]) == "N"):
                        gallinas_obligatorias +=1
                if (str(lista_tablero[int(fila_inicial-2)][int(columna_inicial-2)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial-4)][int(columna_inicial-4)]) == "N"):
                        gallinas_obligatorias +=1
                        
                if gallinas_obligatorias != 0:
                    if (abs(fila_inicial - fila_final) <= 2) and (abs(columna_inicial -columna_final) <= 2):
                        return False
                    elif (fila_inicial +4 == fila_final) and (columna_inicial +4 == columna_final):
                        if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial+2)]) == "G":
                            lista_tablero[int(fila_inicial+2)][int(columna_inicial+2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial +4 == fila_final) and (columna_inicial - 4 == columna_final):
                        if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial-2)]) == "G":
                            lista_tablero[int(fila_inicial+2)][int(columna_inicial-2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO #####
                    elif (fila_inicial -4 == fila_final) and (columna_inicial +4 == columna_final):
                        if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial+2)]) == "G":
                            lista_tablero[int(fila_inicial-2)][int(columna_inicial+2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial -4 == fila_final) and (columna_inicial -4 == columna_final):
                        if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial-2)]) == "G":

                            lista_tablero[int(fila_inicial-2)][int(columna_inicial-2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                
                    elif (fila_inicial -4 == fila_final) and (columna_inicial == columna_final):
                        if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial)]) == "G":
                            lista_tablero[int(fila_inicial-2)][int(columna_inicial)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial +4 == fila_final) and (columna_inicial == columna_final): 
                        if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial)]) == "G":
                            lista_tablero[int(fila_inicial+2)][int(columna_inicial)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial == fila_final) and (columna_inicial -4 == columna_final):    
                        if str(lista_tablero[int(fila_inicial)][int(columna_inicial-2)]) == "G":
                            lista_tablero[int(fila_inicial)][int(columna_inicial-2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial == fila_final) and (columna_inicial +4 == columna_final):
                        if str(lista_tablero[int(fila_inicial)][int(columna_inicial+2)]) == "G":
                            lista_tablero[int(fila_inicial)][int(columna_inicial+2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    else:
                        return False
                
                if gallinas_obligatorias ==0:
                    if (abs(fila_inicial - fila_final) <= 2) and (abs(columna_inicial -columna_final) <= 2):
                        return True
                    else:
                        return False
            #######
            if gallinas == 12:
                if (abs(fila_inicial - fila_final) <= 2) and (abs(columna_inicial -columna_final) <= 2):
                    return True
                elif (fila_inicial +4 == fila_final) and (columna_inicial +4 == columna_final):
                    if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial+2)]) == "G":
                        lista_tablero[int(fila_inicial+2)][int(columna_inicial+2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial +4 == fila_final) and (columna_inicial - 4 == columna_final):
                    if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial-2)]) == "G":
                        lista_tablero[int(fila_inicial+2)][int(columna_inicial-2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO #####
                elif (fila_inicial -4 == fila_final) and (columna_inicial +4 == columna_final):
                    if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial+2)]) == "G":
                        lista_tablero[int(fila_inicial-2)][int(columna_inicial+2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial -4 == fila_final) and (columna_inicial -4 == columna_final):
                    if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial-2)]) == "G":

                        lista_tablero[int(fila_inicial-2)][int(columna_inicial-2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                
                elif (fila_inicial -4 == fila_final) and (columna_inicial == columna_final):
                    if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial)]) == "G":
                        lista_tablero[int(fila_inicial-2)][int(columna_inicial)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial +4 == fila_final) and (columna_inicial == columna_final): 
                    if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial)]) == "G":
                        lista_tablero[int(fila_inicial+2)][int(columna_inicial)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial == fila_final) and (columna_inicial -4 == columna_final):
                    if str(lista_tablero[int(fila_inicial)][int(columna_inicial-2)]) == "G":
                        lista_tablero[int(fila_inicial)][int(columna_inicial-2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial == fila_final) and (columna_inicial +4 == columna_final):
                    if str(lista_tablero[int(fila_inicial)][int(columna_inicial+2)]) == "G":
                        lista_tablero[int(fila_inicial)][int(columna_inicial+2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
            
            
        if (fila_inicial + columna_inicial)%2 ==1: ## Movimientos validos cuando la posicion es impar
            fila_inicial = (2)*fila_inicial
            fila_final = (2)*fila_final
            columna_inicial = (2)*columna_inicial
            columna_final = (2)*columna_final
            
            #######
            if gallinas == 11:
                if (str(lista_tablero[int(fila_inicial)][int(columna_inicial+2)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial)][int(columna_inicial+4)]) == "N"):
                        gallinas_obligatorias +=1
                if (str(lista_tablero[int(fila_inicial)][int(columna_inicial-2)]) == "G"): 
                    if (str(lista_tablero[int(fila_inicial)][int(columna_inicial-4)]) == "N"):
                        gallinas_obligatorias +=1
                if (str(lista_tablero[int(fila_inicial+2)][int(columna_inicial)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial+4)][int(columna_inicial)]) == "N"):
                        gallinas_obligatorias +=1
                if (str(lista_tablero[int(fila_inicial-2)][int(columna_inicial)]) == "G"):
                    if (str(lista_tablero[int(fila_inicial-4)][int(columna_inicial)]) == "N"):
                        gallinas_obligatorias +=1
                    
                    
                    
                if gallinas_obligatorias != 0:
                    if (abs(fila_inicial - fila_final) ==2) and (columna_inicial == columna_final):
                        return False
                    elif (abs(columna_inicial - columna_final)==2) and (fila_inicial == fila_final):
                        return False
                    elif (fila_inicial -4 == fila_final) and (columna_inicial == columna_final):
                        if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial)]) == "G":
                            lista_tablero[int(fila_inicial-2)][int(columna_inicial)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial +4 == fila_final) and (columna_inicial == columna_final): 
                        if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial)]) == "G":
                            lista_tablero[int(fila_inicial+2)][int(columna_inicial)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial == fila_final) and (columna_inicial -4 == columna_final):    
                        if str(lista_tablero[int(fila_inicial)][int(columna_inicial-2)]) == "G":
                            lista_tablero[int(fila_inicial)][int(columna_inicial-2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    elif (fila_inicial == fila_final) and (columna_inicial +4 == columna_final):
                        if str(lista_tablero[int(fila_inicial)][int(columna_inicial+2)]) == "G":
                            lista_tablero[int(fila_inicial)][int(columna_inicial+2)] = "N"
                            lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                            lista_tablero[int(fila_final)][int(columna_final)] = "C"
                            mostrar_tablero(lista_tablero)
                            return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                    else:
                        return False
                if gallinas_obligatorias ==0:
                    if (abs(fila_inicial - fila_final) ==2) and (columna_inicial == columna_final):
                        return True
                    elif (abs(columna_inicial - columna_final)==2) and (fila_inicial == fila_final):
                        return True
                    else:
                        return False
                    
                
            
            #######
            if gallinas == 12:
                if (abs(fila_inicial - fila_final) ==2) and (columna_inicial == columna_final):
                    return True
                elif (abs(columna_inicial - columna_final)==2) and (fila_inicial == fila_final):
                    return True
                elif (fila_inicial -4 == fila_final) and (columna_inicial == columna_final):
                    if str(lista_tablero[int(fila_inicial-2)][int(columna_inicial)]) == "G":
                        lista_tablero[int(fila_inicial-2)][int(columna_inicial)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial +4 == fila_final) and (columna_inicial == columna_final): 
                    if str(lista_tablero[int(fila_inicial+2)][int(columna_inicial)]) == "G":
                        lista_tablero[int(fila_inicial+2)][int(columna_inicial)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial == fila_final) and (columna_inicial -4 == columna_final):    
                    if str(lista_tablero[int(fila_inicial)][int(columna_inicial-2)]) == "G":
                        lista_tablero[int(fila_inicial)][int(columna_inicial-2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                elif (fila_inicial == fila_final) and (columna_inicial +4 == columna_final):
                    if str(lista_tablero[int(fila_inicial)][int(columna_inicial+2)]) == "G":
                        lista_tablero[int(fila_inicial)][int(columna_inicial+2)] = "N"
                        lista_tablero[int(fila_inicial)][int(columna_inicial)] = "N"  
                        lista_tablero[int(fila_final)][int(columna_final)] = "C"
                        mostrar_tablero(lista_tablero)
                        return True ##### PONER CUANDO PUEDE HACER MAS DE UN MOVIMIENTO ######
                else:
                    return False


def nueva_partida():
    Nombre_Gallinas = str(input("El nombre de las Gallinas será: "))
    Nombre_Coyote = str(input("El nombre del Coyote será: "))

    return Nombre_Coyote, Nombre_Gallinas

def revisar_gallinas(lista_tablero):
    gallinas_restantes = 0
    for elemento in lista_tablero:
        for letra in elemento:
            if letra == "G":
                gallinas_restantes+=1
    return gallinas_restantes
            
def revisar_coyote(lista_tablero):
    coyote_atrapado = False
    lista_gallinas = []
    a = 0
    b = 0
    i = 0
    j = 0
    for i in range (len(lista_tablero)):
        for j in range (len(lista_tablero[i])):
            if lista_tablero[i][j] == "C":
                posicion_coyote = i,j
                rp1= "{},{}".format(i+2,j) 
                rp2= "{},{}".format(i+4,j) 
                rp3= "{},{}".format(i-2,j) 
                rp4= "{},{}".format(i-4,j)
                rp5= "{},{}".format(i,j+2) 
                rp6= "{},{}".format(i,j+4) 
                rp7= "{},{}".format(i,j-2) 
                rp8= "{},{}".format(i,j-4) 
                
                rp9= "{},{}".format(i+2,j+2) 
                rp10= "{},{}".format(i+4,j+4) 
                rp11= "{},{}".format(i+2,j-2) 
                rp12= "{},{}".format(i+4,j-4) 
                rp13= "{},{}".format(i-2,j-2)
                rp14= "{},{}".format(i-4,j-4) 
                rp15= "{},{}".format(i-2,j+2) 
                rp16= "{},{}".format(i-4,j+4)   
                break
    for a in range (len(lista_tablero)):
        for b in range (len(lista_tablero[a])):
            if lista_tablero[a][b] == "G":
                lista_gallinas += ["{},{}".format(a,b)]
                
    posicion_gallinas = " ".join(lista_gallinas)
    if posicion_coyote[0] ==4 and posicion_coyote[1] == 4:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and  (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp9 in posicion_gallinas) and (rp10 in posicion_gallinas) and (rp11 in posicion_gallinas) and (rp12 in posicion_gallinas) and (rp13 in posicion_gallinas) and (rp14 in posicion_gallinas) and (rp15 in posicion_gallinas) and  (rp16 in posicion_gallinas):  
            coyote_atrapado = True
            
    if posicion_coyote[0] ==0 and posicion_coyote[1] == 0:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp9 in posicion_gallinas) and (rp10 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas):
            coyote_atrapado = True
            
    if posicion_coyote[0] ==0 and posicion_coyote[1] == 2:
        if (rp7 in posicion_gallinas) and (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas):
            coyote_atrapado = True
            
    if posicion_coyote[0] ==0 and posicion_coyote[1] == 4:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp9 in posicion_gallinas) and (rp10 in posicion_gallinas) and (rp11 in posicion_gallinas) and (rp12 in posicion_gallinas):
            coyote_atrapado = True
            
    if posicion_coyote[0] ==0 and posicion_coyote[1] == 6:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp5 in posicion_gallinas):
            coyote_atrapado = True
            
    if posicion_coyote[0] ==0 and posicion_coyote[1] == 8:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp7 in posicion_gallinas):
            coyote_atrapado = True      
    if posicion_coyote[0] ==2 and posicion_coyote[1] == 0:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas):
            coyote_atrapado = True
    if posicion_coyote[0] ==2 and posicion_coyote[1] == 2:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp9 in posicion_gallinas) and (rp10 in posicion_gallinas) and (rp15 in posicion_gallinas) and (rp13 in posicion_gallinas) and (rp11 in posicion_gallinas) and (rp7 in posicion_gallinas):
            coyote_atrapado = True
    if posicion_coyote[0] ==2 and posicion_coyote[1] == 4:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas)  and (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas):
            coyote_atrapado = True
    if posicion_coyote[0] ==2 and posicion_coyote[1] == 6:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp9 in posicion_gallinas) and (rp15 in posicion_gallinas)  and (rp13 in posicion_gallinas) and (rp11 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp12 in posicion_gallinas):
            coyote_atrapado = True
    if posicion_coyote[0] ==2 and posicion_coyote[1] == 8:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas)  and (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas):
            coyote_atrapado = True
    if posicion_coyote[0] ==4 and posicion_coyote[1] == 0:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp9 in posicion_gallinas) and (rp10 in posicion_gallinas) and (rp15 in posicion_gallinas) and  (rp16 in posicion_gallinas): 
            coyote_atrapado = True
    if posicion_coyote[0] ==4 and posicion_coyote[1] == 2:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas)  and (rp7 in posicion_gallinas): 
            coyote_atrapado = True
    if posicion_coyote[0] ==4 and posicion_coyote[1] == 6:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp8 in posicion_gallinas)  and (rp7 in posicion_gallinas): 
            coyote_atrapado = True
    if posicion_coyote[0] ==4 and posicion_coyote[1] == 8:
        if (rp1 in posicion_gallinas) and (rp2 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp11 in posicion_gallinas) and (rp12 in posicion_gallinas) and (rp13 in posicion_gallinas) and  (rp14 in posicion_gallinas): 
            coyote_atrapado = True
    if posicion_coyote[0] ==6 and posicion_coyote[1] == 0:
        if (rp1 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas):
            coyote_atrapado = True
    if posicion_coyote[0] ==6 and posicion_coyote[1] == 2:
        if (rp1 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp13 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp11 in posicion_gallinas) and (rp15 in posicion_gallinas) and (rp16 in posicion_gallinas) and (rp9 in posicion_gallinas):
            coyote_atrapado = True 
    if posicion_coyote[0] ==6 and posicion_coyote[1] == 4:
        if (rp1 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp7 in posicion_gallinas):
            coyote_atrapado = True 
    if posicion_coyote[0] ==6 and posicion_coyote[1] == 6:
        if (rp1 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp13 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp11 in posicion_gallinas) and (rp15 in posicion_gallinas) and (rp14 in posicion_gallinas) and (rp9 in posicion_gallinas):
            coyote_atrapado = True 
    if posicion_coyote[0] ==6 and posicion_coyote[1] == 8:
        if (rp1 in posicion_gallinas) and (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas):
            coyote_atrapado = True 
    if posicion_coyote[0] ==8 and posicion_coyote[1] == 0:
        if (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp15 in posicion_gallinas) and  (rp16 in posicion_gallinas):
            coyote_atrapado = True   
    if posicion_coyote[0] ==8 and posicion_coyote[1] == 2:
         if (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp7 in posicion_gallinas):
                coyote_atrapado = True 
    if posicion_coyote[0] ==8 and posicion_coyote[1] == 4:
        if (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp6 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp15 in posicion_gallinas) and  (rp16 in posicion_gallinas) and (rp13 in posicion_gallinas) and (rp14 in posicion_gallinas):
            coyote_atrapado = True 
    if posicion_coyote[0] ==8 and posicion_coyote[1] == 6:
        if (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp5 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas):
            coyote_atrapado = True 
    if posicion_coyote[0] ==8 and posicion_coyote[1] == 8:
        if (rp3 in posicion_gallinas) and (rp4 in posicion_gallinas) and (rp7 in posicion_gallinas) and (rp8 in posicion_gallinas) and (rp13 in posicion_gallinas) and (rp14 in posicion_gallinas):
            coyote_atrapado = True 
    
    
    return coyote_atrapado
    
                
    
    
    
######## JUGADA GALLINAS #########    
def jugada_gallinas(Nombre_Gallinas,movimientos,lista_tablero):
    Prefijo_Gallina = ["G"]                                                     
    posicion_valida = False       
    while not posicion_valida:
        Jugada_Gallina = str(input("Es el turno de {}!, ¿Cuál será tu movimiento? \no deseas guardar la partida y salir (G) \no solamente salir (S)\n".format(tupla[1])))
        if Jugada_Gallina == "G":
            return "guardar"
        if Jugada_Gallina == "S": 
            return "salir"
        else:
            lista_gallina = Jugada_Gallina.split(",")
            columna_inicial = int(lista_gallina[0])
            fila_inicial = int(lista_gallina[1])
            columna_final = int(lista_gallina[2])
            fila_final = int(lista_gallina[3])
            if ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                fila_inicial = 2*fila_inicial
                fila_final = 2*fila_final
                columna_inicial = 2*columna_inicial
                columna_final = 2*columna_final
                if not G_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero):
                    print("La posición de partida escogida es incorrecta :( Intenta otra vez!")
                elif not G_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero):
                    print("La posición de llegada escogida es incorrecta :( Intenta otra vez!")
                elif G_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero) and G_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero) :
                    posicion_valida = G_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero) #Tengo que retornar un False
                    Prefijo_Gallina.append(Jugada_Gallina)
                    movimientos += [Prefijo_Gallina]
                    lista_tablero[fila_inicial][columna_inicial] = "N"  
                    lista_tablero[fila_final][columna_final] = "G"
            elif not ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                print("Las coordenadas elegidas no son validas! Intenta otra vez!")
              
    return movimientos
    
####### JUGADA GALLINAS ##########
def jugada_gallinas_cargar(movimientos,lista_tablero,jugada_final):
    Prefijo_Gallina = ["G"]                                                     
    posicion_valida = False       
    while not posicion_valida:
        Jugada_Gallina = jugada_final
        if Jugada_Gallina == "G":
            return "guardar"
        if Jugada_Gallina == "S": 
            return "salir"
        else:
            lista_gallina = Jugada_Gallina.split(",")
            columna_inicial = int(lista_gallina[0])
            fila_inicial = int(lista_gallina[1])
            columna_final = int(lista_gallina[2])
            fila_final = int(lista_gallina[3])
            if ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                fila_inicial = 2*fila_inicial
                fila_final = 2*fila_final
                columna_inicial = 2*columna_inicial
                columna_final = 2*columna_final
                if not G_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero):
                    print("La posición de partida escogida es incorrecta :( Intenta otra vez!")
                elif not G_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero):
                    print("La posición de llegada escogida es incorrecta :( Intenta otra vez!")
                elif G_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero) and G_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero) :
                    posicion_valida = G_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero) #Tengo que retornar un False
                    Prefijo_Gallina.append(Jugada_Gallina)
                    movimientos += [Prefijo_Gallina]
                    lista_tablero[fila_inicial][columna_inicial] = "N"  
                    lista_tablero[fila_final][columna_final] = "G"
            elif not ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                print("Las coordenadas elegidas no son validas! Intenta otra vez!")
              
    return movimientos



####### JUGADA COYOTE ######## 

def jugada_coyote(Nombre_Coyote,movimientos,lista_tablero):
    obligatorio = False
    gallinas = revisar_gallinas(lista_tablero)
    if gallinas<= 10:         
        return True
    if gallinas > 10:
        Prefijo_Coyote = ["C"]                                                                                 
        posicion_valida = False        
        while not posicion_valida:
            gallinas = revisar_gallinas(lista_tablero)
            if gallinas<= 10:
                valido =False
                break
            Jugada_Coyote = str(input("Es el turno de {}!, ¿Cuál será tu movimiento? \no deseas guardar la partida y salir (G) \no solamente salir (S)\n".format(tupla[0])))
            if Jugada_Coyote == "G":
                return "guardar"
            if Jugada_Coyote == "S": 
                return "salir"
            else:
                lista_coyote = Jugada_Coyote.split(",")
                columna_inicial = int(lista_coyote[0])
                fila_inicial = int(lista_coyote[1])
                columna_final = int(lista_coyote[2])
                fila_final = int(lista_coyote[3])
                if ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                    fila_inicial = 2*fila_inicial
                    fila_final = 2*fila_final
                    columna_inicial = 2*columna_inicial
                    columna_final = 2*columna_final
                    if not C_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero):
                        print("La posición de partida escogida es incorrecta :( Intenta otra vez!")
                    if not C_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero,gallinas):
                        print("La posición de llegada escogida es incorrecta :( Intenta otra vez!")
                    elif C_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero) and C_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero,gallinas):
                        posicion_valida = C_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero,gallinas) 
                        Prefijo_Coyote.append(Jugada_Coyote)
                        movimientos += [Prefijo_Coyote]
                        lista_tablero[fila_inicial][columna_inicial] = "N"  
                        lista_tablero[fila_final][columna_final] = "C"
                        gallinas_final = revisar_gallinas(lista_tablero)      
                elif not ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                    print("Las coordenadas elegidas no son validas! Intenta otra vez!")
        
        return movimientos
    
######## JUGADA COYOTE ########   
def jugada_coyote_cargar(movimientos,lista_tablero,jugada_final):
    obligatorio = False
    gallinas = revisar_gallinas(lista_tablero)
    if gallinas<= 10:         
        return True
    if gallinas > 10:
        Prefijo_Coyote = ["C"]                                                                                 
        posicion_valida = False        
        while not posicion_valida:
            gallinas = revisar_gallinas(lista_tablero)
            if gallinas<= 10:
                valido =False
                break
            Jugada_Coyote = jugada_final
            if Jugada_Coyote == "G":
                return "guardar"
            if Jugada_Coyote == "S": 
                return "salir"
            else:
                lista_coyote = Jugada_Coyote.split(",")
                columna_inicial = int(lista_coyote[0])
                fila_inicial = int(lista_coyote[1])
                columna_final = int(lista_coyote[2])
                fila_final = int(lista_coyote[3])
                if ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                    fila_inicial = 2*fila_inicial
                    fila_final = 2*fila_final
                    columna_inicial = 2*columna_inicial
                    columna_final = 2*columna_final
                    if not C_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero):
                        print("La posición de partida escogida es incorrecta :( Intenta otra vez!")
                    if not C_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero,gallinas):
                        print("La posición de llegada escogida es incorrecta :( Intenta otra vez!")
                    elif C_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero) and C_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero,gallinas):
                        posicion_valida = C_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero,gallinas) 
                        Prefijo_Coyote.append(Jugada_Coyote)
                        movimientos += [Prefijo_Coyote]
                        lista_tablero[fila_inicial][columna_inicial] = "N"  
                        lista_tablero[fila_final][columna_final] = "C"
                        gallinas_final = revisar_gallinas(lista_tablero)      
                elif not ((0<= fila_inicial <=4) and (0<= fila_final <=4) and (0<= columna_inicial <=4) and (0<= columna_final <=4)):
                    print("Las coordenadas elegidas no son validas! Intenta otra vez!")
        
        return movimientos



def G_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero):
    if G_confirmar_columna_inicial(fila_inicial,columna_inicial,lista_tablero):
        return True
    else:
        return False
       
    
def G_confirmar_columna_inicial(fila_inicial,columna_inicial,lista_tablero):
    if G_confirmar_posicion_inicial(fila_inicial,columna_inicial,lista_tablero):
        return True
    else:
        return False
        
        
            
def G_confirmar_posicion_inicial(fila_inicial,columna_inicial,lista_tablero):
    if lista_tablero[fila_inicial][columna_inicial] == "G":
        return True
    else:
        return False
    
def C_confirmar_fila_inicial(columna_inicial,fila_inicial,lista_tablero):
    if C_confirmar_columna_inicial(fila_inicial,columna_inicial,lista_tablero):
        return True
    else:
        return False
                     
def C_confirmar_columna_inicial(fila_inicial,columna_inicial,lista_tablero):
    if C_confirmar_posicion_inicial(fila_inicial,columna_inicial,lista_tablero):
        return True
    else:
        return False
                  
def C_confirmar_posicion_inicial(fila_inicial,columna_inicial,lista_tablero):
    if lista_tablero[fila_inicial][columna_inicial] == "C":
        return True
    else:
        return False

######## Jugadas finales ######

def G_confirmar_fila_final(columna_final,fila_final,lista_tablero):
    if G_confirmar_columna_final(fila_final,columna_final,lista_tablero):
        return True
    else:
        return False
           
def G_confirmar_columna_final(fila_final,columna_final,lista_tablero):
    if G_confirmar_posicion_final(fila_final,columna_final,lista_tablero):
        return True
    else:
        return False
                  
def G_confirmar_posicion_final(fila_final,columna_final,lista_tablero):
    if lista_tablero[fila_final][columna_final] == "N":
        return True
    else:
        return False

def C_confirmar_fila_final(columna_final,fila_final,lista_tablero):
    if C_confirmar_columna_final(fila_final,columna_final,lista_tablero):
        return True
    else:
        return False

                     
def C_confirmar_columna_final(fila_final,columna_final,lista_tablero):
    if C_confirmar_posicion_final(fila_final,columna_final,lista_tablero):
        return True
    else:
        return False
            
def C_confirmar_posicion_final(fila_final,columna_final,lista_tablero):
    if lista_tablero[fila_final][columna_final] == "N":
        return True
    else:
        return False

########## -----> CONFIRMAR FINAL-FINAL <-------- ##########

def G_confirmar_final(columna_inicial,fila_inicial,fila_final,columna_final,lista_tablero):
    if not G_confirmar_fila_final(columna_final,fila_final,lista_tablero):
        return False
    if G_confirmar_fila_final(columna_final,fila_final,lista_tablero):
        fila_inicial = (1/2)*fila_inicial
        fila_final = (1/2)*fila_final
        columna_inicial = (1/2)*columna_inicial
        columna_final = (1/2)*columna_final
        if (fila_inicial + columna_inicial)%2 ==0:
            fila_inicial = (2)*fila_inicial
            fila_final = (2)*fila_final
            columna_inicial = (2)*columna_inicial
            columna_final = (2)*columna_final
            if (abs(fila_inicial - fila_final) <= 2) and (abs(columna_inicial -columna_final) <= 2):
                return True
            else:
                return False
        if (fila_inicial + columna_inicial)%2 ==1:
            fila_inicial = (2)*fila_inicial
            fila_final = (2)*fila_final
            columna_inicial = (2)*columna_inicial
            columna_final = (2)*columna_final
            if (abs(fila_inicial - fila_final) ==2) and (columna_inicial == columna_final):
                return True
            if (abs(columna_inicial - columna_final)==2) and (fila_inicial == fila_final):
                return True
            else:
                return False
                          
                
juego = True                
while juego:             
    print("¡Bienvenido al juego del coyote y las gallinas! \nEl tablero consta de 5 filas y 5 columnas, ambas enumeradas del 0 al 4 \nPara moverte a lo largo del tablero debes ingresar tu movimiento en el formato descrito a continuacion \n\"ColumnaInicial,FilaInicial,ColumnaFinal,FilaFinal\"\nPor ejemplo >>\"0,2,0,3\"<<\nIMPORTANTE -> Al momento de guardar o abrir un archivo no debes escribir \".txt\" al final, nosotros lo haremos por ti ;)")
    partida = int(input("Quieres cargar una partida (1) o comenzar una nueva (2)?"))
    if partida ==2:
        movimientos =[]
        tupla = (nueva_partida())
        lista_tablero = generar_nuevo_tablero()
        valido = True
        while valido:
            respuesta_gallinas = jugada_gallinas(tupla[1],movimientos,mostrar_tablero(lista_tablero))
            if respuesta_gallinas == "guardar":
                print("El juego ha sido guardado!")
                guardar(tupla[1], tupla[0],archivo_movimientos(movimientos),archivo_tablero(lista_tablero))
                valido = False
                break
            if respuesta_gallinas == "salir":
                print("El juego termino!")
                valido = False
                break 
            coyote_atrapado = revisar_coyote(lista_tablero)
            if coyote_atrapado:
                print("Las gallinas han atrapado al coyote! El juego ha terminado, gracias por jugar!")
                valido = False
            if not coyote_atrapado:
                respuesta_coyote = jugada_coyote(tupla[0],movimientos,mostrar_tablero(lista_tablero))
                if respuesta_coyote == "guardar":
                    print("El juego ha sido guardado!")
                    guardar(tupla[1], tupla[0],archivo_movimientos(movimientos),archivo_tablero(lista_tablero))
                    valido = False
                    break
                if respuesta_coyote == "salir":
                    print("El juego termino!")
                    valido = False
                    break
                gallinas = revisar_gallinas(lista_tablero)
                if gallinas<= 10:
                    print("Oh no! El Coyote se ha comido a 2 o mas gallinas :(, el juego ha terminado, gracias por jugar!")
                    valido =False
                    break
    
        otra_partida = input("Desean jugar otra vez? (Si/No)\n>")
        if (otra_partida == "No") or (otra_partida == "no"):
            juego = False
            print("Gracias por jugar!")        
        elif (otra_partida == "Si") or (otra_partida == "si"):
            pass
    if partida == 1:
        movimientos = []
        #####
        archivo_por_abrir = input("Que archivo deseas abrir?\n>")
        saved_file = open(archivo_por_abrir+'.txt')
        lines = saved_file.readline()
        print(lines.rstrip())
        i = 0
        for line in saved_file:
            movimientos += [line[0:9]]
            if movimientos[int(i)][0] == "G":
                jugada_final = movimientos[int(i)][2:9]
                jugada_gallinas_cargar(movimientos,mostrar_tablero(lista_tablero),jugada_final)
            if movimientos[int(i)][0] == "C":
                jugada_final = movimientos[int(i)][2:9]
                jugada_coyote_cargar(movimientos,mostrar_tablero(lista_tablero),jugada_final)
            i+=1
            print(line.rstrip())
        saved_file.close()
        #########
        valido = True
        while valido:
            tupla = (nueva_partida())
            respuesta_gallinas = jugada_gallinas(tupla[1],movimientos,mostrar_tablero(lista_tablero))
            if respuesta_gallinas == "guardar":
                print("El juego ha sido guardado!")
                guardar(tupla[1], tupla[0],archivo_movimientos(movimientos),archivo_tablero(lista_tablero))
                valido = False
                break
            if respuesta_gallinas == "salir":
                print("El juego termino!")
                valido = False
                break 
            coyote_atrapado = revisar_coyote(lista_tablero)
            if coyote_atrapado:
                print("Las gallinas han atrapado al coyote! El juego ha terminado, gracias por jugar!")
                valido = False
            if not coyote_atrapado:
                respuesta_coyote = jugada_coyote(tupla[0],movimientos,mostrar_tablero(lista_tablero))
                if respuesta_coyote == "guardar":
                    print("El juego ha sido guardado!")
                    guardar(tupla[1], tupla[0],archivo_movimientos(movimientos),archivo_tablero(lista_tablero))
                    valido = False
                    break
                if respuesta_coyote == "salir":
                    print("El juego termino!")
                    valido = False
                    break
                gallinas = revisar_gallinas(lista_tablero)
                if gallinas<= 10:
                    print("Oh no! El Coyote se ha comido a 2 o mas gallinas :(, el juego ha terminado, gracias por jugar!")
                    valido =False
                    break
    
        otra_partida = input("Desean jugar otra vez? (Si/No)\n>")
        if (otra_partida == "No") or (otra_partida == "no"):
            juego = False
            print("Gracias por jugar!")        
        elif (otra_partida == "Si") or (otra_partida == "si"):
            pass
    



# 

# In[1]:





# In[ ]:




