def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML
    # if app.builder.format != 'html':
    #     return
    print(app.builder.format)
    src = source[0] + 'test'
    # rendered = app.builder.templates.render_string(
    #     src, app.config.html_context
    # )
    source[0] = src

def setup(app):
    app.connect("source-read", rstjinja)