# VIM

## Navegação
- **$** => Ir para o final da linha
- **h** => Vai para esquerda 
- **j** => Vai para baixo 
- **k** => Vai para cima 
- **l** => Vai para direita 
- **^** => Ir para o início da linha 
- **gg** => Ir para início da arquivo 
- **G** => Ir para o final do arquivo
- **0** => Vai para o início da linha (desconsidera identação) 
- **w** => Avança uma palavra 
- **b** => Volta uma palavra 
- **/** => Busca para baixo no arquivo
- **?** => Busca para cima no arquivo
- **ctrl + f** => semelhante ao page down 
- **ctrl + b** => semelhante ao page up 

## Edição
- **i** => Entra no modo de inserção 
- **I** => Entra no modo de inserção no início da linha
- **a** => Entra em inserção no caracter seguinte 
- **x** => Apaga um caracter (delete) 
- **X** => Apaga um caracter (backspace) 
- **r** => Substitui um caracter 
- **o** => Começa a digitar na linha de baixo 
- **O** => Começa a digitar na linha de cima 
- **yy** => Copia a linha atual 
- **dd** => recorta a linha atual 
- **p** => Cola da área de transferência do yank (y) 
- **ec** => apaga a palavra e começa a inserção 
- **S** => apaga a linha e começa a inserção 
- **u** => desfaz ultima alteração 
- **ctrl + R** => refaz ultima alteração 
- **dgg** => apaga da linha atual até o final do arquivo 
- **dG** => apaga da linha atual até o inicio do arquivo 
- **d{n}** => apaga n linhas a partir da linha atual 
- **d$** => apaga até o final da linha 

## Visual Mode
- **v** => entra em modo visual (seleção) 
- **ctrl + v** => entra em visual block mode (seleção em coluna) 
- **V** => Visual mode linhas (seleção de linhas) 

## Comandos
- **.** => refaz a ultima ação 
- **w** => salva o arquivo 
- **q** => fecha o arquivo
- **e** => abre outro arquivo para edição 
- **ZZ** => mesma coisa que wq 
- adicionar ! no final para forçar o comando (ex: q! para sair sem salvar) 
- **:split** => divide em dois paineis 
- **:set number** => Exibe os números das linhas 
- **:set ai** => auto ident 
- **:set ic** => ignore case 
- **:%s/{palavraantiga}/{palavranova}/g** => faz subistituição das palavras 
