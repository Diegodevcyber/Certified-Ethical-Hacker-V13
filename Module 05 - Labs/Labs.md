Realizando Pesquisas de Vulnerabilidade com Sistemas de Pontuação e Bancos de Dados
Pesquisa de Vulnerabilidade na Enumeração de Fraquezas Comuns (CWE)
Para iniciar um scan com o Nikto contra www.certifiedhacker.com, use o seguinte comando:

Bash

sgpt --chat nikto --shell "Launch nikto to execute a scan against the URL www.certifiedhacker.com to identify potential vulnerabilities."
nikto -h www.certifiedhacker.com
Avaliando Vulnerabilidades com Múltiplas Ferramentas
Análise com OpenVAS
Para iniciar o OpenVAS usando Docker, siga os passos abaixo:

Obter privilégios de root:

Bash

sudo su
Comando Docker para iniciar o OpenVAS:

Bash

docker run -d -p 443:443 --name openvas mikesplain/openvas
Análise com Nmap e IA
Use o ShellGPT para gerar o comando Nmap e, em seguida, execute a varredura de vulnerabilidade.

Gerar scan Nmap com IA:

Bash

sgpt --chat vuln --shell "Perform a vulnerability scan on target url www.moviescope.com with nmap and save the results in output.txt"
Executar scan Nmap para verificação de vulnerabilidade:

Bash

nmap -sV --script=vuln www.moviescope.com -oN output.txt
Análise com Skipfish e IA
Use o ShellGPT para gerar o comando do Skipfish e, em seguida, execute o scan e visualize o relatório.

Gerar scan Skipfish com IA:

Bash

sgpt --shell "Perform a vulnerability scan on target url http://testphp.vulnweb.com with skipfish and display the output file index.html in firefox."
Executar scan Skipfish e exibir o relatório:

Bash

skipfish -o /tmp/skipfish_output http://testphp.vulnweb.com && firefox /tmp/skipfish_output/index.html
Análise com Script Python e IA
O ShellGPT pode ajudar a criar um script Python para automatizar varreduras.

Criar script Python com IA:

Bash

sgpt --chat scancode --code "Create a python script to run a fast but comprehensive Nmap scan on the IP addresses in scan1.txt and then execute vulnerability scanning using nikto against each IP address in scan1.txt"
Script Python para automação de scans Nmap e Nikto:

Python

import subprocess
with open('scan1.txt', 'r') as file:
    ip_addresses = file.read().splitlines()
for ip in ip_addresses:
    subprocess.run(['nmap', '-T4', '-A', '-v', ip])
for ip in ip_addresses:
    subprocess.run(['nikto', '-h', ip])
Gerar e executar um scan Nikto com IA:

Bash

sgpt --chat nikto --shell "Launch nikto to execute a scan against the URL www.certifiedhacker.com to identify potential vulnerabilities."
nikto -h www.certifiedhacker.com
Executando Análise de Vulnerabilidade com ShellGPT
Aqui estão alguns exemplos de como usar o ShellGPT para iniciar varreduras de vulnerabilidade com comandos simples.

Nikto:

Bash

sgpt --chat nikto --shell "Launch nikto to execute the URL https://www.certifiedhacker.com to identify potential vulnerabilities."
Nmap (Moviescope):

Bash

sgpt --chat vuln --shell "Perform vulnerability scan on target url http://www.moviescope.com with Nmap"
Skipfish (Testphp):

Bash

sgpt --chat vuln --shell "Perform a vulnerability scan on target url http://testphp.vulnweb.com with skipfish"
