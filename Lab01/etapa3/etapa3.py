from functions.add_noise import adicionar_ruido
from functions.decoders import decode_nrz
from functions.encoders import encode_nrz

import numpy as np
import matplotlib.pyplot as plt
# Assumindo que você tem as funções e bibliotecas necessárias importadas
# from functions.add_noise import adicionar_ruido
# from functions.decoders import decode_nrz
# from functions.encoders import encode_nrz

original_bits = "11011010001110010100011000101"
num_bits = len(original_bits)  # 29 bits

snr_coletados = []
erros_coletados = []

# Itera do SNR -31 dB (início da falha) até -62 dB 
for i in range(31, 126, 1):
    snr_value = -i  

    try:
        clean_signal = encode_nrz(original_bits)
        noisy_signal = adicionar_ruido(clean_signal, snr_value)
        decoded = decode_nrz(noisy_signal, num_bits)
    except NameError:
        print("\nERRO: Por favor, verifique se as funções (encode_nrz, adicionar_ruido, decode_nrz) estão acessíveis.")
        break
    
    erros = 0
    for j in range(num_bits):
        if original_bits[j] != decoded[j]:
            erros += 1
            
    snr_coletados.append(snr_value)
    erros_coletados.append(erros)

    print(f"SNR: {snr_value} dB -> Erros: {erros}/{num_bits}")

print("\n--- coleta de dados finalizada. Gerando gráfico... ---")

plt.figure(figsize=(10, 6))

plt.plot(snr_coletados, erros_coletados, marker='o', linestyle='-', color='blue')

plt.hlines(num_bits / 2, min(snr_coletados), max(snr_coletados), color='red', linestyle='--', label='50% de Erros (Limite Teórico)')

plt.title("Taxa de Erro de Bit (BER) vs. Relação Sinal-Ruído (SNR)")
plt.xlabel("Relação Sinal-Ruído (SNR) em dB")
plt.ylabel(f"Número de Erros Coletados (Máx: {num_bits})")
plt.yticks(np.arange(0, num_bits + 1, 5))
plt.grid(True)
plt.gca().invert_xaxis() 
plt.legend()
plt.show()




""" original_bits = "11011010001110010100011000101" #modifiquei para a minha mensagem

snr=-31

clean_signal = encode_nrz(original_bits)

noisy_signal = adicionar_ruido(clean_signal, snr)
decoded = decode_nrz(noisy_signal, len(original_bits))
print(f"  Original: {original_bits}")
print(f"  Decodificado: {decoded}")
print(f"  Correto: {original_bits == decoded}\n") """