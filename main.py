import numpy as np
import matplotlib.pyplot as plt

dataset = [
    [2632359, 171450],
    [3524093, 215708], 
    [3966793, 235781], 
    [4442173, 220126], 
    [3421561, 224398], 
    [4356888, 254213], 
    [3364653, 249005], 
    [3172396, 320535],
    [2288357, 180506],
    [2890958, 201915],
    [7594840, 394900],
    [3725373, 265283],
    [4250672, 401145],
    [3378163, 230699],
    [3261286, 241574],
    [3157336, 281438],
    [3888997, 373184],
    [2575002, 239034],
    [4418910, 455106],
    [2485337, 213187]
    ]


def create_graph():
    x =  [i[0] for i in dataset]
    y =  [i[1] for i in dataset]


    coef = np.polyfit(x,y,1)
    poly1d_fn = np.poly1d(coef) 
    
    plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')
    plt.xlim(0, len(dataset))
    plt.ylim(0, len(dataset))


def regression(data):
    a=b=x=y=xx=xy=0
    n = len(data)
    for i in range(n):
        x+=data[i][0]
        y+=data[i][1]
        xx+=data[i][0]**2
        xy+=data[i][0]*data[i][1]
    a = (n*xy-x*y)/(n*xx-x**2)
    b = (y-a*x)/n
    return a, b
    

def predict(a, b, x):
    return b+a*x

def init():
    a, b = regression(dataset)
    x = input("Сколько просмотров: ")
    prediction = predict(a, b , int(x))
    print('Лайков будет примерно - ', prediction)
    create_graph()

init()

