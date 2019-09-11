# Distributed processing
- As entidades individuais em um sistema distribuído são chamadas de **nós** (nodes).
- "The nodes in a distributed system run their own operations - these operations are *fast* but the nodes also communicate with each other - communication is *slow*!"
- Comunicação entre nós é um dos maiores problemas da computação distribuída.
- 

# Run Time Complexity (Big O Notation)
- Descreve a performance de um algoritmo;
- **Tipos:**
  - constant (O(1))
  - linear (O(n)) -> iterate whole collection
  - quadratic (O(n²))
  - quasilinear (O(n * log(n))) -> sorting
  - logarithimic (O(log(n))) -> search
  - exponential (O(2 ^ n))
- **Tips:**
  - Iterating Simple Collection?
    ```Probabbly O(n)```
  - Iterating half a Collection?
    ```O(n)```
  - Iterating two **different collections** with separate for loops?
    ```O(n + m)```
  - Two nested for loops iterating the **same** collection?
    ```O(n^2)```
  - Two nested for loops iterating **diferent** collections?
    ```O(n*m)```
  - sorting?
    ```O(n*log(n))```
  - searching a sorted array?
    ```O(log(n))```