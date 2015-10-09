import requests

import json
import urllib2
import urllib

client_id = 'e95edc84c0d31bbd4d2dac9fe2cfe8e3'
client_secret = '3e686b65a53fda5fe4c9ab49e1cc5d2d'
redirect_uri = 'http://123.56.40.56:8080/LoveXY/servlet/ExchangeToken'
call_code_url = 'http://123.56.40.56:8080/LoveXY/servlet/FetchToken'
access_token = '20241b59aa9bf37878481fbd47e7be66'
# url = 'https://api.23andme.com/authorize/'
# para = {"redirect_uri": redirect_uri, "client_id": client_id, "scope": 'basic rs123',"response_type":"code"}
# data = urllib.urlencode(para)
# req = urllib2.Request(url, data)
# resp = urllib2.urlopen(req)
# body = resp.read()



def get_authcode(SNPS):
    url = 'https://api.23andme.com/authorize/'
    para = {"redirect_uri": redirect_uri, "client_id": client_id, "scope": 'basic %s' %' '.join(SNPS) }
    resp = requests.post(url, data=para)
    if resp.status_code != 200:
        print 'error'
        return None
    else:
        code = requests.get("http://123.56.40.56:8080/LoveXY/servlet/FetchToken")
        return code


def get_token(SNPS):
    auth_code = 'bcf9d068622402cb394b80c73a6c42fe'
    # auth_code = get_authcode()
    url = 'https://api.23andme.com/token/'
    resp = requests.post(url, data={"client_id": client_id, "client_secret": client_secret,
                                    "grant_type": "authorization_code", "code": auth_code,
                                    "redirect_uri": redirect_uri, "scope": "basic %s"} %' '.join(SNPS))
    if resp.status_code != 200:
        print 'error'
        return None
    else:
        content = json.loads(resp.text)
        return content["access_token"]



def get_genetype(access_token,SNPS):
    # access_token = get_token(SNPS)
    url = 'https://api.23andme.com/'
    headers = {'Authorization': 'Bearer %s' % access_token}
    genotype_response = requests.get("%s%s" % (url, "1/genotype/"),
                                         params = {'locations': ' '.join(SNPS)},
                                         headers=headers,
                                         verify=False)
    if genotype_response.status_code == 200:
        return genotype_response.json()
    else:
        reponse_text = genotype_response.text
        response.raise_for_status()


print get_token():
