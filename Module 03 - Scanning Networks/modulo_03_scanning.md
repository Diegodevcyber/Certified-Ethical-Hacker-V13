# 📡 CEH v13 - Módulo 03: Scanning Networks

Este laboratório documenta todo o conteúdo técnico e prático do **Módulo 03 do CEH v13**, que aborda o processo de **varredura de redes (network scanning)**, uma das fases críticas do hacking ético.

---

## 📚 Tópicos Estudados

### 1. Introdução ao Scanning

- Conceito de Scanning
- Objetivos da varredura de rede
- Diferença entre Scanning e Footprinting

### 2. Tipos de Scanning

- Scanning de portas
- Scanning de vulnerabilidades
- Scanning de rede

### 3. Técnicas de Descoberta de Host (Host Discovery)

- ICMP Echo Request
- TCP SYN/ACK
- Ferramentas:
  - `ping`
  - `nmap -sn`

### 4. Técnicas de Scanning de Portas

- Full Connect (TCP Connect)
- Half-Open (SYN Scan)
- Stealth Scans (FIN, Xmas, Null)
- UDP Scan
- TCP ACK Scan
- Window Scan

#### Exemplos:

```bash
nmap -sS target.com         # SYN Scan
nmap -sT target.com         # TCP Connect
nmap -sU target.com         # UDP Scan
nmap -sA target.com         # ACK Scan
```

---

## 🔍 Mapeamento de Rede com Nmap

### Opções úteis:

```bash
nmap -sP 192.168.1.0/24     # Ping sweep
nmap -O target.com          # Detectar sistema operacional
nmap -sV target.com         # Versão do serviço
nmap -A target.com          # OS + versão + traceroute + script
```

### Scan de múltiplos alvos:

```bash
nmap 192.168.1.1 192.168.1.2 192.168.1.3
```

---

## 🔐 Detecção de Serviços e Versões

- Identificação de serviços em execução e suas versões
- Ferramenta: `nmap -sV`
- Combinação com detecção de SO: `nmap -A`

---

## 🛡️ Detecção de Sistemas Operacionais (OS Fingerprinting)

- TCP/IP Stack Fingerprinting
- Ferramenta: `nmap -O`
- Técnicas:
  - TTL analysis
  - Window size
  - TCP options

---

## 🧪 Detecção de Vulnerabilidades

- Integração do Nmap com scripts NSE:

```bash
nmap --script vuln target.com
```

- Ferramentas complementares:
  - Nessus
  - OpenVAS
  - Nexpose

---

## 🔬 Técnicas de Bypass de Firewalls

- Fragmentação de pacotes
- Scans disfarçados (Xmas, Null, FIN)
- Uso de proxies e VPNs

---

## ⚙️ Ferramentas Adicionais

| Ferramenta  | Finalidade                              |
| ----------- | --------------------------------------- |
| Nmap        | Scanning, OS/service detection, scripts |
| Unicornscan | Scanning de alto desempenho             |
| Masscan     | Scanning extremamente rápido            |
| Netcat      | Comunicação de rede, banner grabbing    |
| Hping       | Packet crafting e scans personalizados  |

---

## 💪 Prática com Ferramentas

### Banner Grabbing com Netcat

```bash
nc -v target.com 80
```

### TCP Handshake Manual com Hping3

```bash
hping3 -S -p 80 target.com
```

---

## 🧠 Observações Pessoais

> Este módulo foi crucial para entender como mapear uma rede, identificar serviços e explorar vulnerabilidades. Aprendi a usar o **Nmap** em profundidade e a aplicar estratégias evasivas contra firewalls.

---

## 🔜 Próximo Módulo

**Módulo 04: Enumeration**

