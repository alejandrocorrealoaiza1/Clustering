# Clustering

Workshop II

1. Research about the Spectral Clustering method, and answer the following questions:
a. In which cases might it be more useful to apply?
b. What are the mathematical fundamentals of it?
c. What is the algorithm to compute it?
d. Does it hold any relation to some of the concepts previously mentioned in class? Which, and how?

2. Research about the DBSCAN method, and answer the following questions:
a. In which cases might it be more useful to apply?
b. What are the mathematical fundamentals of it?
c. Is there any relation between DBSCAN and Spectral Clustering? If so, what is it?

3. What is the elbow method in clustering? And which flaws does it pose to assess quality?

4. Remember the unsupervised Python package you created in the previous unit?
a. Implement the k-means module using Python and Numpy
b. Implement the k-medoids module using Python and Numpy

5. Let’s use the newly created modules in unsupervised to cluster some toy data.
a. Use the code snippet to create scattered data X
b. Plot the resulting dataset. How many clusters are there? How far are they from one another?
c. For both k-means and k-medoids (your implementations), calculate the silhouette plots and
coefficients for each run, iterating K from 1 to 5 clusters.
d. What number of K got the best silhouette score? What can you say about the figures? Is this the
expected result?

6. Use the code snippet to create different types of scattered data:
a. Plot the different datasets in separate figures. What can you say about them?
b. Apply k-means, k-medoids, DBSCAN and Spectral Clustering from Scikit-Learn over each
dataset and compare the results of each algorithm with respect to each dataset.