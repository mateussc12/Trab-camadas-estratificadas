import numpy as np


def calc(camadas, espessuras, u, f, angulo_r):
    """
    Calcula o coeficiente de reflexão, do meio estratificado
    :param camadas: Coeficiente de refração de cada camada
    :param espessuras: Espessuras de cada camada
    :param u: Velocidade da onda
    :param f: Frequências a serem utilizadas
    :param angulo_r: Ângulo de incidencia do primeiro meio
    :return: coeficiente de reflexão
    """
    lamba_list = []
    for i in range(len(f)):
        lamba_list.append(u / f[i])
    lamba = np.array(lamba_list)

    M = camadas.size - 2

    n1_sen_2 = pow(camadas[0] * np.sin(angulo_r), 2)    # Lei de Snell

    cos_i_list = []
    for i in range(camadas.size):
        cos_i_list.append(np.sqrt(1 - (n1_sen_2 / pow(camadas[i], 2))))    # Coseno do ângulo

    cos_i = np.array(cos_i_list)

    nt_list = []
    for i in range(camadas.size):
        nt_list.append(camadas[i] * cos_i[i])   # Indíce transversal refrativo

    nt = np.array(nt_list)

    #   calculo do coeficiente de reflexão
    reflex_list = []
    for i in range(len(nt) - 1):
        reflex_list.append(-(nt[i + 1] - nt[i]) / (2 * nt[i] + nt[i + 1] - nt[i]))

    reflex = np.array(reflex_list)

    d_list = []
    for i in range(M):
        d_list.append(espessuras[i] * cos_i[i])

    d = np.array(d_list)

    aux = (1, len(lamba))
    coef_reflexao = reflex[M] * np.ones(aux)

    for i in range(M - 1, -1, -1):
        B = (2 * np.pi * d[i]) / lamba
        expz = np.exp(-2 * 1j * B)
        coef_reflexao = (reflex[i] + coef_reflexao * expz) / (1 + reflex[i] * coef_reflexao * expz)

    return coef_reflexao[0]
