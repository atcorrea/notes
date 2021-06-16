# Notes

```dockerfile
# cria um volume no respectivo caminho do container, caso seja especificado um caminho local monta o volume local no volume do container.
docker run -v "[CAMINHO_VOLUME_LOCAL:]CAMINHO_VOLUME_CONTAINER" NOME_DA_IMAGEM
```

```dockerfile
# retorna diversas informações sobre o container.
docker inspect ID_CONTAINER
```

```dockerfile
# constrói e nomeia uma imagem não-oficial informando o caminho para o Dockerfile.
docker build -f CAMINHO_DOCKERFILE/Dockerfile -t NOME_USUARIO/NOME_IMAGEM
```

```dockerfile
# para o container e o remove
docker rm -f <ID>
```

```dockerfile
# pushar imagem para registry
docker login
docker push <imagem>
```

```dockerfile
# mantem container rodando sem processo
CMD tail -f /dev/null
```
