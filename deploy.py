#!/usr/bin/python3
import requests
import json
import os
os.system('mkdir -p IRbaby_deploy_tmp')
url = 'https://api.github.com/repos/Caffreyfans/IRbaby-firmware/releases/latest'
response = requests.get(url)
data = json.loads(response.text)
download_url = data['assets'][0]['browser_download_url']
os.system('wget ' + download_url + ' -P IRbaby_deploy_tmp')
url = 'https://api.github.com/repos/Caffreyfans/IRbaby-android/releases/latest'
response = requests.get(url)
data = json.loads(response.text)
download_url = data['assets'][0]['browser_download_url']
os.system('wget ' + download_url + ' -P IRbaby_deploy_tmp')
os.system('cp -r IRbaby_deploy_tmp /var/www/irbaby/latest')