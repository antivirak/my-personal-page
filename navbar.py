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

# TODO callback for changing page

if __name__ == '__main__':
    ...
