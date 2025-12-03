## Realizar Footprinting por meio de mecanismos de busca 
<kbd>site</kbd>: Restringe os resultados da pesquisa a um site ou domínio específico.<br>
<span style="color:red;">allinurl</span>: Retorna apenas páginas que contêm todos os termos especificados na URL.<br>
<span style="color:red;">inurl</span>: Retorna páginas que contêm uma palavra específica na URL.<br>
<span style="color:red;">intext</span>: Retorna páginas que contêm uma palavra ou frase específica no corpo do texto.<br>
<span style="color:red;">allintitle</span>: Retorna páginas que contêm todos os termos especificados no título da página.<br>
<span style="color:red;">intitle</span>: Restringe os resultados apenas às páginas que contêm o termo especificado no título.<br>
<span style="color:red;">inanchor</span>: Restringe os resultados apenas às páginas que contêm os termos de consulta especificados no texto âncora em links para a página.<br>
<span style="color:red;">allinanchor</span>: Restringe os resultados apenas às páginas que contêm todos os termos de consulta especificados no texto âncora em links para as páginas.<br>
<span style="color:red;">cache</span>: Exibe a versão em cache do Google de uma página da web em vez da versão atual da página.<br>
<span style="color:red;">link</span>: Pesquisa sites ou páginas que contêm links para o site ou página especificados. Não pode ser combinado com palavras-chave comuns e pode ter resultados limitados com outros operadores.<br>
<span style="color:red;">related</span>: Exibe sites semelhantes ou relacionados à URL especificada.<br>
<span style="color:red;">info</span>: Encontra informações para a página da web especificada.<br>
<span style="color:red;">local</span>: Encontra informações sobre um local específico.<br>
<span style="color:red;">filetype</span>: Permite que você pesquise resultados com base em uma extensão de arquivo.<br>
<span style="color:red;">source</span>: Exibe informações de um site específico no Google Notícias.<br>
<span style="color:red;">phonebook</span>: Encontra os números de telefone residenciais e comerciais de uma pessoa ou organização.<br>
<span style="color:red;">before</span>: Filtra os resultados da pesquisa para incluir apenas conteúdo publicado antes de uma data especificada.<br>
<span style="color:red;">after</span>: Encontra informações que foram publicadas após uma determinada data.<br>


## Realizar Footprinting por meio de serviços de pesquisa na internet 
https://sitereport.netcraft.com/<br>
https://dnsdumpster.com/


## Realizar Footprinting por meio de sites de redes sociais
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

