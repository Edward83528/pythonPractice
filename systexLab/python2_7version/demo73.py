import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,10,0.5)
plt.figure(1)
plt.subplot(3,1,1)
plt.plot(t,t,'r-')
plt.subplot(3,1,2)
plt.plot(t,t**2,'g-')
plt.subplot(3,1,3)
plt.plot(t,t**3,'b-')
plt.show()
