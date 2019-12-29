#-*- coding: UTF-8 -*-
import time
import threading
from flask import Flask, render_template, request, url_for
import serial

Subway = 0
StationNumber = 0
Station =""
#아두이노 전역변수
l1WantStation = ""
l2WantStation = ""
l1State = "빈자리"
l2State = "앉음"
_station = []
l1color='#90E8B0'
l2color='#FF624F'

i = 0 #역번호

    
k = 0   
        

        



app = Flask(__name__)

@app.route('/')
def form():
    global l1color, l2color
    sit1 = "없음"
    sit2 = "없음"
    if sit1 == "있음":
        l1color= '#FF624F'
    if sit2 == "있음":
        l2color = '#90E8B0'
        
    return render_template('test.html',l1c = l1color,l2c = l2color)

@app.route('/information', methods=['POST'])
def action():
    return render_template('information.html',current=Station)

'''@app.route('/want', methods=['POST'])
def action2():
    want = request.form['wantnumber']
    sit = request.form['sit']
    return render_template('want.html', want=want,sit = sit)'''

@app.route('/l1', methods=['GET'])
def action3():
    global l1color, l2color, l1State, l1WantStation
    if l1State == "빈자리":
        l1color = '#90E8B0'
    else:
        l1color = '#FF624F'

    return render_template('l1s.html', sit = l1State, want=l1WantStation,l1c = l1color)

@app.route('/l2', methods=['GET'])
def action4():
    global l1color, l2color, l2State, l2WantStation
    if l2State == "빈자리":
        l2color = '#90E8B0'
    else:
        l2color = '#FF624F' 

    return render_template('l2s.html', sit = l2State, want=l2WantStation,l2c = l2color)

@app.route('/move', methods = ['GET'])
def move():
    global Station
    #arduino1 = serial.Serial('COM8',9600)
    stationArr = ["당고개","상계","노원","창동","쌍문","수유","미아","미아삼거리","길음","성신여대입구","한성대입구","혜화","동대문","동대문운동장","충무로","명동","회현","서울역","숙대입구","삼각지","대야미도장","산본","금정","범계","평촌","인덕원","정부과천청사","과천대공원","경마공원","선바위","남태령","사당","총신대입구","동작","이촌","신용산","반월","상록수","한대앞","중앙","고잔","초지","안산","신길온천","정왕","오이도"]
    global k, i
    if(k%2 == 1):#전진
        i+=1
        #print(str(i)+":"+_station[i])
        a#rduino1.write((str(i)).encode())
        
    elif(k%2 == 0):#후진
        i-=1
        #print(str(46-i)+":"+_station[-i])
        #arduino1.write((str(46-i)).encode())
    if i ==45:
        k = 0
    elif i==0:
        k = 1
    #arduino1.close()
    Station = stationArr[i]
    return stationArr[i]
'''
@app.route('/defaultState', methods=['GET'])
def action7():
    sit = "없음" #값을 아두이노에서 받아와야됨
    return render_template('default.html', sit = sit)

@app.route('/defaultStation', methods=['GET'])
def action8():
    want = 0 #값을 아두이노에서 받아와야함
    return render_template('defaultstation.html', want=want)
'''
if __name__ == '__main__':
    
    app.run(host='0.0.0.0', debug= True, threaded=True)
    





