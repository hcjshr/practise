import requests
import pygal
from pygal.style import RotateStyle as RS, LightGreenStyle as LGS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

response_dict = r.json()


names, stars, htmls = [], [], []
repo_dicts = response_dict['items']
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    htmls.append(repo_dict['html_url'])

mystyle = RS('#336699', base_style=LGS)

myconfig = pygal.Config()
myconfig.x_label_rotation = 45
myconfig.show_legend = False
myconfig.title_font_size = 24
myconfig.label_font_size = 18
myconfig.major_label_font_size = 18
myconfig.truncate_label = 15
myconfig.show_y_guides = False
myconfig.width = 1000

chart = pygal.Bar(myconfig, style=mystyle)
chart.title = 'Python Projects'
# chart.x_labels = names
# chart.add('', stars)
# chart.render_to_file('github.svg')


chart.x_labels = ['httpie', 'django', 'flask']
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie'},
    {'value': 15028, 'label': 'Description of django'},
    {'value': 14798, 'label': 'Description of flask'}
]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')

# myconfig.x_label_rotation = 45
# myconfig.show_legend = False
# myconfig.title_font_size = 24
# myconfig.label_font_size = 16
# myconfig.major_label_font_size = 18
# myconfig.truncate_label = 15
# myconfig.show_y_guides = False
# myconfig.width = 1000