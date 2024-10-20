#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argumentos = sys.argv
    cantidad = len(argumentos) - 1

    if cantidad == 0:
        print("0 arguments.")
    elif cantidad == 1:
        print("1 argument:")
    else:
        print(f"{cantidad} arguments:")

    for i in range(1, cantidad + 1):
        print(f"{i}: {argumentos[i]}")
