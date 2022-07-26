# Details
AUTHOR = 'shakyra'
SITENAME = 'Shakyra'
SITEURL = ''
TIMEZONE = 'America/Antigua'
DEFAULT_LANG = 'en'


# ABOUT_ME = 'Here to learn. Here to share'
# AVATAR = 'extra/site_logo.jpg'



# Paths
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images','extra']
PLUGIN_PATHS = ['pelican-plugins']



# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)



# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/shakyracc'),
          ('Github', 'https://github.com/shakyracornelius'),
          ('Instagram', 'https://www.instagram.com/shakyracc'),)

DEFAULT_PAGINATION = 10



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True



# Theme, environments and plugins
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cyborg'
PYGMENTS_STYLE = 'colorful'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites',]
I18N_TEMPLATES_LANG = 'en'
# BOOTSTRAP_FLUID = True


# Custom CSS/JS
CUSTOM_CSS = 'static/css/custom.css'
GOOGLEFONT = 'https://fonts.googleapis.com/css?family=Roboto'
GOOGLEFONT = 'https://fonts.googleapis.com/css?family=Source+Serif+Pro'
CUSTOM_JS = 'static/js/custom.js'



# Navbar
DISPLAY_CATEGORIES_ON_MENU = False
BOOTSTRAP_NAVBAR_INVERSE = True
ARCHIVES_SAVE_AS = 'archives.html'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_ARCHIVE_ON_MENU = True
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
DISPLAY_ARTICLE_INFO_ON_INDEX = False



# Sidebar
HIDE_SIDEBAR = True
SIDEBAR_ON_LEFT = True



# Site Brand
HIDE_SITENAME = False


