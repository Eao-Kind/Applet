import requests

headers = {
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}
url1 = 'http://ebooks.crup.com.cn/openr/46856_output/web/46856_opf_files/dd6574577f1dc0b31b98e8baaf630634_'

for i in range(1, 373, 1):
    url = url1 + str(i) + '.swf'
    with open(str(i) + '.swf', 'wb') as f:
        data = requests.get(url, headers=headers)
        f.write(data.content)
        f.close()
