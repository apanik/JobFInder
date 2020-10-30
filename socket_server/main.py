import json
import ssl
from urllib.parse import parse_qsl
import jwt
import socketio
from aiohttp import web
import requests


socket = socketio.AsyncServer(cors_allowed_origins='*', ping_timeout=35)
app = web.Application()
socket.attach(app)
clients = []

def lookup_client(**kw):
    result = []
    for row in clients:
        for k, v in kw.items():
            if row[k] != v:
                break
        else:
            result.append(row)
    return result

VALID_SERVER_TOKEN= "xNTk3ODk0ODE5LCJqdGkiOiJiMGYxODEyOWI0Mjk0OGU4YmFjMmQwMWRmNDdlNTM0YyIsInVzZXJfaWQiOjUwfQ"

@socket.event
async def connect(sid, env):
    text = 'invalid'
    c = None
    params = dict(parse_qsl(env.get('QUERY_STRING')))
    server_token = params.get('server_token')
    token = params.get('token')

    if server_token:
        if server_token == VALID_SERVER_TOKEN:
            c = {'user_id': "", 'email': "", 'type': "SERVER", 'sid': sid}
            clients.append(c)
            text = 'valid'
    elif token:
        data = validate_token(token)
        if data:
            c = {'user_id': str( data['id']), 'email': data['email'], 'type': "USER", 'sid': sid}
            clients.append(c)
            text = 'valid'

    msg = json.dumps({
        "type": "status",
        "text": text,
        "from": None,
        "to": c
    })
    await socket.emit('receive', msg, to=sid)
    print(clients)


@socket.event
async def disconnect(sid):
    c = lookup_client(sid=sid)
    if len(c) > 0:
        clients.remove(c[0])


def validate_token(token):
    header = {'Authorization': 'Bearer ' + token}
    try:
        response = requests.get('https://jobxprss.com/api/user/verify/', headers=header)
        if response.status_code == 200:
            data = response.json()
            return data
    except:
        return None



@socket.event
async def send(sid, data):
    data = json.loads(data)
    senders = lookup_client(user_id=data['from'])
    if len(senders) == 0:
        sender = data['from']
    else:
        sender = senders[0]

    to_user_id = data['to']
    print(to_user_id)
    if to_user_id == '*':
        print('send message to all active user')
        await socket.emit('receive', data, broadcast=True)
    else:
        list_of_user = to_user_id.split(",")
        for user in list_of_user:
            recipients = lookup_client(user_id=user)
            if recipients:
                for rec in recipients:
                    try:
                        try:
                            data = json.dumps({
                                "type": data['type'],
                                "text": data['text'],
                                "from": sender,
                                "to": rec
                            })
                        except Exception as e:
                            print("data!", e.__class__, "occurred.")
                            print(user)

                        print(data)
                        await socket.emit('receive', data, to=rec['sid'])
                    except Exception as e:
                        print("Oops!", e.__class__, "occurred.")
                        print(rec['sid'])
            else:
                print("This user not online" + user)


if __name__ == '__main__':
    ssl_context = ssl.SSLContext()
    ssl_context.load_cert_chain('cert/iss_ishraak.com.crt', 'cert/iss_ishraak.com.key')
    web.run_app(app, port=443, ssl_context=ssl_context)

   # web.run_app(app, port=80, ssl_context=None)

#await socket.emit('chat', 'hello', to=sid)
