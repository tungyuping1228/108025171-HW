
from sklearn.datasets import load_iris
iris_dataset = load_iris()

print("Keys of iris_dataset:In", iris_dataset.keys())



print(iris_dataset ['DESCR'] [:193] + "In.. .. " )

print("Target names:", iris_dataset['target_names'])
