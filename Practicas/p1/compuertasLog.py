def neurona_McCulloch_Pitts(E, I, u):
    # 1. Revisar entradas inhibitorias: si alguna es 1, salida es 0
    if 1 in I:
        return 0

    # 2) Calcular suma de entradas excitatorias
    suma = sum(E)

    # 3) Comparar con el umbral
    if suma >= u:
        return 1
    else:
        return 0

# --- Definicion de funciones de compuertas logicas usando neuronas McCulloch-Pitts ---
# 1) OR de 2 entradas
def neurona_or2(a, b):
    return neurona_McCulloch_Pitts([a, b], [], 1)

# 2) AND de 2 entradas
def neurona_and2(a, b):
    return neurona_McCulloch_Pitts([a, b], [], 2)

# 3) DELAY / BUFFER (simple neurona que copia la entrada)
def neurona_delay(a):
    return neurona_McCulloch_Pitts([a], [], 1)

# 4) NOT de 1 entrada
def neurona_not(a):
    return neurona_McCulloch_Pitts([], [a], 0)

# 5) MAJORITY de 3 entradas
def neurona_majority3(a, b, c):
    return neurona_McCulloch_Pitts([a, b, c], [], 2)

# 6) el AND (NOT il) --> excitatoria el, inhibitoria il, umbral 1
def neurona_e_and_not_i(el, il):
    return neurona_McCulloch_Pitts([el], [il], 1)

# 7) NOR de 2 entradas (NOT OR) --> dispara solo si ambas entradas son 0
def neurona_nor2(a, b):
    return neurona_McCulloch_Pitts([], [a, b], 0)

# 8) AND de 3 entradas (umbral = 3)
def neurona_and3(a, b, c):
    return neurona_McCulloch_Pitts([a, b, c], [], 3)

# 9) OR de 3 entradas (umbral = 1)
def neurona_or3(a, b, c):
    return neurona_McCulloch_Pitts([a, b, c], [], 1)

# 10) NOT e1 or E1
def neurona_note1_or_e1(e):
    return neurona_McCulloch_Pitts([e], [], 0)

# 11) MAJORITY de 5 entradas
def neurona_majority5(a, b, c, d, e):
    return neurona_McCulloch_Pitts([a, b, c, d, e], [], 3)

# 12) AND(a,b,NOT(i1),NOT(i2))
def neurona_mix_exc2_inh2(a, b, i1, i2):
    return neurona_McCulloch_Pitts([a, b], [i1, i2], 2)

# --- Funciones para probar y mostrar tablas de verdad ---
def probar_tabla(func, n_inputs, nombres=None):
    """
    Circula por todas las combinaciones binarias para una función 'func' que recibe n_inputs.
    Imprime la tabla de verdad.
    """
    if nombres is None:
        nombres = [f'x{i+1}' for i in range(n_inputs)]

    # Encabezados
    header = " ".join(nombres) + " | out"
    print(header)
    print("-" * len(header))

    # Iterar sobre todas las combinaciones binarias
    for val in range(2**n_inputs):
        bits = [(val >> (n_inputs - 1 - i)) & 1 for i in range(n_inputs)]
        out = func(*bits)
        print(" ".join(str(b) for b in bits) + " | " + str(out))
    print()

# Ejecutar comprobaciones (tablas) para cada neurona
if __name__ == "__main__":
    print("1) OR (2 inputs)")
    probar_tabla(neurona_or2, 2, ["a", "b"])

    print("2) AND (2 inputs)")
    probar_tabla(neurona_and2, 2, ["a", "b"])

    print("3) DELAY / BUFFER (1 input)")
    probar_tabla(neurona_delay, 1, ["a"])

    print("4) NOT (1 input)")
    probar_tabla(neurona_not, 1, ["a"])

    print("5) MAJORITY (3 inputs) -> dispara si >= 2 activas")
    probar_tabla(neurona_majority3, 3, ["a", "b", "c"])

    print("6) el AND (NOT i1) (2 inputs: e1,i1)")
    probar_tabla(neurona_e_and_not_i, 2, ["e1", "i1"])

    print("7) NOR (2 inputs) -> NOT(OR)")
    probar_tabla(neurona_nor2, 2, ["a", "b"])

    print("8) AND (3 inputs)")
    probar_tabla(neurona_and3, 3, ["a", "b", "c"])

    print("9) OR (3 inputs)")
    probar_tabla(neurona_or3, 3, ["a", "b", "c"])

    print("10) NEURONA 10")
    probar_tabla(neurona_note1_or_e1, 1, ["e"])

    print("11) NEURONA 11")
    probar_tabla(neurona_majority5, 5, ["a", "b", "c", "d", "e"])

    print("12) NEURONA 12")
    probar_tabla(neurona_mix_exc2_inh2, 4, ["a", "b", "i1", "i2"])