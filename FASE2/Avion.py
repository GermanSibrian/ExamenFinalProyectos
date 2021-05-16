import psycopg2 as p
PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "1234"
PSQL_DB   = "germansibrian"
repetir = True
llave = True
def table_insert(sub, des, tot):
    try:
        conn = p.connect(host=PSQL_HOST, database=PSQL_DB, user=PSQL_USER, password=PSQL_PASS)
        cur = conn.cursor()
        cur.execute("""INSERT INTO public."Aerolinea"(subtotal,descuento,total)VALUES(%s,%s,%s)""", (sub, des, tot))
        print ('#######################################');
        print ('#CONEXIÓN EXITOSA CON LA BASE DE DATOS#');
        print ('#######################################');
        conn.commit()
        conn.close()
    except:
        print ('###########################################');
        print ('#HA OCURRIDO UN ERROR CON LA BASE DE DATOS#');
        print ('###########################################');
def calculo(clas, com, beb, pel):
    try:
        llave = 1
        precios = [[50, 35, 70], [40, 25, 55], [25, 10, 25]]
        pres_op = [precios[clas][a] for a in range(3)]
        sub = com * pres_op[0] + beb * pres_op[1] + pel * pres_op[2]
        if com + beb + pel > 10 and clas > 0:
            total = sub * 0.9
            descu = '10%'
        elif clas == 0 and com > 0 and beb > 0 and pel > 0:
            total = sub * 0.95
            descu = '5%'
        else:
            total = sub
            descu = '0%'
        return str(sub), descu, str(total)
    except:
        print ('###########################################');
        print ('#         HA OCURRIDO UN ERROR            #');
        print ('###########################################');
menu = """#######################################################################
BIENVENIDO A NUESTRA AEREOLINEA\nEscoja una clases:\n1) Primera clase\n2) Segunda clase\n3) Tercera clase"""

menu2 = """#######################################################################
¿Qué acción desea realizar?\n1) Limpiar\n2) Salir\n3) Reporte\n4) Calcular"""

precios = """#######################################################################
Tipo servicio/tipo clase ! primera clase ! segunda clase ! tercera clase
         Comida                 50              40              25
         Bebida                 35              25              10
         Pelicula               70              55              25
"""
while repetir == True:
    try:
        print(precios)
        print(menu)
        print ('###########################################');
        clase = int(input("INGRESE CLASE A SELECCIONAR: "))
        print ('###########################################');
        comida = int(input("SERVICIOS DE COMIDA: "))
        print ('###########################################');
        bebida = int(input("SERVICIOS DE BEBIDA: "))
        print ('###########################################');
        pelicula = int(input("SERVICIOS DE PELÍCULAS: "))
        print ('###########################################');
        print(menu2)
        print ('###########################################');
        select = int(input("ESCOJA UNA OPCIÓN: "))
        print ('###########################################');
        if select == 1:
            clase = 0
            comida = 0
            bebida = 0
            pelicula = 0
        elif select == 2:
            repetir = False
        elif select == 3:
            print("\nUSTED ELIGIÓ VIAJAR EN {}° CLASE, SUS ORDENES SON:\n".format(clase))
            print("{} DE COMIDA\n{} DE BEBIDA\n{} DE PELICULA\n".format(comida, bebida, pelicula))
            des = int(input("DESEA CALCULAR(1)/DESEA SALIR SIN GUARDAR(2): "))
            if des == 1:
                subto, desc, tott = calculo(clase - 1, comida, bebida, pelicula)
                table_insert(subto, desc, tott)
                print("EL SUBTOTAL ES:  {}".format(subto))
                print("EL DESCUENTO ES: {}".format(desc))
                print("El TOTAL ES:     {}".format(tott))
        elif select == 4:
            subto, desc, tott = calculo(clase - 1, comida, bebida, pelicula)
            table_insert(subto, desc, tott)
            print("EL SUBTOTAL ES:  {}".format(subto))
            print("EL DESCUENTO ES: {}".format(desc))
            print("EL TOTAL ES:     {}".format(tott))
        else:
            print("OPCIÓN INVÁLIDA")
    except:
        print ('###########################################');
        print ('#         HA OCURRIDO UN ERROR            #');
        print ('###########################################');