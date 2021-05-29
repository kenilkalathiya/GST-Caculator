def total(*args):
    t=0
    for i in args:
        t += i
    return t

def sub(*args):
    s=args[0] 
    for i in args[1:]:
        s = s - i 
    return s

def mult(*args):
    m=1
    for i in args:
        m *= i
    return m

def div(*args):
    d=args[0]
    for i in args[1:]:
        d = d/i
    return d

def gst(*args):
    a=args[0]
    g = int(input("Enter your GST % :"))
    g_a=a*g/100
    t_a=a + g_a
    return g_a,t_a

 
print("Select Operation : \n 1.Addition \n 2.Subsutution\n 3.Multiplication\n 4.Division\n 5.GST\n 6.Exit")

while True:
    c = int(input("Enter choice :"))
    b = list(map(int,input("Enter your number").split()))
    if c==1:
        print(total(*b))
    elif c==2:
        print(sub(*b))
    elif c==3:
        print(mult(*b))
    elif c==4:
        print(div(*b))
    elif c==5:
        a,d=gst(*b)
        print(f"GST amount : {a}")        
        print(f"Total amount : {d}")        
    else:
        break