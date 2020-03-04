# Dates

## Criando data a partir de uma string:
```python
from datetime import *
dat = "Wed, 26 Feb 2020 22:43:00 GMT"
pubDate = datetime.strptime(dat, "%a, %d %b %Y %H:%M:%S %Z")

year = pubDate.year
month = pubDate.month
day = pubDate.day
```

## Formatando uma data em uma string
```python
from datetime import *
dt = datetime.now()
pubDate = datetime.strftime(dt, "%d/%m/%Y")
```

## Referências:
- [Tabela formatação](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
