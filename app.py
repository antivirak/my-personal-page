from dash import Dash, html, callback, Input, Output, State, page_container
import dash_mantine_components as dmc

from navbar import layout

app = Dash(
    __name__,
    use_pages=True,
    # url_base_pathname='/',
)


def main():
    create_layout()
    app.run(debug=True)


def create_layout():
    app.layout = html.Div([
        layout,
        html.Div(page_container, style={'margin-top': '200px'}),
    ])


def create_layout_old():
    app.layout = html.Div([
        dmc.NumberInput(
            id='input-1',
            label="first input",
            # description="From 0 to infinity, in steps of 5",
            # value=5,
            # min=0,
            # step=5,
            # style={"width": 250},
        ),
        dmc.NumberInput(
            id='input-2',
            label='second input',
        ),
        dmc.Button(
            "Click me",  # or children= kwarg
            id='button',
        ),
        dmc.Text(
            id='output',
        ),
    ])


# @callback(
#     Output('output', 'children'),
#     Input('button', 'n_clicks'),
#     State('input-1', 'value'),
#     State('input-2', 'value'),
#     prevent_initial_call=True,
# )
def update_output(_, input1, input2):
    return str(input1 + input2)  # if input1 and input2 else '' - not needed afer prevent_initial_call=True


if __name__ == "__main__":
    main()
