import requests
from bs4 import BeautifulSoup
import re

abc = requests.session()
response = abc.get('https://bcs.qianxin.com/2019/pptdown.html')

html = response.content.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
qq = soup.select('table>tr')
qq.remove(qq[0])



for q in qq:
    name = q.select('td')[-2].text
    if name.strip() == '':
        name = '未命名'
    url = q.select('td>a')[0]['href']

    name = re.sub('[/:*?"<>|]', '', name)
    print(name)
    # req = abc.get(url)
    # f = open(name + '.pdf', 'wb')
    # f.write(req.content)
    # f.close()
