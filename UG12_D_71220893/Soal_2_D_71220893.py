print("~~~~ Table Matematika nichhhh ~~~~")
print("Pilihan Model Matematika")
print("1. Perkalian")
print("2. Pembagian")
inp = int(input("Masukan Model matematika yang diinginkan 1/2 :"))
x = int(input("Menampilkan table matematika dari angka :"))
if inp == 1 :
    count = 1 
    while count <= 10:
        print(x," x ", count ," = ", x*count)
    count += 1

elif inp == 2 :
    for jing in range(50,65):
        while jing  :
            print(jing," : ",x , " = ",jing/x)
        jing += 1 




