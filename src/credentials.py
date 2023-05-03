from wsgiref.simple_server import make_server
import urllib.parse, json, sys

species ={
    'Cyberman': 'John Lumic',
    'Dalek': 'Davros',
    'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
    'Human': 'Leonardo da Vinci',
    'Ood': 'Klineman Halpen',
    'Silence': 'Tasha Lem',
    'Slitheen': 'Coca-Cola salesman',
    'Sontaran': 'General Staal',
    'Time Lord': 'Rassilon',
    'Weeping Angel': 'The Division Representative',
    'Zygon': 'Broton'
}

def application (environ, start_response):
    pars = urllib.parse.parse_qs(environ['QUERY_STRING'])
    pars_arg = str(*pars['species'])
    if pars_arg in species:
        body = {sys.argv[0][:-3]: species[pars_arg]}  
    else: 
        body = {sys.argv[0][:-3]: "Unknown"}
    status = '200 OK'
    response_body = json.dumps(body).encode('utf-8')
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [response_body]

def run():
    serv = make_server ('localhost', 8888, application)
    serv.handle_request()

if __name__ == '__main__':
    run()