    # 📚 Módulo 02: Footprinting e Reconhecimento - Guia de Laboratório

    ---

    ## 1. Visão Geral e Tipos de Footprinting

    * ***Footprinting*** é a **fase inicial e essencial** de um teste de penetração, focada na coleta de informações públicas e privadas sobre o alvo.

    | Tipo de Footprinting | Descrição | Exemplos de Ferramentas/Comandos |
    | :--- | :--- | :--- |
    | **Passivo (Não-Intrusivo)** | Coleta sem interação direta com o alvo (ex: pesquisa em registros públicos, caches). | ***DNSdumpster***, ***Google Dorks***, Whois Lookup, ***TheHarvester***. |
    | **Ativo (Intrusivo)** | Coleta com interação direta e intencional com o alvo (ex: consultas DNS específicas, varreduras). | ***Recon-ng***, `dig`, `nslookup`, ***ZAP (Spidering)***. |

    ---

    ## 2. Tarefas de Laboratório: Exemplos de Execução

    ### 2.1. 🌐 Footprinting Passivo de DNS (DNSdumpster)

    * ***Objetivo:*** Obter uma **visão estrutural e topológica** do domínio (registros NS, MX, Hosts e IPs).
    * ***Ação:*** Usar a interface web para buscar o domínio alvo, como por exemplo, `certifiedhacker.com`.

    ***Resultado Esperado:***

    * Lista de Servidores de Nome (**NS**).
    * Lista de Registros **MX** (Mail Exchanger).
    * Hosts/Subdomínios (Registros A) e seus endereços IP.
    * Gráfico visual da infraestrutura (**Topologia**).
    * **Documentação:** Download da lista de hosts em formato `.xlsx` (conforme o manual CEH).

    ### 2.2. 📧 Coleta de E-mails, Subdomínios e Hosts (TheHarvester)

    * ***Objetivo:*** Coletar passivamente endereços de e-mail e nomes de hosts usando ***mecanismos de busca e outras fontes abertas (OSINT)***.

    ***Comando de Exemplo:***

    ```bash
    # -d: domínio alvo
    # -l: limite de resultados (limit)
    # -b: fonte de dados (baidu, google, bing, twitter, etc.)
    # -f: salva o output em um arquivo XML para documentação
    theHarvester -d microsoft.com -l 200 -b baidu -f microsoft_emails.xml
    ```

    ### 2.3. 💻 Reconhecimento Ativo/Semi-Ativo com Recon-ng
    * ***Objetivo:*** Utilizar o framework modular para gerenciar o reconhecimento e automatizar a descoberta de hosts (força bruta de subdomínios)***.

    ***Sequência de Comandos no Terminal Recon-ng:***

    ```bash
    # 1. Inicia o framework
    recon-ng

    # 2. Cria ou entra no Workspace do projeto (opcional, mas recomendado)
    workspaces add CEH

    # 3. Adiciona o domínio alvo ao banco de dados (substitua pelo domínio real)
    db insert domains certifiedhacker.com

    # 4. Carrega o módulo de força bruta de hosts/subdomínios
    modules load recon/domains-hosts/brute_hosts

    # 5. (Opcional) Exibe as opções do módulo
    show options

    # 6. Executa a busca ativa (força bruta)
    run

    # 7. Exibe os hosts (subdomínios) descobertos no banco de dados
    show hosts