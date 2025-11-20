import soundfile as sf

from functions.decoders import decode_manchester, decode_nrz, detect_frequency
from config import SAMPLE_RATE
from functions.encoders import encode_manchester, encode_nrz


test_data = "1010100000001111110000010101010111000"



print(f"Criando arquivos de teste para: {test_data}")

# NRZ
nrz_signal = encode_nrz(test_data)
sf.write('teste_nrz.wav', nrz_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_nrz.wav criado")

# Manchester
manchester_signal = encode_manchester(test_data)
sf.write('teste_manchester.wav', manchester_signal, SAMPLE_RATE)
print("\t ✓ Arquivo teste_manchester.wav criado")

original_data = test_data

print(f"\nDados originais: {original_data}")
print(f"Número de bits: {len(original_data)}\n")

# Testa decodificação NRZ
print("1. Decodificando NRZ:")
nrz_audio, _ = sf.read('teste_nrz.wav')
print(detect_frequency(nrz_audio, SAMPLE_RATE))
decoded_nrz = decode_nrz(nrz_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_nrz}")
print(f"Correto: {original_data == decoded_nrz}\n")

# Testa decodificação Manchester
print("3. Decodificando Manchester:")
manchester_audio, _ = sf.read('teste_manchester.wav')
print(detect_frequency(manchester_audio, SAMPLE_RATE))
decoded_manchester = decode_manchester(manchester_audio, len(original_data))
print(f"Original: {original_data}")
print(f"Decodificado: {decoded_manchester}")
print(f"Correto: {original_data == decoded_manchester}")

# Testa decodificação Manchester
print("4. Decodificando Manchester meu áudio:")
manchester_audio1, _ = sf.read('dados_122110391_44100hz.wav')
decoded_manchester = decode_manchester(manchester_audio1, len(original_data))
print(f"Decodificado: {decoded_manchester}")
print(f"Número de bits: {len(decoded_manchester)}\n")