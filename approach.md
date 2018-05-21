### Known Information

1. Data is 3-Dimensional (USER, ITEMS, INTERACTIONS)
2. 2 Dimensions (USER and ITEMS) shall vary with time
3. Dimension of Interaction is Fixed (4 D)

### Papers

1. [Original Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6822125)
2. [Matrix Factorization Techniques](https://arxiv.org/pdf/1503.07475.pdf)
3. [Scalable Techniques](http://delivery.acm.org/10.1145/2130000/2124312/p123-ahmed.pdf?ip=202.3.77.209&id=2124312&acc=ACTIVE%20SERVICE&key=045416EF4DDA69D9%2E6454B2DFDB9CC807%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1526727016_6f11754765626b1d2863dd74e4a33ef9)
4. [Online Learning](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6252670&tag=1)
5. [Demographical Info Usage](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.735.1474&rep=rep1&type=pdf)
6. [Neural Network based Hybrid Technique](https://hal.archives-ouvertes.fr/hal-01281794v1/document)
7. [Large Scale Parallel technique for Collaborative Filtering](https://link.springer.com/content/pdf/10.1007%2F978-3-540-68880-8_32.pdf%20Avik)
8. [Scalable Inference for latent variable models](https://dl.acm.org/citation.cfm?id=2124312)
9. [latent source modelfor online collab filtering](https://arxiv.org/pdf/1411.6591.pdf)
10. [high frequency collab filtering](https://link.springer.com/content/pdf/10.1007%2F978-3-319-25255-1_41.pdf)
11. [multi-task CF for on-the-fly recommender system](https://dl.acm.org/citation.cfm?id=2507176)
12. [online learning for CF](https://ieeexplore.ieee.org/document/6252670/)
### Previous Implementations

1. [Factorizer](https://github.com/katbailey/factorizer)
2. [Tensorrec](https://github.com/jfkirk/tensorrec)
3. [NVIDIA Autoencoders](https://github.com/NVIDIA/DeepRecommender)

### Timeline

1. Algorithm to handle variability in the first 2 dimensions
2. Ways to handle 3 dimensional data:
	* Some form of averaging of the interactions
	* Consider 4 different matrices and append results at the end
3. Prediction method speed testing
	* Matrix Factorization
	* Deep Learning with Auto Encoders
