import matplotlib.pyplot as plt
import numpy as np
def smooth(data):
  data = np.array(data)
  xsort = data[data[:,0].argsort()]
  timeca = xsort[0]
  timeve = xsort[1]-min(xsort[1])
  Averagetime = np.zeros(346)
  Averagecas = np.zeros(346)
  for i in np.linspace(9,354,346).astype(int):
    Averagetime[i-9] = (timeve[i]+timeve[i+1]+timeve[i+2]+timeve[i+3]+timeve[i+4]+timeve[i+5]+timeve[i+6]+timeve[i+7]+timeve[i+8]+timeve[i+9]+timeve[i-1]+timeve[i-2]+timeve[i-3]+timeve[i-4]+timeve[i-5]+timeve[i-6]+timeve[i-7]+timeve[i-8]+timeve[i-9])/19
    Averagecas[i-9] = (timeca[i]+timeca[i+1]+timeca[i+2]+timeca[i+3]+timeca[i+4]+timeca[i+5]+timeca[i+6]+timeca[i+7]+timeca[i+8]+timeca[i+9]+timeca[i-1]+timeca[i-2]+timeca[i-3]+timeca[i-4]+timeca[i-5]+timeca[i-6]+timeca[i-7]+timeca[i-8]+timeca[i-9])/19
  Averagetime = Averagetime
  #return Averagetime, Averagecas
  plt.hold(True)
  plt.plot(Averagetime,Averagecas,'k')
  plt.plot(timeve,timeca,'b--')
  plt.hold(False)
  AverageData = [Averagetime,Averagecas]
  np.savetxt("AverageData.csv", AverageData, delimiter=",")
