def neurona_mcCulloch_pitts(E, I, u):
    """
    Simula una neurona de McCulloch y Pitts.

    Parámetros:
            E : lista de enteros (0 o 1) → entradas excitatorias
            I : lista de enteros (0 o 1) → entradas inhibitorias
            u : entero (umbral)

    Retorna:
            0 → la neurona permanece apagada
            1 → la neurona se activa
    """

    # 1. Revisar si alguna entrada inhibitoria está activa (1).
    #    En el modelo de McCulloch-Pitts, cualquier inhibición anula la activación.
    if 1 in I:
        return 0   # Se apaga la neurona inmediatamente

    # 2. Calcular la suma de las entradas excitatorias.
    #    Cada "1" cuenta como una señal de activación.
    suma = sum(E)

    # 3. Comparar la suma de excitatorias con el umbral.
    #    - Si la suma es mayor o igual al umbral → la neurona se activa.
    #    - Si no alcanza el umbral → la neurona permanece apagada.
    if suma >= u:
        return 1
    else:
        return 0


# Ejemplo de uso:
E = [1, 0, 1, 1]        # entradas excitatorias
I = [0, 0]              # entradas inhibitorias
u = 3                   # umbral

salida = neurona_mcCulloch_pitts(E, I, u)
print("Salida de neurona:", salida)

"""
Explicación del ejemplo:
- La neurona recibe 3 excitaciones activas (1,0,1,1 → suma = 3).
- No hay inhibidores activos.
- Como la suma (3) es igual al umbral (3) → la neurona se activa (salida = 1).
"""

