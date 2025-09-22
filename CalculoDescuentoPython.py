# CalculoDescuentoPython.py
# Programa para calcular descuentos en compras
# Autor: Alan

def calcular_descuento(monto_total, porcentaje_descuento=10):
    if monto_total < 0:
        raise ValueError("El monto no puede ser negativo.")
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def mostrar_resultado(monto, porcentaje=10):
    descuento = calcular_descuento(monto, porcentaje)
    total = monto - descuento
    print(f"Monto: {monto:.2f}  | Descuento ({porcentaje}%): {descuento:.2f}  | Total a pagar: {total:.2f}")

def main():
    monto1 = 150.0
    mostrar_resultado(monto1)        # usa 10% por defecto

    monto2 = 350.0
    mostrar_resultado(monto2, 20)    # usa 20%

if __name__ == "__main__":
    main()
