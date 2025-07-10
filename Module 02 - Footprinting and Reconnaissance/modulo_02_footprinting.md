# 🚁 CEH v13 - Módulo 02: Footprinting and Reconnaissance

Este laboratório documenta meu estudo completo do módulo 02 do curso **Certified Ethical Hacker v13**, focado nas técnicas e ferramentas de **Footprinting e Reconhecimento** — a primeira etapa prática no ciclo de hacking ético.

---

## 📚 Tópicos Estudados

### 1. Introdução ao Footprinting

- Definição e importância do footprinting
- Objetivos do footprinting: coletar informações sobre o alvo

### 2. Metodologia de Footprinting

- Coleta de informações com base em:
  - Domínio
  - Rede
  - Informações de e-mail
  - Informações sobre funcionários
  - Informações de infraestrutura

### 3. Fases do Footprinting

- **Footprinting Passivo**
- **Footprinting Ativo**

---

## 🔍 Técnicas e Ferramentas

### 4. Footprinting via Mecanismos de Busca

- Uso de **Google Hacking** com `dorks`

#### Exemplos de Dorks:

```bash
intitle:"index of" site:target.com
filetype:pdf site:target.com
site:target.com inurl:admin
```

- Pesquisa por:
  - Diretórios públicos
  - Documentos com metadados
  - Credenciais expostas

---

### 5. Footprinting via Redes Sociais

- Coleta de informações pessoais e organizacionais
- Ferramentas: **Maltego**, **theHarvester**

---

### 6. Footprinting via Websites

- Uso de ferramentas como:
  - **Netcraft**
  - **Whois Lookup**
  - **HTTrack** (cópia de websites)
  - **Web Data Extractors**

---

### 7. Coleta de Informações de DNS

- Consultas com:

```bash
nslookup target.com
whois target.com
```

- Verificação de registros:
  - A, MX, NS, TXT, SOA

#### Ferramentas úteis:

- **DNSdumpster**
- **Fierce**
- **dig**

---

### 8. Coleta de Informações de Rede

- **Traceroute**: descobrir caminhos até o alvo

```bash
traceroute target.com   # Linux
tracert target.com      # Windows
```

- Identificação de blocos IP públicos

---

### 9. Footprinting via E-mail

- Técnicas:
  - Análise de cabeçalhos
  - Engenharia social via e-mail
- Ferramentas: **Email Tracker Pro**, **PoliteMail**

---

### 10. Google Hacking Database (GHDB)

- Uso de comandos de busca avançada para descobrir vulnerabilidades

---

### 11. Informações Públicas e WHOIS

```bash
whois target.com
```

- Informações obtidas:
  - Dono do domínio
  - IPs registrados
  - Informações de contato

---

### 12. Ferramentas Gráficas e Automatizadas

| Ferramenta   | Descrição                                     |
| ------------ | --------------------------------------------- |
| Maltego      | Análise gráfica de relações entre entidades   |
| Recon-ng     | Framework para reconhecimento automatizado    |
| theHarvester | Coleta e-mails, nomes, domínios etc           |
| Shodan       | Scanner de dispositivos conectados à internet |
| FOCA         | Extração de metadados de documentos online    |

---

## 💪 Prática com Comandos e Ferramentas

### Whois

```bash
whois example.com
```

### Nslookup

```bash
nslookup
> set type=mx
> target.com
```

### theHarvester

```bash
theHarvester -d target.com -l 500 -b google
```

### Maltego (GUI)

- Executar transformações automáticas em domínios e pessoas

---

## 📌 Conclusão do Módulo

> Este módulo fortaleceu minha habilidade de **coletar dados essenciais de um alvo** usando diversas fontes públicas e técnicas OSINT. Aprendi a usar ferramentas práticas para footprinting com foco em segurança ofensiva e testes de penetração.

---

## 📌 Próximo Módulo

**Módulo 03: Scanning Networks**

