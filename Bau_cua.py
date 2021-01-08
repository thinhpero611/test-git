from random import randint

# yeu cua de bai cho nguoi dung

print('''Hay chon mot nhan vat de dat cuoc trong danh ssach duoc day:
0.Bau
1.Cua
2.ca
3.nai
4.ga
5.tom
SO TIEN( ngan dong)
Ban Chi Duoc Dat Toi Da 10 Lan Thoi\n''')

#du lieu ban dau

select = ['Bau', 'Cua', 'ca', 'nai', 'ga', 'tom']

#Nhap so luot chon

num_of_choice = int(input("So Lan Ban Chon: (Ban Chi duoc nhap toi da la 10) "))
loop = True
attempt =0
if num_of_choice >10:
    while loop:
        num_of_choice = int(input("Xin Loi Ban Da Nhap Qua 10 Lan! Vui Long Nhap Lai Mot Con So Khac: "))
        if num_of_choice <10: loop = False
        attempt +=1
        while loop:
            num_of_choice = int(input('Vui Long Nhap Lai!'))
            attempt +=1
            if attempt > 5:
                print('Ban Da Thu', attempt, 'roi')
            if num_of_choice <10:
                loop = False

#Nhap input
                
human_choice = []
money = []
dice_fit = [0,0,0]
answer = []

for i in range(num_of_choice):
    print('CHon Lan', i+1,':')
    choice = int(input('Nhap nhan vat:'))
    loop1 = True
    while loop1:   
        if choice > 5:
            choice = int(input('Xin Loi Khong co ten Nhan vat nay!Vui Long Nhap Lai: '))
        else: loop1 = False
    human_choice.append(choice)
    money.append(int(input('Nhap so tien dat cuoc cho nhan vat tren: ')))
    answer.append(dice_fit)
    print('-------------------------------------------------\n')

# yeu cau nguoi dung nhap them hay khong

loop2 = True
while loop2:
    ask = input('Ban co muon dat them mot luot nua khong ?(yes or no)')
    if ask == 'yes':
        more = int(input('Ban Muon Chon Lai Them Bao Nhieu Lan Nua'))
        num_of_choice += more
        for i in range(more):
            print('CHon Lan', i+1,':')
            choice = int(input('Nhap nhan vat:'))
            loop1 = True
            while loop1:   
                if choice > 5:
                    choice = int(input('Xin Loi Khong co ten Nhan vat nay!Vui Long Nhap Lai: '))
                else: loop1 = False
            human_choice.append(choice)
            money.append(int(input('Nhap so tien dat cuoc cho nhan vat tren: ')))
            answer.append(dice_fit)
            print('-------------------------------------------------\n')
        while loop2:
            ask_1= input('Ban Muon Dat Them Nua Chu ^.^ (yes or no)')
            if ask_1 == 'yes':
                more_1 = int(input('Ban Muon Chon Lai Them Bao Nhieu Lan Nua'))
                num_of_choice += more_1
                for i in range(more_1):
                    print('CHon Lan', i+1,':')
                    choice = int(input('Nhap nhan vat:'))
                    loop1 = True
                    while loop1:   
                        if choice > 5:
                            choice = int(input('Xin Loi Khong co ten Nhan vat nay!Vui Long Nhap Lai: '))
                        else: loop1 = False
                    human_choice.append(choice)
                    money.append(int(input('Nhap so tien dat cuoc cho nhan vat tren: ')))
                    answer.append(dice_fit)
                    print('-------------------------------------------------\n')
                loop2 = False
                print('''Ban Choi Vui Ve Nhe
Chuc Ban An Nhieu Tien!''')
            else:
                print('''Ban Choi Vui Ve Nhe
Chuc Ban An Nhieu Tien!''')
                loop2 = False
    else: loop2 = False
input('HAY NHAN BAT KY PHIM NAO!')

#tao xuc xac 

computer = []
for i in range(3):
    computer.append(randint(0,5))

#So sanh lua chon cua may va nguoi

print('Tong so tien ban dat cuoc:', sum(money))
print('Vay Ban Chon: ')
for i in range(num_of_choice):
    print(select[human_choice[i]], ':', money[i], 'ngan dong')          

print('\nXIN HAY KIEM TRA LAI MOT LAN NUA')
input('XONG ROI HAY NHAP OK !')

#ket qua xuc xat

print('-------------------------------------------------\n')
print("Ket qua Xuc Xat :")
for i in computer:
    print(select[i])

print('--------------------------------------------------\n')

#Ket qua cua nguoi dung

#kiem tra
    
print('TEST :')
print(f'humnan choice:{human_choice}\n',
      f'computer:{computer}\n',
      f'answer:{answer}\n',
      f'money:{money}\n',
      f'num of choice:{num_of_choice}\n')
print('--------------------------------------------------\n')
input('Press Any Key !......')
#

print('Ket qua ban trung duoc la:')
count = [[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(num_of_choice):
    for j in range(3):
        if select[human_choice[i]] == select[computer[j]]:
            count[i][j] = 1
            answer[i][j] = 1
            print('Ban trung', select[human_choice[i]], '\t')
           #print(f'answer[{i}][{j}] :{answer[i][j]}')
        print(count[i][j], ':', i, j)
    print('---------------------------------------------\n')
# tinh tien thang hay thua cua nguoi dung

money_win = 0
for i in range(num_of_choice):
    for j in range(3):
        money_win += count[i][j]*money[i]
t = money_win-sum(money)
if t > 0:
    print('ban an duoc:', t)
elif t ==0: print('Ban Hoa')
else: print('Ban thua voi tien bi mat la:',-t)

print('answer',answer)
print('count', count)

   
