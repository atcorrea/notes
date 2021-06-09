# VIM

## Navega��o
- **$** => Ir para o final da linha
- **h** => Vai para esquerda 
- **j** => Vai para baixo 
- **k** => Vai para cima 
- **l** => Vai para direita 
- **^** => Ir para o in�cio da linha 
- **gg** => Ir para in�cio da arquivo 
- **G** => Ir para o final do arquivo
- **0** => Vai para o in�cio da linha (desconsidera identa��o) 
- **w** => Avan�a uma palavra 
- **W** => Avan�a uma palavra (ignora .)
- **b** => Vai para o inicio da palavra 
- **e** => Vai para o final da palavra 
- **/** => Busca para baixo no arquivo
- **?** => Busca para cima no arquivo
- **H** => Primeira linha a vista 
- **L** => Ultima linha a vista 
- **{n}G** => Vai ate a {n} linha 
- **%** => vai at� o fechamento do escopo **) ou }**
- **ctrl + u** => page up (meia tela)
- **ctrl + d** => page down (meia tela)
- **ctrl + f** => page down (tela inteira)
- **ctrl + b** => page up (tela inteira)
- **<leader>/busca** => executa um comando (c, d, y) at� a busca. / � pesquisa para baixo e ? pesquisa para cima.

## Edi��o
- **i** => Entra no modo de inser��o 
- **I** => Entra no modo de inser��o no in�cio da linha
- **A** => Entra no modo de inser��o no final da linha
- **a** => Entra em inser��o no caracter seguinte (append)
- **x** => Apaga um caracter (delete) 
- **X** => Apaga um caracter (backspace) 
- **r** => Substitui um caracter 
- **o** => Come�a a digitar na linha de baixo 
- **O** => Come�a a digitar na linha de cima 
- **yy** => Copia a linha atual 
- **Y** => Copia a linha atual 
- **dd** => recorta a linha atual 
- **p** => Cola da �rea de transfer�ncia do VIM (pego com y ou d)
- **cw** => apaga a palavra e come�a a inser��o 
- **s** => apaga caracter e come�a inser��o
- **S** => apaga a linha e come�a a inser��o 
- **cc** => apaga a linha e come�a a inser��o 
- **C** => apaga counteudo da linha ap�s o cursor e entra em inser��o (similar a d$)
- **u** => desfaz ultima altera��o 
- **ctrl + R** => refaz ultima altera��o 
- **dgg** => apaga da linha atual at� o final do arquivo 
- **dG** => apaga da linha atual at� o inicio do arquivo 
- **d{n}** => apaga n linhas a partir da linha atual 
- **d$** => apaga da posi��o do cursor at� o final da linha
- **D** => apaga da posi��o do cursor at� o final da linha 
- **J** => junta linha de baixo no final da atual
- **di<"|'|)|}> => deleta tudo at� o caracter especificado (bom para apagar tudo dentro de uma string por exemplo)

## Visual Mode
- **v** => entra em modo visual (sele��o) 
- **ctrl + v** => entra em visual block mode (sele��o em coluna) 
- **V** => Visual mode linhas (sele��o de linhas) 

## Comandos
- **ZZ** => mesma coisa que wq 
- **.** => refaz a ultima a��o 
- **:w** => salva o arquivo 
- **:q** => fecha o arquivo
- **:e** => abre outro arquivo para edi��o 
- adicionar ! no final para for�ar o comando (ex: q! para sair sem salvar) 
- **:split** => divide em dois paineis 
- **:set number** => Exibe os n�meros das linhas 
- **:set ai** => auto ident 
- **:set ic** => ignore case 
- **:%s/{palavraantiga}/{palavranova}/g** => faz subistitui��o das palavras 

## Cool Plugins
- NERDTree
- Surround (https://github.com/tpope/vim-surround)
- Sneak (https://github.com/justinmk/vim-sneak)