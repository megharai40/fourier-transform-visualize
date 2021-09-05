import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#add an import to Hydralit
from hydralit import HydraHeadApp

#create a wrapper class
class wavepacketapp(HydraHeadApp):

#wrap all your code in this method and you should be done
  def run(self):
    #Slider
    st.title("Wavepacket")
    st.markdown('Instructions at bottom of Page')
    n=1000
    num_k = st.sidebar.slider('Number of Superposed Waves',1,n,1 )
    am = 10.0
    
    #for superposed waves
    sig1=2.0
    k=np.linspace(-10.00,10.00,n)
    k1= np.linspace(-1.8*sig1,1.8*sig1,n)
    x1 = np.linspace(-100.00,100.00,n)

    sum_fx=[]
    fk1=[]
    for i in range(n):
      fk1.append(am*np.exp(-0.5*(k[i]/sig1)**2))

    #Sum of n number of waves
    gaussian = st.checkbox("Gaussian Distribution of k")

    a=np.ones(n)
    if gaussian:
      a=fk1
    for i in range(n):
      fx=[]
      for j in range(num_k):
        fx.append(a[j]*np.sin(k1[j]*x1[i]))
      sum_fx.append(sum(fx))
    
    #Plot of Wavepacket
    fig2,ax = plt.subplots(figsize=(20, 7))
    ax.set_title("Plot of Wavepacket",fontsize=30)
    ax.plot(x1,sum_fx,'black')
    ax.set_xlabel("x",fontsize=30)
    ax.set_ylabel("f(x)",fontsize=30)
    st.pyplot(fig2)
    st.markdown('**_For Wavepacket_** : Increase number of superposed waves using slider. Default values of k are equally spaced between a default range.')
