import random
import pytest


def find_delitels(num):
    sp = []
    for i in range(1,int(num**0.5) +1):
        if num%i==0:
            if i == num//i:
                sp.append(i)
            else:
                sp.append(num//i)
                sp.append(i)
    return sorted(sp)


def perevod(num,x):
    s = ''
    while num>0:
        s = str(num%x)+s
        num//=x
    return int(s)

def find_all_sogl(sp):
    k = 0
    for i in sp:
        if i in 'bcdfghjklmnprstwxz':
            k+=1
    return k

def find_all_glas(sp):
    k = 0
    for i in sp:
        if i in 'aeyuio':
            k+=1
    return k

def find_del_matrix(x11,x12,x21,x22):
    k = x11*x22 - x12*x21
    return k

@pytest.fixture()
def get_sp():
    sp = ''
    for i in range(1,random.randint(10,20)):
        l = random.choice('abcdefghijklmnopqrstuvwxyz')
        sp += l
    return sp