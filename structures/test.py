import dash
import dash_cytoscape as cyto

app = dash.Dash(__name__)
app.layout = dash.html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=[{'data': {'id': '0', 'label': '2 < 3.0'}},
 {'data': {'id': '1', 'label': 'label: 0 \n n_samples = 50'},
  'classes': 'triangle'},
 {'data': {'source': '0', 'target': '1'}},
 {'data': {'id': '2', 'label': '2 < 4.8'}},
 {'data': {'source': '0', 'target': '2'}},
 {'data': {'id': '3', 'label': '3 < 1.5'}},
 {'data': {'source': '2', 'target': '3'}},
 {'data': {'id': '4', 'label': '2 < 5.1'}},
 {'data': {'source': '2', 'target': '4'}},
 {'data': {'id': '5', 'label': 'label: 1 \n n_samples = 34'},
  'classes': 'triangle'},
 {'data': {'source': '3', 'target': '5'}},
 {'data': {'id': '6', 'label': '1 < 3.0'}},
 {'data': {'source': '3', 'target': '6'}},
 {'data': {'id': '7', 'label': 'label: 2 \n n_samples = 13'},
  'classes': 'triangle'},
 {'data': {'source': '4', 'target': '7'}},
 {'data': {'id': '8', 'label': 'label: 2 \n n_samples = 42'},
  'classes': 'triangle'},
 {'data': {'source': '4', 'target': '8'}},
 {'data': {'id': '9', 'label': 'label: 1 \n n_samples = 4'},
  'classes': 'triangle'},
 {'data': {'source': '6', 'target': '9'}},
 {'data': {'id': '10', 'label': 'label: 1 \n n_samples = 7'},
  'classes': 'triangle'},
 {'data': {'source': '6', 'target': '10'}}],
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

if __name__ == '__main__':
    app.run_server(debug=True)