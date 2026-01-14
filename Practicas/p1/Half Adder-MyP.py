def neurona_mcCulloch_pitts(E, I, u):
    """
    Simula una neurona de McCulloch y Pitts.

    Parámetros:
    E : lista de enteros (0 o 1) -> entradas excitatorias
    I : lista de enteros (0 o 1) -> entradas inhibitorias
    u : entero (umbral)

    Retorna:
    0 -> la neurona permanece apagada
    1 -> la neurona se activa
    """
    # 1. Revisar entradas inhibitorias: si alguna está activa, la neurona no dispara
    if 1 in I:
        return 0

    # 2. Calcular la suma de excitatorias
    suma = sum(E)

    # 3. Comparar con el umbral
    if suma >= u:
        return 1
    else:
        return 0


def xor_myp(A, B):
    """
    Implementa XOR usando neuronas McCulloch-Pitts (MyP) con
    entradas excitatorias e inhibitorias.
    Estructura:
      N1: excitatoria A, inhibitoria B, umbral 1  -> dispara solo si A=1 y B=0
      N2: excitatoria B, inhibitoria A, umbral 1  -> dispara solo si A=0 y B=1
      N3: excitatorias N1,N2, sin inhibitorias, umbral 1 (OR)
    Devuelve (n1, n2, n3) donde n3 es A XOR B.
    """
    # N1 = A AND (NOT B)
    n1 = neurona_mcCulloch_pitts(E=[A], I=[B], u=1)

    # N2 = (NOT A) AND B
    n2 = neurona_mcCulloch_pitts(E=[B], I=[A], u=1)

    # N3 = N1 OR N2
    n3 = neurona_mcCulloch_pitts(E=[n1, n2], I=[], u=1)

    return n1, n2, n3


def half_adder(A, B):
    """
    Medio sumador usando neuronas MyP.
    Retorna (S, C, n1, n2) donde:
      S = suma (A XOR B)
      C = carry (A AND B)
      n1,n2 son señales intermedias del XOR
    """
    n1, n2, S = xor_myp(A, B)
    C = neurona_mcCulloch_pitts(E=[A, B], I=[], u=2)  # AND
    return S, C, n1, n2


if __name__ == "__main__":
    print("A B | N1 N2 | S (XOR) C (AND)")
    print("------------------------------")
    for A in (0, 1):
        for B in (0, 1):
            S, C, n1, n2 = half_adder(A, B)
            print(f"{A} {B} |  {n1}  {n2}  |   {S}      {C}")
