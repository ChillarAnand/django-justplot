import json
import functools

from django import template

from ..template import CHART_HTML

register = template.Library()


def chart(name, parser, token):
    """
    Template tag parser function which takes parameters and
    returns a Node object.
    :param name: Name of template tag.
    :param parser: Template parser object.
    :param token: Token currently being processed by parser.
    :return: Template Node object.
    """
    args = token.split_contents()
    return ChartNode(name=name, args=args)


class ChartNode(template.Node):
    """
    Renderer for node object.
    """
    def __init__(self, name, args):
        """
        :param name: Name of template tag.
        :param args: Arguments given for template tag.
        :return: None
        """
        self.name = name
        self.args = args
        self.options = dict(i.split('=') for i in self.args[2:])
        for k, v in self.options.items():
            self.options[k] = template.Variable(v)

    def render(self, context):
        for k, v in self.options.items():
            self.options[k] = self.options[k].resolve(context)
        # if isinstance(self.options['data'], str):
        #     self.options['data'] = json.loads(self.options['data'])
        self.options = add_defaults(self.options)
        return CHART_HTML.format(**self.options)


def add_defaults(d):
    """
    Add defualt options to user options.
    """
    d['height'] = d.get('height', '350px')
    d['width'] = d.get('width', '700px')
    return d


register.tag('line_chart', functools.partial(chart, 'LineChart'))
