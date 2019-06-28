import requests
import pygal
from pygal.style import RotateStyle as RS, LightGreenStyle as LGS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()

repo_dicts = response_dict['items']

plot_dicts, names = [], []
for repo_dict in repo_dicts:
    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : str(repo_dict['description']),
        'xlink' : repo_dict['html_url']
    }

    plot_dicts.append(plot_dict)
    names.append(repo_dict['name'])

mystyle = RS('#333366', base_style=LGS)

myconfig = pygal.Config()
myconfig.x_label_rotation = 45
myconfig.show_legend = False
myconfig.truncate_label = 15
myconfig.show_y_guides = False
myconfig.width = 1300

chart = pygal.Bar(myconfig, style=mystyle)
chart.title = 'Python Projects'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_response.svg')