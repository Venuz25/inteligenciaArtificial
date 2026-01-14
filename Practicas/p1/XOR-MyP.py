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
      H1: excitatoria A, inhibitoria B, umbral 1  -> dispara solo si A=1 y B=0
      H2: excitatoria B, inhibitoria A, umbral 1  -> dispara solo si A=0 y B=1
      Out: excitatorias H1,H2, sin inhibitorias, umbral 1 (OR)
    Devuelve (h1, h2, out)
    """
    # H1 = A AND (NOT B)
    n1 = neurona_mcCulloch_pitts(E=[A], I=[B], u=1)

    # H2 = (NOT A) AND B
    n2 = neurona_mcCulloch_pitts(E=[B], I=[A], u=1)

    # Out = H1 OR H2
    n3 = neurona_mcCulloch_pitts(E=[n1, n2], I=[], u=1)

    return n1, n2, n3


if __name__ == "__main__":
    print("A B | N1 N2 | XOR")
    print("------------------")
    for A in (0, 1):
        for B in (0, 1):
            n1, n2, n3 = xor_myp(A, B)
            print(f"{A} {B} |  {n1}  {n2}  |  {n3}")
