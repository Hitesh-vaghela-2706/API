import numpy as np

# x=[2014.0, 2015.0]
# y=[6.30000019073486, 6.19999980926514]

x= [2010,2011,2012,2013,2014] 
y=[1.5, 2.3, 2.0, 1.8, 2.1]

mean_x = np.mean(x)
mean_y = np.mean(y)
print("mean_x :- ",mean_x) 
print("mean_y :- ",mean_y)

X_MINUS_XBAR = []
Y_MINUS_YBAR = [] 
X_BAR_Y_BAR = [] 
X_MINUS_XBAR_SQUARE = []  

#Calculate (xx(bar)) & (YY(bar))
                  
#Calculate (X-X(bar)) & (YY(bar))
for i in range(len(x)):
    a = x[i] - mean_x
    X_MINUS_XBAR.append(a)
    b = y[i]- mean_y
    c = round(b,2)
    Y_MINUS_YBAR.append(c)
    # X_MINUS_XBAR.append((round(x[i] - mean_x), 2))
    # Y_MINUS_YBAR.append((round(y[i]- mean_y), 2))
print("X_MINUS_XBAR :- ",X_MINUS_XBAR)
print("Y_MINUS_YBAR :- " ,Y_MINUS_YBAR)
#Calculate (x-x(bar))*(YY(bar))

cover = 0.0

for i in range(len(x)):
    cover += (x[i] - mean_x) *  (y[i] - mean_y)
    X_BAR_Y_BAR.append((x[i] - mean_x) * (y[i] - mean_y))

#Calculate Square for (x - x(bar)) print("X MINUS_XBAR ::"X_MINUS_XBAR)

for i in range(len(X_MINUS_XBAR)):
    X_MINUS_XBAR_SQUARE.append(X_MINUS_XBAR[i]*X_MINUS_XBAR[i] )

print("X_MINUS_XBAR_SQUARE ::",X_MINUS_XBAR_SQUARE)

#Summation for (x-x(bar)) (YY(bar)) & (xx(bar)) Square

SUM_X_BAR_Y_BAR = sum(X_BAR_Y_BAR) 
SUM_X_MINUS_XBAR_SQUARE = sum(X_MINUS_XBAR_SQUARE)

#Slope Calculation mSUMX BAR_Y BAR / SUM X MINUS_XBAR_SQUARE
slope = SUM_X_BAR_Y_BAR / SUM_X_MINUS_XBAR_SQUARE
print("slope :- ",round(slope,2))






























#x= [2010,2011,2012,2013,2014] 
#y=[1.5, 2.3, 2.0, 1.8, 2.1]

#x= [2000, 2000, 2001, 2001, 2001, 2002, 2002, 2004, 2004, 2004] 
#y = [23.43, 11.36, 0.61, 0.57, 0.71, 17.37, 23.75, 27.65, 26.94, 23.75]

# x=[2002,2003] 
# y=[37.985,3408]