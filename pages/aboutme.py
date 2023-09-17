import dash_mantine_components as dmc
from dash import register_page

register_page(__name__, path='/about-me')

bout_me = """
I am a data engineer with a background in bioinformatics and a passion for data science.
"""
layout = dmc.Grid([
    dmc.Col([
        dmc.Grid([
            dmc.Divider(label='who am I', size='sm'),
        ]),
        dmc.Grid([
            dmc.Col(dmc.Text(bout_me), span=8),
            dmc.Col(dmc.Image(src='/assets/profile_picture_pingu.svg'), span=4),
        ]),
    ], span=6, offset=3)  # default span=12, finer grid can be created by nesting
])

if __name__ == '__main__':
    ...
