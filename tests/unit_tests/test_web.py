from flask import url_for




def test_app(client):
    assert client.get(url_for('web.monkey')).status_code == 200
    assert b"hello monkey" in client.get(url_for('web.monkey')).data