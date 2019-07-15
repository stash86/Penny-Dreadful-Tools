from typing import Dict, Tuple

from flask import Response, request, session

from shared_web.api import return_json, validate_api_key

from . import APP, importing
from .data import match


@APP.route('/api/admin/')
def admin() -> Response:
    return return_json(session.get('admin'))

@APP.route('/api/matchExists/<match_id>')
def match_exists(match_id: int) -> Response:
    return return_json(match.get_match(match_id) is not None)

@APP.route('/api/upload', methods=['POST'])
def upload() -> Response:
    error = validate_api_key()
    if error:
        return error
    match_id = int(request.form['match_id'])
    if request.form.get('lines'):
        lines = request.form['lines']
        importing.import_log(lines.split('\n'), match_id)
    else:
        importing.import_from_pdbot(match_id)
    start_time = int(request.form['start_time_utc'])
    end_time = int(request.form['end_time_utc'])
    match.get_match(match_id).set_times(start_time, end_time)

    return return_json({'success': True})

@APP.route('/export/<match_id>')
def export(match_id: int) -> Tuple[str, int, Dict[str, str]]:
    local = match.get_match(match_id)
    text = '{format}\n{comment}\n{mods}\n{players}\n\n'.format(
        format=local.format.name,
        comment=local.comment,
        mods=','.join([m.name for m in local.modules]),
        players=','.join([p.name for p in local.players]))
    n = 1
    for game in local.games:
        text += '== Game {n} ({id}) ==\n'.format(n=n, id=game.id)
        n = n + 1
        text += game.sanitized_log().strip()
        text += '\n\n'
    text = text.replace('\n', '\r\n')
    return (text, 200, {
        'Content-type': 'text/plain; charset=utf-8',
        'Content-Disposition': 'attachment; filename={match_id}.txt'.format(match_id=match_id)
        })

@APP.route('/api/status/')
def person_status() -> Response:
    r = {
        'mtgo_username': session.get('mtgo_username'),
        'discord_id': session.get('discord_id'),
        'admin': session.get('admin', False),
        'hide_intro': request.cookies.get('hide_intro', False),
        }
    return return_json(r)
