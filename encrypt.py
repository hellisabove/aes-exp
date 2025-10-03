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
from Crypto.Util.Padding import pad
import os, sys

def encrypt_file(file_path):
    if not os.path.isfile(file_path):
        print("Invalid file path.")
        return

    key = os.urandom(32)
    iv = os.urandom(16)

    with open(file_path, 'rb') as f:
        data = f.read()

    padded = pad(data, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    encrypted_data = cipher.encrypt(padded)
    final_data = iv + encrypted_data

    enc_file_path = file_path + ".enc"
    with open(enc_file_path, 'wb') as f:
        f.write(final_data)
    with open(file_path + ".key", 'wb') as k:
        k.write(key)
    os.remove(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 " + sys.argv[0] + " <path_to_file> (without the <>)")
    else:
        encrypt_file(sys.argv[1])
