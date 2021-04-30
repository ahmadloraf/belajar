print(".::Program Nilai Faktorial::.\n")

def faktorial(i):
    a = 1
    b = str(i) + "!= "

    while i > 1 :
        a =a * i
        b+=str(i) + " * "
        i =i - 1

    b += "1 ="

    print( b , a )

i = int(input("Masukkan nilai bilangan :"))
faktorial(i)