from turtle import *
import random
import time
import datetime
import tkinter as tk

#現在の時刻を取得
dt_now = datetime.datetime.now()
kakudo_byo = dt_now.second
kakudo_fun = dt_now.minute
kakudo_zikan = dt_now.hour
#背景の円を描画
speed(1000)
circleback = penup()
circleback = setpos(0,-325)
circleback = pendown()
circleback = circle(325)
#時計の針を描画
byo = Turtle()
byo.width(5)
byo.rt(kakudo_byo*6-90)　#一秒に動く針の角度
byo.fd(320)
fun = Turtle()
fun.width(10)
fun.rt(kakudo_fun*6-90)
fun.fd(285)
zikan = Turtle()
zikan.width(15)
zikan.rt(kakudo_zikan*30-90)
zikan.fd(200)
#仮のコード（よくわからない）
hari = [byo,fun,zikan]
hari = color("white")
timecount = Turtle()
circleback = Turtle()
i = 0
#プロンプトに時刻を表示
print(kakudo_zikan)
print(kakudo_fun)
print(kakudo_byo)
#おまじない
hideturtle()
begin_fill()
time_sta = time.perf_counter()

input("prompt: ")