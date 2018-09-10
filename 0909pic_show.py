from flask import Flask,render_template,url_for
#三种展示图片的方法  1，用html文件，然后加载该文件；2，直接将html文件的内容写在新建url的返回代码中；3，直接读取本地图片？？？？
app = Flask(__name__)

@app.route('/jjc1/')
def jjc1():
    return render_template('Hello.html')

@app.route('/jjc2/',methods=['GET'])
#不用html文件直接加载对应html代码的操作，感觉优秀的很啊
def jjc2():
    return '''
    <!doctype html>
    <html>
    <body>
    <img src="/static/star2.jpg"  alt="jjc" height="400" width="600"/>
    <form action='/upload' method='post' enctype='multipart/form-data'>
        <input type='file' name='file'>
    <input type='submit' value='Upload'>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
