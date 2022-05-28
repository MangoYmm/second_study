from flask import Flask, escape, request
#实例化flask,获得实例对象app
app = Flask(__name__)

#路由定义，第一个参数传递path
@app.route("/")
def flask_demo():
	#获得url中的参数内容
	print(request.args)
	#通过get方法，获得键对应的value
	print(request.args.get('a'))
	print("11111111")
	#接口的响应值，对应的就是return的内容
	return "hogwarts"

@app.route("/hogwarts",methods=['get','post','delete','put'])
def flask_demo2():
	#获得url中的参数内容
	print(request.args)
	#通过get方法，获得键对应的value
	# print(request.args.get('a'))
	# print("11111111")
	print(request.json)
	#接口的响应值，对应的就是return的内容
	return "hello,demo2"

if __name__=='__main__':
	app.run(debug=True,port=5001)
