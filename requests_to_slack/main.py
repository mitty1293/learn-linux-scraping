import requests

url = 'http://www.usupi.org/sysad/backno.html'
rg = requests.get('http://splash:8050/render.html',
                params={
                    'url':url, 
                    'wait': 2
                }
)
print(rg.text)