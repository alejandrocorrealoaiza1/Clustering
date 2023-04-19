from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

#CREATE DATA
X, y = make_blobs(
n_samples=500,
n_features=2,
centers=4,
cluster_std=1,
center_box=(-10.0, 10.0),
shuffle=True,
random_state=1,
)


#PLOT
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

"""TEHRE ARE FOUR CLUSTER, ONE OF THEM IS FAR TO THE OTHERS AND THE OTHER THREE GROUPS ARE VERY CLOSED EACH OTHER, 
HOWEVER IT'S POSIBLE SEE THE SPACE OCCUPIED AND CLEAR DISTANCE BETWEEN THEM"""