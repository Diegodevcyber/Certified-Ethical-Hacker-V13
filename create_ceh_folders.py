import os

folders = [
    "Module 00 - Welcome to Certified Ethical Hacker",
    "Module 01 - Introduction to Ethical Hacking",
    "Module 02 - Footprinting and Reconnaissance",
    "Module 02 - Labs",
    "Module 03 - Scanning Networks",
    "Module 04 - Enumeration",
    "Module 04 - Labs",
    "Module 05 - Vulnerability Analysis",
    "Module 06 - Labs",
    "Module 06 - System Hacking",
    "Module 07 - Malware",
    "Module 08 - Labs",
    "Module 08 - Sniffing",
    "Module 09 - Social Engineering",
    "Module 10 - Denial-of-Service",
    "Module 10 - Labs",
    "Module 11 - Session Hijacking",
    "Module 12 - Evading IDS, Firewalls, and Honeypots",
    "Module 12 - Labs",
    "Module 13 - Hacking Web Servers",
    "Module 14 - Hacking Web Applications",
    "Module 14 - Labs",
    "Module 15 - SQL Injection",
    "Module 16 - Hacking Wireless Networks",
    "Module 16 - Labs",
    "Module 17 - Hacking Mobile Platforms",
    "Module 18 - IoT and OT Hacking",
    "Module 18 - Labs",
    "Module 19 - Cloud Computing",
    "Module 20 - Cryptography",
    "Module 20 - Labs"
]

for folder in folders:
    try:
        # Cria a pasta
        os.makedirs(folder, exist_ok=True)
        print(f"Pasta criada: {folder}")

        # Caminho completo para o arquivo .gitkeep dentro da pasta
        gitkeep_path = os.path.join(folder, ".gitkeep")

        # Cria o arquivo .gitkeep
        with open(gitkeep_path, 'w') as f:
            pass # Apenas cria o arquivo vazio

        print(f"  - Arquivo .gitkeep criado em: {gitkeep_path}")

    except OSError as e:
        print(f"Erro ao processar pasta {folder}: {e}")

print("\nTodas as pastas e arquivos .gitkeep foram processados.")