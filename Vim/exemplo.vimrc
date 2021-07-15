exemplo de como instalar plugins: https://stackoverflow.com/questions/18050924/how-to-install-plugins-for-vim/18051764

```
set relativenumber
set autoindent
set hlsearch
set backspace=indent,eol,start
set ignorecase
set smartcase
set fileencoding=utf8
set nobomb

" PLUGINS
set nocompatible               " turns off legacy vi mode
filetype off                   " required!

set rtp+=~/vimfiles/bundle/vundle/
call vundle#rc()

Bundle 'gmarik/vundle'         
Bundle 'tpope/vim-surround'   
Bundle 'easymotion/vim-easymotion'
Bundle 'justinmk/vim-sneak'

filetype plugin indent on

" Sneak
map f <Plug>Sneak_s
map F <Plug>Sneak_S
```
