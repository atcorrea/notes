exemplo de como instalar plugins: https://stackoverflow.com/questions/18050924/how-to-install-plugins-for-vim/18051764

set relativenumber
" set cursorline
set t_Co=256 "força o terminal a usar 256 cores
set autoindent
set hlsearch
set backspace=indent,eol,start
set ignorecase
set smartcase
set fileencoding=utf8
set nobomb
syntax on

set completeopt=menuone,longest,preview " simple autocomplete for anything
set wildmode=list:longest,full  " autocomplete for paths and files
set wildignore+=.git            " ignore these extensions on autocomplete

let mapleader = " " " map leader to Space
set clipboard=unnamed 

" PLUGINS
set nocompatible               " turns off legacy vi mode
filetype off                   " required!

set rtp+=~/vimfiles/bundle/vundle/
call vundle#begin()

Plugin 'gmarik/vundle'         
Plugin 'tpope/vim-surround'   
Plugin 'easymotion/vim-easymotion'
Plugin 'justinmk/vim-sneak'
Plugin 'preservim/nerdtree'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'dracula/vim', { 'name': 'dracula' }

call vundle#end()

filetype plugin indent on

"Dracula
colorscheme dracula

"EasyMotion
let g:EasyMotion_smartcase = 1
hi link EasyMotionShade  Comment

" Sneak
nmap f <Plug>Sneak_s
nmap F <Plug>Sneak_S

" NERDTree
let NERDTreeShowHidden=1

" Airline
let g:airline_powerline_fonts = 1
let g:airline_theme = 'base16'

" maps
nmap <silent> <F2> :NERDTreeToggle<CR>
nmap <leader>o o<Esc>k
nmap <leader>O O<Esc>j
nmap <CR> o<ESC>
nmap <C-CR> O<ESC>
nmap <C-\> :vsplit<CR>
nmap <C-z> :split<CR>
nmap <C-L> <C-W><C-L>
nmap <C-H> <C-W><C-H>
nmap <C-J> <C-W><C-J>
nmap <C-K> <C-W><C-K>
