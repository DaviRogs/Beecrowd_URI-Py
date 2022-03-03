import string

abziraldo = list(string.ascii_uppercase)
abziraldo.insert(0, None)
letra = input()

print(abziraldo.index(letra))