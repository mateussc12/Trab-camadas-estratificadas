import func
import numpy as np
from matplotlib import pyplot as plt
from scipy.constants import c


plt.style.use("ggplot")


# --------------------------------------------------------------------------------- ENTRADA
print("==============================================")
print("| PROPAGAÇÃO DE ONDAS EM MEIO COM N CAMADAS  |")
print("==============================================")
print()

# CAMADAS EXTERNAS n_a (esquerda) e n_b (direita)
print('############# VALORES DE ENTRADA ############# ')
n_a = float(input('Indice de refração do primeiro meio: '))
n_b = float(input('Indice de refração do último meio: '))

# NUMERO DE CAMADAS
print()
num_camadas = int(input('Número de camadas: '))

# ANGULO DE INCIDENCIA
angulo_d = float(input('Ângulo de incidência da onda (graus): '))
angulo_r = angulo_d * np.pi / 180

# FREQUENCIA
print()
print('Frequências (Htz)')
a = float(input('Valor inicial:'))
b = float(input('Valor final:'))
f = np.linspace(a, b, 10000)

# --------------------------------------------------------------------------------- PROCESSAMENTO
# VETOR CONTENDO AS IMPEDANCIAS DOS MEIOS
n = [n_a]

# VETOR CONTENDO AS ESPESSURAS DAS CAMADAS
d = []

print()
u = input('Velocidade da onda(m/s): ')
if u == 'c':
    u = c
u = float(u)

print()
for i in range(num_camadas):
    print(f"Indice de refração e espessura da camada {i + 1}")
    n.append(float(input(f'n_{i + 1}: ')))    # COEFICIENTE DE REFRACAO
    d.append(float(input(f'd_{i + 1}: ')))    # ESPESSURA DA CAMADA

espessuras = np.array(d, dtype='float')

camadas = np.array(n, dtype='float')
camadas = np.append(camadas, n_b)


coef_refle = func.calc(camadas, espessuras, u, f, angulo_r)

# --------------------------------------------------------------------------------- PÓS-PROCESSAMENTO (SAÍDA)
#   Gráfico

fig1, ref_trans = plt.subplots()

ref_trans.plot(f, np.abs(coef_refle), label="Reflexão", color="#173F5F")

ref_trans.plot(f, np.abs(coef_refle + 1), label="Transmissão", color='#EC4176')

ref_trans.legend()

ref_trans.set_title(f'Ondas planas em um meio estratificado de {len(camadas)} camadas')

ref_trans.set_xlabel("Frequência [Htz]")

plt.tight_layout()
plt.show()
