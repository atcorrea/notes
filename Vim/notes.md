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
- **b** => Volta uma palavra 
- **/** => Busca para baixo no arquivo
- **?** => Busca para cima no arquivo
- **ctrl + f** => semelhante ao page down 
- **ctrl + b** => semelhante ao page up 

## Edi��o
- **i** => Entra no modo de inser��o 
- **I** => Entra no modo de inser��o no in�cio da linha
- **a** => Entra em inser��o no caracter seguinte 
- **x** => Apaga um caracter (delete) 
- **X** => Apaga um caracter (backspace) 
- **r** => Substitui um caracter 
- **o** => Come�a a digitar na linha de baixo 
- **O** => Come�a a digitar na linha de cima 
- **yy** => Copia a linha atual 
- **dd** => recorta a linha atual 
- **p** => Cola da �rea de transfer�ncia do yank (y) 
- **ec** => apaga a palavra e come�a a inser��o 
- **S** => apaga a linha e come�a a inser��o 
- **u** => desfaz ultima altera��o 
- **ctrl + R** => refaz ultima altera��o 
- **dgg** => apaga da linha atual at� o final do arquivo 
- **dG** => apaga da linha atual at� o inicio do arquivo 
- **d{n}** => apaga n linhas a partir da linha atual 
- **d$** => apaga at� o final da linha 

## Visual Mode
- **v** => entra em modo visual (sele��o) 
- **ctrl + v** => entra em visual block mode (sele��o em coluna) 
- **V** => Visual mode linhas (sele��o de linhas) 

## Comandos
- **.** => refaz a ultima a��o 
- **w** => salva o arquivo 
- **q** => fecha o arquivo
- **e** => abre outro arquivo para edi��o 
- **ZZ** => mesma coisa que wq 
- adicionar ! no final para for�ar o comando (ex: q! para sair sem salvar) 
- **:split** => divide em dois paineis 
- **:set number** => Exibe os n�meros das linhas 
- **:set ai** => auto ident 
- **:set ic** => ignore case 
- **:%s/{palavraantiga}/{palavranova}/g** => faz subistitui��o das palavras 
