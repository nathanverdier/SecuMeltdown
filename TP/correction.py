import subprocess

# Appeler le script2.py
i=0
result=""
while("hey" not in result):
    resultat = subprocess.run(['python3', 'testMeltdown.py', str(i)], capture_output=True, text=True)
    if resultat.stderr == "":
        result=resultat.stdout
        i += 1
print(result)