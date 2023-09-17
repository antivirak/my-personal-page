from utils import nerespoznivny_navigacny_panel

# TODO responsive navbar
layout = nerespoznivny_navigacny_panel({
    'about-me': {'label': 'About me'},
    'experience': {'label': 'Experience'},  # TODO create Enum
    'projects': {'label': 'Projects'},
    'contacts': {'label': 'Contacts'},
}, 'tabler:square-rounded-letter-j')

if __name__ == '__main__':
    ...
