<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Operações: CEH v13</title>
    <style>
        /* Define a animação de movimento da esquerda para a direita e vice-versa */
        @keyframes moveText {
            0% { transform: translateX(-100%); } /* Começa 100% fora da tela à esquerda */
            100% { transform: translateX(100%); } /* Termina 100% fora da tela à direita */
        }

        /* Estilos básicos para o corpo do documento para uma aparência de terminal/hacker */
        body {
            font-family: 'Courier New', Courier, monospace; /* Fonte monoespaçada para estilo hacker */
            background-color: #1a1a1a; /* Fundo escuro */
            color: #e0e0e0; /* Cor do texto principal */
            margin: 20px auto; /* Centraliza o conteúdo horizontalmente */
            padding: 0;
            max-width: 900px; /* Limita a largura do conteúdo para melhor leitura */
            line-height: 1.6;
            box-shadow: 0 0 15px rgba(159, 239, 0, 0.2); /* Sutil brilho verde na borda */
            border-radius: 8px; /* Cantos arredondados */
        }

        /* Estilo para títulos (h1, h2, etc.) */
        h1, h2, h3, h4, h5, h6 {
            color: #9fef00; /* Cor verde vibrante para títulos */
            text-shadow: 0 0 5px rgba(159, 239, 0, 0.5); /* Sutil brilho nos títulos */
            border-bottom: 1px solid #333; /* Linha divisória discreta */
            padding-bottom: 5px;
            margin-top: 30px;
        }

        /* Estilo para a frase animada */
        .animated-phrase {
            color: #9fef00; /* Cor verde vibrante */
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.5em; /* Aumenta um pouco o tamanho */
            overflow: hidden; /* Garante que o texto fora da tela não crie barra de rolagem */
            white-space: nowrap; /* Impede que o texto quebre linha */
            display: inline-block; /* Permite que o transform funcione corretamente */
            animation: moveText 15s linear infinite; /* 15s para a animação, linear, infinito */
            text-shadow: 0 0 8px rgba(159, 239, 0, 0.7); /* Efeito neon mais forte */
            padding: 5px 0; /* Espaçamento para o brilho */
        }

        /* Estilos para a tabela */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #2a2a2a; /* Fundo mais escuro para a tabela */
            border-radius: 5px;
            overflow: hidden; /* Para cantos arredondados com borda */
        }
        table, th, td {
            border: 1px solid #444; /* Bordas da tabela mais claras */
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #3a3a3a; /* Cabeçalho da tabela ainda mais escuro */
            color: #9fef00; /* Cor verde para cabeçalhos */
            text-transform: uppercase;
        }
        tr:nth-child(even) {
            background-color: #202020; /* Fundo listrado para melhor leitura */
        }
        blockquote {
            border-left: 4px solid #9fef00;
            margin-left: 0;
            padding-left: 15px;
            color: #b0b0b0;
            font-style: italic;
        }
        ul {
            list-style-type: '⚡ '; /* Ícone personalizado para listas */
            padding-left: 20px;
        }
        ul li {
            margin-bottom: 5px;
        }
        em {
            color: #9fef00; /* Destaca o texto em itálico */
        }
        strong {
            color: #fff; /* Destaca texto em negrito */
        }
        a {
            color: #00bfff; /* Cor de link */
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<p align="center" style="text-align: center;">
    <span class="animated-phrase">
        DESCRIPTOGRAFANDO O FUTURO: CÓDIGO ESTRATÉGICO EM MOVIMENTO
    </span>
</p>

<p align="center">
    <h1>🚀 Relatório de Operações: CEH v13 🚀</h1>
</p>

<p align="center">
   <em>Desvendando o cenário cibernético: Hacking Ético e Cybersegurança na prática.</em>
</p>

<hr style="border-top: 1px dashed #444; margin: 30px 0;">

## 🎯 Visão Geral do Projeto

Este repositório é um **compêndio abrangente e consolidado** de todo o conhecimento, metodologias, ferramentas e práticas desenvolvidas durante o programa de certificação **CEH v13 (Certified Ethical Hacker)**. Ele serve como um registro detalhado da minha jornada em segurança ofensiva, abordando as táticas e técnicas utilizadas por adversários para identificar e mitigar vulnerabilidades em sistemas e redes.

> "A segurança é um processo, não um produto." - Bruce Schneier

Este projeto demonstra a capacidade de:
* Realizar varreduras e reconhecimento de forma ética.
* Analisar vulnerabilidades e explorar sistemas.
* Compreender e mitigar ameaças como *malware* e ataques de *engenharia social*.
* Aplicar técnicas avançadas de evasão e proteção.

<hr style="border-top: 1px dashed #444; margin: 30px 0;">

## 📂 Estrutura do Repositório: Mapeamento de Conhecimento

A organização deste repositório foi meticulosamente planejada para espelhar a estrutura modular do curso CEH v13, facilitando a navegação e o acesso ao conteúdo específico. Cada diretório principal corresponde a um módulo, e contém subdiretórios ou arquivos para laboratórios e materiais complementares.

Dentro de cada pasta de módulo, você encontrará uma compilação de:
* **Documentação Teórica**: Anotações, resumos e conceitos-chave do módulo.
* **Códigos e Scripts**: Implementações práticas, *proofs of concept* (PoCs) e exemplos de uso de ferramentas.
* **Resultados de Laboratórios**: Evidências, configurações e *logs* de exercícios práticos.

<hr style="border-top: 1px dashed #444; margin: 30px 0;">

## ⚙️ Módulos de Conhecimento: Detalhamento por Domínio

A seguir, a discriminação dos módulos do CEH v13 abordados neste repositório, cada um representando um domínio crítico na segurança cibernética:

| Módulo | Tópico Principal | Conteúdo Programático Essencial |
| :----- | :--------------- | :------------------------------ |
| `01`   | Introdução ao Ethical Hacking | Fundamentos, fases do hacking e princípios éticos. |
| `02`   | Footprinting e Reconnaissance | Coleta de informações: passiva, ativa (OSINT, Whois, etc.). |
| `03`   | Scanning Networks | Varredura de rede, descoberta de hosts, portas e serviços. |
| `04`   | Enumeration | Identificação detalhada de usuários, recursos e serviços de rede. |
| `05`   | Vulnerability Analysis | Escaneamento e análise sistemática de vulnerabilidades. |
| `06`   | System Hacking | Exploração de sistemas operacionais e técnicas de escalonamento de privilégios. |
| `07`   | Malware | Análise de diversos tipos de *malware*, infecção e prevenção. |
| `08`   | Sniffing | Interceptação e análise de tráfego de rede para extração de informações. |
| `09`   | Social Engineering | Ataques baseados em manipulação psicológica e suas contramedidas. |
| `10`   | Denial-of-Service | Ataques de negação de serviço (DoS/DDoS) e estratégias de mitigação. |
| `11`   | Session Hijacking | Roubo e exploração de sessões de comunicação ativas. |
| `12`   | Evading IDS, Firewalls, and Honeypots | Técnicas para bypass de sistemas de segurança e detecção. |
| `13`   | Hacking Web Servers | Avaliação de segurança e ataques comuns a servidores web. |
| `14`   | Hacking Web Applications | Exploração de vulnerabilidades em aplicações web (foco no OWASP Top 10). |
| `15`   | SQL Injection | Técnicas de injeção SQL para comprometer bancos de dados. |
| `16`   | Hacking Wireless Networks | Segurança e ataques a redes sem fio (Wi-Fi). |
| `17`   | Hacking Mobile Platforms | Análise de vulnerabilidades em dispositivos e aplicações móveis. |
| `18`   | IoT and OT Hacking | Desafios de segurança em Internet das Coisas (IoT) e Tecnologia Operacional (OT). |
| `19`   | Cloud Computing | Riscos de segurança e melhores práticas em ambientes de nuvem. |
| `20`   | Cryptography | Fundamentos, algoritmos e análise de vulnerabilidades criptográficas. |

<hr style="border-top: 1px dashed #444; margin: 30px 0;">

## 🤝 Contato e Colaboração

Este repositório é um artefato da minha expertise no CEH v13. Para quaisquer dúvidas, insights ou propostas de colaboração técnica relativas ao conteúdo, sinta-se à vontade para entrar em contato.

<hr style="border-top: 1px dashed #444; margin: 30px 0;">

## 📄 Licença de Uso

Todo o material contido neste repositório é distribuído sob a licença [MIT License](LICENSE). Esteja à vontade para explorar, aprender e utilizar o conteúdo para seus estudos e pesquisas pessoais, em conformidade com os termos especificados.

<hr style="border-top: 1px dashed #444; margin: 30px 0;">

<p align="center">
   <em>Análise. Exploração. Proteção.</em>
   <br>
   <span>D1xgxs3c &copy; 2025 - CyberOps</span>
</p>

</body>
</html>
