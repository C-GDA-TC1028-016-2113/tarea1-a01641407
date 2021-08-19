def main():
    #escribe tu código abajo de esta línea
    
    pesoinicial = int(input("Dame el peso inicial: "))
    pesofinal = int(input("Dame el peso final: "))
    cantidadmeses = int(input("Dame la cantidad de meses: "))
    peso_a_bajar = pesoinicial - pesofinal
    kiloxmes = (peso_a_bajar/ cantidadmeses)
    print("Lo que debes bajar por mes es:",kiloxmes)

if __name__ == '__main__':
    main()
