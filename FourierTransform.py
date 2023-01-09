import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#add an import to Hydralit
from hydralit import HydraHeadApp

#create a wrapper class
class FourierTransformApp(HydraHeadApp):

  #wrap all your code in this method and you should be done
  def run(self):
    st.title("Fourier Transform Visualizer")
    #Slider

    sig = st.slider('Spread of k (σk)',0.01,10.00,5.00 )  # min: , max: , default: 
    height = st.slider('Size of plots',0,20,7)

    ko=0.00
    xo=0.00
    n=1000
    k=np.linspace(-10.00,10.00,n)
    x=np.linspace(-10.00,10.00,n)

    so=0
    ak=[]
    fk=[]
    for i in range(n):
      fk.append((1/(sig*np.sqrt(2*np.pi)))*np.exp((-0.5*1/(sig**2))*(k[i]-ko)**2)) #from lecture 11

    #Sum of n number of waves
    st.markdown('Instructions at bottom of Page')
    u=[]
    for i in range(n):
      u.append(np.exp(-0.5*((x[i]-xo)*sig)**2))

    #Gaussian Spread of Amplitude
    fig,ax = plt.subplots(figsize=(20, height))
    ax.set_title("Gaussian Spread of Amplitude",fontsize=30)
    ax.plot(k,fk,'orange',linewidth = 5)
    ax.grid()
    ax.set_xlabel("k",fontsize=30)
    ax.set_ylabel("A(k)",fontsize=30)
    st.pyplot(fig)

    #Plot of Gaussian Spread of Position
    fig1,ax = plt.subplots(figsize=(20, height))
    ax.set_title("Gaussian Spread of Position",fontsize=30)
    ax.plot(x,u,'g',linewidth = 5)
    ax.grid()
    ax.set_xlabel("x",fontsize=30)
    ax.set_ylabel("u(x)",fontsize=30)
    st.pyplot(fig1)

    st.markdown('**_For Fourier Transform_** : The graphs demonstrate ')
    st.latex(r'''
    u(x) = e^{\frac{-1}{2} ((x-x_o)/\sigma_x)^2}
    ''')
    st.latex(r''' 
    A(k) = \frac{1}{\sqrt{2\pi}\sigma_k}e^{\frac{-1}{2\sigma_k^2} (k-k_o)^2}
    ''')
    st.latex(r''' 
    where \sigma_x = \frac{1}{\sigma_k}
    ''')
    st.markdown('u(x) and A(k) are Fourier Transforms of each other.')
    st.subheader('Made with :heart: by Megha Rai')
