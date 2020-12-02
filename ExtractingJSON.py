import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1084345.json"
dataRaw = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(dataRaw.decode('utf8').replace("'", '"'))
# print(data)
sum = 0
for idx, entry in enumerate(data['comments']):
    # print(entry)
    sum += int(entry['count'])
print(sum)