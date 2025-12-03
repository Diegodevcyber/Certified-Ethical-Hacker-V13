## Realizar Footprinting por meio de mecanismos de busca 🔍
`site`: ****Restringe os resultados da pesquisa a um site ou domínio específico.****<br>
`allinurl`: Retorna apenas páginas que contêm todos os termos especificados na URL.<br>
`inurl`: Retorna páginas que contêm uma palavra específica na URL.<br>
`intext`: Retorna páginas que contêm uma palavra ou frase específica no corpo do texto.<br>
`allintitle`: Retorna páginas que contêm todos os termos especificados no título da página.<br>
`intitle`: Restringe os resultados apenas às páginas que contêm o termo especificado no título.<br>
`inanchor`: Restringe os resultados apenas às páginas que contêm os termos de consulta especificados no texto âncora em links para a página.<br>
`allinanchor`: Restringe os resultados apenas às páginas que contêm todos os termos de consulta especificados no texto âncora em links para as páginas.<br>
`cache`: Exibe a versão em cache do Google de uma página da web em vez da versão atual da página.<br>
`link`: Pesquisa sites ou páginas que contêm links para o site ou página especificados. Não pode ser combinado com palavras-chave comuns e pode ter resultados limitados com outros operadores.<br>
`related`: Exibe sites semelhantes ou relacionados à URL especificada.<br>
`info`: Encontra informações para a página da web especificada.<br>
`local`: Encontra informações sobre um local específico.<br>
`filetype`: Permite que você pesquise resultados com base em uma extensão de arquivo.<br>
`source`: Exibe informações de um site específico no Google Notícias.<br>
`phonebook`: Encontra os números de telefone residenciais e comerciais de uma pessoa ou organização.<br>
`before`: Filtra os resultados da pesquisa para incluir apenas conteúdo publicado antes de uma data especificada.<br>
`after`: Encontra informações que foram publicadas após uma determinada data.<br>

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

