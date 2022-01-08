import  requests
import urllib3

class HttpClient:
	def __init__(self,disable_ssl_verify=False,timeout=60):
		#维持会话,可以让我们在跨请求时保存某些参数
		self.client = requests.session()
		self.disable_ssl_verify = disable_ssl_verify
		self.timeout = timeout
		if self.disable_ssl_verify:
			#屏蔽https证书警告
			urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	def get(self,url,headers=None,data=None,json=None,params=None,*args,**kwargs):
		if headers is None:
			headers = {}
		if self.disable_ssl_verify:
			response = self.client.get(url,headers=headers,data=data,json=json,
						params=params,verify=False,timeout=self.timeout,*args,**kwargs)
		else:
			response = self.client.get(url, headers=headers, data=data, json=json,
									  params=params,timeout=self.timeout, *args, **kwargs)
		return response.text.encode(response.encoding).decode('utf-8')



