#!/usr/bin/env python
import os 
import sys
import io
import socket

a=1
while a==1:
    b=raw_input("Lütfen Kullanıcı adını giriniz:")
    if b== "mustafa":
          a=2 
          print """



  toplama (1)
  cikarma (2)
  caprma  (3)
  bolme   (4)

"""
islem= raw_input("Lütfen istediginiz işlemin numarasınız yazınız:")


if islem=="1":
      toplama1= int(raw_input("Lütfen toplama işlemi icin ilk sayıyı giriniz:"))
      toplama2= int(raw_input("Lütfen toplama işlemi icin ilk sayıyı giriniz:"))
      print toplama1, "+",toplama2,"=",toplama1+toplama2
if islem=="2":
      cikarma1= int(raw_input("Lütfen cikarma işlemi icin ilk sayıyı giriniz:"))
      cikarma2= int(raw_input("Lütfen cikarma işlemi icin ilk sayıyı giriniz:"))
      print cikarma1, "-",cikarma2,"=",cikarma1-cikarma2
if islem=="3":
      carpma1= int(raw_input("Lütfen carpma işlemi icin ilk sayıyı giriniz:"))
      carpma2= int(raw_input("Lütfen carpma işlemi icin ilk sayıyı giriniz:"))
      print carpma1, "x",carpma2,"=",carpma1*carpma2
if islem=="4":
      bolme1= int(raw_input("Lütfen bolme işlemi icin ilk sayıyı giriniz:"))
      bolme2= int(raw_input("Lütfen bolme işlemi icin ilk sayıyı giriniz:"))
      print bolme1, "/",bolme2,"=",bolme1/bolme2





