 
 ## Realizar Footprinting por meio de mecanismos de busca
 
 <img src="https://github.com/Diegodevcyber/Certified-Ethical-Hacker-V13/blob/main/public/images/Footprinting%20and%20Reconnaissance/1.png">

## Realizar Footprinting por meio de serviços de pesquisa na internet

https://sitereport.netcraft.com/<br>
https://dnsdumpster.com/

## Realizar Footprinting por meio de sites de redes sociais

```python
sudo su 
sherlock "Elon musk"
```
## Realizar Footprinting de Whois

```python
https://www.whois.com/whois/

```
## Realizar Footprinting de DNS

**Procurando endereços IP para um site**
```python
nslookup > set type=a > www.amazon.com
```
**Verificando registros de nomes canônicos (CNAME)**
```python
nslookup > set type=cname > amazon.com
```
**Tentando encontrar um endereço IP para um hostmaster de e-mail**
```python
nslookup > set type=a > hostmaster.amazon.com
```
**também pode fazer tudo por aqui**
```python
http://www.kloth.net/services/nslookup.php
```

