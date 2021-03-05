import requests, json

def cek_cradintial():
    try:
      settings = json.load(open('setting/setting.json'))
      headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
      url = "https://eastlombok.site/api/cradential"
      response_api = requests.post(url, data=json.dumps(settings), headers=headers)
      return response_api.json()
    except Exception as e:
        return 'something error'