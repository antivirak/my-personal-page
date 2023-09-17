import dash_mantine_components as dmc
from dash import Input, Output, callback, dcc, register_page
from plotly.express import bar

from utils import priprava_dat

register_page(__name__, path='/analysis')

df = priprava_dat()

layout = dmc.Stack([
    dmc.Select(
        id='select_country',
        label='Select country',
        value=df['uzemi_txt'][0],  # 'Česká republika',
        data=[
            {'label': country, 'value': country} for country in df['uzemi_txt'].drop_duplicates().sort_values()  # .unique?
        ],
    ),
    dcc.Graph(
        id='graph_education',
    ),
])


@callback(
    Output('graph_education', 'figure'),
    Input('select_country', 'value'),
)
def update_graph_education(country):
    # TODO utils.stylizuj_graf
    tmp_df = df.copy()
    tmp_df = tmp_df[tmp_df['uzemi_txt'] == country]
    tmp_df = tmp_df.groupby(['vzdelani_txt'])['hodnota'].sum().reset_index()

    # fig = dmc.PlotlyFigure(
    #     data=[
    #         bar(
    #             tmp_df,
    #             x='vzdelani_txt',
    #             y='hodnota',
    #         ),
    #     ],
    # )

    return bar(
        tmp_df,
        x='vzdelani_txt',
        y='hodnota',
    )


if __name__ == '__main__':
    ...
