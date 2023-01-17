def outcode(x,y):
    bit=[None,None,None,None]
    if x<xmin:
        bit[0]=1
    else:
        bit[0]=0
    if x>xmax:
        bit[1]=1
    else:
        bit[1]=0
    if y<ymin:
        bit[2]=1
    else:
        bit[2]=0
    if y>ymax:
        bit[3]=1
    else:
        bit[3]=0
    return "{}{}{}{}".format(bit[3],bit[2],bit[1],bit[0])

def cs_right(x,y):
    yn=y+m*(xmax-x)
    xn=xmax
    return xn,yn
def cs_left(x,y):
    yn=y+m*(xmin-x)
    xn=xmin
    return xn,yn
def cs_top(x,y):
    yn=ymax
    xn=x+(1/m)*(ymax-y)
    return xn,yn
def cs_bottom(x,y):
    yn=ymin
    xn=x+(1/m)*(ymin-y)
    return xn,yn

def cohen_sutherland(x1,y1,x2,y2):
    print("Cohen Sutherland")
    oc1=outcode(x1,y1)
    oc2=outcode(x2,y2)
    while(True):
        print(oc1)
        print(oc2)
        print("({},{}) ({},{})".format(x1,y1,x2,y2))
        if (oc1=='0000' and oc2=='0000'):
            print("Inside zone")
            break 
        elif (int(oc1,2)& int(oc2,2)):
            print("completely outside")
            break
        else:
            if(oc1!="0000"):
                print("outcode 1 is not zero")
                if oc1[0]=="0":
                    x1,y1=cs_top(x1,y1)
                    oc1=outcode(x1,y1)
                if oc1[1]=="0":
                    x1,y1=cs_bottom(x1,y1)
                    oc1=outcode(x1,y1)
                if oc1[2]=="0":
                    x1,y1=cs_right(x1,y1)
                    oc1=outcode(x1,y1)
                if oc1[3]=="0":
                    x1,y1=cs_left(x1,y1)
                    oc1=outcode(x1,y1)
            else:
                print("outcode 2 is not zero")
                if oc2[0]=="0":
                    x2,y2=cs_top(x2,y2)
                    oc2=outcode(x2,y2)
                if oc2[1]=="0":
                    x2,y2=cs_bottom(x2,y2)
                    oc2=outcode(x2,y2)
                if oc2[2]=="0":
                    x2,y2=cs_right(x2,y2)
                    oc2=outcode(x2,y2)
                if oc2[3]=="0":
                    x2,y2=cs_left(x2,y2)
                    oc2=outcode(x2,y2)


f=open("clipping.txt")
n=int(f.readline())
for i in range(n):
    a=f.readline().split(" ")
    xmin,ymin,xmax,ymax=int(a[0]),int(a[1]),int(a[2]),int(a[3])
    print(xmin,ymin,xmax,ymax)
    m=int(f.readline())
    for j in range(m):
        b=f.readline().split(" ")
        x1,y1,x2,y2=int(b[0]),int(b[1]),int(b[2]),int(b[3])
        print(x1,y1,x2,y2)
        m=(y2-y1)/(x2-x1)
        print(m)
        cohen_sutherland(x1,y1,x2,y2)