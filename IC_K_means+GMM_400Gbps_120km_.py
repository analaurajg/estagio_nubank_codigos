#!/usr/bin/env python
# coding: utf-8

# #*Testes*

# # **1. Importação dos dados e BER por Máxima Verossimilhança**

# In[5]:


import numpy as np                # For numerical functions
import matplotlib.pyplot as plt   # For graphical representation
import pickle                     # For variable storage
import pandas as pd               # For data processing
import time                       # For time-related functions

# Machine learning tools
from sklearn import preprocessing                     # Preprocessing functions
from sklearn.neural_network import MLPClassifier      # MLP classifier
from sklearn.neural_network import MLPRegressor       # MLP regressor
from sklearn.model_selection import train_test_split  # Train-test split

# File manipulation
import os                         # Operating system-related functions
import csv                        # CSV read and write functions

# No Jupyter local, o comando abaixo mostra a pasta onde o seu arquivo .ipynb está salvo
print("Diretório atual de trabalho:", os.getcwd())

"""## 1. Import the data:"""

# 1. Definir a distância
distance_text = '120km'

# 2. Definir o caminho base do seu computador (usando 'r' antes das aspas)
# Note que parei o caminho antes do "Dados_", pois o código abaixo completa com a distância.
base_path = r'C:\Users\User\Desktop\Iniciação Científica 2025-2026'

# 3. Construir o caminho final da pasta de dados
path_data_folder = base_path + r'\Dados_' + distance_text

print('The selected data folder is:', path_data_folder)

# Load ideal (reference) data
# Monta o caminho completo para o arquivo CSV da constelação ideal
# No Windows, o Python aceita a barra '/' mesmo em caminhos locais, facilitando a concatenação
path_ideal_file = path_data_folder + '/400gbps_IdealConstellationDiagram_ref_' + distance_text + '.csv'

print('\t Loading:', path_ideal_file)

# Leitura do arquivo ideal
df = pd.read_csv(path_ideal_file, skiprows=1) 
data_ideal = np.round(df.to_numpy()) 
m, n = np.shape(data_ideal)

print(f"path_data_folder = {path_data_folder}")
print(f"path_ideal_file = {path_ideal_file}")

# Carregar as constelações distorcidas
print('\nLoading distorted constellations:', path_data_folder)

power_text = [
    'Diagram_0dbm_', 'Diagram_1dbm_', 'Diagram_2dbm_', 'Diagram_3dbm_',
    'Diagram_4dbm_', 'Diagram_5dbm_', 'Diagram_6dbm_', 'Diagram_7dbm_',
    'Diagram_8dbm_', 'Diagram_9dbm_', 'Diagram_10dbm_', 'Diagram_11dbm_',
    'Diagram_12dbm_', 'Diagram_13dbm_', 'Diagram_14dbm_', 'Diagram_15dbm_', 
    'Diagram_16dbm_', 'Diagram_17dbm_', 'Diagram_18dbm_', 'Diagram_19dbm_',
    'Diagram_20dbm_',
]

# Lista os arquivos da pasta local
files = os.listdir(path_data_folder)

def BER(X_test, Y_test):
    Y_test_hat = X_test
    # X polarization
    aux = 4*np.clip(np.round((Y_test[:,0]-1)/2)+2,0,3)+np.clip(np.round((Y_test[:,1]-1)/2)+2,0,3)
    sym_X_test = aux.astype(int)
    # Y polarization
    aux = 4*np.clip(np.round((Y_test[:,2]-1)/2)+2,0,3)+np.clip(np.round((Y_test[:,3]-1)/2)+2,0,3)
    sym_Y_test = aux.astype(int)
    
    # X polarization hat
    aux = 4*np.clip(np.round((Y_test_hat[:,0]-1)/2)+2,0,3)+np.clip(np.round((Y_test_hat[:,1]-1)/2)+2,0,3)
    sym_X_test_Multisym = aux.astype(int)
    # Y polarization hat
    aux = 4*np.clip(np.round((Y_test_hat[:,2]-1)/2)+2,0,3)+np.clip(np.round((Y_test_hat[:,3]-1)/2)+2,0,3)
    sym_Y_test_Multisym = aux.astype(int)
    
    BER = (sum(sym_X_test!=sym_X_test_Multisym)/len(sym_X_test)+sum(sym_Y_test!=sym_Y_test_Multisym)/len(sym_Y_test))/8
    return BER

# Preenchimento da matriz data_real
data_real = np.zeros([len(power_text), m, n])

for counter, power_counter in enumerate(power_text):
    for file_counter in files:
        # Verifica se não é arquivo oculto e se contém os nomes necessários
        if file_counter[0] != '.':
            if ('400gbps_RealConstellationDiagram' in file_counter) and (power_text[counter] in file_counter):
                path_real_file = path_data_folder + '/' + file_counter
                print('\tLoading:', path_real_file)
                
                df_real = pd.read_csv(path_real_file, skiprows=1)
                data_real_aux = df_real.to_numpy()
                data_real[counter, :, :] = data_real_aux


# In[8]:


# importação das bibliotecas necessárias
import numpy as np
import pandas as pd # leitura dos dados
from matplotlib import pyplot as plt # plotagem dos gráficos
import os

def BER(X_test, Y_test):
    Y_test_hat = X_test
    # X polarization
    aux = 4*np.clip(np.round((Y_test[:,0]-1)/2)+2,0,3)+np.clip(np.round((Y_test[:,1]-1)/2)+2,0,3)
    sym_X_test = aux.astype(int)
    # Y polarization
    aux = 4*np.clip(np.round((Y_test[:,2]-1)/2)+2,0,3)+np.clip(np.round((Y_test[:,3]-1)/2)+2,0,3)
    sym_Y_test = aux.astype(int)

    # Detection of the real symbols
    # X polarization
    aux = 4*np.clip(np.round((Y_test_hat[:,0]-1)/2)+2,0,3)+np.clip(np.round((Y_test_hat[:,1]-1)/2)+2,0,3)
    sym_X_test_Multisym = aux.astype(int)
    # Y polarization
    aux = 4*np.clip(np.round((Y_test_hat[:,2]-1)/2)+2,0,3)+np.clip(np.round((Y_test_hat[:,3]-1)/2)+2,0,3)
    sym_Y_test_Multisym = aux.astype(int)

    # BER calculation
    BER_val = (sum(sym_X_test!=sym_X_test_Multisym)/len(sym_X_test)+sum(sym_Y_test!=sym_Y_test_Multisym)/len(sym_Y_test))/8
    return BER_val

# --- AJUSTE DE CAMINHOS ---
distance_text = '120km'

# Caminho base do ambiente local
base_path = r'C:\Users\User\Desktop\Iniciação Científica 2025-2026'

# Caminho final da pasta (compatível com a Opção 2 que você aplicou)
path_data_folder = base_path + r'\Dados_' + distance_text

# Carregamento do dado Ideal
# Ajuste com a barra invertida para Windows
ideal_file = path_data_folder + r'\400gbps_IdealConstellationDiagram_ref_' + distance_text + '.csv'
print(f"Lendo arquivo ideal: {ideal_file}")

# Leitura seguindo a lógica (transposta)
ideal_data = np.transpose(pd.read_csv(ideal_file, sep=',', skiprows=1).values)

# Atualizado para abranger os dados até 20 dBm presentes na sua pasta
powers = list(range(21))  
ber_values = []

for p in powers:
    # Ajuste do nome do arquivo real para o padrão local (com a barra invertida)
    real_file = path_data_folder + r'\400gbps_RealConstellationDiagram_' + str(p) + 'dbm_' + distance_text + '.csv'

    if os.path.exists(real_file):
        print(f"Processando: {p}dBm")
        real_data = np.transpose(pd.read_csv(real_file, sep=',', skiprows=1).values)

        # Retorna ao formato original antes da função
        ber = BER(real_data.T, ideal_data.T)
        ber_values.append(ber)
    else:
        print(f"Aviso: Arquivo não encontrado para {p}dBm")

print("\nBER values:", ber_values)

# Plot
plt.figure(figsize=(8, 6))
plt.semilogy(powers[:len(ber_values)], ber_values, 'o-')
plt.xlabel('Power (dBm)')
plt.ylabel('BER')
plt.title(f'BER vs Power for {distance_text}')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()


# In[10]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import pickle

# --- DEFINIÇÃO DE CAMINHOS ---
distance_text = '120km'

# Caminho base do ambiente local
base_path = r'C:\Users\User\Desktop\Iniciação Científica 2025-2026'
# Caminho final da pasta
path_data_folder = base_path + r'\Dados_' + distance_text

print('The selected data folder is:', path_data_folder)

# --- CARREGAMENTO DOS DADOS IDEAIS ---
# Ajuste com a barra invertida para Windows
path_ideal_file = path_data_folder + r'\400gbps_IdealConstellationDiagram_ref_' + distance_text + '.csv'

# CORREÇÃO CRÍTICA: Lógica de importação idêntica ao código 3
# O .values converte para numpy, np.transpose inverte e .T volta para o shape original
# Isso garante que a ordem das colunas e a escala não sejam alteradas pelo Pandas
df_ideal = pd.read_csv(path_ideal_file, skiprows=1)
data_ideal = np.transpose(df_ideal.values).T

m, n = np.shape(data_ideal)

# --- CARREGAMENTO DAS CONSTELAÇÕES DISTORCIDAS ---
power_array = np.arange(0, 21, 1)
power_text = [f'Diagram_{p}dbm_' for p in power_array]
files = os.listdir(path_data_folder)

data_real = np.zeros([len(power_text), m, n])

for counter, p_text in enumerate(power_text):
    for file_counter in files:
        if file_counter[0] != '.':
            if ('400gbps_RealConstellationDiagram' in file_counter) and (p_text in file_counter):
                # Ajuste da barra para juntar a pasta com o nome do arquivo lido
                path_real_file = path_data_folder + '\\' + file_counter
                
                # CORREÇÃO: Mesma transposição para os dados reais
                df_real = pd.read_csv(path_real_file, skiprows=1)
                data_real_aux = np.transpose(df_real.values).T
                data_real[counter, :, :] = data_real_aux

# --- CÁLCULO DA BER ---
signal_ID_array = np.arange(0, len(power_array))
BER_ML_array = np.zeros(len(signal_ID_array))

for counter_ID, signal_ID in enumerate(signal_ID_array):

    # Seleção dos dados para a potência atual
    current_ideal = data_ideal
    current_real = data_real[signal_ID, :, :]

    # Labels Ideais (Onde o símbolo DEVERIA estar)
    # Mudamos para a fórmula exata do Código 3: (x-1)/2 + 2
    # X polarization
    sym_X_ideal = 4*np.clip(np.round((current_ideal[:,0]-1)/2)+2,0,3) + np.clip(np.round((current_ideal[:,1]-1)/2)+2,0,3)
    # Y polarization
    sym_Y_ideal = 4*np.clip(np.round((current_ideal[:,2]-1)/2)+2,0,3) + np.clip(np.round((current_ideal[:,3]-1)/2)+2,0,3)

    # Detecção nos dados REAIS (Onde o símbolo REALMENTE caiu)
    # X polarization
    sym_X_real = 4*np.clip(np.round((current_real[:,0]-1)/2)+2,0,3) + np.clip(np.round((current_real[:,1]-1)/2)+2,0,3)
    # Y polarization
    sym_Y_real = 4*np.clip(np.round((current_real[:,2]-1)/2)+2,0,3) + np.clip(np.round((current_real[:,3]-1)/2)+2,0,3)

    # Cálculo da BER (Média das duas polarizações dividida por 8 bits por símbolo total)
    BER_X = np.sum(sym_X_real != sym_X_ideal.astype(int)) / len(sym_X_ideal)
    BER_Y = np.sum(sym_Y_real != sym_Y_ideal.astype(int)) / len(sym_Y_ideal)

    BER_ML_array[counter_ID] = (BER_X + BER_Y) / 8
    print(f'Power {power_array[signal_ID]} dBm | BER: {BER_ML_array[counter_ID]:.2e}')

# --- PLOTAGEM ---
plt.figure(figsize=(8, 5))
plt.semilogy(power_array, BER_ML_array, 'o-')
plt.grid(True, which="both", ls="-")
plt.xlabel('Power (dBm)')
plt.ylabel('BER')
plt.title(f'BER vs Power - {distance_text} (Corrigido)')
plt.show()


# # **2. Processamento K-Means + GMM**

# ## **K-Means + GMM para aplicação no MLP**

# In[ ]:


# Supostamente consertado

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans           # Necessário para o passo 1
from sklearn.mixture import GaussianMixture  # Necessário para o passo 2
from numpy.matlib import repmat

plt.rcParams.update({'font.size': 16})  # Configuração de fonte

# Dicionários para armazenar os resultados
ber_no_clust_results = {}
ber_clust_results = {}

# Inicializamos o tensor para guardar os símbolos estimados de todos os sinais
# Assumimos que 'data_real' já existe no ambiente (formato [Sinais, Amostras, 4])
estimated_symbols_tensor = np.zeros(np.shape(data_real))
# ------------------------------------


# Loop para signal_ID variando de 0 a 12 (conforme seu snippet)
for signal_ID in range(5, 17):
    print(f"Rodando para signal_ID = {signal_ID} dBm...")


    # Geração dos rótulos ideais
    sym_X = np.round((data_ideal[:, 0] + 3) / 2) * 4 + np.round((data_ideal[:, 1] + 3) / 2)
    sym_Y = np.round((data_ideal[:, 2] + 3) / 2) * 4 + np.round((data_ideal[:, 3] + 3) / 2)
    sym_XY = sym_X * 16 + sym_Y

    # Matrizes de entrada e saída
    X_X = data_real[signal_ID, :, :2]
    X_Y = data_real[signal_ID, :, 2:]
    X = data_real[signal_ID, :, :]

    # Detecção sem clustering (MLP/Threshold simples)
    X_X_dig = 4 * np.clip(np.round((X_X[:, 0] - 1) / 2) + 2, 0, 3) + np.clip(np.round((X_X[:, 1] - 1) / 2) + 2, 0, 3)
    sym_X_ML = X_X_dig.astype(int)
    BER_X_ML = (sum(sym_X_ML != sym_X) / len(sym_X)) / 4

    X_Y_dig = 4 * np.clip(np.round((X_Y[:, 0] - 1) / 2) + 2, 0, 3) + np.clip(np.round((X_Y[:, 1] - 1) / 2) + 2, 0, 3)
    sym_Y_ML = X_Y_dig.astype(int)
    BER_Y_ML = (sum(sym_Y_ML != sym_Y) / len(sym_Y)) / 4

    BER_no_clust = (BER_X_ML + BER_Y_ML) / 2
    print(f'  Média BER sem clustering: {BER_no_clust}')
    ber_no_clust_results[signal_ID] = BER_no_clust

    # Inicialização "Ideal" (init0)
    init0 = np.zeros((16 * 16, 4))
    aux0 = np.array([0, 1, 2, 3] * 16 * 4)
    aux1 = np.array(([0] * 4 + [1] * 4 + [2] * 4 + [3] * 4) * 16)
    aux2 = np.array(([0] * 16 + [1] * 16 + [2] * 16 + [3] * 16) * 4)
    aux3 = np.array(([0] * 16 * 4 + [1] * 16 * 4 + [2] * 16 * 4 + [3] * 16 * 4))
    init0[:, 0] = aux0 * 2 - 3
    init0[:, 1] = aux1 * 2 - 3
    init0[:, 2] = aux2 * 2 - 3
    init0[:, 3] = aux3 * 2 - 3

    # --- PASSO 1: K-MEANS ---
    # Usamos o init0 (ideal) para guiar o K-Means
    kmeans_X = KMeans(
        n_clusters=16 * 16,
        random_state=0,
        n_init=1,
        init=init0  # Começa do ideal
    ).fit(X)

    # Extraímos os centróides que o K-Means encontrou
    kmeans_centroids = kmeans_X.cluster_centers_

    # --- PASSO 2: GMM (Gaussian Mixture Model) ---
    # Inicializamos o GMM com os centróides JÁ AJUSTADOS pelo K-Means
    gmm_X = GaussianMixture(
        n_components=16 * 16,
        random_state=0,
        n_init=1,
        means_init=kmeans_centroids,  # Começa de onde o K-Means parou
        covariance_type='full'        # Permite ajustar a elipticidade
    ).fit(X)

    # Pegamos os resultados finais do GMM
    cluster_ID = gmm_X.predict(X)
    gmm_centroids = gmm_X.means_

#-----------------------------------------------------#

    # Cria a matriz temporária para a potência atual
    estimated_symbols = np.zeros(np.shape(X))

    # Mapeia cada amostra para o seu centróide GMM correspondente
    # O cluster_ID diz qual é o grupo, o gmm_centroids dá a coordenada desse grupo
    for counter, cluster_idx in enumerate(cluster_ID):
        estimated_symbols[counter, :] = np.round(gmm_centroids[cluster_idx, :])

    # Salva no tensor global para o Código B usar depois
    estimated_symbols_tensor[signal_ID, :, :] = estimated_symbols
#-----------------------------------------------------#

    # Conversão de clusters para BER
    sym_cluster = np.zeros(len(sym_XY))
    for cluster_ind in range(16 * 16):
        ind = np.where(cluster_ind == cluster_ID)[0]
        if len(ind) > 0:
            sym_aux = int(np.median(sym_XY[ind]))
            sym_cluster[ind] = sym_aux * np.ones(len(ind))

    BER_clust = (sum(sym_XY != sym_cluster) / len(sym_XY)) / 8
    print(f'  Média BER com GMM (Init KMeans): {BER_clust}')
    ber_clust_results[signal_ID] = BER_clust



# Exibir os resultados ao final do loop
print("\nResumo dos BERs (GMM inicializado por K-Means):")
for signal_ID in range(5, 13):
    print(f"  {signal_ID} dBm -> BER sem clustering: {ber_no_clust_results[signal_ID]:.6f}, BER Final: {ber_clust_results[signal_ID]:.6f}")

## Exibe os gráficos de maneira sobreposta
signal_powers = list(ber_no_clust_results.keys())
ber_no_clust = [ber_no_clust_results[pid] for pid in signal_powers]
ber_clust = [ber_clust_results[pid] for pid in signal_powers]

#plt.figure(figsize=(10, 6))
#plt.semilogy(signal_powers, ber_no_clust, 'o-', label='Sem Clustering')
#plt.semilogy(signal_powers, ber_clust, '^-', label='Com GMM (Init K-Means)', color='green')
#plt.title('BER vs Potência do Sinal (Híbrido K-Means + GMM)')
#plt.xlabel('Potência (dBm)')
#plt.ylabel('Bit Error Ratio (BER)')
#plt.grid(True, which='both')
#plt.legend()
#plt.tight_layout()


# In[ ]:


# --- BLOCO DE CÓDIGO 4: PLOTAGEM DOS RESULTADOS DE CLUSTERIZAÇÃO ---

# Extração dos dados dos dicionários para listas (garantindo a ordem das potências)
signal_powers = sorted(ber_no_clust_results.keys())
ber_no_clust = [ber_no_clust_results[p] for p in signal_powers]
ber_clust = [ber_clust_results[p] for p in signal_powers]

plt.figure(figsize=(12, 7))

# Plotagem da BER sem clustering (referência do código anterior)
plt.semilogy(signal_powers, ber_no_clust, 'o--', color='red', label='Detecção ML (Sem Clustering)', alpha=0.7)

# Plotagem da BER com a clusterização Híbrida (K-Means + GMM)
plt.semilogy(signal_powers, ber_clust, 's-', color='blue', linewidth=2, label='Clusterização (K-Means + GMM)')

# Configurações estéticas do gráfico
plt.title(f'BER vs Potência do Sinal - Distância: {distance_text}', fontsize=18)
plt.xlabel('Potência de Lançamento (dBm)', fontsize=14)
plt.ylabel('Bit Error Ratio (BER)', fontsize=14)

# Definir limites para visualização clássica de BER
plt.ylim([1e-7, 1])
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend(loc='best', fontsize=12)


plt.tight_layout()

# Salvar o gráfico final
plt.savefig(f'Comparativo_BER_Clustering_{distance_text}.png', dpi=300)
plt.show()

print(f"\nGráfico gerado com sucesso para a distância de {distance_text}!")
print("Os valores foram comparados entre a detecção padrão e o refinamento via GMM.")


# # **MLP não supervisionado para diversas potências (loop)**

# In[ ]:


import time
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

# implementa uma simulação de rede neural (MLP) para avaliar a taxa de erro de bits (BER) de sinais em diferentes níveis de potência óptica,
# usando diferentes configurações de quantidade de símbolos simultâneos e número de neurônios.
# O objetivo é treinar modelos para prever sinais ideais com base em sinais reais recebidos em diferentes condições.

# ------------------------ #
# Basic configurations

# quantidade de símbolos a serem processados por execução -> reduzimos de 2^18 para 200.000
Nsym = 200000                                  # Number of processed symbols

# quantas vezes repetir a simulação
# Número de vezes que cada configuração será testada
Nrepetitions = 10                              # Number of repetitions

# define quantos símbolos simultâneos (ou seja, em sequência) serão usados como entrada na rede neural.
# a rede pode aprender padrões mais complexos ou relações de dependência entre símbolos próximos
NsymSim_array = np.array([7]) # Simultaneously processed symbols

##### MUDEI AQUI EM CIMA PARA 1

# Um vetor que define o número de neurônios na rede neural, variando de 10 a 250 em incrementos de 10.
neuron_number_array = np.arange(10,310,10)     # Number of neurons
#neuron_number_array = np.arange(10,30,10)     # Number of neurons

# O número de neurônios na camada oculta controla a capacidade de aprendizado da rede.
# Mais neurônios -> maior capacidade de modelar padrões complexos, mas também maior risco de overfitting e maior custo computacional.
# ------------------------ #

# ========================================== #
# NOVO LOOP DAS POTÊNCIAS (ÍNDICES 5 A 12)
# ========================================== #
signal_IDs_to_process = range(5, 13)

# Calculation of the number of runs
# Calcula o total de execuções que a simulação fará agora multiplicando também pelas potências
number_of_runs = len(signal_IDs_to_process) * Nrepetitions * len(NsymSim_array) * len(neuron_number_array)
print('The number of runs is:', number_of_runs)

counter_iter = 0  # Counter for total number of runs

# ADAPTAÇÃO NECESSÁRIA: Adicionada a dimensão len(signal_IDs_to_process) no início do tensor
# para guardar os resultados de todas as potências sem sobrescrever.
BER_tensor_blind = np.zeros([len(signal_IDs_to_process), len(NsymSim_array), len(neuron_number_array), Nrepetitions])

# Loop externo iterando sobre as potências escolhidas
for counter_p, signal_ID in enumerate(signal_IDs_to_process):

    print('\n======================================================')
    print('Processing power level:', power_array[signal_ID], 'dBm')
    print('The signal to be processed is:', power_text[signal_ID])
    print('======================================================\n')

    # Iterate over the number of symbols (1 symbol, 3 symbols, 5 symbols...)
    # Loop que varia a quantidade de símbolos simultâneos utilizados
    for counter_sym, NsymSim in enumerate(NsymSim_array):

        # Iterate over the number of neurons (10 neurons, 20 neurons...)
        for counter_neuron_number, neuron_number in enumerate(neuron_number_array):
        # Segundo loop: varia o número de neurônios ocultos da rede neural
            print('Power level =',power_array[signal_ID],'Nsym =',NsymSim,'Neuron number =',neuron_number,'Iteration:',counter_iter+1,'(',number_of_runs,')')
            # Imprime informações sobre a simulação atual

            # Iterate over the repetitions
            # Esse loop serve para repetir o mesmo experimento várias (20) vezes
            for counter_rep in range(Nrepetitions):
                counter_iter += 1

                # Initialize the timer
                # o timer serve para ver quanto tempo a rede demora pra treinar)
                start_time = time.time() # armazena o tempo inicial

                # The raw data for the particular power level
                # Seleciona os dados reais (X) e ideais (Y) para o nível de potência atual
                X = data_real[signal_ID,:,:]
                Y = estimated_symbols_tensor[signal_ID,:,:]

                # We build the input and output matrices

                # Input matrix extended
                # Cria a matriz de entrada estendida X_ext, considerando 4 componentes por símbolo.
                X_ext = np.zeros([Nsym,4*NsymSim])
                for counter in range(NsymSim):
                    ind_i = counter         # Initial index
                    ind_f = Nsym+counter    # Final index
                    X_ext[:,counter*4:counter*4+4] = X[ind_i:ind_f,:]


                # Output matrix
                counter = int(np.floor(NsymSim/2))
                ind_i = counter              # Initial index
                ind_f = Nsym+counter         # Final index
                Y_ext = Y[ind_i:ind_f,:]
                # Não entendi também essa parte

                # Processing of multiple symbols
                #scaler = preprocessing.StandardScaler().fit(X_ext)
                #X_ext = scaler.transform(X_ext)

                # Split train-test (configure the splitting ratio)
                # Divide os dados em 50% para treino e 50% para teste
                X_train, X_test, Y_train, Y_test = train_test_split(X_ext,Y_ext,test_size=0.5)

                # Generate the model (in this case an MLP regressor)
                ## Cria a rede neural MLP com a quantidade de neurônios definida e função de ativação ReLU.
                ## RELU = quão importante é a saída daquele neurônio ???
                clf = MLPRegressor(random_state=1, hidden_layer_sizes=(neuron_number,), max_iter=1000, activation = 'relu')
                # ReLU (Rectified Linear Unit) é uma função de ativação amplamente utilizada em redes neurais.
                # Se o valor de entrada for positivo, ReLU retorna o próprio valor.
                # Se o valor de entrada for negativo, ReLU retorna 0.

                # Train the model (with training data)
                clf.fit(X_train, Y_train)
                ## treina a rede neural MLP com a quantidade de neurônios definida e função de ativação ReLU.

                ############## The test should be done with respect to the original data ############################
                Y_original = data_ideal
                Y_original_ext = Y_original[ind_i:ind_f,:]

                # Predict the values
                Y_hat = clf.predict(X_ext)
                ## Usa a rede treinada para prever a saída com os dados de teste.

                # Detection of the ideal symbols
                # X polarization
                aux = 4*np.clip(np.round((Y_original_ext[:,0]-1)/2)+2,0,3)+np.clip(np.round((Y_original_ext[:,1]-1)/2)+2,0,3)
                sym_X_test = aux.astype(int)
                # Y polarization
                aux = 4*np.clip(np.round((Y_original_ext[:,2]-1)/2)+2,0,3)+np.clip(np.round((Y_original_ext[:,3]-1)/2)+2,0,3)
                sym_Y_test = aux.astype(int)

                # Detection of the real symbols with multiple symbol
                # X polarization
                aux = 4*np.clip(np.round((Y_hat[:,0]-1)/2)+2,0,3)+np.clip(np.round((Y_hat[:,1]-1)/2)+2,0,3)
                sym_X_test_Multisym = aux.astype(int)
                # Y polarization
                aux = 4*np.clip(np.round((Y_hat[:,2]-1)/2)+2,0,3)+np.clip(np.round((Y_hat[:,3]-1)/2)+2,0,3)
                sym_Y_test_Multisym = aux.astype(int)

                # Corrected to calculate BER instead of SER
  

                BER = (sum(sym_X_test!=sym_X_test_Multisym)/len(sym_X_test)+sum(sym_Y_test!=sym_Y_test_Multisym)/len(sym_Y_test))/8
                # Guarda o valor do BER calculado para essa repetição, com esse número de neurônios e número de símbolos simultâneos.
                end_time = time.time()
                # mede o tempo decorrido da repetição — o quanto demorou para treinar e testar a rede neural
                elapsed_time = end_time - start_time
                print('\t Repetion =',counter_rep,'[',power_array[signal_ID],'',NsymSim,'',neuron_number,'',counter_rep,'], BER:',BER,'(Elapsed time:',elapsed_time,')')

                # Salvando no tensor usando o novo índice `counter_p`
                BER_tensor_blind[counter_p, counter_sym, counter_neuron_number, counter_rep] = BER


# ## Análise numérica dos resultados (5 a 12 dBm)

# In[ ]:


import numpy as np
import csv

print("======================================================")
print("MÉDIAS DO MÉTODO MLP COM K-MEANS + GMM (Análise por Potência)")
print("======================================================")

# Dicionários opcionais para guardar o melhor resultado de cada potência
melhores_neuronios_por_potencia = {}
melhores_bers_por_potencia = {}

# Loop varrendo as potências que processamos (índices 5 a 12)
for counter_p, signal_ID in enumerate(signal_IDs_to_process):

    potencia_atual = power_array[signal_ID]
    print(f"\n\n---> ANÁLISE PARA A POTÊNCIA: {potencia_atual} dBm <---")

    # Extrai os valores de BER para a potência atual (counter_p) e
    # para o único valor de NsymSim que usamos (índice 0).
    # O resultado volta a ser uma matriz 2D: (n_neuronios, n_repeticoes)
    BER_dados_reais = BER_tensor_blind[counter_p, 0, :, :]

    # 1) Média geral de todas as BERs desta potência
    media_geral_ber = np.mean(BER_dados_reais)
    print(f"\n1) Média geral de todas as BERs (repetições): {media_geral_ber:.4e}")

    # 2) Média da BER por número de neurônios (média sobre as repetições)
    medias_ber_por_neuronio = np.mean(BER_dados_reais, axis=1)  # shape: (n_neuronios,)

    # Encontrar o índice da menor média para essa potência
    indice_melhor_neuronio = np.argmin(medias_ber_por_neuronio)
    melhor_neuronio = neuron_number_array[indice_melhor_neuronio]
    melhor_media_ber = medias_ber_por_neuronio[indice_melhor_neuronio]

    print(f"\n2) Melhor configuração para {potencia_atual} dBm:")
    print(f"   Melhor número de neurônios: {melhor_neuronio}")
    print(f"   Melhor média de BER: {melhor_media_ber:.5e}")

    # Salva para uso futuro (ex: plotar um gráfico)
    melhores_neuronios_por_potencia[potencia_atual] = melhor_neuronio
    melhores_bers_por_potencia[potencia_atual] = melhor_media_ber

    # 3) Exibir todas as médias individuais por número de neurônios
    print("\n3) Médias individuais de BER por número de neurônios:")
    for i, n_neuronios in enumerate(neuron_number_array):
        media_ber = medias_ber_por_neuronio[i]
        print(f"   {n_neuronios} neurônios: {media_ber:.4e}")

print("\n======================================================")
print("Análise concluída para todas as potências!")
print("Melhores BERs encontradas por potência:", melhores_bers_por_potencia)

