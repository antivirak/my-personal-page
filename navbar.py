from dash import Input, Output, State, callback

from utils import navigacny_panel as respoznivny_navigacny_panel

# layout = nerespoznivny_navigacny_panel({
#     'about-me': {'label': 'About me'},
#     'experience': {'label': 'Experience'},
#     'projects': {'label': 'Projects'},
#     'contacts': {'label': 'Contacts'},
# }, 'tabler:square-rounded-letter-j')

layout = respoznivny_navigacny_panel({
    'about-me': {'label': 'About me'},
    'experience': {'label': 'Experience'},  # TODO create Enum
    'projects': {'label': 'Projects'},
    'contacts': {'label': 'Contacts'},
}, 'tabler:square-rounded-letter-j')


@callback(
    Output('provider_theme', 'theme'),
    Input('change_theme_button', 'n_clicks'),  # dmc.ActionIcon (button) defined in utils
    State('provider_theme', 'theme'),
    prevent_initial_call=True,
)
def change_theme(_, theme):  # TODO save setting to local storage
    return {'colorScheme': 'dark' if theme['colorScheme'] == 'light' else 'light'}
