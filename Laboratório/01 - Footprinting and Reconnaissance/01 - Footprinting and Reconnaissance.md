## Realizar Footprinting por meio de mecanismos de busca 🔍
`site`: <sub>Restringe os resultados da pesquisa a um site ou domínio específico.</sub><br>
`allinurl`: <sub>Retorna apenas páginas que contêm todos os termos especificados na URL.<sub><br>
`inurl`: <sub>Retorna páginas que contêm uma palavra específica na URL.<sub><br>
`intext`: <sub>Retorna páginas que contêm uma palavra ou frase específica no corpo do texto.<sub><br>
`allintitle`: <sub>Retorna páginas que contêm todos os termos especificados no título da página.<sub><br>
`intitle`: <sub>Restringe os resultados apenas às páginas que contêm o termo especificado no título.<sub><br>
`inanchor`: <sub>Restringe os resultados apenas às páginas que contêm os termos de consulta especificados no texto âncora em links para a página.<sub><br>
`allinanchor`: <sub>Restringe os resultados apenas às páginas que contêm todos os termos de consulta especificados no texto âncora em links para as páginas.<sub><br>
`cache`: <sub>Exibe a versão em cache do Google de uma página da web em vez da versão atual da página.<sub><br>
`link`: <sub>Pesquisa sites ou páginas que contêm links para o site ou página especificados. Não pode ser combinado com palavras-chave comuns e pode ter resultados limitados com outros operadores.<sub><br>
`related`: <sub>Exibe sites semelhantes ou relacionados à URL especificada.<sub><br>
`info`: <sub>Encontra informações para a página da web especificada.<sub><br>
`local`: <sub>Encontra informações sobre um local específico.<sub><br>
`filetype`: <sub>Permite que você pesquise resultados com base em uma extensão de arquivo.<sub><br>
`source`: <sub>Exibe informações de um site específico no Google Notícias.<sub><br>
`phonebook`: <sub>Encontra os números de telefone residenciais e comerciais de uma pessoa ou organização.<sub><br>
`before`: <sub>Filtra os resultados da pesquisa para incluir apenas conteúdo publicado antes de uma data especificada.<sub><br>
`after`: <sub>Encontra informações que foram publicadas após uma determinada data.<sub><br>

## Realizar Footprinting por meio de serviços de pesquisa na internet 🌐
https://sitereport.netcraft.com/<br>
https://dnsdumpster.com/<br>

## Realizar Footprinting por meio de sites de redes sociais 👤
```
 sudo su 
sherlock "Elon musk"
```

## Realizar Footprinting de Whois
https://www.whois.com/whois/<br>


## Realizar Footprinting de DNS


Procurando endereços IP para um site
nslookup > set type=a > www.amazon.com

Verificando registros de nomes canônicos (CNAME)
nslookup > set type=cname > amazon.com

Tentando encontrar um endereço IP para um hostmaster de e-mail
nslookup > set type=a > hostmaster.amazon.com

----------------------------------------------------------------------------------------------

também pode fazer tudo por aqui
http://www.kloth.net/services/nslookup.php

