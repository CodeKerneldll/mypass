# mini_password_manager.py
import json, os, getpass

file_path = "passwords.json"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
else:
    data = {}

def save_data():
    with open(file_path, "w") as f:
        json.dump(data, f)

while True:
    action = input("Add ou Get senha (add/get/exit): ").lower()
    if action == "add":
        site = input("Site/App: ")
        pwd = getpass.getpass("Senha: ")
        data[site] = pwd
        save_data()
        print("Senha salva")
    elif action == "get":
        site = input("Site/App: ")
        print("Senha:", data.get(site, "Não encontrada"))
    elif action == "exit":
        break
    else:
        print("Comando inválido")
