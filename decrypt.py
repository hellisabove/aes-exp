"""
Copyright (C) 2025  hellisabove

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os, sys

def decrypt_file(enc_file_path, enc_key):
    if not os.path.isfile(enc_file_path):
        print("Invalid file path.")
        return

    with open(enc_key, 'rb') as e:
        key = e.read()
   
    with open(enc_file_path, 'rb') as f:
        enc_data = f.read()
    
    iv = enc_data[:16]
    data = enc_data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)

    final_data = unpad(cipher.decrypt(data), AES.block_size)
    final_path = enc_file_path.replace('.enc', '')

    with open(final_path, 'wb') as ff:
        ff.write(final_data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 " + sys.argv[0] + " <path_to_encrypted_file> <path_to_encryption_key> (without the <>)")
    else:
        decrypt_file(sys.argv[1], sys.argv[2])
