# -*- coding: utf-8 -*-

"""
Created on Fri Dec  3 09:08:17 20210

吴桐 210450303 三班
@author: Sebastian
"""
name='admin'
password=123456#密码为整数q

i=5
while i > 0:
    i-=1
    n=input('用户名:') 
    p=int(input('密码:'))#输入整数密码
    if (n == name) and (password == p):
        print('登录成功')
        break
    else:
        print('用户名或密码错误')#五次以内输入
while i == 0:
    n=input('用户名:') 
    p=input('密码:')
    print('输入次数过多已锁定请找管理员解锁')
        
