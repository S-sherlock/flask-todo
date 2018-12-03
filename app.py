from flask import Flask,render_template,url_for,redirect,request
from datetime import datetime
import pymongo



app = Flask(__name__)
# 数据库实例
db = pymongo.MongoClient('127.0.0.1',27017)
db.todo
# mongo  TODO文档结构
class Todo(object):
    '''
    一行待办事项数据结构。
    字段：事项内容，添加创建时间，状态（未完成，已完成），完成时间
    '''

    def create_doc(self,content,status):
        return {
            'content': content,
            'creat_time': datetime.now(),
            'status': 0,      # 0未完成 1已完成,
            'finish_time': None
        }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
    # 展示todo列表
    pass

@app.route('/add')
def add():
    pass


@app.route('/finish')
def finish():
    # 更新状态为已完成
    pass

@app.route('/delete')
def delete():
    # 删除无用的todo
    pass


if __name__ == '__main__':
    app.run()
