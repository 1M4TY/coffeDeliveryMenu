from os import system
userInput = ">>> "

#Code by Kydo
#Duoc UC

i = 1

Numeracion = ""
PreciosCafesPrint = ""
TamanosCafesPrint = ""
TiposCafesPrint = ""
codDescuento = ""

TiposCafes = []
TamanosCafes = []
PreciosCafes = []

Total = 0

while True:
    try:
        system('cls')
        print("   Starbucks - Menú   ")
        print("   Tu hot coffe aquí  ")
        print("")
        print("1. Agregar café       ")
        print("2. Codigo de descuento")
        print("3. Completar pedido   ")
        print("4. Salir del programa ")
        print("")
        print("¿Que desea hacer? (1/2/3)")
        
        opMenu = int(input(userInput))

        system('cls')

        if opMenu == 1:
            print("  Starbucks - Cafés  ")
            print("  Tu hot coffe aquí  ")
            print("")
            print("1. Café Americano    ")
            print("2. Café con Leche    ")
            print("3. Té Negro          ")
            print("4. Chocolate Caliente")
            print("")
            print("¿Qué tipo de café desea? (1/2/3/4)")
            
            opTipoCafe = int(input(userInput))
            
            system('cls')

            if opTipoCafe == 1:

                TipoCafe = "Café Americano"

                print("    Café americano    ")
                print("")
                print("")
                print(f"1. Pequeño: $1200")
                print(f"2. Mediano: $1500")
                print(f"3. Grande : $1800")
                print("")
                print("¿Qué tamaño de café desea? (1/2/3)")
                opTamanoCafe = int(input(userInput))

                system('cls')
                
                if opTamanoCafe == 1:
                    TamanoCafe = "Pequeño"
                    PrecioCafe = 1200
                elif opTamanoCafe == 2:
                    TamanoCafe = "Mediano"
                    PrecioCafe = 1500
                elif opTamanoCafe == 3:
                    TamanoCafe = "Grande"
                    PrecioCafe = 1800
                else:
                    print(f"La opción {opTamanoCafe} no es valida.")
                    continue
                
            elif opTipoCafe == 2:
                
                TipoCafe = "Café con Leche"
                
                print("    Café con Leche   ")
                print("")
                print("")
                print(f"1. Pequeño: $1300")
                print(f"2. Mediano: $1600")
                print(f"3. Grande : $1900")
                print("")
                print("¿Qué tamaño de café desea? (1/2/3)")
                opTamanoCafe = int(input(userInput))

                system('cls')
                
                if opTamanoCafe == 1:
                    TamanoCafe = "Pequeño"
                    PrecioCafe = 1300
                elif opTamanoCafe == 2:
                    TamanoCafe = "Mediano"
                    PrecioCafe = 1600
                elif opTamanoCafe == 3:
                    TamanoCafe = "Grande"
                    PrecioCafe = 1900
                else:
                    print(f"La opción {opTamanoCafe} no es valida.")
                    continue
                
            elif opTipoCafe == 3:
                
                TipoCafe = "Té Negro"
                
                print("       Té Negro      ")
                print("")
                print("")
                print(f"1. Pequeño: $1000")
                print(f"2. Mediano: $1300")
                print(f"3. Grande : $1600")
                print("")
                print("¿Qué tamaño de café desea? (1/2/3)")
                opTamanoCafe = int(input(userInput))

                system('cls')
                
                if opTamanoCafe == 1:
                    TamanoCafe = "Pequeño"
                    PrecioCafe = 1000
                elif opTamanoCafe == 2:
                    TamanoCafe = "Mediano"
                    PrecioCafe = 1300
                elif opTamanoCafe == 3:
                    TamanoCafe = "Grande"
                    PrecioCafe = 1600
                else:
                    print(f"La opción {opTamanoCafe} no es valida.")
                    continue

            elif opTipoCafe == 4:
                
                TipoCafe = "Chocolate Caliente"
                
                print(" Chocolate Caliente ")
                print("")
                print("")
                print(f"1. Pequeño: $1400")
                print(f"2. Mediano: $1700")
                print(f"3. Grande : $2000")
                print("")
                print("¿Qué tamaño de café desea? (1/2/3)")
                opTamanoCafe = int(input(userInput))

                system('cls')
                
                if opTamanoCafe == 1:
                    TamanoCafe = "Pequeño"
                    PrecioCafe = 1400
                elif opTamanoCafe == 2:
                    TamanoCafe = "Mediano"
                    PrecioCafe = 1700
                elif opTamanoCafe == 3:
                    TamanoCafe = "Grande"
                    PrecioCafe = 2000
                else:
                    print(f"La opción {opTamanoCafe} no es valida.")
                    continue
                
        elif opMenu == 2:
            if Total == 0:
                system('cls')
                print("No ha evaluado su pedido")
                print("")
                system('pause')
                continue
            
            print("    Codigo de descuento    ")
            print("")

            print("¿Desea ingresar un codigo de descuento? (Si/No)")
            opCodDescuento = input(userInput)
            opCodDescuento = opCodDescuento.title()
            
            system('cls')
            
            if opCodDescuento == "Si" or opCodDescuento == "S":
                while True:
                    print("    Codigo de descuento    ")
                    print("")
                    print("Ingrese su codigo de descuento")
                    codDescuento = input(userInput)
                    codDescuento = codDescuento.upper()

                    system('cls')
                    
                    if codDescuento == "CAFELIFE":
                        print("Codigo de descuento valido")
                        print("Se ha aplicado su descuento")
                        print("")
                        system('pause')
                        break
                    else:
                        print("Codigo de descuento invalido")
                        print("")
                        print("¿Desea reingresar su codigo de descuento? (Si/No)")
                        opCodDescuento2 = input(userInput)
                        opCodDescuento2 = opCodDescuento2.title()

                        if opCodDescuento2 == "Si" or opCodDescuento2 == "S":
                            continue
                        elif opCodDescuento2 == "No" or opCodDescuento2 == "N":
                            break
                        
                continue
            elif opCodDescuento == "No" or opCodDescuento == "N":
                continue 
            else:
                print("Opcion invalida")
                print("")
                system('pause')
                continue
                
        elif opMenu == 3:
            if Total == 0:
                system('cls')
                print("No ha evaluado su pedido")
                print("")
                system('pause')
                continue
            
            for Cafes in TiposCafes:
                
                Numeracion = Numeracion + "|".center(3) + str(i).center(20)
                TiposCafesPrint = TiposCafesPrint + "|".center(3) + str(Cafes).center(20)
                
                i += 1
            else:
                TiposCafesPrint = TiposCafesPrint + "|".center(3)
                Numeracion = Numeracion + "|".center(3)

            for Tamanos in TamanosCafes:
                TamanosCafesPrint = TamanosCafesPrint + "|".center(3) + str(Tamanos).center(20)
            else:
                TamanosCafesPrint = TamanosCafesPrint + "|".center(3)
                
            for Precios in PreciosCafes:
                PreciosCafesPrint = PreciosCafesPrint + "|".center(3) + str(Precios).center(20)
            else:
                PreciosCafesPrint = PreciosCafesPrint + "|".center(3)

                
            if codDescuento == "CAFELIFE":  
                Total = Total * 0.90
                Total = round(Total)
            else:
                Total = Total

            titulo = (i * 20) + 3
            
            print("BOLETA DE CAFÉ".center(titulo))
            print("")
            print("|      ID     ", Numeracion)
            print("")
            print("|   Tipo Café ", TiposCafesPrint)
            print("")
            print("|  Tamaño Café", TamanosCafesPrint)
            print("")
            print("|  Precio Café", PreciosCafesPrint)
            print("")
            print("")
            print("")
            print("|     Total     |", str(Total).center(20), "|")
            print("")
            
            print("")
            system('pause')
            
            system('cls')
            print("Su pedido ha sido recibido")
            print("")
            system('pause')
            
            i = 1
            TiposCafes = []
            TamanosCafes = []
            PreciosCafes = []
            Total = 0

            system('cls')
            print("¿Desea hacer otro pedido? (Si/No)")
            
            opBoleta = input(userInput)
            opBoleta = opBoleta.title()
            
            if opBoleta == "Si" or opBoleta == "S":
                continue
            elif opBoleta == "No" or opBoleta == "N":
                break
            else:
                system('cls')
                print(f"La opción {opBoleta} no es valida.")
                print("")
                system('pause')
        
                continue
        
        elif opMenu == 4:
            system('cls')
            print("¿Estás seguro? (Si/No)")
            validarSalida = input(userInput)
            validarSalida = validarSalida.title()

            if validarSalida == "Si" or validarSalida == "S":
                break

            elif validarSalida == "No" or validarSalida == "N":
                system('cls')

                print("Volverás al menú")
                print("")
                system('pause')
                continue

            else:
                print(f"La opción {validarSalida} no es valida.")
        else:
            system('cls')

            print(f"La opción {opTipoCafe} no es valida.")
            print("")

            system('pause')

        TiposCafes.append(TipoCafe)

        TamanosCafes.append(TamanoCafe)

        PreciosCafes.append(PrecioCafe)
        
        if PrecioCafe > 0:
            Total += PrecioCafe
        
        TipoCafe = None
        TamanoCafe = None
        PrecioCafe = 0
        
        system('cls')
        
    except ValueError:
        system('cls')
        print("El valor ingresado no es valido")
        print("")

        system('pause')
        continue
    except KeyboardInterrupt:
        break
    
system('cls')
