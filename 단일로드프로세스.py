# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 13:59:21 2018

@author: JINSUNG
"""

#m/1/1 도착포아송 프로세스에 의해 결정/ 작업 서비스 시간은 지수 분포/ 큐는 단일 서버를 갖는 시스템의 큐 길이/가장 간단한 큐잉 기법 peopel.brunel.ac.uk/~mastjjb/jeb/or/queue.html
# 도착 포아송 프로세스에 의해 결정, 작업 서비스 시간은 지수 분포 큐는 단일 서버를 갖는 시스템의 큐 길이 
import queue
import numpy.random
import time
import sys

singlequeue =queue.Queue() #single큐 생성 선입선출


singlequeue.put(1) #1들어감
singlequeue.put(2) #2들어감
singlequeue.put(3) #3들어감

print(singlequeue.get())

singlequeue = queue.Queue(2) #2명들어갈수있는 큐

if singlequeue.empty():   #큐가 비어있을때 empty 1넣어줌
    print('empty')
    singlequeue.put(1)
    
if not singlequeue.empty():  #큐가 비어있지 않다면 뱉어내
    print(singlequeue.get())
    
singlequeue.put(3)
singlequeue.put(5)
print(singlequeue.full())

#평균 도착시간 평균3 평균 프로세스 시간 5
import queue
import numpy.random
import time
import sys

lamb = float(5)  #interarrival time(도착시간간격)
mu = float(3) #service time

queue = queue.Queue()

nextArrival = numpy.random.exponential(lamb)
nextService = nextArrival+numpy.random.exponential(mu)
i = 1
print("sequence:"+str(i))
print("nextService:"+str(nextService))
print("nextArrival:"+str(nextArrival))
print("=======================")
#조건문 1번이 꽉찼따 2번 들어가라 
while i<100: #i = process
    i+=1
    while nextArrival<nextService:
        queue.put(nextArrival)
        print("queu length:"+str(queue.qsize()))
        nextArrival += numpy.random.exponential(lamb)
    arrival = queue.get()
    
    wait = nextService -arrival
    
    if queue.empty():
        nextService = nextArrival+numpy.random.exponential(mu)
    else:
        nextService = nextService+numpy.random.exponential(mu)
    print("sequence:"+str(i))
    print("nextService:"+str(nextService))
    print("nextArrival:"+str(nextArrival))
    print('waittime : ' + str(wait))
    print("=======================")
    time.sleep(3) #interval time 