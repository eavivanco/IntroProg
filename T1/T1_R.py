
# coding: utf-8

# In[2]:


from Tarea_1 import *

root = tk.Tk()
root.geometry('{}x{}'.format("550", "650"))
app = Application(master=root)

app.mostrar_dinero(1,"Esperando apuestas!")
app.mostrar_dinero(2,"Esperando apuestas!")
app.mostrar_mensaje("Bienvenidos jugadores!")


###  arreglar el nuevo monto inicial y la nueva apuesta

def terminar_juego():
    if (monto_total1 == 0):
        juego_terminado = str(input("El jugador 1 se ha quedado sin fondos! El ganador es el jugador 2! Pulsa \"enter\" para terminar"))
        if (juego_terminado == ""):      
            return app.cerrar_ventana()
        else:
            return app.cerrar_ventana()
    if (monto_total2 == 0):
        juego_terminado = str(input("El jugador 2 se ha quedado sin fondos! El ganador es el jugador 1! Pulsa \"enter\" para terminar"))
        if (juego_terminado == ''):
            return app.cerrar_ventana()
        else:
            return app.cerrar_ventana()

def nueva_apuesta(monto_total1, monto_total2):#monto inicial
    global bet  
    if (monto_total1 == 0):
        juego_terminado = str(input("El jugador 1 se ha quedado sin fondos! El ganador es el jugador 2! Pulsa \"enter\" para terminar"))
        if (juego_terminado == ""):      
            return app.cerrar_ventana()
        else:
            return app.cerrar_ventana()
    if (monto_total2 == 0):
        juego_terminado = str(input("El jugador 2 se ha quedado sin fondos! El ganador es el jugador 1! Pulsa \"enter\" para terminar"))
        if (juego_terminado == ''):
            return app.cerrar_ventana()
        else:
            return app.cerrar_ventana()
    else:    
        app.mostrar_dinero(1,monto_total1)
        app.mostrar_dinero(2,monto_total2)    
        bet = (int(input("Su apuesta será de:")))
        while ((monto_total1 < bet) or (monto_total2 < bet)):     
            app.mostrar_mensaje("Saldo insuficiente!")        
            bet = (int(input("Debes apostar lo mismo o menos que tu monto actual!")))          
        app.mostrar_mensaje("Vamos a jugar!")    
        app.poner_apuesta(bet)
        app.mostrar_dinero(1,monto_total1 - bet)
        app.mostrar_dinero(2,monto_total2 - bet)

    return bet
    

def nuevo_carton():         # funcion nuevo carton
    p=1
    while p <= 2:
        j=0   
        while j ==0:
            b0=random.randint(1,20)
            b1=random.randint(1,20)
            b2=random.randint(1,20)
            b3=random.randint(1,20)
            b4=random.randint(1,20)
            while ((b0 == b1) or (b0 == b2) or (b0==b3) or(b0== b4) or (b1==b2) or(b1 ==b3) or (b1==b4) or (b2==b3) or (b2==b4) or (b3 ==b4)):
                b0=random.randint(1,20)
                b1=random.randint(1,20)
                b2=random.randint(1,20)
                b3=random.randint(1,20)
                b4=random.randint(1,20)
            if not ((b0 == b1) or (b0 == b2) or (b0==b3) or(b0== b4) or (b1==b2) or(b1 ==b3) or (b1==b4) or (b2==b3) or (b2==b4) or (b3 ==b4)):
                app.colocar_numero(0,j,b0,p)
                app.colocar_numero(1,j,b1,p)
                app.colocar_numero(2,j,b2,p)
                app.colocar_numero(3,j,b3,p)
                app.colocar_numero(4,j,b4,p)
                    
                j +=1      
        while j == 1:
            i0=random.randint(21,40)
            i1=random.randint(21,40)
            i2=random.randint(21,40)
            i3=random.randint(21,40)
            i4=random.randint(21,40)      
            while ((i0 == i1) or (i0 == i2) or (i0==i3) or(i0== i4) or (i1==i2) or(i1 ==i3) or (i1==i4) or (i2==i3) or (i2==i4) or (i3 ==i4)):
                i0=random.randint(21,40)
                i1=random.randint(21,40)
                i2=random.randint(21,40)
                i3=random.randint(21,40)
                i4=random.randint(21,40)
            if not ((i0 == i1) or (i0 == i2) or (i0==i3) or(i0== i4) or (i1==i2) or(i1 ==i3) or (i1==i4) or (i2==i3) or (i2==i4) or (i3 ==i4)):
                app.colocar_numero(0,j,i0,p)
                app.colocar_numero(1,j,i1,p)
                app.colocar_numero(2,j,i2,p)
                app.colocar_numero(3,j,i3,p)
                app.colocar_numero(4,j,i4,p)
                    
                j +=1
                           
        while j ==2:    
            n0=random.randint(41,60) 
            n1=random.randint(41,60)
            n2=random.randint(41,60)
            n3=random.randint(41,60)
            n4=random.randint(41,60)           
            while ((n0 == n1) or (n0 == n2) or (n0==n3) or(n0== n4) or (n1==n2) or(n1 ==n3) or (n1==n4) or (n2==n3) or (n2==n4) or (n3 ==n4)):
                n0=random.randint(41,60)
                n1=random.randint(41,60)
                n2=random.randint(41,60)
                n3=random.randint(41,60)
                n4=random.randint(41,60)
            if not ((n0 == n1) or (n0 == n2) or (n0==n3) or(n0== n4) or (n1==n2) or(n1 ==n3) or (n1==n4) or (n2==n3) or (n2==n4) or (n3 ==n4)):
                app.colocar_numero(0,j,n0,p)
                app.colocar_numero(1,j,n1,p)
                app.colocar_numero(2,j,n2,p)
                app.colocar_numero(3,j,n3,p)
                app.colocar_numero(4,j,n4,p)
                  
                j +=1
        while j ==3:
            g0=random.randint(61,80)
            g1=random.randint(61,80)
            g2=random.randint(61,80)
            g3=random.randint(61,80)
            g4=random.randint(61,80)
               
            while ((g0 == g1) or (g0 == g2) or (g0==g3) or(g0== g4) or (g1==g2) or(g1 ==g3) or (g1==g4) or (g2==g3) or (g2==g4) or (g3 ==g4)):
                g0=random.randint(61,80)
                g1=random.randint(61,80)
                g2=random.randint(61,80)
                g3=random.randint(61,80)
                g4=random.randint(61,80)
            if not ((g0 == g1) or (g0 == g2) or (g0==g3) or(g0== g4) or (g1==g2) or(g1 ==g3) or (g1==g4) or (g2==g3) or (g2==g4) or (g3 ==g4)):
                app.colocar_numero(0,j,g0,p)
                app.colocar_numero(1,j,g1,p)
                app.colocar_numero(2,j,g2,p)
                app.colocar_numero(3,j,g3,p)
                app.colocar_numero(4,j,g4,p)
                   
                j +=1
        while j ==4:
            o0=random.randint(81,100)
            o1=random.randint(81,100)
            o2=random.randint(81,100)
            o3=random.randint(81,100)
            o4=random.randint(81,100)
               
            while ((o0 == o1) or (o0 == o2) or (o0==o3) or(o0== o4) or (o1==o2) or(o1 ==o3) or (o1==o4) or (o2==o3) or (o2==o4) or (o3 ==o4)):
                o0=random.randint(81,100)
                o1=random.randint(81,100)
                o2=random.randint(81,100)
                o3=random.randint(81,100)
                o4=random.randint(81,100)
            if not ((o0 == o1) or (o0 == o2) or (o0==o3) or(o0== o4) or (o1==o2) or(o1 ==o3) or (o1==o4) or (o2==o3) or (o2==o4) or (o3 ==o4)):
                app.colocar_numero(0,j,o0,p)
                app.colocar_numero(1,j,o1,p)
                app.colocar_numero(2,j,o2,p)
                app.colocar_numero(3,j,o3,p)
                app.colocar_numero(4,j,o4,p)
                 
                j +=1
        p +=1

def reiniciar_carton():#funcion reiniciar carton

    app.marcar_numero(0,0,False,1)
    app.marcar_numero(0,4,False,1)        
    app.marcar_numero(1,1,False,1)        
    app.marcar_numero(1,3,False,1)        
    app.marcar_numero(2,2,False,1)        
    app.marcar_numero(3,2,False,1)
    app.marcar_numero(4,2,False,1)
    app.marcar_numero(3,3,False,1)
    app.marcar_numero(4,4,False,1)
    app.marcar_numero(0,1,False,1)
    app.marcar_numero(0,2,False,1)
    app.marcar_numero(0,3,False,1)
    app.marcar_numero(1,0,False,1)
    app.marcar_numero(1,2,False,1)
    app.marcar_numero(1,4,False,1)
    app.marcar_numero(2,0,False,1)
    app.marcar_numero(2,1,False,1)
    app.marcar_numero(2,3,False,1)
    app.marcar_numero(2,4,False,1)
    app.marcar_numero(3,0,False,1)
    app.marcar_numero(3,1,False,1)
    app.marcar_numero(3,4,False,1)
    app.marcar_numero(4,0,False,1)
    app.marcar_numero(4,1,False,1)
    app.marcar_numero(4,3,False,1)
    
    app.marcar_numero(0,0,False,2)
    app.marcar_numero(0,4,False,2)
    app.marcar_numero(1,1,False,2)
    app.marcar_numero(1,3,False,2)
    app.marcar_numero(2,2,False,2)
    app.marcar_numero(3,2,False,2)
    app.marcar_numero(4,2,False,2)
    app.marcar_numero(3,3,False,2)
    app.marcar_numero(4,4,False,2)
    app.marcar_numero(0,1,False,2)
    app.marcar_numero(0,2,False,2)
    app.marcar_numero(0,3,False,2)
    app.marcar_numero(1,0,False,2)
    app.marcar_numero(1,2,False,2)
    app.marcar_numero(1,4,False,2)
    app.marcar_numero(2,0,False,2)
    app.marcar_numero(2,1,False,2)
    app.marcar_numero(2,3,False,2)
    app.marcar_numero(2,4,False,2)
    app.marcar_numero(3,0,False,2)
    app.marcar_numero(3,1,False,2)
    app.marcar_numero(3,4,False,2)
    app.marcar_numero(4,0,False,2)
    app.marcar_numero(4,1,False,2)
    app.marcar_numero(4,3,False,2) 
    
    
monto_inicial = int(input("Bienvendios! Con cuanto dinero desean participar?"))   

app.mostrar_dinero(1,monto_inicial)
app.mostrar_dinero(2,monto_inicial)

monto_total1 = monto_inicial         ########## primer turno
monto_total2 = monto_inicial
nuevo_carton()
nueva_apuesta(monto_total1, monto_total2)

def turno():
    monto_total1 = int(app.preguntar_monto(1))         ########## primer turno
    monto_total2 = int(app.preguntar_monto(2))
       
    number01 = app.obtener_numero(0,0,1)
    number02 = app.obtener_numero(0,1,1)
    number03 = app.obtener_numero(0,2,1)
    number04 = app.obtener_numero(0,3,1)
    number05 = app.obtener_numero(0,4,1)
    number06 = app.obtener_numero(1,0,1)
    number07 = app.obtener_numero(1,1,1)
    number08 = app.obtener_numero(1,2,1)
    number09 = app.obtener_numero(1,3,1)
    number10 = app.obtener_numero(1,4,1)
    number11 = app.obtener_numero(2,0,1)
    number12 = app.obtener_numero(2,1,1)
    number13 = app.obtener_numero(2,2,1)
    number14 = app.obtener_numero(2,3,1)
    number15 = app.obtener_numero(2,4,1)
    number16 = app.obtener_numero(3,0,1)
    number17 = app.obtener_numero(3,1,1)
    number18 = app.obtener_numero(3,2,1)
    number19 = app.obtener_numero(3,3,1)
    number20 = app.obtener_numero(3,4,1)
    number21 = app.obtener_numero(4,0,1)
    number22 = app.obtener_numero(4,1,1)
    number23 = app.obtener_numero(4,2,1)
    number24 = app.obtener_numero(4,3,1)
    number25 = app.obtener_numero(4,4,1)
    number26 = app.obtener_numero(0,0,2)
    number27 = app.obtener_numero(0,1,2)
    number28 = app.obtener_numero(0,2,2)
    number29 = app.obtener_numero(0,3,2)
    number30 = app.obtener_numero(0,4,2)
    number31 = app.obtener_numero(1,0,2)
    number32 = app.obtener_numero(1,1,2)
    number33 = app.obtener_numero(1,2,2)
    number34 = app.obtener_numero(1,3,2)
    number35 = app.obtener_numero(1,4,2)
    number36 = app.obtener_numero(2,0,2)
    number37 = app.obtener_numero(2,1,2)
    number38 = app.obtener_numero(2,2,2)
    number39 = app.obtener_numero(2,3,2)
    number40 = app.obtener_numero(2,4,2)
    number41 = app.obtener_numero(3,0,2)
    number42 = app.obtener_numero(3,1,2)
    number43 = app.obtener_numero(3,2,2)
    number44 = app.obtener_numero(3,3,2)
    number45 = app.obtener_numero(3,4,2)
    number46 = app.obtener_numero(4,0,2)
    number47 = app.obtener_numero(4,1,2)
    number48 = app.obtener_numero(4,2,2)
    number49 = app.obtener_numero(4,3,2)
    number50 = app.obtener_numero(4,4,2)
    
    otro_numero = False
    while otro_numero == False:
        fila = random.randint(0,4)
        columna = random.randint(0,4)
        jugador = random.randint(1,2)
        number = app.obtener_numero(fila,columna,jugador)
        unico = app.agregar(number)
        if unico == True:
            if number == number01:
                app.marcar_numero(0,0,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number02:
                app.marcar_numero(0,1,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number03:
                app.marcar_numero(0,2,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number04:
                app.marcar_numero(0,3,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number05:
                app.marcar_numero(0,4,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number06:
                app.marcar_numero(1,0,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number07:
                app.marcar_numero(1,1,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number08:
                app.marcar_numero(1,2,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number09:
                app.marcar_numero(1,3,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number10:
                app.marcar_numero(1,4,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number11:
                app.marcar_numero(2,0,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number12:
                app.marcar_numero(2,1,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number13:
                app.marcar_numero(2,2,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number14:
                app.marcar_numero(2,3,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number15:
                app.marcar_numero(2,4,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number16:
                app.marcar_numero(3,0,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number17:
                app.marcar_numero(3,1,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number18:
                app.marcar_numero(3,2,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number19:
                app.marcar_numero(3,3,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number20:
                app.marcar_numero(3,4,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number21:
                app.marcar_numero(4,0,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number22:
                app.marcar_numero(4,1,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number23:
                app.marcar_numero(4,2,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number24:
                app.marcar_numero(4,3,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number25:
                app.marcar_numero(4,4,True,1)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number26:
                app.marcar_numero(0,0,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number27:
                app.marcar_numero(0,1,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number28:
                app.marcar_numero(0,2,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number29:
                app.marcar_numero(0,3,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number30:
                app.marcar_numero(0,4,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number31:
                app.marcar_numero(1,0,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number32:
                app.marcar_numero(1,1,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number33:
                app.marcar_numero(1,2,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number34:
                app.marcar_numero(1,3,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number35:
                app.marcar_numero(1,4,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number36:
                app.marcar_numero(2,0,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number37:
                app.marcar_numero(2,1,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number38:
                app.marcar_numero(2,2,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number39:
                app.marcar_numero(2,3,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number40:
                app.marcar_numero(2,4,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number41:
                app.marcar_numero(3,0,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number42:
                app.marcar_numero(3,1,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number43:
                app.marcar_numero(3,2,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number44:
                app.marcar_numero(3,3,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number45:
                app.marcar_numero(3,4,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number46:
                app.marcar_numero(4,0,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number47:
                app.marcar_numero(4,1,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number48:
                app.marcar_numero(4,2,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number49:
                app.marcar_numero(4,3,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True
            if number == number50:
                app.marcar_numero(4,4,True,2)
                app.mostrar_mensaje(number)
                otro_numero = True 
        else:
            otro_numero = False
    yc1= app.esta_marcado(0,0,1)
    y2= app.esta_marcado(0,4,1)        
    yc3= app.esta_marcado(1,1,1)        
    y4= app.esta_marcado(1,3,1)        
    yc5= app.esta_marcado(2,2,1)        
    y6= app.esta_marcado(3,2,1)
    y7= app.esta_marcado(4,2,1)
    c8= app.esta_marcado(3,3,1)
    c9= app.esta_marcado(4,4,1)
    cc110= app.esta_marcado(0,1,1)
    cc111= app.esta_marcado(0,2,1)
    cc112= app.esta_marcado(0,3,1)
    cc113= app.esta_marcado(1,0,1)
    cc114= app.esta_marcado(1,2,1)
    cc115= app.esta_marcado(1,4,1)
    cc116= app.esta_marcado(2,0,1)
    cc117= app.esta_marcado(2,1,1)
    cc118= app.esta_marcado(2,3,1)
    cc119= app.esta_marcado(2,4,1)
    cc120= app.esta_marcado(3,0,1)
    cc121= app.esta_marcado(3,1,1)
    cc122= app.esta_marcado(3,4,1)
    cc123= app.esta_marcado(4,0,1)
    cc124= app.esta_marcado(4,1,1)
    cc125= app.esta_marcado(4,3,1)
    
    yc21=app.esta_marcado(0,0,2)
    y22=app.esta_marcado(0,4,2)
    yc23=app.esta_marcado(1,1,2)
    y24=app.esta_marcado(1,3,2)
    yc25=app.esta_marcado(2,2,2)
    y26=app.esta_marcado(3,2,2)
    y27=app.esta_marcado(4,2,2)
    c28= app.esta_marcado(3,3,2)
    c29= app.esta_marcado(4,4,2)
    cc210= app.esta_marcado(0,1,2)
    cc211= app.esta_marcado(0,2,2)
    cc212= app.esta_marcado(0,3,2)
    cc213= app.esta_marcado(1,0,2)
    cc214= app.esta_marcado(1,2,2)
    cc215= app.esta_marcado(1,4,2)
    cc216= app.esta_marcado(2,0,2)
    cc217= app.esta_marcado(2,1,2)
    cc218= app.esta_marcado(2,3,2)
    cc219= app.esta_marcado(2,4,2)
    cc220= app.esta_marcado(3,0,2)
    cc221= app.esta_marcado(3,1,2)
    cc222= app.esta_marcado(3,4,2)
    cc223= app.esta_marcado(4,0,2)
    cc224= app.esta_marcado(4,1,2)
    cc225= app.esta_marcado(4,3,2)
    
    if(yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1 carton completo  
        if (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225): #si 2 carton completo
            app.mostrar_mensaje("Empate!")
            app.mostrar_dinero(1, monto_total1) 
            app.mostrar_dinero(2, monto_total2) 
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Empate!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1,monto_total2)
                app.mostrar_ventana(True)
                reiniciar_carton()
                nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
        if not (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225):# si 2 no carton completo
            app.mostrar_mensaje("Gana jugador 1 con carton completo!")
            app.mostrar_dinero(1, monto_total1)           
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Gana jugador 1 con carton completo!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1 + 2*bet ,monto_total2)
                if((monto_total1 != 0) and (monto_total2 != 0)):
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
            
    elif(yc1 and y2 and yc3 and y4 and yc5 and y6 and y7): #si 1 y
        if(yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1 carton completo  
            if (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225):
                app.mostrar_mensaje("Empate!")
                app.mostrar_dinero(1, monto_total1) 
                app.mostrar_dinero(2, monto_total2) 
                app.reiniciar_contador()
                app.mostrar_ventana(False)
                otra_partida = str(input("Empate!, desean jugar otra vez? "))
                while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                    otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                if ((otra_partida == "si") or (otra_partida == "Si")):
                    nueva_apuesta(monto_total1,monto_total2)
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton() 
                elif((otra_partida == "no") or (otra_partida == "No")):
                    app.cerrar_ventana()
            if not (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225):
                app.mostrar_mensaje("Gana jugador 1 con carton completo!")
                app.mostrar_dinero(1, monto_total1)            
                app.reiniciar_contador()
                app.mostrar_ventana(False)
                otra_partida = str(input("Gana jugador 1 con carton completo!, desean jugar otra vez? "))
                while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                    otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                if ((otra_partida == "si") or (otra_partida == "Si")):
                    nueva_apuesta(monto_total1 + 2*bet  ,monto_total2)
                    if((monto_total1 != 0) and (monto_total2 != 0)):
                        app.mostrar_ventana(True)
                        reiniciar_carton()
                        nuevo_carton()
                elif((otra_partida == "no") or (otra_partida == "No")):
                    app.cerrar_ventana()
        if not (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27): #si 2 no y   
            app.mostrar_mensaje("Gana jugador 1 con la \"Y\"!")
            app.mostrar_dinero(1, monto_total1)            
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Gana jugador 1 con la \"Y\"!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1 + 2*bet, monto_total2 )
                if((monto_total1 != 0) and (monto_total2 != 0)):
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
    
    elif (yc1 and yc3 and yc5 and c8 and c9): # si 1 cruzado
        if (yc21 and yc23 and yc25 and c28 and c29): #si tambien 2 cruzado
            if(yc1 and y2 and yc3 and y4 and yc5 and y6 and y7): #si 1 y
                if(yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1 carton completo  
                    if (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225):
                        app.mostrar_mensaje("Empate!")
                        app.mostrar_dinero(1, monto_total1) 
                        app.mostrar_dinero(2, monto_total2) 
                        app.reiniciar_contador()
                        app.mostrar_ventana(False)
                        otra_partida = str(input("Empate!, desean jugar otra vez? "))
                        while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                            otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                        if ((otra_partida == "si") or (otra_partida == "Si")):
                            nueva_apuesta(monto_total1, monto_total2)
                            app.mostrar_ventana(True)
                            reiniciar_carton()
                            nuevo_carton()
                        elif((otra_partida == "no") or (otra_partida == "No")):
                            app.cerrar_ventana()
                    if not (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225):
                        app.mostrar_mensaje("Gana jugador 1 con carton completo!")
                        app.mostrar_dinero(1, monto_total1)            
                        app.reiniciar_contador()
                        app.mostrar_ventana(False)
                        otra_partida = str(input("Gana jugador 1 con carton completo!, desean jugar otra vez? "))
                        while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                            otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                        if ((otra_partida == "si") or (otra_partida == "Si")):
                            nueva_apuesta(monto_total1 + 2*bet ,monto_total2)
                            if((monto_total1 != 0) and (monto_total2 != 0)):
                                app.mostrar_ventana(True)
                                reiniciar_carton()
                                nuevo_carton()
                        elif((otra_partida == "no") or (otra_partida == "No")):
                            app.cerrar_ventana()
                if not (yc21 and y22 and yc23 and y24 and yc25 and y26 and y27): #si 2 no y
                    app.mostrar_mensaje("Gana jugador 1 con la \"Y\"!")
                    app.mostrar_dinero(1, monto_total1)         
                    app.reiniciar_contador()
                    app.mostrar_ventana(False)
                    otra_partida = str(input("Gana jugador 1 con la \"Y\"!, desean jugar otra vez? "))
                    while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                        otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                    if ((otra_partida == "si") or (otra_partida == "Si")):
                        nueva_apuesta(monto_total1 + 2*bet , monto_total2 )
                        if((monto_total1 != 0) and (monto_total2 != 0)):
                            app.mostrar_ventana(True)
                            reiniciar_carton()
                            nuevo_carton()
                    elif((otra_partida == "no") or (otra_partida == "No")):
                        app.cerrar_ventana()
        if not(yc21 and yc23 and yc25 and c28 and c29): # si 2 no cruzado
            app.mostrar_mensaje("Gana jugador 1 con la diagonal!")
            app.mostrar_dinero(1, monto_total1)        
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Gana jugador 1 con la diagonal!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1 + 2*bet ,monto_total2 )
                if((monto_total1 != 0) and (monto_total2 != 0)):
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
            
            
    elif(yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225): # si 2 carton completo 
        if (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1  carton completo
            app.mostrar_mensaje("Empate!")
            app.mostrar_dinero(1, monto_total1)
            app.mostrar_dinero(2, monto_total2) 
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Empate!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1,monto_total2)
                app.mostrar_ventana(True)
                reiniciar_carton()
                nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
        if not (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1 no carton completo
            app.mostrar_mensaje("Gana jugador 2 con carton completo!")
            app.mostrar_dinero(2, monto_total2)           
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Gana jugador 2 con carton completo!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1, monto_total2 + 2*bet)
                if((monto_total1 != 0) and (monto_total2 != 0)):
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
      
    elif(yc21 and y22 and yc23 and y24 and yc25 and y26 and y27): #si 2 y
        if(yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225): # si 2 carton completo 
            if (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1  carton completo
                app.mostrar_mensaje("Empate!")
                app.mostrar_dinero(1, monto_total1)
                app.mostrar_dinero(2, monto_total2) 
                app.reiniciar_contador()
                app.mostrar_ventana(False)
                otra_partida = str(input("Empate!, desean jugar otra vez? "))
                while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                    otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                if ((otra_partida == "si") or (otra_partida == "Si")):
                    nueva_apuesta(monto_total1 ,monto_total2)
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton()
                elif((otra_partida == "no") or (otra_partida == "No")):
                    app.cerrar_ventana()
            if not (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1 no carton completo
                app.mostrar_mensaje("Gana jugador 2 con carton completo!")
                app.mostrar_dinero(2, monto_total2)         
                app.reiniciar_contador()
                app.mostrar_ventana(False)
                otra_partida = str(input("Gana jugador 2 con carton completo!, desean jugar otra vez? "))
                while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                    otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                if ((otra_partida == "si") or (otra_partida == "Si")):
                    nueva_apuesta(monto_total1,monto_total2 + 2*bet )
                    if((monto_total1 != 0) and (monto_total2 != 0)):
                        app.mostrar_ventana(True)
                        reiniciar_carton()
                        nuevo_carton()
                elif((otra_partida == "no") or (otra_partida == "No")):
                    app.cerrar_ventana()
        if not (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7): #si 1 no y
            app.mostrar_mensaje("Gana jugador 2 con la \"Y\"!")
            app.mostrar_dinero(2, monto_total2)          
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Gana jugador 2 con la \"Y\"!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1 ,monto_total2 + 2*bet)
                if((monto_total1 != 0) and (monto_total2 != 0)):
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
                       
    elif (yc21 and yc23 and yc25 and c28 and c29): # si 2 cruzado
        if (yc1 and yc3 and yc5 and c8 and c9): #si tambien 1 cruzado
            if(yc21 and y22 and yc23 and y24 and yc25 and y26 and y27): #si 2 y
                if(yc21 and y22 and yc23 and y24 and yc25 and y26 and y27 and c28 and c29 and cc210 and cc211 and cc212 and cc213 and cc214 and cc215 and cc216 and cc217 and cc218 and cc219 and cc220 and cc221 and cc222 and cc223 and cc224 and cc225): # si 2 carton completo 
                    if (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1  carton completo
                        app.mostrar_mensaje("Empate!")
                        app.mostrar_dinero(1, monto_total1)
                        app.mostrar_dinero(2, monto_total2) 
                        app.reiniciar_contador()
                        app.mostrar_ventana(False)
                        otra_partida = str(input("Empate!, desean jugar otra vez? "))
                        while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                            otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                        if ((otra_partida == "si") or (otra_partida == "Si")):
                            nueva_apuesta(monto_total1,monto_total2)
                            app.mostrar_ventana(True)
                            reiniciar_carton()
                            nuevo_carton()
                        elif((otra_partida == "no") or (otra_partida == "No")):
                            app.cerrar_ventana()
                    if not (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7 and c8 and c9 and cc110 and cc111 and cc112 and cc113 and cc114 and cc115 and cc116 and cc117 and cc118 and cc119 and cc120 and cc121 and cc122 and cc123 and cc124 and cc125): # si 1 no carton completo
                        app.mostrar_mensaje("Gana jugador 2 con carton completo!")
                        app.mostrar_dinero(2, monto_total2)         
                        app.reiniciar_contador()
                        app.mostrar_ventana(False)
                        otra_partida = str(input("Gana jugador 2 con carton completo!, desean jugar otra vez? "))
                        while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                            otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                        if ((otra_partida == "si") or (otra_partida == "Si")):
                            nueva_apuesta(monto_total1, monto_total2 + 2*bet)
                            if((monto_total1 != 0) and (monto_total2 != 0)):
                                app.mostrar_ventana(True)
                                reiniciar_carton()
                                nuevo_carton()
                        elif((otra_partida == "no") or (otra_partida == "No")):
                            app.cerrar_ventana()
                if not (yc1 and y2 and yc3 and y4 and yc5 and y6 and y7): #si 1 no y
                    app.mostrar_mensaje("Gana jugador 2 con la \"Y\"!")
                    app.mostrar_dinero(2, monto_total2)            
                    app.reiniciar_contador() 
                    app.mostrar_ventana(False)
                    otra_partida = str(input("Gana jugador 2 con la \"Y\"!, desean jugar otra vez? "))
                    while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                        otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
                    if ((otra_partida == "si") or (otra_partida == "Si")):
                        nueva_apuesta(monto_total1,monto_total2 + 2*bet)
                        if((monto_total1 != 0) and (monto_total2 != 0)):
                            app.mostrar_ventana(True)
                            reiniciar_carton()
                            nuevo_carton()
                    elif((otra_partida == "no") or (otra_partida == "No")):
                        app.cerrar_ventana()
        if not(yc1 and yc3 and yc5 and c8 and c9): # si 1 no cruzado
            app.mostrar_mensaje("Gana jugador 2 con la diagonal!")
            app.mostrar_dinero(2, monto_total2)          
            app.reiniciar_contador()
            app.mostrar_ventana(False)
            otra_partida = str(input("Gana jugador 2 con la diagonal!, desean jugar otra vez? "))
            while not((otra_partida == "si") or (otra_partida == "Si") or (otra_partida == "no") or (otra_partida == "No")):
                otra_partida = str(input("Debes responder \"si\" o \"no\"!"))
            if ((otra_partida == "si") or (otra_partida == "Si")):
                nueva_apuesta(monto_total1,monto_total2 + 2*bet)
                if((monto_total1 != 0) and (monto_total2 != 0)):
                    app.mostrar_ventana(True)
                    reiniciar_carton()
                    nuevo_carton()
            elif((otra_partida == "no") or (otra_partida == "No")):
                app.cerrar_ventana()
            
            
    
        
    
            
    
    
    
    

        
    
    
    
 

# Aqui empieza su programa


# ESTO NO SE TOCA
app.button.config(command=turno)
app.mainloop()


# 

# In[ ]:




