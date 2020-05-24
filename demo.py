import requests
post_url = 'http://support.baixiaokang.top/post.php'
data = {"msg":"艺术来源于什么又高于什么"}
req = requests.post(post_url,data)
print(req.text)
