import sounddevice as sd

from config import SAMPLE_RATE
from functions.encoders import encode_manchester, encode_nrz

test_bits = "111110"
print(f"Dados originais: {test_bits}\n")

# Testa cada modulação
print("1. NRZ:")
nrz_signal = encode_nrz(test_bits,debug=True)

print("\n3. Manchester:")
manchester_signal = encode_manchester(test_bits,debug=True)

"""sd.play(nrz_signal, SAMPLE_RATE)
sd.wait()"""

sd.play(manchester_signal, SAMPLE_RATE)
sd.wait()