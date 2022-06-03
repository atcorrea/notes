# VIM

## Navegação
- **$** => Ir para o final da linha
- **h** => Vai para esquerda 
- **j** => Vai para baixo 
- **k** => Vai para cima 
- **l** => Vai para direita 
- **^** => Ir para o inicio da linha 
- **gg** => Ir para inicio da arquivo 
- **G** => Ir para o final do arquivo
- **0** => Vai para o inicio da linha (desconsidera identação) 
- **w** => Avança uma palavra 
- **W** => Avança uma palavra (ignora .)
- **b** => Vai para o inicio da palavra 
- **e** => Vai para o final da palavra 
- **/** => Busca para baixo no arquivo
- **?** => Busca para cima no arquivo
- **H** => Primeira linha a vista 
- **L** => Ultima linha a vista 
- **{n}G** => Vai ate a {n} linha 
- **%** => vai até o fechamento do escopo **) ou }**
- **ctrl + u** => page up (meia tela)
- **ctrl + d** => page down (meia tela)
- **ctrl + f** => page down (tela inteira)
- **ctrl + b** => page up (tela inteira)
- **<leader>/busca** => executa um comando (ex: c, d, y) até a busca. / pesquisa para baixo e ? pesquisa para cima.
- **m{tecla}** => marca um ponto no arquivo a uma letra. ex.  ```m1``` marca a linha na tecla ```1```.
- **'{tecla}** => vai até o ponto marcado com o comando m. ex ```'1``` vai ate o ponto marcado com ```m1```.

## Busca
- **\*** => busca ocorrencias da palavra que o cursor esta em cima

## Edição
- **i** => Entra no modo de inseção 
- **I** => Entra no modo de inseção no início da linha
- **A** => Entra no modo de inserção no final da linha
- **a** => Entra em inserção no caracter seguinte (append)
- **x** => Apaga um caracter (delete) 
- **X** => Apaga um caracter (backspace) 
- **r** => Substitui um caracter 
- **o** => começa a digitar na linha de baixo 
- **O** => começa a digitar na linha de cima 
- **yy** => Copia a linha atual 
- **Y** => Copia a linha atual 
- **dd** => recorta a linha atual 
- **p** => Cola da área de transferência do VIM (pego com y ou d)
- **cw** => apaga a palavra e começa a inserção 
- **s** => apaga caracter e começa inserção
- **S** => apaga a linha e começa a inserção 
- **cc** => apaga a linha e começa a inserção 
- **C** => apaga counteudo da linha após o cursor e entra em inserção (similar a d$)
- **u** => desfaz ultima alteração 
- **ctrl + R** => refaz ultima alteração 
- **dgg** => apaga da linha atual até o final do arquivo 
- **dG** => apaga da linha atual até o inicio do arquivo 
- **d{n}** => apaga n linhas a partir da linha atual 
- **d$** => apaga da posição do cursor até o final da linha
- **D** => apaga da posição do cursor até o final da linha 
- **J** => junta linha de baixo no final da atual
- **di<"|'|)|}> => deleta tudo até o caracter especificado (bom para apagar tudo dentro de uma string por exemplo)
- **{n}=** => corrige identação para um numero informado de linhas
	> gg=G formataria o arquivo inteiro
	> == formata somente a linha atual
	> =% formata até o final do método

## Visual Mode
- **v** => entra em modo visual (seleção) 
- **ctrl + v** => entra em visual block mode (seleção em coluna) 
- **V** => Visual mode linhas (seleção de linhas) 

## Comandos
- **:h {tecla}** => mostra ajuda para comando associados aquela tecla
- **ZZ** => mesma coisa que wq 
- **.** => refaz a ultima ação 
- **:w** => salva o arquivo 
- **:q** => fecha o arquivo
- **:e** => abre outro arquivo para edição 
- **:m {numero da linha}** => move a linha selecionada para o numero de linha solicitado
- adicionar ! no final para forçar o comando (ex: q! para sair sem salvar) 
- **:split** => divide em dois paineis 
- **:set number** => Exibe os números das linhas 
- **:set ai** => auto ident 
- **:set ic** => ignore case 
- **:{n}s/{palavraantiga}/{palavranova}/g** => faz substituição das palavras 
	> s é o comando 'substitute' e o **n** é o range para aplicar a substitução. Ex. ```:1-10s``` aplica o comando da linha 1 até a linha 10. Podemos utilizar o **%** para aplicar no arquivo todo.
- **:g/pattern/d** => remove linhas que tem determinado padrão
	> :g! para negativa do pattern (:v também faz o mesmo)
- **:v/pattern/d** => remove linhas que não tem determinado padrão
- **:sort** => organiza as linhas selecionadas em ordem alfabetica
- **:g/{pattern}/:{comando}** => executa o determinado comando para o padrão selecionado

## Combinações bacanas
- :g/^/m 0 => troca as linhas do arquivo.
- :g/{pattern}/normal {@macro} => executa a macro nas linhas com o padrão selecionado

## Cool Plugins
- NERDTree (https://github.com/preservim/nerdtree)
- Surround (https://github.com/tpope/vim-surround)
- Sneak (https://github.com/justinmk/vim-sneak)
- EasyMotion (https://github.com/easymotion/vim-easymotion)

## Surround Plugin
- **cs{old}{new}** => troca caracter em volta de palavras. Ex. trocar ```"palavras a"``` por ```'palavras a'```.
	> pode se usar t para identificar tag xml ou html.
- **ds{char}** => exclui caracter em volta das palavras. Ex. trocar ```"palavras a"``` por ```palavras a```.  
- **ysw{char}** => adiciona caracter em volta de palavras. Ex. trocar ```palavras a``` por ```"palavras a"```.

