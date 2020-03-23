from flask import Response, make_response, redirect, request, url_for

from decksite import APP
from decksite.cache import cached
from decksite.views import About, AboutPdm, CommunityGuidelines, Faqs


@APP.route('/about/')
@cached()
def about_pdm() -> str:
    view = AboutPdm()
    return view.page()

@APP.route('/gp/')
@cached()
def about_gp() -> Response:
    return make_response(redirect(url_for('about', src='gp')))

@APP.route('/about/pd/')
@cached()
def about() -> str:
    view = About(request.args.get('src'))
    return view.page()

@APP.route('/faqs/')
@cached()
def faqs() -> str:
    view = Faqs()
    return view.page()

@APP.route('/community/guidelines/')
@cached()
def community_guidelines() -> str:
    view = CommunityGuidelines()
    return view.page()
