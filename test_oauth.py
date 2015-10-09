# -*- coding: utf-8 -*-
import oauth_copy as oauth

if __name__=='__main__':
    CLIENT_ID = 'e95edc84c0d31bbd4d2dac9fe2cfe8e3'
    CLIENT_SECRET = '3e686b65a53fda5fe4c9ab49e1cc5d2d'
    CALLBACK_URL = 'http://localhost:5000/receive_code/'

    client = oauth.APIClient(app_key=CLIENT_ID, app_secret=CLIENT_SECRET, redirect_uri=CALLBACK_URL)
    auth_url = client.get_authorize_url(scope)
    print auth_url
    r = client.request_access_token('c0c7a27ba1914193c22066f85bfebc36') #返回的CODE
    client.set_access_token(r.access_token, r.expires_in)
    print client.get.user__home()