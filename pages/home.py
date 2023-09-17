import dash_mantine_components as dmc
from dash import register_page

register_page(__name__, path='/')

layout = dmc.Text('home')

if __name__ == '__main__':
    ...
