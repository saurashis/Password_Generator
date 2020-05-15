import random
length=input('Enter your pasword length : ')
length=int(length)
alphabtes=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','_','+','=','~']
password=[]
word=''
if length<= 5 or length >= 20:
    print('minimum length should be-6 and maximum should be-20')
else:
    alp_len=length//2
    int_len=length-alp_len
    upper_alp_len=alp_len//2
    lower_alp_len=alp_len-upper_alp_len

    for i in range(lower_alp_len):
        lower=random.randint(0,25)
        password.append(alphabtes[lower])
    for t in range(upper_alp_len):
        upper_alph=random.randint(0,25)
        password.append(alphabtes[upper_alph].upper())


    for j in range(int_len):
        f=random.randint(0,22)
        password.append(number[f])

random.shuffle(password)

for k in password:
    word=word+k
print('your passsword- '+word)
