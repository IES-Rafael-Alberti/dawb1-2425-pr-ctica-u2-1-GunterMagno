
COMANDOS = ["compra", "venta", "saldo", "reset", "fin"]
MENSAJE_ERROR = "*ERROR* Entrada inválida"


def comprobar_importe(valor: str) -> bool:
    valor = valor.replace(",", ".").strip()
    if valor.startswith("-"):
        valor = valor[1:]
        return (valor.isdigit())
    else:
      pos_punto = valor.find(".")
    if pos_punto >= 0:
        valor = valor[:pos_punto] + valor[pos_punto + 1:]
        return valor.isdigit()
    else:
        return valor.isdigit()


def comprobar_comando(comando: str) -> bool:
    if comando in ["compra", "venta", "saldo", "reset", "fin"]:
        comando = True
        return(comando)
    else:
        comando = False
        return(comando)


def mostrar_mensaje_error():
    print("*ERROR* Entrada inválida")


def procesar_compra(saldo: float, importe: float) -> float:
    saldo = saldo - importe
    return(saldo)


def procesar_venta(saldo: float, importe: float) -> float:
    saldo = saldo + importe
    return(saldo)


def mostrar_saldo(saldo: float, cont_compras: int, cont_ventas: int):
    print(f"El saldo actual es = {saldo}  ({cont_compras} compras y {cont_ventas} ventas)")


def resetear_saldo(saldo: float, cont_compras: int, cont_ventas: int) -> tuple[float, int, int]:
    print(f"El saldo anterior es = {saldo}  ({cont_compras} compras y {cont_ventas} ventas)")
    saldo = 0 
    cont_compras = 0
    cont_ventas = 0
    print(f"El saldo actual es = {saldo}  ({cont_compras} compras y {cont_ventas} ventas)")
    return (0, 0, 0)

def recuperar_comando_e_importe(linea: str) -> tuple[str, str]:
    linea = input("> ").strip().lower()
    lista_palabras = linea.split()

    if len(lista_palabras) == 1:
        return lista_palabras[0], None
    elif len(lista_palabras) == 2:
        return lista_palabras[0], lista_palabras[1]
    else:
        return None, None

def main():
    cont_compras = 0
    cont_ventas = 0
    saldo = 0
    encuentra_fin = False
    linea = None

    while not encuentra_fin:

        comando, importe = recuperar_comando_e_importe(linea)

        if comando is None or not comprobar_comando(comando):
            mostrar_mensaje_error()
        elif comando in ("saldo", "reset", "fin") and importe is not None:
            mostrar_mensaje_error()
        elif comando == "saldo":
            mostrar_saldo(saldo, cont_compras, cont_ventas)
        elif comando == "reset":
            saldo, cont_compras, cont_ventas = resetear_saldo(saldo, cont_compras, cont_ventas)
        elif comando == "fin":
            encuentra_fin = True
        elif importe is None or not comprobar_importe(importe): 
            mostrar_mensaje_error()
        else:
            importe_float = float(importe)
            if comando == "compra":
                saldo = procesar_compra(saldo, importe_float)
                cont_compras += 1
            elif comando == "venta":
                saldo = procesar_venta(saldo, importe_float)
                cont_ventas += 1

            
if __name__ == "__main__":
    main()