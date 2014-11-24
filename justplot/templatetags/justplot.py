import json
import functools

from django import template

from ..template import CHART_HTML


register = template.Library()

def chart(name, parser, token):
    args = token.split_contents()
    args = parse_options(args)
    return ChartNode(name=name, args=args)


def parse_options(source):
    """parses chart tag options"""
    options = {}
    tokens = [t.strip() for t in source.split('=')]

    name = tokens[0]
    for token in tokens[1:-1]:
        value, next_name = token.rsplit(' ', 1)
        options[name.strip()] = value
        name = next_name
    options[name.strip()] = tokens[-1].strip()
    return options


class ChartNode(template.Node):

    def __init__(self, name, args):
        self.name = name
        self.args = args
        self.options = dict(i.split('=') for i in args[2:])
        for k, v in self.options.items():
            self.options[k] = template.Variable(v)

    def render(self, context):
        for k, v in self.options.items():
            self.options[k] = self.options[k].resolve(context)
        if isinstance(self.options['data'], basestring):
            self.options['data'] = json.loads(self.options['data'])
        return CHART_HTML.format(id=self.options['id'],
                                 data=[self.options['data']],
                                 height='100px', width='200px')
        #return self.args, self.options

register.tag('line_chart', functools.partial(chart, 'LineChart'))
register.tag('pie_chart', functools.partial(chart, 'PieChart'))
