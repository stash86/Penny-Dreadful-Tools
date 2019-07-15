import json

import requests
from lxml import etree

from . import repo


def main() -> None:
    manifest = requests.get('http://mtgoclientdepot.onlinegaming.wizards.com/MTGO.application')
    tree = etree.fromstring(manifest.content)
    identity = tree.find('{urn:schemas-microsoft-com:asm.v1}assemblyIdentity')
    version = identity.attrib['version']

    print('Current MTGO Version is {0}'.format(version))

    data = {'version': version}
    with open('mtgo_version.json', mode='w') as f:
        json.dump(data, f)

    project = repo.get_verification_project()
    current = [c for c in project.get_columns() if c.name == version]
    if not current:
        print(f'Creating column for {version}')
        project.create_column(version)
