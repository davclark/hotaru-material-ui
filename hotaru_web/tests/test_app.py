import morepath
import hotaru_web

from webtest import TestApp as Client


def test_root():
    morepath.scan(hotaru_web)
    morepath.commit(hotaru_web.App)

    client = Client(hotaru_web.App())
    root = client.get('/')

    assert root.status_code == 200
    assert len(root.json['greetings']) == 2
