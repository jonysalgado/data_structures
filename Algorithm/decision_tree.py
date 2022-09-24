from math import log
from typing import List, Union
from collections import Counter
import numpy as np
import pandas as pd
from collections import Counter
import dash
import dash_cytoscape as cyto
from collections import deque

class Decision_node:
    def __init__(self, feature=None, split_value=None, info_gain=None):
        self.feature = feature
        self.split_value = split_value
        self.info_gain = info_gain
        self.left = None
        self.right = None

class Leaf_node:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.label = Counter(y).most_common()[0][0]
    

class DecisionTreeClassifier:
    
    def __init__(self, max_depth=float('inf'), minimal_node_size=2, criterion='entropy'):
        self.max_depth = max_depth
        self.minimal_node_size = minimal_node_size
        self.criterion = criterion
        self.root = None

    def get_entropy(self, input: List[int|float]) -> float:
        
        n = len(input)
        P = [p/n for p in Counter(input).values()]
        H = -sum([p * log(p, 2) for p in P])
        return H

    def info_gain(self, lst: List[Union[int,float]], lst1: List[Union[int,float]], lst2: List[Union[int,float]]) -> float:

        return self.get_entropy(lst)                               \
                    - self.get_entropy(lst1) * len(lst1)/len(lst)  \
                    - self.get_entropy(lst2) * len(lst2)/len(lst)

    def calculateMaxInfoGain(self, feature: List[float], classes: List[str]) -> float:
            
            
        data = sorted(zip(feature, classes), key=lambda x: x[0])
        sorted_classes = [x[1] for x in data]
            
        max_gain = 0
        value_to_split = None
        for i in range(len(data)):
            actual_gain = self.info_gain(sorted_classes, sorted_classes[:i], sorted_classes[i:])
            if actual_gain > max_gain:
                max_gain = actual_gain
                value_to_split = data[i][0]
        
        return max_gain, value_to_split

    def fit(self, X:pd.DataFrame, y:List[int]):


        self.root = self.build_decision_tree(X, y)

        return

    def check_base_cases(self, X, y, depth):
        if len(set(y)) == 1  or X.shape[0] <= self.minimal_node_size or depth > self.max_depth:
            return True

        return False

    def find_best_split(self, X:pd.DataFrame, y):

        max_gain = 0
        value_to_split = None
        feature = None
        for i in range(X.shape[1]):

            actual_gain, value = self.calculateMaxInfoGain(X.iloc[:, i].to_list(), y)
            if actual_gain > max_gain:
                max_gain = actual_gain
                value_to_split = value
                feature = X.columns[i]
            
        return feature, value_to_split, max_gain

    def split(self, X, y, feature, value):

        data = sorted(zip(X[feature].to_list(), y), key=lambda x: x[0])
        sorted_classes = [x[1] for x in data]
        sorted_X = [x[0] for x in data]

        i = sorted_X.index(value)
        return X.sort_values(feature, axis=0).iloc[:i, :], X.sort_values(feature, axis=0).iloc[i:, :], sorted_classes[:i],  sorted_classes[i:]

    def build_decision_tree(self, X, y, depth=0):


        if self.check_base_cases(X, y, depth):
            return Leaf_node(X, y)

        feature_to_split, split_value, info_gain = self.find_best_split(X, y)
        X_left, X_right, y_left, y_right = self.split(X, y, feature_to_split, split_value)
        if len(y_left) <= self.minimal_node_size or len(y_right) <= self.minimal_node_size:
            return Leaf_node(X, y)
        new_node = Decision_node(feature_to_split, split_value, info_gain)
        new_node.left = self.build_decision_tree(X_left, y_left, depth+1)
        new_node.right = self.build_decision_tree(X_right, y_right, depth+1)

        return new_node

    def plot_tree(self):
        root = self.root
        elements = []
        edges = {}
        id = 0
        queue = deque()
        visited = set()
        queue.append((id, root))
        visited.add(id)

        while len(queue) > 0:

            size = len(queue)
            for _ in range(size):
                _id, cur = queue.popleft()
                
                if isinstance(cur, Decision_node):

                    data = {'data': {'id': str(_id), 'label': f'{cur.feature} < {cur.split_value}'}}
                    elements.append(data)
                    if cur.left not in visited:
                        id += 1
                        queue.append((id, cur.left))
                        visited.add(id)
                        edges[str(id)] = edges.get(str(id), []) + [{'data': {'source': str(_id), 'target': str(id)}}]
                    if cur.right not in visited:
                        id += 1
                        queue.append((id, cur.right))
                        visited.add(id)
                        edges[str(id)] = edges.get(str(id), []) + [{'data': {'source': str(_id), 'target': str(id)}}]  
                    
                    elements.extend(edges.get(str(_id), []))

                else:
                    data = {'data': {'id': str(_id), 'label': f'{cur.label}; n_samples = {cur.X.shape[0]}'}, 'classes': 'triangle'}
                    elements.append(data)
                    elements.extend(edges.get(str(_id), []))

        app = dash.Dash(__name__)
        app.layout = dash.html.Div([
            cyto.Cytoscape(
                id='cytoscape',
                elements=elements,
                layout={
                    'name': 'breadthfirst',
                    'roots': '[id = "0"]'
                },
                style={'width': '600px', 'height': '600px'},
                stylesheet=[
                    # Group selectors
                    {
                        'selector': 'node',
                        'style': {
                            'content': 'data(label)'
                        }
                    },
                    {
                        'selector': '.triangle',
                        'style': {
                            'shape': 'triangle'
                        }
                    }
                ]
            )
        ])

        app.run_server(debug=True)

