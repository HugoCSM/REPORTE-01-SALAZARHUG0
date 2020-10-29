from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products

#Administradores que solo pueden acceder a lifestore
Administradores =[["Hugo", "1"], ["Javier", "tienda123"]]

#Ingresa datos 
usr_name = input ("Ingresa tu nombre de usuario: ")
usr_password =  input ("Ingresa tu contraseña: ")

Acceso= 0
M_ventas = []
#Validiación de datos para dar acceso
for usuario in Administradores:
  if usuario[0] == usr_name and usuario [1]== usr_password:
    Acceso=1
#Si eres administrador, tienes acceso al menú Lifestore
if Acceso ==1:
  print("***Bienvenido "+usr_name+" a lifestore***")
  print("Elige una opción")
  print("1.- Categorías con menores ventas y categorías con menores búsquedas. \n2.- Categorías con mayores ventas y categorías con mayores búsquedas. \n3.- 50 productos con mayores ventas y los 100 productos con mayor búsquedas. \n4.- Por categoria,los productos con menores ventas y busquedas \n5.- Productos con mejores y peores reseñas. \n6.-Total de ingresos y ventas promedio mensuales,total anual y meses con mas ventas en el año")
  opcion=int(input("Opción seleccionada -> "))#Muestra que opción se seleccionó
  #Comienza la opción 1
  if opcion==1:
    contador=0
    Lista_menores_ventas= []
    #Se recorren listas
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]== venta[1]:
          contador +=1
      #Se agregan los resultados a Lista_menores_ventas
      Lista_menores_ventas.append([producto[3],contador])
      contador=0
    #Se ordenan los datos de menor a mayor
    Lista_ordenada=[]
    while Lista_menores_ventas:
      menor=Lista_menores_ventas[0][1]
      lista_actual=Lista_menores_ventas[0]
      for producto in Lista_menores_ventas:
        if producto[1]< menor:
          menor = producto[1]
          lista_actual=producto
      #Se agregan los datos ordendos
      Lista_ordenada.append(lista_actual)
      Lista_menores_ventas.remove(lista_actual)
    #Se acomodarán los datos de acuerdo a las categorías
    categorias=["memorias usb","pantallas","bocinas","audifonos"]  
    print("Las categorías con menores ventas son: ")
    for categoria in categorias:
      contador=0
      for lista in Lista_ordenada:
        if lista[0]== categoria:
          contador += lista [1]
    
      print("La categoria ",categoria, "vendió: ",contador)
    
  
    contador=0
    Lista_menores_busquedas= []
    for producto in lifestore_products:#Se recorren listas
      for busqueda in lifestore_searches:
        if producto[0]== busqueda[1]:
          contador +=1
      #Se agregan los datos a Lista_menores_busquedas
      Lista_menores_busquedas.append([producto[3],contador])
      contador=0
    #Se ordenan los datos de menor a mayor
    Lista_ordenada=[]
    while Lista_menores_busquedas:
      menor=Lista_menores_busquedas[0][1]
      lista_actual=Lista_menores_busquedas[0]
      for producto in Lista_menores_busquedas:
        if producto[1]< menor:
          menor = producto[1]
          lista_actual=producto
      #Se agregan los datos ordenados
      Lista_ordenada.append(lista_actual)
      Lista_menores_busquedas.remove(lista_actual)
     #Se acomodarán los datos de acuerdo a las categorías
    categorias=["memorias usb","pantallas","bocinas","audifonos"]  
    
    print("Las categorías con menores busquedas son: ")
    for categoria in categorias:
      contador=0
      for lista in Lista_ordenada:
        if lista[0]== categoria:
          contador += lista [1]
    
      print("La categoria ",categoria, "tuvó : ",contador," búsquedas")

  #Comienza la opción 2
  if opcion==2:
    contador=0
    Lista_mayores_ventas= [] 
    for producto in lifestore_products:#Se recorren listas
      for venta in lifestore_sales:
        if producto[0]== venta[1]:
          contador +=1
      #Se agregan los valores a Lista_mayores_ventas
      Lista_mayores_ventas.append([producto[3],contador])
      contador=0
    #Se ordenan los datos de mayor a menor
    Lista_ordenada=[]
    while Lista_mayores_ventas:
      mayor=Lista_mayores_ventas[0][1]
      lista_actual=Lista_mayores_ventas[0]
      for producto in Lista_mayores_ventas:
        if producto[1]> mayor:
          mayor = producto[1]
          lista_actual=producto
      #Se agregan los datos ordenados
      Lista_ordenada.append(lista_actual)
      Lista_mayores_ventas.remove(lista_actual)
    #Se acomodarán los datos de acuerdo a las categorías
    categorias=["procesadores","tarjetas de video","tarjetas madre","discos duros"]  
    print("Las categorías con mayores ventas son: ")
    for categoria in categorias:
      contador=0
      for lista in Lista_ordenada:
        if lista[0]== categoria:
          contador += lista [1]
    
      print("La categoria ",categoria, "vendió: ",contador)

    contador=0
    Lista_mayores_busquedas= []
    for producto in lifestore_products:
      for busqueda in lifestore_searches:
        if producto[0]== busqueda[1]:
          contador +=1

      Lista_mayores_busquedas.append([producto[3],contador])
      contador=0
    
    Lista_ordenada=[]
    while Lista_mayores_busquedas:
      mayor=Lista_mayores_busquedas[0][1]
      lista_actual=Lista_mayores_busquedas[0]
      for producto in Lista_mayores_busquedas:
        if producto[1]> mayor:
          mayor = producto[1]
          lista_actual=producto

      Lista_ordenada.append(lista_actual)
      Lista_mayores_busquedas.remove(lista_actual)
    #Se acomodarán los datos de acuerdo a las categorías
    categorias=["procesadores","tarjetas de video","tarjetas madre","discos duros"]  
    
    print("Las categorías con mayores busquedas son: ")
    for categoria in categorias:
      contador=0
      for lista in Lista_ordenada:
        if lista[0]== categoria:
          contador += lista [1]
    
      print("La categoria ",categoria, "tuvó : ",contador," búsquedas")
  #Comienza la opción 3
  if opcion==3:
    M_ventas= []
   
    print("Mes de enero: ")
    for producto in lifestore_products: #Se recorren las listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="01": #Se coloca este slicing para obtener los datos del mes de enero
          
         formato=[producto[1],venta[3]]
        #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
   
    print("Mes de febrero: ")
    for producto in lifestore_products:#Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="02": #Se coloca este slicing para obtener los datos del mes de febrero
          
         formato=[producto[1],venta[3]]
        #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de marzo: ")
    for producto in lifestore_products: #Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="03":#Se coloca este slicing para obtener los datos del mes de marzo
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)
    
    M_ventas= []
   
    print("Mes de abril: ")
    for producto in lifestore_products:#Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="04":#Se coloca este slicing para obtener los datos del mes de Abril
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de mayo: ")
    for producto in lifestore_products: #Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="05":#Se coloca este slicing para obtener los datos del mes de Mayo
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de junio: ")
    for producto in lifestore_products: #Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="06":#Se coloca este slicing para obtener los datos del mes de Junio
         
         formato=[producto[1],venta[3]]
            #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
   
    print("Mes de julio: ")
    for producto in lifestore_products:#Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="07": #Se coloca este slicing para obtener los datos del mes de Julio
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de agosto: ")
    for producto in lifestore_products: #Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="08":#Se coloca este slicing para obtener los datos del mes de Agosto
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de septiembre: ")
    for producto in lifestore_products:#Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="09":#Se coloca este slicing para obtener los datos del mes de Septiembre
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de octubre: ")
    for producto in lifestore_products:#Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="10":#Se coloca este slicing para obtener los datos del mes de Octubre
          #num_ventas +=1
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de noviembre: ")
    for producto in lifestore_products:#Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="11":#Se coloca este slicing para obtener los datos del mes de Noviembre
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    M_ventas= []
    
    print("Mes de diciembre: ")
    for producto in lifestore_products: #Se recorren listas
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="12":#Se coloca este slicing para obtener los datos del mes de Diciembre
          
         formato=[producto[1],venta[3]]
         #Se agregan los datos obtenidos a M_ventas
         M_ventas.append(formato)
    
    print(M_ventas)

    print("Los productos con mayores ventas son:")
    M_ventas=[]
    for producto in lifestore_products:#Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if venta [1]== producto [0] :
          num_ventas +=1
         
      formato = [producto[1],num_ventas]    
      
      if num_ventas >=1:#Se coloca este if para eliminar los que son 0 ventas
       M_ventas.append(formato)
       num_ventas=0
    #Se ordenan los datos de mayor a menor
    Lista_ordenada=[]
    while M_ventas:
      mayor=M_ventas[0][1]
      lista_actual=M_ventas[0]
      for producto in M_ventas:
        if producto[1]> mayor:
          mayor = producto[1]
          lista_actual=producto
      #Se agregan los datos a Lista_ordenada
      Lista_ordenada.append(lista_actual)
      M_ventas.remove(lista_actual)

    print(Lista_ordenada)

    print("Los productos mas buscados son: ")

    M_busqueda=[]
    for producto in lifestore_products:#Se recorren listas
      num_busqueda=0
      for search in lifestore_searches:
        if search [1]== producto [0] :
          num_busqueda +=1
         
      formato = [producto[1],num_busqueda]    
      
      if num_busqueda >=1:#Se coloca este if para eliminar los que son 0 busquedas
       M_busqueda.append(formato)
       num_busqueda=0
    
    Lista_ordenada=[] #Se ordenan los datos de mayor a menor
    while M_busqueda:
      mayor=M_busqueda[0][1]
      lista_actual=M_busqueda[0]
      for producto in M_busqueda:
        if producto[1]> mayor:
          mayor = producto[1]
          lista_actual=producto
      #Se agregan los datos en Lista_ordenada
      Lista_ordenada.append(lista_actual)
      M_busqueda.remove(lista_actual)

    
    print(Lista_ordenada)
  if opcion==4: #Comienza la opción  4

    categorias = [lifestore_products[0][3]]#Se insertan los datos requeridos de lifestore_products en categorias
    print("Los productos con menores ventas son:")
    
    for producto in lifestore_products: #Se recorren listas
      num=0
      for categoria in categorias:
        if producto [3]== categoria:
          continue
        else:
          num +=1

        if num +1 > len (categorias):
          categorias.append(producto[3])#Se agregan los datos en la lista de categorias
    
    for categoria in categorias: #Se recorren listas
      top_50= []
      for producto in lifestore_products:
        ventas_producto =0
        for venta in lifestore_sales:
          if producto [0]== venta[1] and producto [3]== categoria:
            ventas_producto +=1
        
        if producto[3]==categoria:# Si se cumplen las condiciones de acuerdo a la categoria, se insertan los datos en top_50
          top_50.append([ventas_producto,producto])
       #Se ordenan los datos
      for i in range(len(top_50)):
        for j in range (len(top_50)):
          if top_50[i]<top_50[j]:
            auxiliar = top_50[j]
            top_50[j] = top_50[i]
            top_50[i]= auxiliar

      top_50 = top_50[0:50]#Se coloca el límite de datos a mostrar

      print ("\n Los productos con Menores ventas de la categoria",categoria,"es: \n")
      for producto in top_50:
         print (producto)
         
         
      
    categorias = [lifestore_products[0][3]]#Se insertan los datos requeridos de lifestore_products en categorias
    print("Los productos con menores busquedas son:")
    
    for producto in lifestore_products: #Se recorren listas
      num=0
      for categoria in categorias:
        if producto [3]== categoria:
          continue
        else:
          num +=1

        if num +1 > len (categorias):
          categorias.append(producto[3])#Se agregan los datos en la lista de categorias
    
    for categoria in categorias: #Se recorren listas
      top_100= []
      for producto in lifestore_products:
        busquedas_producto =0
        for busqueda in lifestore_searches:
          if producto [0]== busqueda[1] and producto [3]== categoria:
            busquedas_producto +=1
        
        if producto[3]==categoria:
          top_100.append([busquedas_producto,producto])# Si se cumplen las condiciones de acuerdo a la categoria, se insertan los datos en top_100

      for i in range(len(top_100)):
        for j in range (len(top_100)):
          if top_100[i]<top_100[j]:
            auxiliar = top_100[j]
            top_100[j] = top_100[i]
            top_100[i]= auxiliar

      top_100 = top_100[0:100]#Se coloca el límite de datos a mostrar

      print ("\n Los productos con Menores busquedas de la categoria",categoria,"es: \n")
      for producto in top_100:
         print (producto)
   #Comienza la opción 5
  if opcion==5:
    contador=0
    z=0 #Se declara para guardar el resltado final de mejores reseñas
    print("Los productos con mejores reseñas son: ") 
    M_reseña=[]
    for producto in lifestore_products: #Se recorren listas
    
      num=0
      for reseña in lifestore_sales:
        if producto [0]==reseña[1]:
          contador +=1
          num =reseña[2]*contador #Para realizar un agrupamiento de productos y agregando el valor de la reseña
          z=num/contador   #Se divide para obtener el valor promedio de las reseñas 
      
      if contador >=1: #Se eliminan los productos con reseña =0
       M_reseña.append([producto[1],contador,z])
       contador=0 
    M_reseña = M_reseña[0:20] #Límite de los datos a mostar
    print(M_reseña)
    

    contador=0
    z=0#Se declara para guardar el resltado final de mejores reseñas
    print("Los productos con peores reseñas son: ")
    
    M_reseña=[]
    for producto in lifestore_products: #Se recorren listas
      num=0
      for reseña in lifestore_sales:
        if producto [0]==reseña[1]:
          contador +=1
          num =reseña[2]*contador #Para realizar un agrupamiento de productos y agregando el valor de la reseña
          z=num/contador    #Se divide para obtener el valor promedio de las reseñas
      
      if contador >=1: #Se eliminan los productos con reseña =0
       M_reseña.append([producto[1],contador,z])
       contador=0 
    M_reseña = M_reseña[20:40] #Límite de los datos a mostar
    print(M_reseña)
  #Comienza la opción 6
  if opcion ==6:
    z=0 #Se declara para guardar el resltado final de meses con mas ventas
    Total =[]
    contador=0
    for producto in lifestore_products: #Se recorren listas
      precio=0
      for ventas in lifestore_sales:
        if producto[0]==ventas[1] :
         contador +=1
        precio =producto[2]*contador #Se multiplica el precio por la veces que aparece un producto vendido
      #Se agregan los valores obtenidos en Total
      Total.append([contador,precio])
   
    total_in=0
    for totali in Total:
      total_in += totali[1]#Se suman todas las ventas
   
    print("EL TOTAL DE INGRESOS ES: ",total_in)

    M_ventas= []
    a=0 #Total de ventas del mes
    print("Mes de enero: ")
    for producto in lifestore_products:#Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="01"and venta[3][6:10]=="2020":#Obtener informacion del mes de Enero del 2020
          num_ventas +=1
          formato=[producto[1],venta[3],num_ventas]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    a=len(M_ventas)#Ventas del mes
    print(M_ventas)
    print(a)

    M_ventas= []
    b=0 #Total de ventas del mes
    print("Mes de febrero: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="02"and venta[3][6:10]=="2020": #Obtener informacion del mes de Febrero del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    b=len(M_ventas)#Ventas del mes
    print(M_ventas)
    print (b)

    M_ventas= []
    c=0 #Total de ventas del mes
    print("Mes de marzo: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="03"and venta[3][6:10]=="2020": #Obtener informacion del mes de Marzo del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    c=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (c)
    
    M_ventas= []
    d=0  #Total de ventas del mes
    print("Mes de abril: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="04"and venta[3][6:10]=="2020": #Obtener informacion del mes de Abril del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
           #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    d=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (d)

    M_ventas= []
    e=0  #Total de ventas del mes
    print("Mes de mayo: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="05"and venta[3][6:10]=="2020": #Obtener informacion del mes de Mayo del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    e=len(M_ventas)  #Ventas del mes
    print(M_ventas)
    print (e)

    M_ventas= []
    f=0  #Total de ventas del mes
    print("Mes de junio: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="06"and venta[3][6:10]=="2020":#Obtener informacion del mes de Junio del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    f=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (f)

    M_ventas= []
    g=0  #Total de ventas del mes
    print("Mes de julio: ")
    for producto in lifestore_products:#Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="07"and venta[3][6:10]=="2020":#Obtener informacion del mes de Julio del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    g=len(M_ventas)#Ventas del mes
    print(M_ventas)
    print (g)

    M_ventas= []
    h=0  #Total de ventas del mes
    print("Mes de agosto: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="08"and venta[3][6:10]=="2020":#Obtener informacion del mes de Agosto del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    h=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (h)

    M_ventas= []
    i=0  #Total de ventas del mes
    print("Mes de septiembre: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="09"and venta[3][6:10]=="2020": #Obtener informacion del mes de Septiembre del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    i=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (i)

    M_ventas= []
    j=0  #Total de ventas del mes
    print("Mes de octubre: ")
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="10"and venta[3][6:10]=="2020": #Obtener informacion del mes de Octubre del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
           #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    j=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (j)

    M_ventas= []
    k=0  #Total de ventas del mes
    print("Mes de noviembre: ")
    
    for producto in lifestore_products: #Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="11" and venta[3][6:10]=="2020":#Obtener informacion del mes de Noviembre del 2020
          num_ventas +=1
          formato=[producto[1],venta[3],num_ventas]
           #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    k=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (k)

    M_ventas= []
    l=0  #Total de ventas del mes
    print("Mes de diciembre: ")
    for producto in lifestore_products:#Se recorren listas
      num_ventas=0
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[3][3:5]=="12"and venta[3][6:10]=="2020": #Obtener informacion del mes de Diciembre del 2020
          num_ventas +=1
          formato=[producto[1],venta[3]]
          #Se agregan los datos en M_ventas
          M_ventas.append(formato)
    
    l=len(M_ventas) #Ventas del mes
    print(M_ventas)
    print (l)

    z=a+b+c+d+e+f+g+h+i+j+k+l #Se suman las ventas por cada mes
    z=z/12 #Se dividen entre 12 para obtener el promedio mensual
    print("El promedio de ventas mensual es de: ",z)

    Total =[]
    contador=0
    for producto in lifestore_products: #Se recorren listas
      precio=0
      for ventas in lifestore_sales:
        if producto[0]==ventas[1] and ventas[3][6:10]=="2020":#Obtener informacion del año 2020
         contador +=1
        precio =producto[2]*contador#Se multiplica el precio por la veces que aparece un producto vendido
      #Se agregan los valores obtenidos en Total
      
      Total.append([contador,precio])
   
    total_in=0
    for totali in Total:
      total_in += totali[1] #Se suman las ventas del año
   
    print("EL TOTAL ANUAL: ",total_in)
    #Contadores de ventas por meses
    print("Los meses con mas ventas en el año son:") 
    print("Enero:",a)
    print("Febrero:",b)
    print("Marzo:",c)
    print("Abril:",d)
    print("Mayo",e)
  
  


#No tienes acceso a lifestore por que no eres administrador    
else:
 print("No eres administrador")
  






