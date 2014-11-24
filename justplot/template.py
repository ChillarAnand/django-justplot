from __future__ import absolute_import


CHART_HTML = """
<div id="{id}" style="height: {height}; width: {width};">
</div>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>

<link href="//cdn.jsdelivr.net/jqplot/1.0.8/jquery.jqplot.css" />
<script  src="//cdn.jsdelivr.net/jqplot/1.0.8/jquery.jqplot.js"></script>
<script>
$.jqplot ("{id}", {data});
</script>
"""
