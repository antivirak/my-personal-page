# from dash import register_page
# import dash_mantine_components as dmc

from utils import nerespoznivny_navigacny_panel

layout = nerespoznivny_navigacny_panel({
    'about-me': {'label': 'About me'},
    'experience': {'label': 'Experience'},  # TODO create Enum
    'projects': {'label': 'Projects'},
    'contacts': {'label': 'Contacts'},
}, 'tabler:square-rounded-letter-j')

if __name__ == '__main__':
    ...
