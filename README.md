# Portfólio de Projetos - Processo Seletivo Nubank

Olá! Este repositório foi criado para compartilhar dois códigos que desenvolvi durante minha graduação em Engenharia Eletrônica e de Telecomunicações na UNESP. 

### 1. Machine Learning para Processamento de Sinais (Iniciação Científica - FAPESP)
**Arquivo:** `IC_K_means+GMM_400Gbps_120km_.ipynb` 

Este código faz parte da minha pesquisa focada na mitigação de ruídos e compensação de efeitos não lineares em sistemas de comunicação coerentes de alta capacidade (como links de 400 Gbps). 
O script integra algoritmos de aprendizado não supervisionado (**K-means** e **GMM** - *Gaussian Mixture Models*) para clusterização prévia dos dados, operando em conjunto com Redes Neurais (**MLP** - *Multilayer Perceptron*) para processar e corrigir as distorções do sinal. É uma aplicação direta de Inteligência Artificial para otimização de sistemas e tratamento de dados complexos.

### 2. Projeto Final de Sistemas de Comunicação Digital (SCD)
**Arquivo:** `projeto_scd.py`

Projeto final desenvolvido para a disciplina de Sistemas de Comunicações Digitais. Consiste na implementação em Python de um link de comunicação completo (ponta a ponta).
O código simula toda a cadeia de transmissão de dados:
* **Transmissor:** Conversão de texto para bits, mapeamento de símbolos e formatação de pulso.
* **Canal:** Simulação de transmissão com inserção de ruído branco (AWGN) e efeitos de dispersão.
* **Receptor:** Sincronização, equalização, filtragem e decodificação para a reconstrução exata da mensagem de texto original.

---
*Fique à vontade para explorar os códigos!*
