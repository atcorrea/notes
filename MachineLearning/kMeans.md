# K-means

- Aprendizado não supervisionado
- Infere informações sobre datasets
- Algorítimo de **Clustering**
  > A cluster refers to a collection of data points aggregated together because of certain similarities.

- Defina um ***target K***, um número de grupos onde podem se agrupar as informações em um gráfico.
  - Normalmente a área de negócio que define o número de categorias (K)
  - É possível prever o número ótimo de K utilizando o ***elbow method***
- Dentro do gráfico, cada K se torna uma **centroid** que é um ponto imaginário.
- O algorítmo mede a distância (normalmente ***euclidiana***) dos pontos do gráfico até a centroid, e ao analizar todos, tira uma distância média, isso conclui uma iteração. O algorítmo roda ***n*** iterações até a centroid estar localizada no centro do que se entende como um grupo daquelas informações.
  > the K-means algorithm identifies k number of centroids, and then allocates every data point to the nearest cluster, while keeping the centroids as small as possible.
- Após aplicado o algorítmo, o modelo está pronto para prever em qual cluster (grupo) se encaixariam novos pontos de dados.


## Exemplos:
### Python (scikit learn)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

X= -2 * np.random.rand(100,2)
X1 = 1 + 2 * np.random.rand(50,2)
X[50:100, :] = X1
plt.scatter(X[ : , 0], X[ :, 1], s = 50, c = ‘b’)

Kmean = KMeans(n_clusters=2)
Kmean.fit(X)
centroids = Kmean.cluster_centers_

plt.scatter(X[ : , 0], X[ : , 1], s =50, c=’b’)
plt.scatter(centroids[0,0], centroids[0,1], s=200, c=’g’, marker=’s’)
plt.scatter(centroids[1,0], centroids[1,1], s=200, c=’r’, marker=’s’)
plt.show()

sample_test=np.array([-3.0,-3.0])
second_test=sample_test.reshape(1, -1)
Kmean.predict(second_test)
```
- **Pandas** for reading and writing spreadsheets
- **Numpy** for carrying out efficient computations 
  - --> Gera datasets aleatórios
- **Matplotlib** for visualization of data
  - --> Gráficos fáceis


### Referências:
[Understanding K-means Clustering in Machine Learning](https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1)