juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'Brightworks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

def leer_opcion():
    """Solicita la opción y valida que sea un entero entre 1 y 6."""
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def stock_plataforma(plataforma, dicc_juegos, dicc_inventario):
    """Suma el stock de los juegos que pertenecen a la plataforma dada."""
    total_stock = 0
    
    for codigo in dicc_juegos.keys():
        datos_juego = dicc_juegos[codigo]
        plataforma_juego = datos_juego[1]
        
        if plataforma_juego.upper() == plataforma.upper():
            if codigo in dicc_inventario:
                datos_inv = dicc_inventario[codigo]
                stock = datos_inv[1]
                total_stock = total_stock + stock
                
    print(f"El total de stock disponibles es: {total_stock}")

def busqueda_precio(p_min, p_max, dicc_juegos, dicc_inventario):
    resultados = []
    for codigo in dicc_inventario.keys():
        datos_inv = dicc_inventario[codigo]
        precio = datos_inv[0]
        stock = datos_inv[1]
        
        if precio >= p_min and precio <= p_max and stock > 0:
            if codigo in dicc_juegos:
                datos_juego = dicc_juegos[codigo]
                titulo = datos_juego[0]
                resultados.append(f"{titulo}--{codigo}")
                
    if len(resultados) > 0:
        resultados.sort()
        print(f"Los juegos encontrados son: {resultados}")
    else:
        print("No hay juegos en ese rango de precios.")

def actualizar_precio(codigo, nuevo_precio, dicc_juegos, dicc_inventario):
    for k in dicc_inventario.keys():
        if k.upper() == codigo.upper():
            dicc_inventario[k][0] = nuevo_precio
            return True
    return False

def validar_codigo(codigo, dicc_juegos):
    if codigo == "" or codigo.strip() == "":
        return False
    for k in dicc_juegos.keys():
        if k.upper() == codigo.upper():
            return False
    return True

def validar_titulo(titulo):
    if titulo == "" or titulo.strip() == "":
        return False
    else:
        return True

def validar_plataforma(plataforma):
    if plataforma == "" or plataforma.strip() == "":
        return False
    else:
        return True

def validar_genero(genero):
    if genero == "" or genero.strip() == "":
        return False
    else:
        return True

def validar_clasificacion(clasificacion):
    if clasificacion == 'E' or clasificacion == 'T' or clasificacion == 'M':
        return True
    else:
        return False

def validar_multiplayer(multiplayer):
    if multiplayer.lower() == 's' or multiplayer.lower() == 'n':
        return True
    else:
        return False

def validar_editor(editor):
    if editor == "" or editor.strip() == "":
        return False
    else:
        return True

def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False

def validar_stock(stock):
    if stock >= 0:
        return True
    else:
        return False


def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, dicc_juegos, dicc_inventario):
    for k in dicc_juegos.keys():
        if k.upper() == codigo.upper():
            return False
            
    if multiplayer.lower() == 's':
        mp_bool = True
    else:
        mp_bool = False
        
    codigo_up = codigo.upper()
    dicc_juegos[codigo_up] = [titulo, plataforma, genero, clasificacion, mp_bool, editor]
    dicc_inventario[codigo_up] = [precio, stock]
    return True


def eliminar_juego(codigo, dicc_juegos, dicc_inventario):
    """Busca el código y lo elimina de ambos diccionarios si existe."""
    for k in dicc_juegos.keys():
        if k.upper() == codigo.upper():
            del dicc_juegos[k]
            del dicc_inventario[k]
            return True
    return False

def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("====================================")
        
        opc = leer_opcion()
        

        if opc == 1:
            plat = input("Ingrese plataforma a consultar: ")
            stock_plataforma(plat, juegos, inventario)
            

        elif opc == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max, juegos, inventario)
                        break
                    else:
                        print("Debe ingresar valores válidos (mayores a cero y mín <= máx)")
                except ValueError:
                    print("Debe ingresar valores enteros")
                    

        elif opc == 3:
            procesando_precios = True
            while procesando_precios == True:
                cod = input("Ingrese código del juego: ")
                try:
                    n_precio = int(input("Ingrese nuevo precio: "))
                    if n_precio > 0:
                        if actualizar_precio(cod, n_precio, juegos, inventario) == True:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El precio debe ser un entero positivo.")
                except ValueError:
                    print("Debe ingresar un valor entero")
                
                while True:
                    resp = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                    if resp == 'n':
                        procesando_precios = False
                        break
                    elif resp == 's':
                        break
                        

        elif opc == 4:
            todo_valido = True   
            cod = input("Ingrese código del juego: ")
            if validar_codigo(cod, juegos) == False:
                print("Error: Código inválido o ya existente.")
                todo_valido = False

            if todo_valido == True:
                tit = input("Ingrese título: ")
                if validar_titulo(tit) == False:
                    print("Error: El título no puede estar vacío.")
                    todo_valido = False
                    
            if todo_valido == True:
                plat = input("Ingrese plataforma: ")
                if validar_plataforma(plat) == False:
                    print("Error: La plataforma no puede estar vacía.")
                    todo_valido = False
                    
            if todo_valido == True:
                gen = input("Ingrese género: ")
                if validar_genero(gen) == False:
                    print("Error: El género no puede estar vacío.")
                    todo_valido = False
                    
            if todo_valido == True:
                clas = input("Ingrese clasificación (E, T, M): ")
                if validar_clasificacion(clas) == False:
                    print("Error: Clasificación debe ser 'E', 'T' o 'M'.")
                    todo_valido = False
                    
            if todo_valido == True:
                mult = input("¿Es multiplayer? (s/n): ")
                if validar_multiplayer(mult) == False:
                    print("Error: Debe ingresar 's' o 'n'.")
                    todo_valido = False
                    
            if todo_valido == True:
                edit = input("Ingrese editor: ")
                if validar_editor(edit) == False:
                    print("Error: El editor no puede estar vacío.")
                    todo_valido = False
                    
            if todo_valido == True:
                try:
                    prec = int(input("Ingrese precio: "))
                    if validar_precio(prec) == False:
                        print("Error: El precio debe ser un entero mayor que cero.")
                        todo_valido = False
                except ValueError:
                    print("Error: El precio debe ser un número entero.")
                    todo_valido = False
                    
            if todo_valido == True:
                try:
                    stk = int(input("Ingrese stock: "))
                    if validar_stock(stk) == False:
                        print("Error: El stock debe ser un entero mayor o igual a cero.")
                        todo_valido = False
                except ValueError:
                    print("Error: El stock debe ser un número entero.")
                    todo_valido = False
            
            if todo_valido == True:
                if agregar_juego(cod, tit, plat, gen, clas, mult, edit, prec, stk, juegos, inventario) == True:
                    print("Juego agregado")
                else:
                    print("El código ya existe")
                

        elif opc == 5:
            cod = input("Ingrese código del juego a eliminar: ")
            if eliminar_juego(cod, juegos, inventario) == True:
                print("Juego eliminado")
            else:
                print("El código no existe")
                

        elif opc == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()