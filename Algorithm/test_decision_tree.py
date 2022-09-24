from sklearn.datasets import load_iris
from decision_tree import DecisionTreeClassifier
import pandas as pd

data = load_iris()
df = pd.DataFrame(data['data'])
y = data['target']
tree = DecisionTreeClassifier(max_depth =5)

tree.fit(df, y)

tree.plot_tree()