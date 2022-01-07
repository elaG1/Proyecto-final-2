import csv

print("---R E P O R T E   S Y N E R G Y   L O G I S T I C S---","\n")
print("************************************************************")
print("OPCIÓN 1. RUTAS DE IMPORTACIÓN Y EXPORTACIÓN","\n")
print("---------------RUTAS IMPORTACIONES------------------","\n")
# Se usa el método reader para leer la información línea por
# línea y que las muestre en forma de lista
with open("synergy.csv", "r") as database:
    lector = csv.reader(database)

    # Se itera sobre el objeto lector y se filtran las líneas
    # que pertenecen a importación para que a la variable datos_imp
    # se agreguen en forma de lista la ruta y su valor
    datos_imp=list()
    lista_de_rutas_imp=list()
    total_value=0
    total_value_imp=0 # Se comienza el contador en 0 para obtener 
    # el valor total respectivo a rutas de importación
    for line in lector:
        try:
            direction=line[1]
            valor=int(line[9])
            total_value+=valor
        except:
            continue
        if direction != "Imports":
            continue
        else:
            origen,destino,valor_imp,transporte=line[2],line[3],int(line[9]),line[7]
            ruta=(origen+"-"+destino+"-"+transporte)
            total_value_imp+=valor_imp
            datos_imp.append([ruta,valor_imp])
    #print(total_value_imp) # Muestra el valor total de importaciones
    #print(total_value) # Muestra el valor total, es decir sin distinguir entre importaciones y exportaciones
    #print(datos_imp)
    
    # En esta parte se busca obtener una lista solo con las
    # rutas de importación, así que se agrega únicamente el
    # primer valor de cada elemento de la lista anterior si
    # es que no se ha agregado
    for dato in datos_imp:
        ruta=dato[0]
        if ruta not in lista_de_rutas_imp:
            lista_de_rutas_imp.append(ruta)
    #print(lista_de_rutas_imp)
    print("Número de rutas de importación: ",len(lista_de_rutas_imp),"\n")
    
    # Se itera sobre la lista de rutas y sobre la lista de 
    # datos_imp y si la ruta en lista de rutas coincide con
    # la ruta en la base de datos_imp, se suma su valor
    # para así obtener el valor total por ruta. Para
    # esto el contador empieza en cero con cada nueva ruta
    valor_por_ruta=list()
    total_ruta_imp=list()
    for ruta in lista_de_rutas_imp:
        suma=0
        for dato in datos_imp:
            if ruta in dato:
                valor=int(dato[1])
                suma+=valor
            else:
                continue
        # Para obtener el peso que cada ruta representa sobre el valor 
        # total de importaciones se divide el valor de cada
        # ruta entre el valor total de importaciones y se expresa
        # en términos de porcentaje. La ruta y su valor se agregan
        # a la lista total_ruta_imp para ordenarlo de mayor a menor valor
        # y así obtener las 10 rutas más importantes
        peso = round(((suma/total_value_imp)*100),2)
        total_ruta_imp.append((peso,ruta))
        total_ruta_imp=sorted(total_ruta_imp,reverse=True)
    print("Las 10 rutas de importación que generan mayor valor (% del valor total de importaciones): ",total_ruta_imp[:10],"\n")
    #print(total_ruta_imp)
    # Se crea un contador para que después de sumar el valor de las
    # primer 10 rutas se detenga
    porcentaje_suma_imp=0
    n=0
    for valor in total_ruta_imp:
        porcentaje=valor[0]
        n+=1
        if n < 11:
            porcentaje_suma_imp+=porcentaje
        else:
            break
    porcentaje_rutas=round(porcentaje_suma_imp,2)
    print("Porcentaje que representan las 10 rutas sobre el valor total de importaciones: ",porcentaje_rutas,"\n")
    porcentaje_im_tot=round((total_value_imp*porcentaje_rutas/total_value),2)
    print("Porcentaje que representan sobre el valor total: ",porcentaje_im_tot,"\n")
    
print("---------------RUTAS EXPORTACIONES-------------------","\n")
with open("synergy.csv", "r") as database:
    lector = csv.reader(database)
    
    # El código que se usa para esta parte es el mismo que se usó
    # para la parte de importaciones, lo único que cambia es la
    # dirección, ahora se filtra para que las únicas líneas que 
    # tome en cuenta sean las de exportaciones
    datos_exp=list()
    lista_de_rutas_exp=list()
    total_value_exp=0
    for line in lector:
        direction=line[1]
        if direction != "Exports":
            continue
        else:
            origen,destino,valor_exp,transporte=line[2],line[3],int(line[9]),line[7]
            ruta=(origen+"-"+destino+"-"+transporte)
            total_value_exp+=valor_exp
            datos_exp.append([ruta,valor_exp])
    #print(total_value_exp)
    #print(datos_exp)
    
    for dato in datos_exp:
        ruta=dato[0]
        if ruta not in lista_de_rutas_exp:
            lista_de_rutas_exp.append(ruta)
    #print(lista_de_rutas_exp)
    print("Número de rutas de exportación: ",len(lista_de_rutas_exp),"\n")
    
    valor_por_ruta=list()
    total_ruta_exp=list()
    for ruta in lista_de_rutas_exp:
        suma=0
        #print(ruta)
        for dato in datos_exp:
            if ruta in dato:
                valor=int(dato[1])
                suma+=valor
            else:
                continue
        peso = round(((suma/total_value_exp)*100),2)
        total_ruta_exp.append((peso,ruta))
        total_ruta_exp=sorted(total_ruta_exp,reverse=True)
    print("Las 10 rutas de exportación que generan mayor valor (% del valor total de exportaciones): ",total_ruta_exp[:10],"\n")
    porcentaje_suma_exp=0
    n=0
    for valor in total_ruta_exp:
        money=valor[0]
        n+=1
        if n < 11:
            porcentaje_suma_exp+=money
        else:
            break
    porcentaje_rutas=round(porcentaje_suma_exp,2)
    print("Porcentaje que representan las 10 rutas sobre el valor total de exportaciones: ",porcentaje_rutas,"\n")
    porcentaje_exp_tot=round((total_value_exp*porcentaje_rutas/total_value),2)
    print("Porcentaje que representan sobre el valor total: ",porcentaje_exp_tot,"\n")
    

    print("--------VALOR QUE GENERAN LAS 20 RUTAS MÁS IMPORTANES--------","\n")
    print("Número de rutas en total: ",len(lista_de_rutas_imp)+len(lista_de_rutas_exp),"\n")
    rutas_tot=round((20/(len(lista_de_rutas_imp)+len(lista_de_rutas_exp))*100),2)
    print("Porcentaje del total de rutas que representan las 20 rutas más importantes: ",rutas_tot,"\n")
    print("Porcentaje del valor total que generan las 20 rutas más importantes: ",porcentaje_im_tot+porcentaje_exp_tot,"\n")
    
print("************************************************************")
print("OPCIÓN 2. MEDIO DE TRANSPORTE UTILIZADO","\n")
print("---------------TRANSPORTES-----------------","\n")
with open("synergy.csv", "r") as database:
    lector = csv.reader(database)                
    
    # Se usa el mismo código que para las secciones anteriores, solo
    # se hacen pequeños cambios para adaptarlo, por ejemplo
    # no se usa un valor para filtrar exportaciones o importaciones,
    # ya que se está considerando el valor total de cada transporte
    datos_t = list()
    lista_de_transportes = list()
    for line in lector:
        try:
            transporte,valor=line[7],int(line[9])
            datos_t.append([transporte,valor])
            if transporte not in lista_de_transportes:
                lista_de_transportes.append(transporte)
        except:
            continue
    #print(total_value)
    #print(datos_t)
    #print(lista_de_transportes)
    
    valor_por_transporte=list()
    total_transporte=list()
    for transporte in lista_de_transportes:
        suma=0
        #print(transporte)
        for dato in datos_t:
            if transporte in dato:
                valor=int(dato[1])
                suma+=valor
            else:
                continue
        peso = round(((suma/total_value)*100),2)
        total_transporte.append((peso,transporte))
        total_transporte=sorted(total_transporte,reverse=True)
    print("Valor por transporte (% del valor total): ", total_transporte,"\n")
    print("Los 3 transportes con mayor relevancia (% del valor total): ",total_transporte[:3],"\n")
            
    
print("************************************************************")
print("OPCIÓN 3. PAÍSES","\n")
print("---------------PAÍSES CON MÁS IMPORTANCIA---------------","\n")
with open("synergy.csv", "r") as database:
    lector = csv.reader(database)
    
    datos = list()
    lista_de_paises = list()
    total_value=0
    for line in lector:
        try:
            origen,destino,valor=line[2],line[3],int(line[9])
            total_value+=valor
            # se agrega a la lista datos cada país y su valor,
            # sin importar si es de origen o destino
            datos.append([origen,valor])
            datos.append([destino,valor])
        except:
            continue
    #print(total_value)
    #print(datos)

    for dato in datos:
        pais=dato[0]
        if pais not in lista_de_paises:
            # para evitar repeticiones se agrega a la lista_de_paises
            # solo los países que aún no se han agregado
            lista_de_paises.append(pais)
    #print(lista_de_paises)
    print("Número de países: ",len(lista_de_paises),"\n")
   
    pais_conteo=list()
    # Se itera sobre la lista_de_paise anteriormente creada y sobre la lista
    # datos y si el país en la lista de países coincide con el 
    # país en la base datos, se suma su valor, esto para tener el 
    # valor total por país aunque no se está distinguiendo, es decir, si el país es China
    # se suman todos los valores donde aparezca China, sin importar
    # si es el país de origen o destino, esto con el objetivo de obtener
    # el valor que generan las transacciones en las que está involucrada China
    for pais in lista_de_paises:
        count=0
        for dato in datos:
            pais_en_datos=dato[0]
            valor=dato[1]
            if pais_en_datos == pais:
                count+=valor
            else:
                continue
        peso = round(((count/total_value)*100),2)
        # En país_conteo tenemos cada país y el porcentaje que
        # generan las transacciones en las que dicho país participa
        pais_conteo.append((peso,pais))
        pais_conteo=sorted(pais_conteo,reverse=True)
    #print("Valor por país %: ",pais_conteo)
    
    # Se buscan obtener los países que generan el 80% del valor 
    # total. Se crea un contador suma_p que empeiece en 0. Se itera
    # sobre la lista país_conteo y se va sumando el valor en la
    # variable suma, siempre y cuando la suma total aún no esté 
    # en 85, esto con el fin de agregar a la lista conexiones 
    # los países que al sumar las transacciones en las que
    # participan den alredeor del 80% del valor total 
    print("Países con mayor relevancia (% del valor total): ")
    suma_p=0
    conexiones=list()
    for pais in pais_conteo:
        valor= pais[0]
        suma_p+= valor
        if suma_p < 85:
            conexiones.append(pais)
        else:
            break # Para que se detenga si la suma llegó a 85
    print(conexiones,"\n")
    paises_tot=round((len(conexiones)/len(lista_de_paises)*100),2)
    print("Porcentaje que representan los países más importantes como parte del total de países: ",paises_tot)

