# -*- coding: utf-8 -*-
"""데이터 분석 및 시각화2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18MiGkH9r0Et2KNyvVDzYQagkiD7SSIZU
"""

import math

while True:
    print('넓이를 구하고 싶은 도형이 3개 중 무엇입니까?\n\t(정삼각형, 원, 사각형)')
    sub = input('도형: ')
    if (sub == '정삼각형'):
        print("정삼각형의 한 변의 길이를 입력하세요")
        lengthTri = int(input('길이: '))
        S1 = (math.sqrt(3)/4)*(lengthTri**2)
        print('넓이: ',S1)
    elif (sub == '원'):
        print("원의 반지름의 길이를 입력하세요")
        lengthCir = int(input('길이:'))
        S2 = (lengthCir**2)*3.14
        print('넓이: ',S2)
    else:
        print("사각형의 변의 길이를 공백을 두고 입력하세요\n길이:")
        length1, length2 = map(int,input().split())
        S3 = length1 * length2
        print('넓이: ',S3)

print('약수를 알려주고 소수인지 아닌지 판별 종료 끝내기')

number = []

while True:
    num = int(input('입력: '))
    for i in range(1, num+1):
        if num%i == 0:
            print(i, end=" ")


    # 소수 판별하기
    number.append(num)

    print("\n지금 까지 입력했던 수 중 소수가 있는지 알고싶으면\n '소수판별' 이라고 치세요")
    check = input("소수가 있는지 알고싶나요?: ")
    if check == '소수판별':
        chk = True
        for i in int(num): 
            if num%i == 0:
                chk = False 
                break

        if chk:
            print(num, ": 소수")
        else :
            print(num, ": 소수 아님")
    else:
        print('알기 싫은가 보군요..')
    print(number)

import random
ds = [random.randint(1, 100) for x in range(5)]
print(ds)
for a in range(len(ds)-2,-1,-1):
    for b in range(0, a+1):
        if ds[b]>ds[b+1]:
            ds[b],ds[b+1] = ds[b+1],ds[b]
print(ds)

name = []
score = []

while True:
    
    n = input("1.입력 2.삭제 3.전체삭제 4.성적순 출력(낮은순) 5. 성적순 출력(높은순) 6.이름순 출력(오름차순) 7. 이름순 출력(내림차순) 8.종료: ")
    
    if n == '1' or n == '입력':
        Name = input('이름: ')
        Score = int(input('성적: '))
        name.append(Name)
        score.append(Score)
        
    elif n == '2' or n == '삭제':
        k = input('삭제할 학생의 이름: ')
        if k in name:
            a = name.index(k)
            del name[a]
            del score[a]
        else:
            print('그런 학생은 없습니다.')
            
    elif n == '3' or n == '전체삭제':
        del name[0:]
        del score[0:]

        
    elif n == '4' or n == '성적순 출력(낮은순)':
        for a in range(len(score)-2,-1,-1):
            for b in range(0, a+1):
                if score[b]>score[b+1]:
                    score[b],score[b+1] = score[b+1],score[b]
                    name[b],name[b+1] = name[b+1],name[b]

        for i in range(0, len(score)):
            print(name[i], ': ', score[i] ,end=' ')
        print()
        
        
    elif n == '5' or n == '성적순 출력(높은순)':
        for a in range(len(score)-2,-1,-1):
            for b in range(0, a+1):
                if score[b]>score[b+1]:
                    score[b],score[b+1] = score[b+1],score[b]
                    name[b],name[b+1] = name[b+1],name[b]

        score.reverse()
        name.reverse()
        for i in range(0, len(score)):
            print(name[i], ': ', score[i] ,end=' ')
        print()
    
        
    elif n == '6' or n == '이름순 출력(오름차순)':
        for a in range(len(name)-2,-1,-1):
            for b in range(0, a+1):
                if name[b]>name[b+1]:
                    name[b],name[b+1] = name[b+1],name[b]
                    score[b],score[b+1] = score[b+1],score[b]
        for p in range(0, len(name)):
            print(name[p], ': ', score[p] ,end=' ')
    
    elif n == '7' or n == '이름순 출력(내림차순)':
        for a in range(len(name)-2,-1,-1):
            for b in range(0, a+1):
                if name[b]>name[b+1]:
                    name[b],name[b+1] = name[b+1],name[b]
                    score[b],score[b+1] = score[b+1],score[b]
        
        score.reverse()
        name.reverse()
        
        for p in range(0, len(name)):
            print(name[p], ': ', score[p] ,end=' ')
        
    elif n == '8' or n == '종료':
        print('시스템 종료')
        break

name = []
hight = []
#인트로
for y in range(10):
    y = '*'*120
    print(y)

print('이름과 키를 입력하세요')
while True:
    Name = input('이름: ')
    '''
    중복 입력 구현 불가
    
    if Name in name:
        print('이미 그 사람의 데이터는 있습니다!\n데이터를 추가하려면 1번, 데이터를 수정하려면 2번을 누르세요!\n 아무것도 아니면 3번을 누르세요!')
        u = int(input('몇번: '))
    if u == 2:
        k = input('수정할 학생의 이름: ')
        if k in name:
            a = name.index(k)
            del name[a]
            del score[a]
        name.append(k)
        t = input('키: ')
        hight.append(t)
    
    '''
    Hight= int(input('키: '))
    name.append(Name)
    hight.append(Hight)

    n = input('데이터를 확인하고 싶으면 1번을 누르세요: ')
    if n == '1':
        for a in range(len(hight)-2,-1,-1):
            for b in range(0, a+1):
                if hight[b]>hight[b+1]:
                    hight[b],hight[b+1] = hight[b+1],hight[b]
                    name[b],name[b+1] = name[b+1],name[b]

        hight.reverse()
        name.reverse()
        for i in range(0, len(hight)):
            print(name[i], ': ', hight[i] ,end=' ')
            print()