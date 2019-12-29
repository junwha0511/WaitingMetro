#-*- coding: UTF-8 -*-
import threading
import time
from flask import Flask, render_template, request, url_for

class Hello(threading.Thread):
    def run(self):
        def fuck1():
            while(1):
                def station(j,k,i): #j: 지하철번호(18181), k: 홀수=>정방향, 짝수=>역방향, i: 역 번호
                    _station = ["당고개","상계","노원","창동","쌍문","수유","미아","미아삼거리","길음","성신여대입구","한성대입구","혜화","동대문","동대문운동장","충무로","명동","회현","서울역","숙대입구","삼각지","대야미도장","산본","금정","범계","평촌","인덕원","정부과천청사","과천대공원","경마공원","선바위","남태령","사당","총신대입구","동작","이촌","신용산","반월","상록수","한대앞","중앙","고잔","초지","안산","신길온천","정왕","오이도"]
                    if(k%2 == 1):#전진
                        print(str(i)+":"+_station[i])
                        return j, i, _station[i]

                    elif(k%2 == 0):#후진
                        print(str(46-i)+":"+_station[-i])
                        return j, 46-i, _station[-i]

                _k = 1
                i = 0
                first = 1
                while(1):
                    Subway, StationNumber, Station = station(18181,_k,i)
                            
                    if(StationNumber == 45 and _k % 2 == 1):
                        i = 1
                        _k += 1
                    elif(StationNumber == 0 and first == 0 and _k % 2 == 0):
                        i = 0
                        _k += 1
                    else:
                        i += 1
                        first = 0
                    time.sleep(5)
class Hi(threading.Thread):
    def run(self):
        app = Flask(__name__)

        @app.route('/')
        def form():
            return render_template('test.html')

        @app.route('/information', methods=['POST'])
        def sync():
            currnent = Station
            want = request.form['wantnumber']
            sit = request.form['sit']
            return render_template('information.html', want=want,sit = sit)

        if __name__ == '__main__':
            app.run(host='127.0.0.1', debug= True, threaded=True)

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()