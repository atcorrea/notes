# K-means

- Aprendizado não supervisionado
    > K-means clustering is a type of unsupervised learning, which is used when you have unlabeled data (i.e., data without defined categories or groups). The goal of this algorithm is to find groups in the data, with the number of groups represented by the variable K. The algorithm works iteratively to assign each data point to one of K groups based on the features that are provided. Data points are clustered based on feature similarity.   
- Infere informações sobre datasets
- Algorítimo de **Clustering**
  > Clustering is the process of dividing the entire data into groups (also known as clusters) based on the patterns in the data.
- Defina um ***target K***, um número de grupos onde podem se agrupar as informações em um gráfico.
  - Normalmente a área de negócio que define o número de categorias (K)
  - É possível prever o número ótimo de K utilizando o ***elbow method***
- Dentro do gráfico, cada K se torna uma **centroid** que é um ponto imaginário.
  - Centroids podem ser alocados randomicamente no gráfico ou podem ser inseridos 'a olho'
- O algorítmo mede a distância (normalmente ***euclidiana***) dos pontos do gráfico até a centroid, e ao analizar todos, tira uma distância média, isso conclui uma iteração. O algorítmo roda ***n*** iterações até a centroid estar localizada no centro do que se entende como um grupo daquelas informações.
  > the K-means algorithm identifies k number of centroids, and then allocates every data point to the nearest cluster, while keeping the centroids as small as possible.

  > There is an algorithm that tries to minimize the distance of the points in a cluster with their centroid – the k-means clustering technique.

  > The main objective of the K-Means algorithm is to minimize the sum of distances between the points and their respective cluster centroid.

- A distância de um ponto de dado até o centroid é chamada de **intra cluster distance**. A soma de todas as intra cluster distances é chamada de **inertia**.
 > Keeping this in mind, we can say that the lesser the inertia value, the better our clusters are.
- O índice Dunn mede a distância entre os centroids de dois clusters, e é chamada de **inter cluster distance**. Quanto maior o índice Dunn, melhores os clusteres
 - Índice Dunn = min(inter cluster distance) / max(intra cluster distance) 
- Após aplicado o algorítmo, o modelo está pronto para prever em qual cluster (grupo) se encaixariam novos pontos de dados.
- Normalmente utilizado para agrupamento, segmentação de público, etc.

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


## Referências:
- [Understanding K-means Clustering in Machine Learning](https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1)
- [Introduction To K-Means Clustering](https://www.datascience.com/blog/k-means-clustering)
- [The Most Comprehensive Guide to K-Means Clustering You’ll Ever Need](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/)

## Dúvidas:
1. Pq eu limitaria o número de iterações? O que ganhamos com isso?
2. 