import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1084344.xml"
html = urllib.request.urlopen(url, context=ctx).read()
print(html.decode())
tree = ET.fromstring(html)
counts = tree.findall('.//count')
sum = 0
for idx, count in enumerate(counts):
    sum += int(count.text)
print(sum)