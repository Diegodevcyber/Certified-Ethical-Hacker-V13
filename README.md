<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CEH v13 Project CyberSentinel - Relatório de Operações</title>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* Estilos Globais */
        body {
            background-color: #0d1117; /* Fundo escuro */
            color: #00ff00; /* Texto verde neon */
            font-family: 'Fira Code', monospace; /* Fonte estilo terminal */
            line-height: 1.6;
            margin: 20px;
            padding: 0;
            overflow-x: hidden; /* Evita scroll horizontal */
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #30363d; /* Borda sutil */
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.2); /* Sombra neon */
        }

        h1, h2, h3, h4, h5, h6 {
            color: #00ff00; /* Títulos em verde neon */
            text-shadow: 0 0 5px rgba(0, 255, 0, 0.5); /* Sombra para títulos */
            border-bottom: 1px dashed #30363d;
            padding-bottom: 5px;
            margin-top: 30px;
        }

        h1 { font-size: 2.5em; text-align: center; }
        h2 { font-size: 1.8em; }
        h3 { font-size: 1.4em; }

        a {
            color: #00ffff; /* Links em ciano neon */
            text-decoration: none;
            transition: color 0.3s ease;
        }

        a:hover {
            color: #00ccff;
            text-decoration: underline;
        }

        /* Estilos para Badges e GIFs */
        .center-content {
            text-align: center;
            margin-bottom: 20px;
        }

        .center-content img {
            margin: 5px;
            border-radius: 5px;
        }

        /* Estilos de Bloco de Código / Terminal */
        pre, code {
            background-color: #161b22; /* Fundo mais escuro para blocos de código */
            color: #00ff00;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto; /* Scroll para código longo */
            font-size: 0.9em;
            border: 1px solid #21262d;
            margin-bottom: 15px;
        }

        .bash-output {
            color: #00ff00; /* Verde para output de terminal */
        }

        .json-output {
            color: #ff00ff; /* Magenta para JSON */
        }

        /* Estilos de Lista */
        ul {
            list-style: none;
            padding-left: 20px;
        }

        ul li::before {
            content: ">> ";
            color: #00ffff; /* Ciano para marcadores de lista */
            font-weight: bold;
        }

        /* Tabela de Módulos */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }

        th, td {
            border: 1px solid #21262d;
            padding: 8px;
            text-align: left;
            color: #00ff00;
        }

        th {
            background-color: #161b22;
            color: #00ffff;
            text-transform: uppercase;
        }

        /* Detalhes (Collapsible) */
        details {
            background-color: #161b22;
            border: 1px solid #21262d;
            border-radius: 5px;
            margin-top: 20px;
            padding: 10px;
        }

        summary {
            cursor: pointer;
            color: #00ffff;
            font-weight: bold;
            padding: 5px;
            outline: none;
        }

        summary:hover {
            color: #00ccff;
        }

        /* Barra de Progresso */
        .progress-bar {
            background-color: #21262d;
            border-radius: 5px;
            height: 20px;
            margin-top: 10px;
            overflow: hidden;
        }

        .progress-fill {
            width: 100%; /* Exemplo: 100% para estrutura completa */
            height: 100%;
            background-color: #00ff00;
            border-radius: 5px;
            box-shadow: 0 0 8px rgba(0, 255, 0, 0.5);
        }

    </style>
</head>
<body>
    <div class="container">
        <h1 style="font-size: 3em;">⚡️ CEH v13 :: Project CyberSentinel // Log de Operações D3dg3s ⚡️</h1>

        <p class="center-content">
            <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&color=00FF00&size=35&center=true&vCenter=true&width=700&lines=D3dg3s%20CyberSec%20//%20CEH%20v13%20Operational%20Log;Acompanhando%20a%20Jornada%20do%20Ethical%20Hacker;Decifrando%20M%C3%B3dulos%20de%20Seguran%C3%A7a" alt="Typing SVG Banner">
        </p>

        <p class="center-content">
            <img src="https://img.shields.io/badge/Certifica%C3%A7%C3%A3o-CEH%20v13-blueviolet?style=for-the-badge&logo=hackthebox&logoColor=white" alt="Badge CEH v13">
            <img src="https://img.shields.io/badge/Status-Criptografando%20Conhecimento-important?style=for-the-badge&logo=codecademy&logoColor=white" alt="Badge Status Criptografando Conhecimento">
            <img src="https://img.shields.io/badge/%C3%9Altimoo%20Log%20Atualizado-09%20Jul%202025-lightgrey?style=for-the-badge" alt="Badge Último Log Atualizado">
        </p>

        <p class="center-content">
            <img src="https://media.giphy.com/media/xT9IAqfF2T4z9n1JjW/giphy.gif" width="600" alt="Animated Terminal Hacker GIF - Substitua por um GIF relevante: Terminal digitando, visualização de dados, ou algo 'cyber'. Procure em Giphy ou similar.">
        </p>

        <h2>**1. 🎯 :: Protocolo de Início :: Visão Geral e Objetivo da Missão**</h2>
        <pre><code class="bash-output">root@D3dg3s_Workstation:~# cat /project/manifesto.txt
[+] Bem-vindos ao meu repositório de inteligência cibernética.
[+] Este log detalha a jornada operacional e o acúmulo de expertise para a certificação
[+] Certified Ethical Hacker (CEH) v13.
[+] A meta é simples: consolidar, aplicar e demonstrar o domínio das táticas de segurança ofensiva.
[+] Analisando dados... Concluído.</code></pre>
        <p>Este repositório não é apenas um diretório de arquivos; é uma <strong>rede de dados interativa e um portfólio técnico dinâmico</strong>, construído para mapear minha progressão no universo do hacking ético. Ele serve como uma <strong>auditoria transparente e um registro de campo</strong> das minhas habilidades em cibersegurança.</p>
        <p>Minha missão primária é apresentar uma evidência clara e estruturada da minha capacidade de executar e analisar operações de segurança. Este material é ideal para <strong>avaliação por recrutadores de elite, para validação com pares da indústria e como um recurso de conhecimento aberto</strong> para a comunidade.</p>

        <h2>**2. 📁 :: Topografia da Rede :: Arquitetura e Framework Operacional**</h2>
        <h3>2.1. Metadados do Host</h3>
        <ul>
            <li><strong>Codinome do Projeto:</strong> <code>D3dg3s/CEH_v13_CipherLog</code> (Sugestão de nome para impacto "hacker"!)</li>
            <li><strong>Ponto de Acesso GitHub:</strong> <a href="https://github.com/D3dg3s/adiciona-restoria-inicial-de-estudos-CEH-v13">https://github.com/D3dg3s/adiciona-restoria-inicial-de-estudos-CEH-v13</a> *(<strong>ALERTA</strong>: Atualize este link com o URL real do seu repositório!)*</li>
            <li><strong>Linguagem Principal de Scripting:</strong> 🐍 Python (<code class="bash-output">print("Iniciando varredura profunda...")</code>) - Meu motor para automatização de rotinas, desenvolvimento de Provas de Conceito (PoCs), engenharia reversa de conceitos e criação de ferramentas sob demanda.</li>
        </ul>

        <h3>2.2. Mapeamento de Módulos (Estrutura de Dados)</h3>
        <p>A arquitetura do repositório espelha com precisão a estrutura de curso do CEH v13, com <strong>20 compartimentos de dados principais</strong>. Cada diretório de módulo (<code>Módulo XX - [Título do Módulo]</code>) é um micro-cosmos dedicado a conter:</p>
        <ul>
            <li><strong><code>0x00_INTELIGENCIA/</code></strong>: <code>ANOTACOES.md</code>, <code>MAPAS_MENTAIS.png</code>, <code>RESUMOS_CONCEITUAIS.pdf</code> - Dados de inteligência teórica, anotações de aula, e documentação primária do módulo.</li>
            <li><strong><code>0x01_LAB_REPORTS/</code></strong>: <code>LAB_ID_XXX_RELATORIO.md</code>, <code>CAPTURES/</code>, <code>LOGS/</code>, <code>ANALISE_POS_OP.md</code> - Relatórios detalhamentos de exercícios práticos, incluindo:
                <ul>
                    <li><code>SETUP/</code>: Diagramas de topologia de rede e configurações de VMs.</li>
                    <li><code>PASSOS_OPERACIONAIS/</code>: Sequência de comandos executados e justificativas técnicas.</li>
                    <li><code>EVIDENCIAS/</code>: Capturas de tela (screenshots), GIFs animados de execuções de exploits e logs de saída das ferramentas.</li>
                    <li><code>ANALISE_CRITICA/</code>: Lições aprendidas, vulnerabilidades exploradas, e propostas de mitigação.</li>
                </ul>
            </li>
            <li><strong><code>0x02_FERRAMENTAS_CUSTOM/</code></strong>: <code>script_personalizado.py</code>, <code>payloads/</code>, <code>config_templates/</code> - Scripts desenvolvidos, payloads personalizados e configurações de ferramentas utilizadas ou modificadas.</li>
            <li><strong><code>0x03_RECURSOS/</code></strong>: <code>RFCs/</code>, <code>PAPERS_PESQUISA/</code>, <code>LINKS_UTEIS.md</code> - Biblioteca de recursos externos para aprofundamento.</li>
        </ul>

        <h3>2.3. Protocolo de Engajamento (Metodologia de Estudo)</h3>
        <p>Minha metodologia de aprendizado é um ciclo contínuo de <strong>Investigação -> Execução -> Validação -> Documentação</strong>:</p>
        <ol>
            <li><strong>Fase 1: Coleta de Dados (Teoria):</strong> Imersão nos conceitos fundamentais de cada módulo do CEH v13.</li>
            <li><strong>Fase 2: Simulação de Ataque (Prática):</strong> Reconstrução e execução de cenários de ataque em ambientes controlados e realistas.</li>
            <li><strong>Fase 3: Desenvolvimento de Ferramentas (Customização):</strong> Codificação de scripts para automação, análise de dados ou criação de PoCs.</li>
            <li><strong>Fase 4: Análise Forense e Relato:</strong> Documentação minuciosa de cada passo, resultado e descoberta, transformando dados brutos em inteligência acionável.</li>
            <li><strong>Fase 5: Otimização e Debug:</strong> Revisão crítica do material e das técnicas para aprimoramento contínuo.</li>
        </ol>

        <h2>**3. 📚 :: Mapeamento de Credenciais :: Log de Progresso por Módulo**</h2>
        <p>A arquitetura base dos 20 módulos do CEH v13 está ativa e aguarda a injeção completa de conteúdo. Esta estrutura reflete uma abordagem sistemática para a maestria do currículo.</p>

        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
        <p class="center-content"><code>[████████████████████████████████] 100% Carga Base Completa</code></p>

        <details>
            <summary>:: Decifrar Log de Módulos (Clique para expandir) ::</summary>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Módulo CEH v13</th>
                        <th>Status de Documentação</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td><code>0x00</code></td><td>Bem-vindo ao Certified Ethical Hacker</td><td>⚙️ <code>SYSTEM_INIT</code></td></tr>
                    <tr><td><code>0x01</code></td><td>Introdução ao Hacking Ético</td><td>⚙️ <code>FUNDAMENTALS_SCAN</code></td></tr>
                    <tr><td><code>0x02</code></td><td>Footprinting e Reconhecimento</td><td>⚙️ <code>INTEL_GATHERING</code></td></tr>
                    <tr><td><code>0x03</code></td><td>Varredura de Redes</td><td>⚙️ <code>NETWORK_PROBE</code></td></tr>
                    <tr><td><code>0x04</code></td><td>Enumeração</td><td>⚙️ <code>RESOURCE_DISCOVERY</code></td></tr>
                    <tr><td><code>0x05</code></td><td>Análise de Vulnerabilidades</td><td>⚙️ <code>WEAKNESS_ASSESSMENT</code></td></tr>
                    <tr><td><code>0x06</code></td><td>Hacking de Sistemas</td><td>⚙️ <code>SYSTEM_COMPROMISE</code></td></tr>
                    <tr><td><code>0x07</code></td><td>Ameaças de Malware</td><td>⚙️ <code>MALWARE_ANALYSIS</code></td></tr>
                    <tr><td><code>0x08</code></td><td>Sniffing</td><td>⚙️ <code>DATA_INTERCEPTION</code></td></tr>
                    <tr><td><code>0x09</code></td><td>Engenharia Social</td><td>⚙️ <code>HUMAN_EXPLOITATION</code></td></tr>
                    <tr><td><code>0x0A</code></td><td>Negação de Serviço (DoS)</td><td>⚙️ <code>SERVICE_DISRUPTION</code></td></tr>
                    <tr><td><code>0x0B</code></td><td>Sequestro de Sessão</td><td>⚙️ <code>SESSION_HIJACK</code></td></tr>
                    <tr><td><code>0x0C</code></td><td>Evasão de IDS, Firewalls e Honeypots</td><td>⚙️ <code>DEFENSE_EVASION</code></td></tr>
                    <tr><td><code>0x0D</code></td><td>Hacking de Servidores Web</td><td>⚙️ <code>WEB_SERVER_EXPLOIT</code></td></tr>
                    <tr><td><code>0x0E</code></td><td>Hacking de Aplicações Web</td><td>⚙️ <code>WEB_APP_EXPLOIT</code></td></tr>
                    <tr><td><code>0x0F</code></td><td>SQL Injection</td><td>⚙️ <code>SQL_INJECTION</code></td></tr>
                    <tr><td><code>0x10</code></td><td>Hacking de Redes Wireless</td><td>⚙️ <code>WIRELESS_COMPROMISE</code></td></tr>
                    <tr><td><code>0x11</code></td><td>Hacking de Plataformas Móveis</td><td>⚙️ <code>MOBILE_EXPLOIT</code></td></tr>
                    <tr><td><code>0x12</code></td><td>Hacking de IoT e OT</td><td>⚙️ <code>IOT_OT_PENETRATION</code></td></tr>
                    <tr><td><code>0x13</code></td><td>Computação em Nuvem</td><td>⚙️ <code>CLOUD_SECURITY</code></td></tr>
                    <tr><td><code>0x14</code></td><td>Criptografia</td><td>⚙️ <code>CRYPTOGRAPHY_ANALYSIS</code></td></tr>
                </tbody>
            </table>
        </details>

        <h2>**4. 🛠️ :: Kit de Ferramentas Operacional e Ambientes de Simulação**</h2>
        <p>Para a execução de operações táticas e o aprimoramento de habilidades, o seguinte arsenal de ferramentas e ambientes é constantemente mobilizado:</p>
        <ul>
            <li><strong>Plataformas de Virtualização (Sandboxes Seguras):</strong>
                <ul>
                    <li><strong>VirtualBox / VMware Workstation:</strong> Meus campos de treinamento virtuais para construir e destruir sistemas de forma controlada (Kali Linux, Windows Server, VMs vulneráveis).</li>
                </ul>
                <p class="center-content">
                    <img src="https://media.giphy.com/media/v1.gif" width="300" alt="GIF de VM bootando"> <!-- SUBSTITUA POR UM GIF DE VM BOOTANDO OU DE AMBIENTE VIRTUAL -->
                </p>
            </li>
            <li><strong>Sistemas Operacionais (Plataformas de Ataque/Defesa):</strong>
                <ul>
                    <li><strong>Kali Linux:</strong> A distribuição definitiva para o operador de segurança ofensiva.</li>
                    <li><strong>Windows Server / Cliente:</strong> Para engenharia reversa de ambientes corporativos e suas vulnerabilidades.</li>
                </ul>
            </li>
            <li><strong>Campos de Batalha Cibernéticos (CTF & Labs Online):</strong>
                <ul>
                    <li><strong>TryHackMe / Hack The Box:</strong> Campos de testes dinâmicos para aprimorar técnicas em cenários realísticos e desenvolver a mentalidade de um atacante.</li>
                </ul>
            </li>
            <li><strong>Ferramentas de Desenvolvimento e Suporte (Kit de Ferramentas do Engenheiro):</strong>
                <ul>
                    <li><strong>Visual Studio Code (VS Code):</strong> Minha interface principal para codificação, análise e documentação.</li>
                    <li><strong>Git / GitHub Desktop:</strong> Essencial para controle de versão, garantindo a integridade dos meus logs de projeto.</li>
                    <li><strong>Pylint:</strong> Para garantir que cada script Python esteja otimizado e livre de vulnerabilidades.</li>
                    <li><strong>Anaconda:</strong> Meu centro de controle para gerenciar ambientes Python e dependências de ferramentas.</li>
                </ul>
            </li>
        </ul>

        <h2>**5. 👤 :: Perfil do Operador :: Contribuinte Chave**</h2>
        <pre><code class="json-output">{
  "agente_designacao": "D3dg3s - Diego CyberSec",
  "funcao_primaria": "Aspirante a Certified Ethical Hacker",
  "estado_operacional": "Entusiasta de Cibersegurança em Formação",
  "credenciais_profissionais": "https://www.linkedin.com/in/seu-perfil/",
  "objetivo_estrategico": "Maestria no hacking ético e contribuição para a segurança digital global."
}</code></pre>

        <h2>**6. 📈 :: Roteiro de Implementação :: Próximos Alvos & Estratégias**</h2>
        <p>A evolução deste log de projeto é uma operação contínua. As próximas fases incluem:</p>
        <ul>
            <li><strong>Infiltração Profunda de Conteúdo:</strong> Preenchimento sistemático de cada diretório de módulo com:
                <ul>
                    <li>Anotações táticas e aprofundadas.</li>
                    <li>Scripts de exploração e automação testados em campo.</li>
                    <li>Relatórios de laboratório detalhados, com fluxogramas de ataque e mitigações.</li>
                </ul>
            </li>
            <li><strong>Simulação de Cenários de Ataque Complexos:</strong> Desenvolvimento e documentação de cenários que transcendem os labs padrão do curso.</li>
            <li><strong>Análise e Customização de Ferramentas:</strong> Estudo aprofundado e modificação de ferramentas avançadas para cada fase do ciclo de ataque.</li>
            <li><strong>Integração de Inteligência CTF:</strong> Inclusão de "write-ups" e metodologias de desafios de Capture The Flag (CTF) relevantes, para solidificar o pensamento fora da caixa.</li>
            <li><strong>Controle de Versão e Atualização:</strong> Manutenção proativa do repositório, garantindo que a inteligência de ameaças mais recente seja incorporada.</li>
        </ul>

        <h2>**7. ✨ :: Log de Eventos :: Destaques Operacionais e Anomalias do Sistema (Lições Aprendidas)**</h2>
        <ul>
            <li><strong>Destaques Operacionais (Conquistas Desbloqueadas):</strong>
                <ul>
                    <li>Implantação bem-sucedida de uma <strong>estrutura modular CEH-compliant</strong>, projetada para rastreamento eficaz de conhecimento e demonstração de proficiência.</li>
                    <li>Desenvolvimento de um <strong>Protocolo de Estudo híbrido (teoria + prática intensa)</strong>, utilizando plataformas de labs reais para validação de habilidades.</li>
                    <li>Adoção de um <strong>arsenal de ferramentas profissionais</strong>, replicando o ambiente de um operador de segurança cibernética no mundo real.</li>
                </ul>
            </li>
            <li><strong>Anomalias do Sistema (Desafios Encontrados e Superados):</strong>
                <ul>
                    <li>A <strong>vasta e complexa paisagem do currículo CEH v13</strong> exige um gerenciamento rigoroso de tempo e foco para garantir a absorção completa do conhecimento.</li>
                    <li>Manter a <strong>documentação granular e de alta qualidade</strong> para cada laboratório e conceito é uma operação de alto nível que requer disciplina e atenção aos detalhes.</li>
                    <li>A <strong>velocidade da evolução das ameaças cibernéticas</strong> impulsiona a necessidade constante de pesquisa e atualização para além do material do curso.</li>
                </ul>
            </li>
        </ul>

        <h2>**8. ✍️ :: Conclusão da Missão :: Próximos Horizontes**</h2>
        <pre><code class="bash-output">root@D3dg3s_Workstation:~# echo "Finalizando entrada no logbook..."
[+] Missão em andamento.
[+] Próxima fase: Infiltração e documentação avançada de módulos.
[+] Mantenha-se seguro. Over and out.
</code></pre>
        <p>Este Log de Projeto CEH v13 é mais do que um repositório; é um testemunho da minha paixão incessante pela cibersegurança e da minha busca pela maestria no hacking ético. Ele serve como uma prova concreta das minhas capacidades teóricas e práticas. Convido a comunidade a inspecionar este log e a colaborar para fortalecer a fronteira digital.</p>
    </div>
</body>
</html>
