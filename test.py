import numpy as np
N=5
press_2d = np.zeros((N,N))
press = np.zeros(N*N+1)

def guess(press_2d):
  for i in range(0,N):
    for j in range(0,N):
      cal_sum = 0
      for ii in range(0,N):
        cal_sum = cal_sum + press_2d[i][ii]
      for jj in range(0,N):
        cal_sum = cal_sum + press_2d[jj][j]

      cal_sum = cal_sum - press_2d[i][j]
      if (cal_sum %2 == 0):
        return 0

  return 1

def enumerate():
  #while(guess(press_2d)==0):
  i = 0
  while (i<2**(N*N)):
  #while (i<16):
    one_two(press, press_2d)
    if (guess(press_2d)==1):
      print press_2d

    i = i +1
    press[0]=press[0]+1
    c=0
    while(press[c]>1):
      press[c]=0
      c=c+1
      press[c]=press[c]+1
  return

def one_two(press, press_2d):
  #16,4
  for j in range(0,N*N):
    i1=j/N
    i2=j%N

    press_2d[i1][i2]=press[j]
    #print press_2d
  return press_2d

enumerate()
