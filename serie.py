#region serie fibonacci

#en sin usar DEF, es decir, sin funciones
#fn=f-1 + f-2
#f-1 va aser "a"
#f-2 va aser "b"
#fn resultado final
a,b = 0,1
#a=0 b=1
#iterante es una variable que tendra un comportamiento
#intrementar en el ciclo
for i in range(10):
    print(a)
    a,b=b,a+b
    #a=b y b=a+b
# 0 a,b=b,a+b a=0 b=1+0=1
# 1 a,b=b,a+b a=1 b=0+1=1
# 2 a,b=b,a+b a=1 b=1+1=2
# 3 a,b=b,a+b a=2 b=1+2=3
# 4 a,b=b,a+b a=3 b=2+3=5
# 5 a,b=b,a+b a=5 b=3+5=8
# 6 a,b=b,a+b a=8 b=5+8=13
# 7 a,b=b,a+b a=13 b=8+13=21
# 8 a,b=b,a+b a=21 b=13+21=34
# 9 a,b=b,a+b a=34 b=21+34=55
#of the fibonacci sequence