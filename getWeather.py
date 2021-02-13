# coding: utf-8
from requests import get
import json
from pprint import pprint
from temperature import myTemp
import requests

params = {
  'access_key': 'a444b9c25620d2e0b3a949620a4dcf18',
  'query': 'New York'
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()

temperature = api_response['current']['temperature']

myTemp(temperature)
