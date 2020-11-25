s1=str(input('Primul cuvant:'))
s2=str(input('Al doilea cuvint:'))
s3=str(input('Al treilea cuvint:'))
s4=str(input('Al patrulea cuvint:'))
if len(s1)<3 and len(s2)<3 and len(s3)<3 and len(s4)<3:
    print('Conditia nu se respecta')
else:
    cuvantul=s1[0] + s1[1] + s2[0] + s3[0] + s3[1] + s3[2]
for i in range (len(s4)//2):
    cuvantul+=s4
print(f'Cuvintele introduse: {s1}, {s2}, {s3}, {s4}')
print('Cuvvintul nou este:',cuvantul)