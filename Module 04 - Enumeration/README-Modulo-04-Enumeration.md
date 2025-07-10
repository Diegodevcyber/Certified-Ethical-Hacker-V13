# 🧾 CEH v13 - Módulo 04: Enumeration

Este laboratório reúne os principais conceitos, ferramentas e comandos práticos estudados no **Módulo 04 do CEH v13**, dedicado à fase de **Enumeração** — quando o atacante interage ativamente com os sistemas alvo para extrair informações úteis.

---

## 📚 Tópicos Estudados

### 1. Introdução à Enumeração
- Definição e objetivo da enumeração
- Diferença entre Scanning e Enumeration
- Importância na coleta de informações pós-scanning

### 2. Tipos de Enumeração
- Enumeração de usuários
- Enumeração de grupos e recursos compartilhados
- Enumeração de serviços de rede
- Enumeração de vulnerabilidades

---

## 🔐 Protocolos e Serviços Alvo

### 3. Enumeração de NetBIOS
- Uso de `nbtstat`:
```bash
nbtstat -A [IP]
nbtstat -a [hostname]
```
- Ferramentas: **NBTscan**, **Hyena**, **SoftPerfect Network Scanner**

### 4. Enumeração de SNMP
- Coleta de informações de dispositivos de rede
- Comandos SNMP:
```bash
snmpwalk -v1 -c public [IP]
snmp-check [IP]
```
- Ferramentas: **SNMPUtil**, **OpUtils**, **SolarWinds IP Network Browser**

### 5. Enumeração LDAP
- Listagem de usuários, grupos, atributos de diretório
- Ferramentas: **JXplorer**, **LDAP Admin Tool**, `ldapsearch`

```bash
ldapsearch -x -h [IP] -b "dc=exemplo,dc=com"
```

### 6. Enumeração SMTP
- Identificação de usuários válidos via resposta de erro
- Técnicas:
  - VRFY, EXPN, RCPT TO

```bash
telnet target.com 25
HELO test
VRFY joao
```

### 7. Enumeração RPC
- Identificação de serviços e interfaces remotas
- Ferramentas: **rpcinfo**, **ShowMount**, **rpcclient**

```bash
rpcinfo -p [IP]
rpcclient -U "" [IP]
```

### 8. Enumeração NFS
- Verificar diretórios compartilhados anonimamente

```bash
showmount -e [IP]
```

---

## 🧰 Ferramentas Populares

| Ferramenta          | Descrição                                 |
|---------------------|---------------------------------------------|
| enum4linux          | Enumeração de Windows via SMB              |
| NBTscan             | Descoberta de NetBIOS                      |
| SNMPWalk            | Coleta SNMP                                |
| rpcclient           | Enumeração RPC                             |
| ldapsearch          | Enumeração de diretórios LDAP              |
| smtp-user-enum      | Enumeração de usuários via SMTP            |
| Nessus/OpenVAS      | Identificação de vulnerabilidades           |

---

## 💪 Exemplos de Uso

### Enumeração SMB com enum4linux
```bash
enum4linux -a [IP]
```

### Enumeração SNMP com snmpwalk
```bash
snmpwalk -v2c -c public [IP]
```

### Enumeração de serviços RPC
```bash
rpcinfo -p [IP]
rpcclient -U "" [IP]
```

---

## 🧠 Observações Pessoais

> A enumeração é uma etapa ativa e essencial do hacking ético. Aprendi a usar protocolos padrão para extrair detalhes internos de sistemas-alvo. Essas técnicas se mostraram poderosas, principalmente contra configurações fracas ou mal protegidas.

---

## 🔜 Próximo Módulo
**Módulo 05: Vulnerability Analysis**
