<h2>Realizar pesquisas de vulnerabilidade com sistemas de pontuação de vulnerabilidade e bancos de dados</h2>

<span style="color: yellow;">Realizar Pesquisa de Vulnerabilidade na Enumeração de Fraquezas Comuns (CWE)</span>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: #39ff14;">sgpt --chat nikto --shell "Launch nikto to execute a scan against the URL www.certifiedhacker.com to identify potential vulnerabilities."<br>
nikto -h www.certifiedhacker.com</span>
</div>

<h2>Realizar avaliação de vulnerabilidade usando várias ferramentas de avaliação de vulnerabilidade</h2>
Análise com OpenVAS

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando para obter privilégios de root:</span><br>
<span style="color: #39ff14;">sudo su</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando Docker para iniciar o OpenVAS:</span><br>
<span style="color: #39ff14;">docker run -d -p 443:443 --name openvas mikesplain/openvas</span>
</div>

Análise com Nmap e IA

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando sgpt para gerar um scan Nmap com IA:</span><br>
<span style="color: #39ff14;">sgpt --chat vuln --shell "Perform a vulnerability scan on target url www.moviescope.com with nmap and save the results in output.txt"</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando nmap para verificação de vulnerabilidade:</span><br>
<span style="color: #39ff14;">nmap -sV --script=vuln www.moviescope.com -oN output.txt</span>
</div>

Análise com Skipfish e IA

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando sgpt para gerar um scan Skipfish com IA:</span><br>
<span style="color: #39ff14;">sgpt --shell "Perform a vulnerability scan on target url http://testphp.vulnweb.com with skipfish and display the output file index.html in firefox."</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando skipfish para scan e exibição do relatório:</span><br>
<span style="color: #39ff14;">skipfish -o /tmp/skipfish_output http://testphp.vulnweb.com && firefox /tmp/skipfish_output/index.html</span>
</div>

Análise com Python Script e IA

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando sgpt para criar um script Python:</span><br>
<span style="color: #39ff14;">sgpt --chat scancode --code "Create a python script to run a fast but comprehensive Nmap scan on the IP addresses in scan1.txt and then execute vulnerability scanning using nikto against each IP address in scan1.txt"</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Script Python para automação de scans Nmap e Nikto:</span><br>
<span style="color: #39ff14;">import subprocess
with open('scan1.txt', 'r') as file:
    ip_addresses = file.read().splitlines()
for ip in ip_addresses:
    subprocess.run(['nmap', '-T4', '-A', '-v', ip])
for ip in ip_addresses:
    subprocess.run(['nikto', '-h', ip])</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando sgpt para gerar um scan Nikto com IA:</span><br>
<span style="color: #39ff14;">sgpt --chat nikto --shell "Launch nikto to execute a scan against the URL www.certifiedhacker.com to identify potential vulnerabilities."</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Comando nikto para verificação de vulnerabilidade:</span><br>
<span style="color: #39ff14;">nikto -h www.certifiedhacker.com</span>
</div>

<h2>Executar análise de vulnerabilidade usando ShellGPT</h2>
<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Executar análise de vulnerabilidade usando ShellGPT</span><br>
<span style="color: #39ff14;">Comando: sgpt --chat nikto --shell "Launch nikto to execute the URL https://www.certifiedhacker.com to identify potential vulnerabilities."</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Varredura de vulnerabilidade no Moviescope com Nmap</span><br>
<span style="color: #39ff14;">Comando: sgpt --chat vuln --shell "Perform vulnerability scan on target url http://www.moviescope.com with Nmap"</span>
</div>

<div style="background-color: #2d2d2d; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: monospace;">
<span style="color: yellow;">Verificação de vulnerabilidade no Testphp com Skipfish</span><br>
<span style="color: #39ff14;">Comando: sgpt --chat vuln --shell "Perform a vulnerability scan on target url http://testphp.vulnweb.com with skipfish"</span>
</div>