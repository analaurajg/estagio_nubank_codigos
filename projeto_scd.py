import numpy as np
import matplotlib.pyplot as plt
import json
from scipy.special import erfc
from scipy.signal import butter, filtfilt
np.set_printoptions(linewidth=np.inf)

# ==========================================
# CONFIGURAÇÃO DA SIMULAÇÃO (VIA ARQUIVO EXTERNO)
# ==========================================

input_text = "A long time ago, in a galaxy far, far, away... A vast sea of stars serves as the backdrop for the main title. War drums echo through the heavens as a rollup slowly crawls into infinity. It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the Death Star, an armored space station with enough power to destroy an entire planet. Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy... The awesome yellow planet of Tatooine emerges from a total eclipse, her two moons glowing against the darkness. A tiny silver spacecraft, a Rebel Blockade Runner firing lasers from the back of the ship, races through space. It is pursed by a giant Imperial Stardestroyer. Hundreds of deadly laserbolts streak from the Imperial Stardestroyer, causing the main solar fin of the Rebel craft to disintegrate. INT. REBEL BLOCKADE RUNNER - MAIN PASSAGEWAY An explosion rocks the ship as two robots, Artoo-Detoo (R2- D2) and See-Threepio (C-3PO) struggle to make their way through the shaking, bouncing passageway. Both robots are old and battered. Artoo is a short, claw-armed tripod. His face is a mass of computer lights surrounding a radar eye. Threepio, on the other hand, is a tall, slender robot of human proportions. He has a gleaming bronze-like metallic surface of an Art Deco design. Another blast shakes them as they struggle along their way. THREEPIO Did you hear that? They've shut down the main reactor. We'll be destroyed for sure. This is madness! Rebel troopers rush past the robots and take up positions in the main passageway. They aim their weapons toward the door. THREEPIO We're doomed! The little R2 unit makes a series of electronic sounds that only another robot could understand. THREEPIO There'll be no escape for the Princess this time. Artoo continues making beeping sounds. Tension mounts as loud metallic latches clank and the scream of heavy equipment are heard moving around the outside hull of the ship. THREEPIO What's that? EXT. SPACECRAFT IN SPACE The Imperial craft has easily overtaken the Rebel Blockade Runner. The smaller Rebel ship is being drawn into the underside dock of the giant Imperial starship. INT. REBEL BLOCKADE RUNNER The nervous Rebel troopers aim their weapons. Suddenly a tremendous blast opens up a hole in the main passageway and a score of fearsome armored spacesuited stormtroopers make their way into the smoke-filled corridor. In a few minutes the entire passageway is ablaze with laserfire. The deadly bolts ricochet in wild random patterns creating huge explosions. Stormtroopers scatter and duck behind storage lockers. Laserbolts hit several Rebel soldiers who scream and stagger through the smoke, holding shattered arms and faces. An explosion hits near the robots. THREEPIO I should have known better than to trust the logic of a half-sized thermocapsulary dehousing assister... Artoo counters with an angry rebuttal as the battle rages around the two hapless robots. EXT. TATOOINE - DESERT WASTELAND - DAY A death-white wasteland stretches from horizon to horizon. The tremendous heat of two huge twin suns settle on a lone figure, Luke Skywalker, a farm boy with heroic aspirations who looks much younger than his eighteen years. His shaggy hair and baggy tunic give him the air of a simple but lovable lad with a prize-winning smile. A light wind whips at him as he adjusts several valves on a large battered moisture vaporator which sticks out of the desert floor much like an oil pipe with valves. He is aided by a beatup tread-robot with six claw arms. The little robot appears to be barely functioning and moves with jerky motions. A bright sparkle in the morning sky catches Luke's eye and he instinctively grabs a pair of electrobinoculars from his utility belt. He stands transfixed for a few moments studying the heavens, then dashed toward his dented, crudely repaired Landspeeder (an auto-like transport that travels a few feet above the ground on a magnetic-field). He motions for the tiny robot to follow him. LUKE Hurry up! Come with me! What are you waiting for?! Get in gear! The robot scoots around in a tight circle, stops short, and smoke begins to pour out of every joint. Luke throws his arms up in disgust. Exasperated, the young farm boy jumps into his Landspeeder leaving the smoldering robot to hum madly. INT. REBEL BLOCKADE RUNNER - MAIN HALLWAY The awesome, seven-foot-tall Dark Lord of the Sith makes his way into the blinding light of the main passageway. This is Darth Vader, right hand of the Emperor. His face is obscured by his flowing black robes and grotesque breath mask, which stands out next to the fascist white armored suits of the Imperial stormtroopers. Everyone instinctively backs away from the imposing warrior and a deathly quiet sweeps through the Rebel troops. Several of the Rebel troops break and run in a frenzied panic. INT. REBEL BLOCKADE RUNNER A woman's hand puts a card into an opening in Artoo's dome. Artoo makes beeping sounds. INT. REBEL BLOCKADE RUNNER Threepio stands in a hallway, somewhat bewildered. Artoo is nowhere in sight. The pitiful screams of the doomed Rebel soldiers can be heard in the distance. THREEPIO Artoo! Artoo-Detoo, where are you? A familiar clanking sound attacks Threepio's attention and he spots little Artoo at the end of the hallway in a smoke- filled alcove. A beautiful young girl (about sixteen years old) stands in front of Artoo. Surreal and out of place, dreamlike and half hidden in the smoke, she finishes adjusting something on Artoo's computer face, then watches as the little robot joins his companion. THREEPIO At last! Where have you been? Stormtroopers can be heard battling in the distance. THREEPIO They're heading in this direction. What are we going to do? We'll be sent to the spice mine of Kessel or smashed into who knows what! Artoo scoots past his bronze friend and races down the subhallway. Threepio chases after him. THREEPIO Wait a minute, where are you going? Artoo responds with electronic beeps. INT. REBEL BLOCKADE RUNNER - CORRIDOR The evil Darth Vader stands amid the broken and twisted bodies of his foes. He grabs a wounded Rebel Officer by the neck as an Imperial Officer rushes up to the Dark Lord. IMPERIAL OFFICER The Death Star plans are not in the main computer. Vader squeezes the neck of the Rebel Officer, who struggles in vain. VADER Where are those transmissions you intercepted? Vader lifts the Rebel off his feet by his throat. VADER What have you done with those plans? REBEL OFFICER We intercepted no transmissions. Aaah... This is a consular ship. Were on a diplomatic mission. VADER If this is a consular ship... were is the Ambassador? The Rebel refuses to speak but eventually cries out as the Dark Lord begins to squeeze the officer's throat, creating a gruesome snapping and choking, until the soldier goes limp. Vader tosses the dead soldier against the wall and turns to his troops. VADER Commander, tear this ship apart until you've found those plans and bring me the Ambassador. I want her alive! The stormtroopers scurry into the subhallways. INT. REBEL BLOCKADE RUNNER - SUBHALLWAY The lovely young girl huddles in a small alcove as the stormtroopers search through the ship. She is Princess Leia Organa, a member of the Alderaan Senate. The fear in her eyes slowly gives way to anger as the muted crushing sounds of the approaching stormtroopers grow louder. One of the troopers spots her. TROOPER There she is! Set for stun! Leia steps from her hiding place and blasts a trooper with her laser pistol. She starts to run but is felled by a paralyzing ray. The troopers inspect her inert body. TROOPER She'll be all right. Inform Lord Vader we have a prisoner. INT. REBEL BLOCKADE RUNNER - SUBHALLWAY Artoo stops before the small hatch of an emergency lifepod. He snaps the seal on the main latch."

# 1. Carrega o dicionário diretamente do arquivo JSON
try:
    with open('config (1).json', 'r') as arquivo:
        config = json.load(arquivo)
except FileNotFoundError:
    raise FileNotFoundError("Arquivo 'config.json' não encontrado! Verifique se ele está na mesma pasta do script.")

# 2. Cálculo dinâmico do 'span'
if config['roll_off'] > 0:
    config['span'] = max(6, int(3 / config['roll_off']))
else:
    config['span'] = 50

# ==========================================
# 1. FUNÇÕES DE CONVERSÃO (TEXTO <-> BITS)
# ==========================================

def text_to_bits(text):
    bits = []
    for char in text:
        bin_str = format(ord(char), '08b')
        bits.extend([int(b) for b in bin_str])
    return np.array(bits)

def bits_to_text(bits_array):
    text_chars = []
    for i in range(0, len(bits_array), 8):
        byte_array = bits_array[i:i+8]
        byte_str = "".join(byte_array.astype(str))
        ascii_val = int(byte_str, 2)
        text_chars.append(chr(ascii_val))
    return "".join(text_chars)

def formatar_titulo(mod_format, M=None, pulse_type=None):
    """
    Padroniza títulos acadêmicos: exibe '16-QAM RRC' ou 'BPSK NRZ'.
    """
    # Formata a modulação
    if mod_format == 'polar':
        mod_str = "BPSK"
    else:
        tipo = mod_format.replace('m', '').upper()
        mod_str = f"{M}-{tipo}" if M else tipo
    
    # Adiciona o pulso se estiver presente
    if pulse_type:
        return f"{mod_str} {pulse_type.upper()}"
    return mod_str

# ==========================================
# 2. FUNÇÕES DE SHUFFLING (EMBARALHAMENTO)
# ==========================================

def shuffle_bits(bits_array, seed=42):
    rng = np.random.RandomState(seed)
    permutation_indices = rng.permutation(len(bits_array))
    shuffled_bits = bits_array[permutation_indices]
    return shuffled_bits, permutation_indices

def deshuffle_bits(shuffled_bits, permutation_indices):
    inverse_indices = np.argsort(permutation_indices)
    unshuffled_bits = shuffled_bits[inverse_indices]
    return unshuffled_bits

# ==========================================
# 3. FUNÇÕES DE MAPEAMENTO (BITS <-> SÍMBOLOS)
# ==========================================

def mapping(bits, mod_format='polar', M=2):
    """
    Converte um array de bits em símbolos usando if/elif para o Mod_format.
    Suporta: 'polar' (M=2), 'mPAM' (M=4, 8) e 'mQAM' (M=4, 16).
    """
    # Número de bits por símbolo: k = log2(M)
    k = int(np.log2(M))
    
    # Garante que a quantidade de bits seja múltipla de 'k'
    sobra = len(bits) % k
    if sobra != 0:
        zeros_faltantes = k - sobra
        bits = np.append(bits, np.zeros(zeros_faltantes, dtype=int))
        
    simbolos = []
    
    # ----------------------------------------------------
    # 1. MODULAÇÃO BINÁRIA (POLAR)
    # ----------------------------------------------------
    if mod_format == 'polar':
        return 2 * bits - 1

    # ----------------------------------------------------
    # 2. MODULAÇÃO MULTINÍVEL (mPAM)
    # ----------------------------------------------------
    elif mod_format == 'mPAM':
        if M == 4:
            tabela = {(0,0): -3, (0,1): -1, (1,1): 1, (1,0): 3}
        elif M == 8:
            tabela = {
                (0,0,0): -7, (0,0,1): -5, (0,1,1): -3, (0,1,0): -1,
                (1,1,0): 1,  (1,1,1): 3,  (1,0,1): 5,  (1,0,0): 7
            }
        else:
            raise ValueError("mPAM suporta apenas M=4 ou M=8 neste projeto.")
            
        for i in range(0, len(bits), k):
            grupo = tuple(bits[i:i+k])
            simbolos.append(tabela[grupo])
            
        return np.array(simbolos)

    # ----------------------------------------------------
    # 3. MODULAÇÃO COMPLEXA (mQAM)
    # ----------------------------------------------------
    elif mod_format == 'mQAM':
        if M == 4:
            # 4-QAM (QPSK)
            tabela = {
                (0,0): -1-1j, (0,1): -1+1j,
                (1,1):  1+1j, (1,0):  1-1j
            }
        elif M == 16:
            # 16-QAM: Combinação de dois 4-PAMs (Real e Imaginário)
            # Primeiros 2 bits definem a componente Em Fase (I), últimos 2 a Quadratura (Q)
            pam4_base = {(0,0): -3, (0,1): -1, (1,1): 1, (1,0): 3}
            tabela = {}
            # Gerando a tabela 16-QAM dinamicamente para não digitar 16 linhas
            for b1 in [0,1]:
                for b2 in [0,1]:
                    for b3 in [0,1]:
                        for b4 in [0,1]:
                            real = pam4_base[(b1, b2)]
                            imag = pam4_base[(b3, b4)]
                            tabela[(b1, b2, b3, b4)] = real + 1j * imag
        else:
            raise ValueError("mQAM suporta apenas M=4 ou M=16 neste projeto.")
            
        for i in range(0, len(bits), k):
            grupo = tuple(bits[i:i+k])
            simbolos.append(tabela[grupo])
            
        return np.array(simbolos)

    else:
        raise ValueError("Mod_format inválido! Escolha 'polar', 'mPAM' ou 'mQAM'.")

def demapping(symbols, mod_format='polar', M=2):
    """
    Converte símbolos de volta para bits usando a distância Euclidiana mínima.
    """
    bits = []
    
    # ----------------------------------------------------
    # 1. MODULAÇÃO BINÁRIA (POLAR)
    # ----------------------------------------------------
    if mod_format == 'polar':
        # Usa np.real() por segurança, caso algum ruído complexo apareça
        return (np.real(symbols) > 0).astype(int)

    # ----------------------------------------------------
    # 2. MODULAÇÃO MULTINÍVEL (mPAM)
    # ----------------------------------------------------
    elif mod_format == 'mPAM':
        if M == 4:
            niveis_ideais = np.array([-3, -1, 1, 3])
            tabela_inversa = {-3: [0,0], -1: [0,1], 1: [1,1], 3: [1,0]}
        elif M == 8:
            niveis_ideais = np.array([-7, -5, -3, -1, 1, 3, 5, 7])
            tabela_inversa = {
                -7: [0,0,0], -5: [0,0,1], -3: [0,1,1], -1: [0,1,0],
                 1: [1,1,0],  3: [1,1,1],  5: [1,0,1],  7: [1,0,0]
            }
            
        for sym in symbols:
            # Encontra o nível real mais próximo da amplitude recebida
            idx_mais_proximo = np.argmin(np.abs(niveis_ideais - np.real(sym)))
            nivel_decidido = niveis_ideais[idx_mais_proximo]
            bits.extend(tabela_inversa[nivel_decidido])
            
        return np.array(bits)

    # ----------------------------------------------------
    # 3. MODULAÇÃO COMPLEXA (mQAM)
    # ----------------------------------------------------
    elif mod_format == 'mQAM':
        if M == 4:
            niveis_ideais = np.array([-1-1j, -1+1j, 1+1j, 1-1j])
            tabela_inversa = {-1-1j: [0,0], -1+1j: [0,1], 1+1j: [1,1], 1-1j: [1,0]}
            
        elif M == 16:
            # Reconstrói os 16 pontos ideais do 16-QAM
            niveis_ideais = []
            tabela_inversa = {}
            pam4_base = {(0,0): -3, (0,1): -1, (1,1): 1, (1,0): 3}
            # Mapeamento reverso automático
            for b_tupla, val_pam in pam4_base.items():
                for b_tupla2, val_pam2 in pam4_base.items():
                    ponto_complexo = val_pam + 1j * val_pam2
                    niveis_ideais.append(ponto_complexo)
                    tabela_inversa[ponto_complexo] = list(b_tupla) + list(b_tupla2)
            niveis_ideais = np.array(niveis_ideais)
            
        for sym in symbols:
            # Encontra o ponto complexo mais próximo (distância euclidiana no plano 2D)
            distancias = np.abs(niveis_ideais - sym)
            idx_mais_proximo = np.argmin(distancias)
            ponto_decidido = niveis_ideais[idx_mais_proximo]
            bits.extend(tabela_inversa[ponto_decidido])
            
        return np.array(bits)
    
# ==========================================
# 4. PULSE SHAPING (FORMATAÇÃO DE PULSO)
# ==========================================

def get_pulse_shape(pulse_type, K1, roll_off=0.5, span=6, duty_cycle=0.5): 
    """Gera o filtro formador de pulso escolhido."""
    if pulse_type == 'NRZ':
        return np.ones(K1) 
        
    elif pulse_type == 'RZ':
        p = np.zeros(K1)
        largura_ativa = int(np.round(K1 * duty_cycle))
        largura_ativa = max(1, min(largura_ativa, K1 - 1))
        p[:largura_ativa] = 1 
        return p
        
    elif pulse_type == 'RRC':
        # Projeto na Frequência
        N = 2 * span * K1 + 1
        f = np.fft.fftshift(np.fft.fftfreq(N, d=1/K1))
        H_f = np.zeros(N)
        f1 = (1.0 - roll_off) / 2.0
        f2 = (1.0 + roll_off) / 2.0
        
        # Montagem da máscara espectral (Filtro Passa-Baixas ideal nas bordas)
        for i, freq in enumerate(f):
            abs_f = np.abs(freq)
            if abs_f <= f1:
                H_f[i] = 1.0 
            elif f1 < abs_f <= f2:
                H_f[i] = np.sqrt(0.5 * (1.0 + np.cos((np.pi / roll_off) * (abs_f - f1))))
            else:
                H_f[i] = 0.0
                
        # Transformada Inversa para o Tempo
        h_t = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(H_f)))
        h_t = np.real(h_t) # Limpa os resíduos imaginários de máquina da IFFT
        
        # Normaliza a onda para que o pico seja exatamente 1.0 (Ganho unitário)
        h_t = h_t / np.max(h_t)
        
        return h_t
    else:
        raise ValueError("Pulse shape inválido.")

def pulse_shaping_tx(symbols, pulse_type, K1, roll_off=0.5, span=6, duty_cycle=0.5):
    """
    Aplica o upsampling (insere zeros) e passa o sinal pelo filtro formador no TX.
    """
    pulso = get_pulse_shape(pulse_type, K1, roll_off, span=span, duty_cycle=duty_cycle)
    
    # Upsampling: Insere zeros entre cada símbolo
    upsampled_symbols = np.zeros(len(symbols) * K1, dtype=complex) 
    upsampled_symbols[::K1] = symbols 
    
    if pulse_type in ['NRZ', 'RZ']:
        # Operação mais eficiente no Tempo (Pulsos retangulares finitos)
        sinal_formatado = np.convolve(upsampled_symbols, pulso, mode='full')
        
    elif pulse_type == 'RRC':
        # Fast Convolution: Multiplicar na frequência é mais rápido e estável para filtros longos.
        # Importante: Filtramos as componentes Reais (I) e Imaginárias (Q) separadamente 
        # para que uma não vaze para a outra e destrua a constelação complexa.
        # Operação mais precisa na Frequência com proteção de fase (I e Q separados)
        N_fft = len(upsampled_symbols) + len(pulso) - 1
        H_f = np.fft.fft(pulso, N_fft)
        
        S_f_I = np.fft.fft(np.real(upsampled_symbols), N_fft)
        I_formatado = np.real(np.fft.ifft(S_f_I * H_f))
        
        S_f_Q = np.fft.fft(np.imag(upsampled_symbols), N_fft)
        Q_formatado = np.real(np.fft.ifft(S_f_Q * H_f))
        
        sinal_formatado = I_formatado + 1j * Q_formatado
        
    else:
        raise ValueError("Pulse type inválido.")
        
    return sinal_formatado, pulso

def matched_filter_rx(sinal_recebido, pulso_tx, pulse_type, K1, span=6):
    """
    Filtro Casado com Compensação de Atraso Integrada.
    Corta o tempo transitório do TX e do RX para entregar a onda 
    perfeitamente alinhada no índice 0 para o bloco de amostragem.
    O filtro casado é matematicamente a cópia invertida e conjugada do pulso TX
    """
    # A resposta do filtro casado é o pulso do TX invertido no tempo e conjugado
    pulso_casado = np.conj(pulso_tx[::-1])
    energia_pulso = np.sum(np.abs(pulso_casado)**2)
    
    # Calcula o atraso total (Soma do atraso de grupo do TX + RX)
    if pulse_type == 'RRC':
        delay_total = 2 * span * K1
    else:
        delay_total = K1 - 1
        
    if pulse_type in ['NRZ', 'RZ']:
        sinal_filtrado_full = np.convolve(sinal_recebido, pulso_casado, mode='full')
        
        # Slicing: Corta o atraso (silêncio) inicial do sinal para alinhar o t=0
        sinal_filtrado = sinal_filtrado_full[delay_total:]
        
    elif pulse_type == 'RRC':
        N_fft = len(sinal_recebido) + len(pulso_casado) - 1
        H_casado_f = np.fft.fft(pulso_casado, N_fft)
        
        # Proteção I e Q: Impede que o 16-QAM vaze fase e destrua a constelação
        R_f_I = np.fft.fft(np.real(sinal_recebido), N_fft)
        I_filtrado = np.real(np.fft.ifft(R_f_I * H_casado_f))
        
        R_f_Q = np.fft.fft(np.imag(sinal_recebido), N_fft)
        Q_filtrado = np.real(np.fft.ifft(R_f_Q * H_casado_f))
        
        sinal_filtrado_full = I_filtrado + 1j * Q_filtrado
        
        # Como a onda agora está alinhada, o primeiro pico útil já está no índice 0
        sinal_filtrado = sinal_filtrado_full[delay_total:]
        
    else:
        raise ValueError("Pulse type inválido.")
        
    return sinal_filtrado / energia_pulso

def sampling_rx(sinal_filtrado, K1):
    """
    Amostragem (Downsampling).
    Como o filtro casado já eliminou o atraso no bloco anterior, a fase ideal é t=0.
    Basta amostrar pulando de K1 em K1.
    """
    simbolos_recuperados = sinal_filtrado[::K1]
    return simbolos_recuperados

# ==========================================
# 5. CONVERSOR DIGITAL-ANALÓGICO E ANALÓGICO-DIGITAL
# ==========================================

def emular_dac_tx(sinal_discreto, K2):
    """
    Emulação do DAC: Inserção de Zeros + Filtragem Passa-Baixas (LPF).
    Processa as componentes I e Q separadamente para garantir simetria perfeita
    e evitar qualquer distorção de fase na quadratura.
    """
    if K2 <= 1:
        return sinal_discreto

    N_orig = len(sinal_discreto)
    N_k2 = N_orig * K2
    
    # 1. Inserção de Zeros (Zero-stuffing)
    s_zeros = np.zeros(N_k2, dtype=complex)
    s_zeros[::K2] = sinal_discreto
    
    # 2. Construção do Filtro Passa-Baixas (LPF) no domínio shiftado
    # Trabalhar com o freqs 'shiftado' facilita muito visualizar a simetria
    freqs = np.fft.fftshift(np.fft.fftfreq(N_k2))
    H_lpf_shifted = np.zeros(N_k2)
    cutoff = 1.0 / (2.0 * K2)
    
    for i, f in enumerate(freqs):
        # np.isclose previne erros de arredondamento de float na borda do filtro
        if abs(f) < cutoff and not np.isclose(abs(f), cutoff):
            H_lpf_shifted[i] = K2 # Ganho K2 compensa a energia perdida pelos zeros inseridos
        elif np.isclose(abs(f), cutoff):
            H_lpf_shifted[i] = K2 / 2.0
            
    # Retorna o filtro para o formato padrão do numpy para multiplicar pela FFT
    H_lpf = np.fft.ifftshift(H_lpf_shifted)
    

    # 3. FILTRAGEM  (I e Q separados para não haver interferência cruzada)
    
    # -> Processa só a componente Em Fase (I)
    S_f_I = np.fft.fft(np.real(s_zeros))
    I_filtrado = np.real(np.fft.ifft(S_f_I * H_lpf))
    
    # -> Processa só a componente Em Quadratura (Q)
    S_f_Q = np.fft.fft(np.imag(s_zeros))
    Q_filtrado = np.real(np.fft.ifft(S_f_Q * H_lpf))
    
    # 4. Recombina o sinal analógico complexo
    sinal_analogico = I_filtrado + 1j * Q_filtrado
    
    return sinal_analogico

def emular_adc_rx(sinal_analogico, K2):
    """
    Decimação Ideal (ADC): LPF Anti-Aliasing rigoroso + Downsampling.
    Processa as componentes I e Q separadamente para evitar vazamento 
    de energia/fase entre os eixos durante a filtragem via FFT.
    """
    if K2 <= 1:
        return sinal_analogico

    N_k2 = len(sinal_analogico)
    
    # 1. Construção do Filtro Passa-Baixas (LPF) no domínio shiftado
    freqs = np.fft.fftshift(np.fft.fftfreq(N_k2))
    H_lpf_shifted = np.zeros(N_k2)
    cutoff = 1.0 / (2.0 * K2)
    
    for i, f in enumerate(freqs):
        # Utiliza np.isclose para lidar com as dízimas do float com segurança
        if abs(f) < cutoff and not np.isclose(abs(f), cutoff):
            H_lpf_shifted[i] = 1.0  # Ganho unitário na recepção
        elif np.isclose(abs(f), cutoff):
            H_lpf_shifted[i] = 0.5  # Metade da energia exatamente na borda de Nyquist
            
    H_lpf = np.fft.ifftshift(H_lpf_shifted)
    
    # 2. FILTRAGEM (I e Q separados)

    # -> Processa só a componente Em Fase (I)
    R_f_I = np.fft.fft(np.real(sinal_analogico))
    I_filtrado = np.real(np.fft.ifft(R_f_I * H_lpf))

    # -> Processa só a componente Em Quadratura (Q)
    R_f_Q = np.fft.fft(np.imag(sinal_analogico))
    Q_filtrado = np.real(np.fft.ifft(R_f_Q * H_lpf))
    
    # 3. Recombina o sinal filtrado
    sinal_base_complexo = I_filtrado + 1j * Q_filtrado
    
    # 4. Decimação / Downsampling (Pega 1 amostra a cada K2)
    sinal_discreto_rx = sinal_base_complexo[::K2]
    
    return sinal_discreto_rx

# =======================================================================
# 6. CANAL MULTIPERCURSO E EQUALIZAÇÃO ZF
# =======================================================================

def canal_multipercurso_fft(sinal_analogico, h_discrete, K1, K2):
    """
    Aplica 3 caminhos complexos após o DAC usando FFT com Zero-Padding.
    Simula o atraso e os ecos que o sinal sofre no ar.
    """
    # Expande os taps do canal para a taxa da onda contínua (analógica).
    # O espaçamento entre os ecos depende de K1 e K2.
    amostras_por_simbolo = K1 * K2
    tamanho_h_ana = (len(h_discrete) - 1) * amostras_por_simbolo + 1
    h_analog = np.zeros(tamanho_h_ana, dtype=complex)
    
    for i, ganho_complexo in enumerate(h_discrete):
        h_analog[i * amostras_por_simbolo] = ganho_complexo

    # Convolução rápida (FFT) para aplicar a interferência   
    N_fft = len(sinal_analogico) + len(h_analog) - 1
    S_f = np.fft.fft(sinal_analogico, N_fft)
    H_f = np.fft.fft(h_analog, N_fft)
    
    sinal_com_isi = np.fft.ifft(S_f * H_f)
    # Trunca a cauda da convolução para manter o vetor do tamanho original
    return sinal_com_isi[:len(sinal_analogico)]

def equalizador_zf(simbolos_rx, h_discrete):
    """
    Equalizador Zero-Forcing (ZF) implementado no Domínio da Frequência.
    Recebe os símbolos no tempo correto e calcula a divisão do espectro.
    Anula o efeito do canal aplicando a função inversa: 1 / H(f).
    """

    N = len(simbolos_rx)
    
    H_f = np.fft.fft(h_discrete, N)
    # Se o canal zerar uma frequência profunda, 
    # a divisão por zero estoura o Python. Limitamos o fundo a 1e-12.
    H_f[np.abs(H_f) < 1e-12] = 1e-12 
    
    # Equalização direta: Divide o espectro recebido pelo espectro do canal
    R_f = np.fft.fft(simbolos_rx)
    S_eq_f = R_f / H_f
    
    # Devolve a onda limpa (sem ISI) para o domínio do tempo
    simbolos_eq = np.fft.ifft(S_eq_f)
    
    return simbolos_eq


# ---------------------------------------------------------------------------
# 7. CÁLCULO DE ENERGIA ANALÍTICA (LATHI)
# ---------------------------------------------------------------------------

def energia_simbolo(mod_format, M):
    """
    Calcula a energia teórica média por símbolo (Es) baseada na constelação.
    Usar a energia matemática garante que a curva simulada empate com a teórica.
    Se medíssemos a energia empírica da onda, textos curtos teriam desvio padrão
    na distribuição de símbolos, o que calcularia a injeção de ruído AWGN errada.
    """
    if mod_format == 'polar':
        return 1.0                              # BPSK (+1, -1): Módulo sempre 1
    elif mod_format == 'mPAM':
        return (M**2 - 1) / 3.0                 # Ex: 4-PAM tem níveis ±1, ±3. Es = 5.0
    elif mod_format == 'mQAM':
        return 2.0 * (M - 1) / 3.0              # Ex: 16-QAM. Es = 10.0
    else:
        raise ValueError(f"Formato inválido: {mod_format}")

# ---------------------------------------------------------------------------
# 8. INJEÇÃO DE RUÍDO AWGN
# ---------------------------------------------------------------------------

def canal_awgn(sinal, ebn0_db, mod_format, M, oversampling=1):
    """
    Adiciona AWGN baseado na Energia do Bit por Densidade de ruído (Eb/N0).
    Substitui a variável genérica 'snr_db' pelo eixo matemático real 'ebn0_db'.
    """
    # 1. Encontra os valores teóricos (k, Es, Eb)
    k = int(np.log2(M))
    Es = energia_simbolo(mod_format, M)
    Eb = Es / k # Energia média por bit
    
    # 2. Converte Eb/N0 (dB) para linear
    ebn0_linear = 10 ** (ebn0_db / 10.0)
    
    # 3. Calcula a Densidade Espectral do Ruído (N0)
    N0 = Eb / ebn0_linear
    
    # 4. Ajuste para a banda de amostragem
    # Se aplicado na onda (oversampling > 1), o ruído se espalha.
    # Se aplicado direto nos símbolos (oversampling = 1), a variância é N0 puro.
    variancia_ruido = N0 * oversampling
    
    # 5. Injeção blindada (Complexo x Real)
    if np.iscomplexobj(sinal):
        # Ruído complexo: metade da variância vai para I, metade para Q
        ruido = np.sqrt(variancia_ruido / 2.0) * (np.random.randn(len(sinal)) + 1j * np.random.randn(len(sinal)))
    else:
        # Ruído real: A variância equivalente de banda base também deve ser N0/2
        ruido = np.sqrt(variancia_ruido / 2.0) * np.random.randn(len(sinal))
         
    return sinal + ruido

# =======================================================================
# 9. ANÁLISE DE BER E SER
# =======================================================================

def Q(x):
    """
    Função Q(x) clássica de probabilidade de erro de cauda Gaussiana.
    Derivada a partir da função erro complementar (erfc).
    """
    return 0.5 * erfc(x / np.sqrt(2))

def calcular_ber_teorica(ebn0_db, mod_format, M):
    """
    Calcula a Taxa de Erro de Bit (BER) teórica para AWGN puro 
    Usamos as equações do livro do B.P. Lathi.
    Agora recebe diretamente o Eb/N0 (em dB) do eixo do gráfico.
    """
    # 1. Converte Eb/N0 de dB para escala linear
    eb_n0_linear = 10 ** (ebn0_db / 10.0)
    bits_por_simbolo = np.log2(M)
    
    # 2. Fórmulas de Probabilidade de Erro do Lathi
    if mod_format == 'mPAM':
        fator_externo = 2 * ((M - 1) / (M * bits_por_simbolo))
        fator_interno = np.sqrt( (6 * bits_por_simbolo / (M**2 - 1)) * eb_n0_linear )
        return fator_externo * Q(fator_interno)
        
    elif mod_format == 'mQAM':
        if M == 4:
            # 4-QAM é matematicamente idêntico ao QPSK / dois BPSK ortogonais
            return Q(np.sqrt(2 * eb_n0_linear))
        elif M == 16:
            # Equação Exata (Mais precisa que a aproximação comum)
            termo_Q = Q(np.sqrt(0.8 * eb_n0_linear))
            return 0.75 * termo_Q - 0.5625 * (termo_Q ** 2)
            
    elif mod_format == 'polar' and M == 2:
        return Q(np.sqrt(2 * eb_n0_linear))
        
    return 0

# =======================================================================
# 10. ANÁLISE FÍSICA COMPLETA: AS 5 CURVAS DE BER
# =======================================================================

def simular_todas_as_curvas_ber(pacote_tx, cfg, ebn0_range_db, h_discrete):
    """
    Simula o sinal físico extraindo a BER na ordem original da sua arquitetura.
    Avalia o impacto do ruído, do atraso e da ISI em cada estágio do receptor.
    """

    bits_tx_reais = text_to_bits(pacote_tx['texto_original'])
    tam_sync_simb = len(pacote_tx['simbolos_sync'])
    tam_payload_simb = len(pacote_tx['simbolos'])
    tamanho_total_simb = tam_sync_simb + tam_payload_simb

    # Pré-calcula a distorção do canal (ISI)
    sinal_com_isi = canal_multipercurso_fft(pacote_tx['sinal_analogico'], h_discrete, cfg['K1'], cfg['K2'])
    oversampling = cfg['K1'] * cfg['K2']

    ber_teo = []
    ber_awgn_base = []
    ber_cega = []
    ber_sync = []
    ber_eq = []

    print("\n" + "="*85)
    print(" EXTRAINDO BERS DA CADEIA FÍSICA: ESTÁGIO POR ESTÁGIO")
    print(" Eb/N0 | 1. Teórica | 2. AWGN | 3. Cega (Laranja) | 4. Apenas Sync (Azul) | 5. Eq + Sync (Verde)")
    print("=" * 85)

    for ebn0 in ebn0_range_db:
        # 1. Curva Teórica (Preta): Referência
        ber_t = calcular_ber_teorica(ebn0, cfg['formato_mod'], cfg['ordem_M'])
        ber_teo.append(ber_t)

        # 2. Curva AWGN Discreta (Vermelha): Simulação direta a nível de símbolos
        Es_teo = energia_simbolo(cfg['formato_mod'], cfg['ordem_M'])
        k_bits = int(np.log2(cfg['ordem_M']))
        N0 = (Es_teo / k_bits) / (10**(ebn0 / 10.0))
        
        simbolos_base = pacote_tx['simbolos']
        if np.iscomplexobj(simbolos_base):
            ruido_base = np.sqrt(N0/2) * (np.random.randn(len(simbolos_base)) + 1j * np.random.randn(len(simbolos_base)))
        else:
            ruido_base = np.sqrt(N0/2) * np.random.randn(len(simbolos_base))
            
        bits_base = demapping(simbolos_base + ruido_base, cfg['formato_mod'], cfg['ordem_M'])[:len(bits_tx_reais)]
        bits_base_des = deshuffle_bits(bits_base, pacote_tx['idx_perm'])
        ber_awgn_base.append(np.sum(bits_tx_reais != bits_base_des) / len(bits_tx_reais))

        # --- PROCESSAMENTO DA ONDA FÍSICA ---
        # Injeta ruído variante na onda analógica distorcida
        sinal_rx_ana = canal_awgn(sinal_com_isi, ebn0, cfg['formato_mod'], cfg['ordem_M'], oversampling=oversampling)
        sinal_disc_rx = emular_adc_rx(sinal_rx_ana, cfg['K2'])
        sinal_filtrado = matched_filter_rx(sinal_disc_rx, pacote_tx['pulso_usado'], cfg['tipo_pulso'], cfg['K1'], span=cfg['span'])

        # Função interna para calcular o erro estornando o Shuffling do transmissor
        def safe_ber(simbolos_fatiados):
            bits = demapping(simbolos_fatiados, cfg['formato_mod'], cfg['ordem_M'])
            if len(bits) < len(bits_tx_reais):
                bits = np.append(bits, np.zeros(len(bits_tx_reais) - len(bits), dtype=int))
            b_des = deshuffle_bits(bits[:len(bits_tx_reais)], pacote_tx['idx_perm'])
            return np.sum(bits_tx_reais != b_des) / len(bits_tx_reais)

        # 3. Pior curva (Laranja): Fatiamento no t=0 da onda. Sofre com atraso e com ISI.
        simbolos_cegos = sinal_filtrado[0 :: cfg['K1']]
        if len(simbolos_cegos) >= tamanho_total_simb:
            ber_cega.append(safe_ber(simbolos_cegos[tam_sync_simb : tamanho_total_simb]))
        else:
            ber_cega.append(0.5)

        # 4. Curva de Sincronização (A onda acha a fase perfeita, mas mantém o ruído multipercurso)
        simbolos_rx_alinhados, _, _, _ = sincronizar_receptor_por_correlacao(
            sinal_filtrado, pacote_tx['simbolos_sync'], cfg['K1'], h_discrete
        )
        
        bloco_completo_bruto = simbolos_rx_alinhados[:tamanho_total_simb]
        payload_sync = bloco_completo_bruto[tam_sync_simb : tamanho_total_simb]
        ber_sync.append(safe_ber(payload_sync))

        # 5. Curva Equalizada (Verde): Cadeia completa. Sincronismo perfeito + remoção de ISI via ZF.
        bloco_completo_eq = equalizador_zf(bloco_completo_bruto, h_discrete)
        payload_eq = bloco_completo_eq[tam_sync_simb : tamanho_total_simb]
        ber_eq.append(safe_ber(payload_eq))

        print(f" {ebn0:4.1f}  | {ber_t:.3e} | {ber_awgn_base[-1]:.3e} |   {ber_cega[-1]:.3e}     |   {ber_sync[-1]:.3e}     |   {ber_eq[-1]:.3e}")

    print("="*85)
    return ebn0_range_db, ber_teo, ber_awgn_base, ber_cega, ber_sync, ber_eq

# ==========================================
# 11. SINCRONIZAÇÃO (CABEÇALHO E CORRELAÇÃO)
# ==========================================

def gerar_simbolos_sincronia(cfg):
    """
    Gera um cabeçalho longo o suficiente para garantir um pico de correlação 
    imune ao ruído do canal (Ganho de Processamento Máximo).
    O ganho de processamento da correlação cruzada depende do tamanho desse texto.
    """
    texto_sync = "SINC_LAB_SCD_CABECALHO_MAXIMA_ROBUSTEZ_101010"
    bits_sync = text_to_bits(texto_sync)
    
    # Preenche com zeros se não for múltiplo exato dos bits por símbolo
    k = int(np.log2(cfg['ordem_M']))
    sobra = len(bits_sync) % k
    if sobra != 0:
        bits_sync = np.append(bits_sync, np.zeros(k - sobra, dtype=int))
        
    simbolos_sync = mapping(bits_sync, mod_format=cfg['formato_mod'], M=cfg['ordem_M'])
    return bits_sync, simbolos_sync

def emular_perda_de_relogio(sinal_analogico, n_init=26, n_final=50): 
    """Simula a perda de sincronismo inserindo Nzeros_init e Nzeros_final."""
    zeros_iniciais = np.zeros(n_init, dtype=complex)
    zeros_finais = np.zeros(n_final, dtype=complex)
    return np.concatenate((zeros_iniciais, sinal_analogico, zeros_finais))

def sincronizar_receptor_por_correlacao(sinal_filtrado, simbolos_sync_ideal, K1, h_discrete=None):
    """
    Correlação Cruzada com compensação de canal.
    Garante o alinhamento de fase exato no pico do pulso antes de decimar.
    """
    tamanho_cabecalho_amostras = len(simbolos_sync_ideal) * K1
    sync_up = np.zeros(tamanho_cabecalho_amostras, dtype=complex)
    sync_up[::K1] = simbolos_sync_ideal
    
    # Se o canal é informado, aplica-se a distorção dos ecos no 
    # gabarito ideal de busca para evitar desvios fracionários no pico da correlação.
    if h_discrete is not None:
        h_up = np.zeros((len(h_discrete)-1)*K1 + 1, dtype=complex)
        h_up[::K1] = h_discrete
        template_busca = np.convolve(sync_up, h_up, mode='full')
    else:
        template_busca = sync_up

    # Varredura linear deslizante (convolução reversa) buscando casamento perfeito de fase    
    correlacao = np.abs(np.correlate(sinal_filtrado, template_busca, mode='full'))
    
    # O ponto mais alto da correlação indica o instante exato do alinhamento temporal
    indice_pico = np.argmax(correlacao)
    inicio_amostra = indice_pico - len(template_busca) + 1
    
    if inicio_amostra < 0:
        inicio_amostra = 0

    # Fatia o sinal analógico contínuo a partir do pico, pulando de K1 em K1 (ADC)    
    simbolos_rx_sincronizados = sinal_filtrado[inicio_amostra :: K1]
    
    return simbolos_rx_sincronizados, correlacao, inicio_amostra, len(template_busca)

# ==========================================
# FUNÇÕES DE PLOTAGEM (GRÁFICOS)
# ==========================================


def plotar_comparacao_constelacao(simbolos_tx, simbolos_rx, mod_format, M, pulse_type):
    """
    Plota a constelação TX e RX com limites fixos para evitar o auto-zoom do Matplotlib.
    """
    titulo = formatar_titulo(mod_format, M, pulse_type)
    
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(f"Constelação de símbolos ({titulo}) - TX vs. RX", fontsize=14, fontweight='bold')
    
    # Descobre o limite quadrado perfeito para o gráfico (+1 de margem)
    limite = np.max(np.abs(simbolos_tx)) + 1
    
    # TX (Esquerda)
    axs[0].scatter(np.real(simbolos_tx), np.imag(simbolos_tx), color='blue', alpha=0.6)
    axs[0].set_title("Transmissor: mapeamento original")
    axs[0].grid(True, linestyle='--', alpha=0.6)
    axs[0].set_xlabel("Em fase (I)")
    axs[0].set_ylabel("Quadratura (Q)")
    axs[0].axhline(0, color='black', lw=0.8) # Linha do eixo X
    axs[0].axvline(0, color='black', lw=0.8) # Linha do eixo Y
    axs[0].set_xlim(-limite, limite)         # Trava o zoom horizontal
    axs[0].set_ylim(-limite, limite)         # Trava o zoom vertical
    
    # RX (Direita)
    axs[1].scatter(np.real(simbolos_rx), np.imag(simbolos_rx), color='red', marker='.', alpha=0.1)
    axs[1].set_title("Receptor: símbolos recuperados")
    axs[1].grid(True, linestyle='--', alpha=0.6)
    axs[1].set_xlabel("Em fase (I)")
    axs[1].axhline(0, color='black', lw=0.8)
    axs[1].axvline(0, color='black', lw=0.8)
    axs[1].set_xlim(-limite, limite)
    axs[1].set_ylim(-limite, limite)
    
    plt.tight_layout()

def plotar_comparacao_pulse_shaping(sinal_tx, simbolos_tx, simbolos_rx, K1, tipo_pulso, span=6, amostras_simbolos=15):
    """
    Plota a saída do Pulse Shaping (onda discreta) no TX 
    vs a saída do Sampling (símbolos recuperados) no RX.
    """
    # Só considera complexo se a componente imaginária for maior que o ruído de máquina
    is_complex = np.any(np.abs(np.imag(simbolos_tx)) > 1e-8)
    
    # ---> A CORREÇÃO DO DESALINHAMENTO VISUAL AQUI <---
    if tipo_pulso.upper() == 'RRC':
        delay_tx = span * K1
    else:
        delay_tx = 0  # NRZ e RZ não têm cauda transitória inicial
        
    # Quantidade de amostras para o gráfico do transmissor
    amostras_view_tx = amostras_simbolos * K1
    view_tx = sinal_tx[delay_tx : delay_tx + amostras_view_tx]
    
    eixo_x_tx = np.arange(amostras_view_tx)
    eixo_x_rx = np.arange(amostras_simbolos)
    
    simbolos_tx_view = simbolos_tx[:amostras_simbolos]
    simbolos_rx_view = simbolos_rx[:amostras_simbolos]
    
    if is_complex:
        fig, axs = plt.subplots(2, 2, figsize=(16, 8))
        fig.suptitle(f"Formatação (TX) vs Recuperação de símbolos (RX)", fontsize=14, fontweight='bold')
        
        # --- I (Fase) ---
        axs[0, 0].stem(eixo_x_tx, np.real(view_tx), basefmt=" ", markerfmt="b.", linefmt="b-")
        axs[0, 0].set_title("TX: Saída do pulse shaping (I)", fontsize=12)
        axs[0, 0].set_ylabel("Amplitude da onda", fontsize=10)
        
        axs[0, 1].stem(eixo_x_rx, np.real(simbolos_tx_view), basefmt=" ", markerfmt="bo", linefmt="b-", label="Enviado (TX)")
        axs[0, 1].stem(eixo_x_rx, np.real(simbolos_rx_view), basefmt=" ", markerfmt="rx", linefmt="r--", label="Recuperado (RX)")
        axs[0, 1].set_title("RX: Símbolos após sampling (I)", fontsize=12)
        
        # --- Q (Quadratura) ---
        axs[1, 0].stem(eixo_x_tx, np.imag(view_tx), basefmt=" ", markerfmt="c.", linefmt="c-")
        axs[1, 0].set_title("TX: Saída do pulse shaping (Q)", fontsize=12)
        axs[1, 0].set_xlabel("Amostras discretas (K1)", fontsize=10)
        axs[1, 0].set_ylabel("Amplitude da onda", fontsize=10)
        
        axs[1, 1].stem(eixo_x_rx, np.imag(simbolos_tx_view), basefmt=" ", markerfmt="co", linefmt="c-", label="Enviado (TX)")
        axs[1, 1].stem(eixo_x_rx, np.imag(simbolos_rx_view), basefmt=" ", markerfmt="rx", linefmt="m--", label="Recuperado (RX)")
        axs[1, 1].set_title("RX: Símbolos após sampling (Q)", fontsize=12)
        axs[1, 1].set_xlabel("Índice do símbolo (n)", fontsize=10)
        
        for ax in axs.flat:
            ax.grid(True, linestyle='--', alpha=0.6)
            if ax in [axs[0, 1], axs[1, 1]]: ax.legend(loc="upper right")
    else:
        # Gráfico apenas para I se a modulação for unidimensional (ex: PAM)
        fig, axs = plt.subplots(1, 2, figsize=(16, 4))
        fig.suptitle(f"Formatação (TX) vs. Recuperação de símbolos (RX)", fontsize=14, fontweight='bold')
        
        axs[0].stem(eixo_x_tx, np.real(view_tx), basefmt=" ", markerfmt="b.", linefmt="b-")
        axs[0].set_title("TX: Saída do pulse shaping (I)", fontsize=12)
        axs[0].set_ylabel("Amplitude", fontsize=10)
        
        axs[1].stem(eixo_x_rx, np.real(simbolos_tx_view), basefmt=" ", markerfmt="bo", linefmt="b-", label="Enviado (TX)")
        axs[1].stem(eixo_x_rx, np.real(simbolos_rx_view), basefmt=" ", markerfmt="rx", linefmt="r--", label="Recuperado (RX)")
        axs[1].set_title("RX: Símbolos após sampling (I)", fontsize=12)
        
        for ax in axs:
            ax.grid(True, linestyle='--', alpha=0.6)
        axs[1].legend(loc="upper right")

    plt.tight_layout()

def plotar_comparacao_dac_adc(sinal_disc_tx, sinal_ana_tx, sinal_disc_rx, K1, K2, tipo_pulso, span=6, amostras=150):
    """Plota a Sobreamostragem vs Downsampling alinhados no tempo absoluto."""
    
    # Proteção contra ruído de máquina para modulações unidimensionais (PAM)
    is_complex = np.any(np.abs(np.imag(sinal_disc_tx)) > 1e-8)
    
    # ---> CORREÇÃO: O Pulo do tempo visual agora respeita o tipo de pulso <---
    if tipo_pulso.upper() == 'RRC':
        delay_disc_tx = span * K1
        delay_ana_tx = span * K1 * K2
        delay_disc_rx = span * K1
    else:
        delay_disc_tx = 0
        delay_ana_tx = 0
        delay_disc_rx = 0
    
    view_disc_tx = sinal_disc_tx[delay_disc_tx : delay_disc_tx + amostras]
    view_ana_tx = sinal_ana_tx[delay_ana_tx : delay_ana_tx + amostras * K2]
    view_disc_rx = sinal_disc_rx[delay_disc_rx : delay_disc_rx + amostras]
    
    eixo_x_disc = np.arange(amostras) * K2
    eixo_x_adc = np.arange(amostras)
    
    if is_complex:
        fig, axs = plt.subplots(2, 2, figsize=(16, 9))
        fig.suptitle(f"Domínio analógico: DAC vs ADC ($K_2$={K2} | {tipo_pulso})", fontsize=14, fontweight='bold')
        
        # --- I (Fase) ---
        axs[0, 0].stem(eixo_x_disc, np.real(view_disc_tx), basefmt=" ", markerfmt="C0o", linefmt="C0-", label="Discreto (K1)")
        axs[0, 0].plot(np.real(view_ana_tx), color='red', lw=2, label="Analógico (K2)")
        axs[0, 0].set_title("TX: DAC Emulado (I)", fontsize=12)
        axs[0, 0].set_ylabel("Amplitude analógica", fontsize=10)
        
        axs[0, 1].stem(eixo_x_adc, np.real(view_disc_tx), basefmt=" ", markerfmt="C0o", linefmt="C0-", label="TX: Original")
        axs[0, 1].stem(eixo_x_adc, np.real(view_disc_rx), basefmt=" ", markerfmt="rx", linefmt="r--", label="RX: Após ADC")
        axs[0, 1].set_title("RX: ADC Downsampling (I)", fontsize=12)
        
        # --- Q (Quadratura) ---
        axs[1, 0].stem(eixo_x_disc, np.imag(view_disc_tx), basefmt=" ", markerfmt="C0o", linefmt="C0-")
        axs[1, 0].plot(np.imag(view_ana_tx), color='orange', lw=2)
        axs[1, 0].set_title("TX: DAC Emulado (Q)", fontsize=12)
        axs[1, 0].set_xlabel("Amostras interpoladas", fontsize=10)
        axs[1, 0].set_ylabel("Amplitude analógica", fontsize=10)
        
        axs[1, 1].stem(eixo_x_adc, np.imag(view_disc_tx), basefmt=" ", markerfmt="C0o", linefmt="C0-")
        axs[1, 1].stem(eixo_x_adc, np.imag(view_disc_rx), basefmt=" ", markerfmt="rx", linefmt="r--")
        axs[1, 1].set_title("RX: ADC Downsampling (Q)", fontsize=12)
        axs[1, 1].set_xlabel("Índice do símbolo discreto", fontsize=10)
        
        for ax in axs.flat:
            ax.grid(True, linestyle='--', alpha=0.6)
            if ax in [axs[0, 0], axs[0, 1]]: ax.legend(loc='upper right')
            
    else:
        # --- Gráfico para PAM (Unidimensional) ---
        fig, axs = plt.subplots(1, 2, figsize=(16, 4))
        fig.suptitle(f"Domínio analógico: DAC vs ADC ($K_2$={K2} | {tipo_pulso})", fontsize=14, fontweight='bold')
        
        axs[0].stem(eixo_x_disc, np.real(view_disc_tx), basefmt=" ", markerfmt="C0o", linefmt="C0-", label="Discreto (K1)")
        axs[0].plot(np.real(view_ana_tx), color='red', lw=2, label="Analógico (K2)")
        axs[0].set_title("TX: DAC Emulado (I)", fontsize=12)
        axs[0].set_xlabel("Amostras interpoladas", fontsize=10)
        axs[0].set_ylabel("Amplitude analógica", fontsize=10)
        
        axs[1].stem(eixo_x_adc, np.real(view_disc_tx), basefmt=" ", markerfmt="C0o", linefmt="C0-", label="TX: Original")
        axs[1].stem(eixo_x_adc, np.real(view_disc_rx), basefmt=" ", markerfmt="rx", linefmt="r--", label="RX: Após ADC")
        axs[1].set_title("RX: ADC Downsampling (I)", fontsize=12)
        axs[1].set_xlabel("Índice do símbolo discreto", fontsize=10)
        
        for ax in axs:
            ax.grid(True, linestyle='--', alpha=0.6)
            ax.legend(loc='upper right')
            
    plt.tight_layout()
        
def plotar_percurso_sinal(simbolos_tx, sinal_tx, sinal_adc_rx, sinal_filt_rx, simbolos_rx, K1, tipo_pulso, span=6, view=15):

    fig, axs = plt.subplots(3, 2, figsize=(16, 10))
    fig.suptitle(f"Análise do percurso do sinal discreto ({tipo_pulso})", fontsize=16, fontweight='bold')
    
    amostras_k1 = view * K1
    eixo_simbolos = np.arange(view)
    eixo_k1 = np.arange(amostras_k1)
    
    sinal_up_tx_visual = np.zeros(amostras_k1, dtype=complex)
    sinal_up_tx_visual[::K1] = simbolos_tx[:view]
    
    # Ajuste de atraso apenas para a visualização do Transmissor (TX)
    if tipo_pulso.upper() == 'RRC':
        delay_tx = span * K1
    else:
        delay_tx = 0 # NRZ e RZ começam direto no tempo 0, sem cauda
        
    # --- COLUNA 1: TRANSMISSOR ---
    axs[0, 0].stem(eixo_simbolos, np.real(simbolos_tx[:view]), basefmt=" ", markerfmt="bo", linefmt="b-")
    axs[0, 0].set_title("1. TX: Símbolos mapeados")
    
    axs[1, 0].stem(eixo_k1, np.real(sinal_up_tx_visual), basefmt=" ", markerfmt="bo", linefmt="b-")
    axs[1, 0].set_title(f"2. TX: Inserção de zeros (Upsampling K1={K1})")
    
    view_tx = sinal_tx[delay_tx : delay_tx + amostras_k1]
    axs[2, 0].stem(eixo_k1, np.real(view_tx), basefmt=" ", markerfmt="b.", linefmt="b-")
    axs[2, 0].set_title("3. TX: Saída do pulse shaping")
    
    # --- COLUNA 2: RECEPTOR ---
    view_adc = sinal_adc_rx[delay_tx : delay_tx + amostras_k1]
    axs[0, 1].stem(eixo_k1, np.real(view_adc), basefmt=" ", markerfmt="r.", linefmt="r-")
    axs[0, 1].set_title("4. RX: Entrada do filtro casado")
    
    # Retiramos o delay_rx daqui, pois a função matched_filter_rx já cortou o atrasO
    view_filt_rx = sinal_filt_rx[:amostras_k1]
    
    axs[1, 1].stem(eixo_k1, np.real(view_filt_rx), basefmt=" ", markerfmt="m.", linefmt="m-", label="Onda do Filtro")
    axs[1, 1].stem(eixo_k1[::K1], np.real(view_filt_rx[::K1]), basefmt=" ", markerfmt="mX", linefmt="none", label="Pico amostrado")
    axs[1, 1].set_title("5. RX: Saída do filtro casado")
    axs[1, 1].legend()
    
    axs[2, 1].stem(eixo_simbolos, np.real(simbolos_rx[:view]), basefmt=" ", markerfmt="ro", linefmt="r-")
    axs[2, 1].set_title("6. RX: Remoção de zeros")
    
    for ax in axs.flat:
        ax.grid(True, linestyle='--', alpha=0.6)
        
    plt.tight_layout()
  
def plotar_efeito_isi_equalizacao(simbolos_rx_com_isi, simbolos_rx_equalizados, mod_format, M, pulse_type):
    """Plota a constelação antes e depois do Equalizador ZF."""
    titulo = formatar_titulo(mod_format, M, pulse_type)
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle(f"Efeito do canal seletivo e equalização ZF ({titulo})", fontsize=14, fontweight='bold')
    
    limite = np.max(np.abs(simbolos_rx_equalizados)) + 2
    
    # Gráfico 1: Antes da Equalização
    axs[0].scatter(np.real(simbolos_rx_com_isi), np.imag(simbolos_rx_com_isi), color='orange', alpha=0.2, marker='o')
    axs[0].set_title("1. Símbolos no RX com ISI")
    axs[0].set_xlabel("Em fase (I)", fontsize=12)
    axs[0].set_ylabel("Quadratura (Q)", fontsize=12)
    axs[0].grid(True, linestyle='--', alpha=0.6)
    axs[0].axhline(0, color='black', lw=0.8)
    axs[0].axvline(0, color='black', lw=0.8)
    axs[0].set_xlim(-limite, limite)
    axs[0].set_ylim(-limite, limite)
    
    # Gráfico 2: Após a Equalização
    axs[1].scatter(np.real(simbolos_rx_equalizados), np.imag(simbolos_rx_equalizados), color='green', alpha=0.2, marker='.')
    axs[1].set_title("2. Símbolos após equalizador ZF")
    axs[1].set_xlabel("Em fase (I)", fontsize=12)
    axs[1].set_ylabel("Quadratura (Q)", fontsize=12)
    axs[1].grid(True, linestyle='--', alpha=0.6)
    axs[1].axhline(0, color='black', lw=0.8)
    axs[1].axvline(0, color='black', lw=0.8)
    axs[1].set_xlim(-limite, limite)
    axs[1].set_ylim(-limite, limite)
    
    plt.tight_layout()

def plotar_prova_matematica_zf(h_discrete):
    """
    Gera as provas matemáticas do Equalizador ZF e o perfil do canal:
    1. Magnitude do Perfil de Atraso do Canal (|h[n]|).
    2. A resposta em frequência (Canal, Equalizador e Combinada plana).
    3. A resposta ao impulso combinada (O Delta de Dirac / "Zero").
    """
    import scipy.signal as signal
    h = np.asarray(h_discrete, dtype=complex)
    
    # 1. CÁLCULOS DO CANAL (MAGNITUDE)
    magnitudes = np.abs(h)
    taps = np.arange(len(h))
    
    # 2. CÁLCULO DAS RESPOSTAS EM FREQUÊNCIA
    w, H_f = signal.freqz(h, [1.0], worN=1024)
    w, F_f = signal.freqz([1.0], h, worN=1024)
    
    H_f_db = 20 * np.log10(np.abs(H_f) + 1e-12)
    F_f_db = 20 * np.log10(np.abs(F_f) + 1e-12)
    Comb_db = 20 * np.log10(np.abs(H_f * F_f) + 1e-12)
    
    # 3. CÁLCULO DA RESPOSTA AO IMPULSO
    impulso_ideal = np.zeros(20)
    impulso_ideal[0] = 1.0
    saida_canal = signal.lfilter(h, [1.0], impulso_ideal)
    saida_equalizador = signal.lfilter([1.0], h, saida_canal)
    
    # 4. PLOTAGEM (COM 3 COLUNAS)
    fig, axs = plt.subplots(1, 3, figsize=(20, 5))
    fig.suptitle("Perfil do canal e validação do Zero-Forcing", fontsize=15, fontweight='bold')
    
    # Gráfico 1: Magnitude do Canal
    axs[0].stem(taps, magnitudes, basefmt=" ", markerfmt="bo", linefmt="b-")
    axs[0].set_title("1. Magnitude do canal |h[n]|", fontsize=13)
    axs[0].set_xlabel("Índice do atraso", fontsize=11)
    axs[0].set_ylabel("Amplitude linear", fontsize=11)
    axs[0].set_xticks(taps)
    axs[0].grid(True, linestyle='--', alpha=0.6)
    for i, mag in enumerate(magnitudes):
        axs[0].text(i, mag + 0.05, f"{mag:.2f}", ha='center', color='blue', fontweight='bold')
    
    # Gráfico 2: Resposta em Frequência
    axs[1].plot(w/np.pi, H_f_db, label='Canal |H(f)|', color='red', lw=2)
    axs[1].plot(w/np.pi, F_f_db, label='Equalizador |F(f)|', color='blue', lw=2)
    axs[1].plot(w/np.pi, Comb_db, label='Combinada |H(f) * F(f)|', color='green', linestyle='--', lw=3)
    axs[1].set_title("2. Resposta em frequência", fontsize=13)
    axs[1].set_xlabel(r"Frequência normalizada (x $\pi$ rad/amostra)", fontsize=11)
    axs[1].set_ylabel("Magnitude (dB)", fontsize=11)
    axs[1].grid(True, linestyle='--', alpha=0.6)
    axs[1].legend(loc='lower left')
    axs[1].set_ylim([-15, 15])
    
    # Gráfico 3: Resposta ao Impulso
    eixo_n = np.arange(20)
    axs[2].stem(eixo_n, np.real(saida_equalizador), basefmt=" ", markerfmt="go", linefmt="g-")
    axs[2].set_title("3. Resposta ao impulso (Canal + ZF)", fontsize=13)
    axs[2].set_xlabel("Índice da amostra (n)", fontsize=11)
    axs[2].set_ylabel("Amplitude", fontsize=11)
    axs[2].grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()

def plotar_alinhamento_amostragem(sinal_filtrado, inicio_amostra, K1, view_simbolos=15):
    """
    Prova visual da importância do sincronismo na fase de amostragem.
    Mostra a diferença entre amostrar às cegas (errando os picos)
    e amostrar no índice exato encontrado pela correlação cruzada.
    """
    amostras_view = view_simbolos * K1
    
    # Define uma janela de visualização ao redor do início do pacote
    start_idx = max(0, inicio_amostra - 2 * K1)
    end_idx = inicio_amostra + amostras_view
    
    eixo_n = np.arange(start_idx, end_idx)
    onda_view = sinal_filtrado[start_idx:end_idx]
    
    # 1. Amostras cegas (Receptor que liga no t=0 e pula de K1 em K1)
    indices_cegos = np.arange(0, end_idx, K1)
    indices_cegos = indices_cegos[indices_cegos >= start_idx]
    
    # 2. Amostras Sincronizadas (Receptor guiado pela Correlação)
    indices_sync = np.arange(inicio_amostra, end_idx, K1)
    
    fig, axs = plt.subplots(2, 1, figsize=(14, 8))
    fig.suptitle("Alinhamento da fase de amostragem (Timing Recovery)", fontsize=14, fontweight='bold')
    
    # Amostragem Cega
    axs[0].plot(eixo_n, np.real(onda_view), 'k-', alpha=0.4, label='Onda contínua (após filtro casado)')
    axs[0].stem(indices_cegos, np.real(sinal_filtrado[indices_cegos]), linefmt='r-', markerfmt='rX', basefmt=' ', label='Amostras desincronizadas')
    axs[0].set_title("1. Receptor sem sincronismo: amostras nas ladeiras do sinal", fontsize=12)
    axs[0].grid(True, linestyle='--', alpha=0.6)
    axs[0].legend(loc='upper right')
    axs[0].set_ylabel("Amplitude")
    
    # Plot Inferior: Amostragem Sincronizada
    axs[1].plot(eixo_n, np.real(onda_view), 'k-', alpha=0.4, label='Onda contínua (após Filtro casado)')
    axs[1].stem(indices_sync, np.real(sinal_filtrado[indices_sync]), linefmt='g-', markerfmt='go', basefmt=' ', label='Amostras sincronizadas')
    axs[1].set_title(f"2. Receptor sincronizado: amostras nos picos de energia (início na amostra {inicio_amostra})", fontsize=12)
    axs[1].grid(True, linestyle='--', alpha=0.6)
    axs[1].legend(loc='upper right')
    axs[1].set_xlabel("Índice do tempo discreto (amostras n)", fontsize=11)
    axs[1].set_ylabel("Amplitude")
    
    plt.tight_layout()

def plotar_5_curvas_ber(ebn0_db, ber_teo, ber_awgn_base, ber_cega, ber_sync, ber_eq, cfg, M, pulse_type):
    """Gera o Gráfico Logarítmico exigido, interrompendo as linhas quando a BER atinge zero."""
    titulo = formatar_titulo(cfg['formato_mod'], M, pulse_type)
    plt.figure(figsize=(11, 8))
    #plt.title(f"BER por etapa ({cfg['formato_mod']} | Pulso {cfg['tipo_pulso']})", fontsize=15, fontweight='bold')
    plt.title(f"BER por etapa ({titulo})", fontsize=15, fontweight='bold')

    
    # Substituição de zeros absolutos por NaN para cortar a linha visualmente no gráfico
    ber_awgn_plot = np.array(ber_awgn_base, dtype=float)
    ber_awgn_plot[ber_awgn_plot == 0] = np.nan
    
    ber_eq_plot = np.array(ber_eq, dtype=float)
    ber_eq_plot[ber_eq_plot == 0] = np.nan

    plt.semilogy(ebn0_db, ber_teo, 'k-', linewidth=2.5, label="1. Teórica (Lathi)")
    plt.semilogy(ebn0_db, ber_awgn_plot, 'r--', marker='o', markersize=6, alpha=0.9, label="2. Discreta AWGN")
    
    plt.semilogy(ebn0_db, ber_cega, color='orange', linestyle='-', marker='s', linewidth=2, alpha=0.8, label="3. Saída desincronizada e sem equalização")
    
    # Nomenclatura mantida conforme a sua configuração
    plt.semilogy(ebn0_db, ber_sync, color='blue', linestyle='-', marker='d', linewidth=2, alpha=0.8, label="4. Saída apenas equalizada")
    plt.semilogy(ebn0_db, ber_eq_plot, color='green', linestyle='-', marker='^', markersize=8, linewidth=2.5, label="5. Saída final: equalizada + sincronizada")

    # Eixo X fixado com o título obrigatório estipulado para o projeto
    plt.xlabel("$E_b/N_0$ (dB)", fontsize=13)
    plt.ylabel("Razão de Erro de Bit (BER)", fontsize=13)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.ylim([1e-5, 1])
    plt.xlim([min(ebn0_db), max(ebn0_db)])
    plt.legend(fontsize=12, loc='lower left')
    plt.tight_layout()

def plotar_pico_sincronizacao(correlacao, inicio_amostra, tamanho_cabecalho_amostras):
    """Plota a comprovação visual do alinhamento do cabeçalho."""

    plt.figure(figsize=(10, 4))    
    plt.title("Sincronização por correlação cruzada no receptor", fontsize=14, fontweight='bold')
    
    # Desloca o eixo X para que o pico matemático intercepte exatamente o início do pacote
    eixo_x = np.arange(len(correlacao)) - tamanho_cabecalho_amostras + 1
    
    plt.plot(eixo_x, correlacao, color='purple', alpha=0.8, label='Varredura de correlação')
    #plt.axvline(inicio_amostra, color='red', linestyle='--', linewidth=2, label=f'Início do Pacote (Amostra: {inicio_amostra})')
    
    # Eixos corrigidos para a realidade do processamento de sinais
    plt.xlabel("Tempo discreto (amostras)", fontsize=12)
    plt.ylabel("Magnitude da correlação", fontsize=12)
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.xlim([min(eixo_x), max(eixo_x)])
    plt.legend(loc='upper right')
    plt.tight_layout()


# =======================================================================
# MÓDULOS DE COMUNICAÇÃO
# =======================================================================

def transmissor(texto, cfg):
    """Encapsula toda a lógica do Transmissor (Com Sincronismo e Fase Alinhada)."""
    print("="*60)
    print("TRANSMISSOR")
    print("="*60)

    # 1. Geração do Cabeçalho de Sincronia
    bits_sync, simbolos_sync = gerar_simbolos_sincronia(cfg) 
    print(f"[TX Bloco 1] Cabeçalho gerado com {len(simbolos_sync)} símbolos.")

    # 2. Processamento da Mensagem
    print(f"\n[TX Bloco 2] Texto a ser comunicado:\n'{texto[:120]}...'") 
    bits_payload = text_to_bits(texto)
    
    # 3. Mapeamento e Agrupamento
    bits_emb, idx_perm = shuffle_bits(bits_payload, seed=cfg.get('seed', 42))
    simbolos_payload = mapping(bits_emb, mod_format=cfg['formato_mod'], M=cfg['ordem_M'])
    
    simbolos_tx = np.concatenate((simbolos_sync, simbolos_payload))
    print(f"\n[TX Bloco 3] Símbolos totais (Cabeçalho + Payload): {len(simbolos_tx)}")

    # 4. Formatação de Pulso e DAC
    sinal_disc_tx, pulso_usado = pulse_shaping_tx(
        simbolos_tx, cfg['tipo_pulso'], cfg['K1'], 
        roll_off=cfg['roll_off'], span=cfg['span'], duty_cycle=cfg['duty_cycle']
    )
    sinal_ana_tx_limpo = emular_dac_tx(sinal_disc_tx, cfg['K2'])
    print("\n[TX Bloco 4] Pulse Shaping e Conversão DAC aplicados com sucesso.")
    
    # 5. Inserção do Atraso Analógico
    n_init_base = cfg.get('Nzeros_init', 26)
    n_init_alinhado = n_init_base * cfg['K2'] 
    n_final = max(cfg.get('Nzeros_final', 50), 200)
    
    sinal_ana_tx_atrasado = emular_perda_de_relogio(sinal_ana_tx_limpo, n_init_alinhado, n_final)
    print(f"\n[TX Bloco 5] Desincronização: Nzeros_init={n_init_alinhado} (Fase Protegida) e Nzeros_final={n_final} aplicados.")

    return {
        'texto_original': texto,
        'sinal_analogico': sinal_ana_tx_atrasado,
        'sinal_discreto': sinal_disc_tx,
        'simbolos': simbolos_payload, 
        'simbolos_sync': simbolos_sync,
        'pulso_usado': pulso_usado,
        'idx_perm': idx_perm,
        'tamanho_bits_payload': len(bits_emb)
    }

def canal(sinal_tx_analogico, cfg, h_discrete=None):
    """Simula a passagem da onda pelo espaço livre (Meio físico)."""
    print("\n" + "="*60)
    print("CANAL DE COMUNICAÇÃO")
    print("="*60)
    
    # 1. Aplica o Multipercurso (Ecos/ISI)
    if h_discrete is not None:
        print("[Canal Bloco 1] Aplicando canal multipercurso (ISI) via convolução circular (FFT).")
        sinal_com_isi = canal_multipercurso_fft(sinal_tx_analogico, h_discrete, cfg['K1'], cfg['K2'])
    else:
        print("[Canal Bloco 1] Canal ideal (Sem ISI).")
        sinal_com_isi = sinal_tx_analogico.copy()
        
    # 2. Adiciona o Ruído Térmico (AWGN)
    usar_ruido = True 
    if usar_ruido:
        oversampling_total = cfg['K1'] * cfg['K2']
        sinal_rx = canal_awgn(sinal_com_isi, cfg['snr_db'], cfg['formato_mod'], cfg['ordem_M'], oversampling=oversampling_total)
        print(f"[Canal Bloco 2] Sinal degradado pelo meio físico. Ruído AWGN injetado (Eb/N0 Eq. = {cfg['snr_db']} dB).")
    else:
        print("[Canal Bloco 2] Simulação sem ruído AWGN.")
        sinal_rx = sinal_com_isi.copy()
        
    return sinal_rx

def receptor(sinal_rx_analogico, cfg, tx_info, h_discrete=None):
    """Encapsula a lógica do Receptor com a arquitetura inicial funcional."""
    print("\n" + "="*60)
    print("RECEPTOR")
    print("="*60)

    # 1. Conversão Analógico Digital e Filtro Casado
    sinal_disc_rx = emular_adc_rx(sinal_rx_analogico, cfg['K2'])
    sinal_filtrado = matched_filter_rx(sinal_disc_rx, tx_info['pulso_usado'], cfg['tipo_pulso'], cfg['K1'], span=cfg['span'])
    print("[RX Bloco 1] O sinal foi amostrado e filtrado.")
    
    # 2. Sincronização e Downsampling
    print("\n[RX Bloco 2] Iniciando varredura de correlação cruzada para alinhamento...")
    simbolos_rx_alinhados, correlacao, inicio_amostra, tamanho_template = sincronizar_receptor_por_correlacao(
        sinal_filtrado, tx_info['simbolos_sync'], cfg['K1'], h_discrete
    )
    print(f"             Alinhamento concluído. Pico ideal na amostra: {inicio_amostra}")
    
    tamanho_cab_simbolos = len(tx_info['simbolos_sync'])
    tamanho_payload_simbolos = len(tx_info['simbolos'])
    tamanho_total = tamanho_cab_simbolos + tamanho_payload_simbolos
    
    bloco_completo_bruto = simbolos_rx_alinhados[:tamanho_total]
    
    # 3. Equalização de Canal
    if h_discrete is not None:
        print("\n[RX Bloco 3] Equalizador ZF aplicado no pacote completo para corrigir o multipercurso.")
        bloco_completo_eq = equalizador_zf(bloco_completo_bruto, h_discrete)
    else:
        print("\n[RX Bloco 3] Sinal processado sem equalização (Canal Ideal).")
        bloco_completo_eq = bloco_completo_bruto
        
    # 4. Extração do Texto e Demapeamento
    simbolos_rx_payload_eq = bloco_completo_eq[tamanho_cab_simbolos : tamanho_total]
    simbolos_rx_payload_brutos = bloco_completo_bruto[tamanho_cab_simbolos : tamanho_total]

    bits_desmapeados = demapping(simbolos_rx_payload_eq, mod_format=cfg['formato_mod'], M=cfg['ordem_M'])
    bits_desmapeados = bits_desmapeados[:tx_info['tamanho_bits_payload']]
    
    bits_desemb = deshuffle_bits(bits_desmapeados, tx_info['idx_perm'])
    texto_recuperado = bits_to_text(bits_desemb)

    print(f"\n[RX Bloco 4] Texto recebido:\n'{texto_recuperado[:80]}...'")

    # 5. Relatório de Desempenho (BER e SER)
    bits_tx = text_to_bits(tx_info['texto_original']) 
    simbolos_tx = tx_info['simbolos']
    
    total_bits = len(bits_tx)
    erros_bit = np.sum(bits_tx != bits_desemb)
    ber_simulada = erros_bit / total_bits
    
    simbolos_decididos = mapping(bits_desmapeados, mod_format=cfg['formato_mod'], M=cfg['ordem_M'])
    total_simbolos = len(simbolos_tx)
    erros_simbolo = np.sum(simbolos_tx != simbolos_decididos)
    ser_simulada = erros_simbolo / total_simbolos
    
    print(f"\n[RX Bloco 5] Relatório de desempenho (Eb/N0 Eq. = {cfg['snr_db']} dB):")
    print(f"-> SER Simulada: {ser_simulada:.2e} | BER Simulada: {ber_simulada:.2e}")

    return {
        'sinal_discreto_rx': sinal_disc_rx,
        'sinal_filtrado': sinal_filtrado,
        'simbolos_rx_brutos': simbolos_rx_payload_brutos, 
        'simbolos_rx_eq': simbolos_rx_payload_eq,
        'correlacao': correlacao,
        'inicio_amostra': inicio_amostra,
        'tamanho_cabecalho_amostras': tamanho_template
    }


# Chamada das plotagens dos resultados
def plotar_resultados(pacote_tx, pacote_rx, cfg, h_discrete=None):
    """Exibe todos os gráficos na ordem física dos acontecimentos."""
    print("\nDesenhando gráficos base (Aguarde)...")

    plotar_pico_sincronizacao(
        pacote_rx['correlacao'], 
        pacote_rx['inicio_amostra'], 
        pacote_rx['tamanho_cabecalho_amostras'],
    )
    
    
    plotar_alinhamento_amostragem(
        pacote_rx['sinal_filtrado'], 
        pacote_rx['inicio_amostra'], 
        cfg['K1'],
        #cfg['ordem_M']
    )

    plotar_comparacao_dac_adc(
        pacote_tx['sinal_discreto'], pacote_tx['sinal_analogico'], pacote_rx['sinal_discreto_rx'], 
        cfg['K1'], cfg['K2'], cfg['tipo_pulso'], span=cfg['span'], amostras=60
    )
    
    plotar_percurso_sinal(
        pacote_tx['simbolos'], pacote_tx['sinal_discreto'], pacote_rx['sinal_discreto_rx'], 
        pacote_rx['sinal_filtrado'], pacote_rx['simbolos_rx_brutos'], cfg['K1'], cfg['tipo_pulso'], span=cfg['span']
    )

    if h_discrete is not None:
        plotar_prova_matematica_zf(h_discrete)

    plotar_efeito_isi_equalizacao(
        pacote_rx['simbolos_rx_brutos'], pacote_rx['simbolos_rx_eq'], cfg['formato_mod'], cfg['ordem_M'], cfg['tipo_pulso']
    )

    plotar_comparacao_constelacao(
        pacote_tx['simbolos'], pacote_rx['simbolos_rx_eq'], cfg['formato_mod'], cfg['ordem_M'], cfg['tipo_pulso']
    )

def main():
    """Função principal que organiza a simulação completa."""
    canal_h_discreto = np.array([
        1.0 + 0j,       # Principal
        0.4 + 0.3j,     # Eco 1
        -0.2 - 0.1j     # Eco 2
    ])
    
    pacote_tx = transmissor(input_text, config)
    sinal_no_receptor = canal(pacote_tx['sinal_analogico'], config, h_discrete=canal_h_discreto)
    pacote_rx = receptor(sinal_no_receptor, config, pacote_tx, h_discrete=canal_h_discreto)
    
    # Passamos h_discrete=canal_h_discreto para os plots
    plotar_resultados(pacote_tx, pacote_rx, config, h_discrete=canal_h_discreto)

    # Análise das 5 Curvas Estágio por Estágio
    ebn0_values = np.arange(0, 22, 2) 
    ebn0, ber_teo, ber_awgn_base, ber_cega, ber_sync, ber_eq = simular_todas_as_curvas_ber(
        pacote_tx, config, ebn0_values, canal_h_discreto
    )
    
    plotar_5_curvas_ber(
        ebn0, 
        ber_teo, 
        ber_awgn_base, 
        ber_cega, 
        ber_sync, 
        ber_eq, 
        config, 
        config['ordem_M'],     # Busca o M aqui
        config['tipo_pulso']   # Busca o pulso aqui
    )

    print("\nProcessamento concluído. Abrindo visualizações...")
    plt.show()

if __name__ == "__main__":
    main()
