
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.title("Fourier Transform Visualizer")
#Slider


num_k = st.sidebar.slider('Number of Superposed Waves',1,1000,1 )
am = st.sidebar.slider('Maximum k of Superposed Waves',1.0,30.0,10.0 )
sig = st.sidebar.slider('Spread of k (sigma)',0.01,10.00,2.00 )  # min: , max: , default: 
height = st.sidebar.slider('Size of plots',0,20,7)

ko=0.00
xo=0.00
n=1000
k=np.linspace(-10.00,10.00,n)
x=np.linspace(-10.00,10.00,n)
#for superposed waves
sig1=2.0

k1= np.linspace(-1.8*sig1,1.8*sig1,n)
x1=np.linspace(-100.00,100.00,n)

sum_fx=[]
so=0
ak=[]
fk=[]
fk1=[]
for i in range(n):
  fk.append((sig/np.sqrt(2*np.pi))*np.exp((-0.5*sig**2)*(k[i]-ko)**2)) #from lecture 11
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


u=[]
for i in range(n):
  u.append(np.exp(-0.5*((x[i]-xo)/sig)**2))

#Plot of Wavepacket
fig2,ax = plt.subplots(figsize=(20, height))
ax.set_title("Plot of Wavepacket",fontsize=30)
ax.plot(x1,sum_fx)
ax.set_xlabel("x",fontsize=30)
ax.set_ylabel("f(x)",fontsize=30)
st.pyplot(fig2)

#Gaussian Spread of Amplitude
fig,ax = plt.subplots(figsize=(20, height))
ax.set_title("Gaussian Spread of Amplitude",fontsize=30)
ax.plot(k,fk)
ax.set_xlabel("k",fontsize=30)
ax.set_ylabel("A(k)",fontsize=30)
st.pyplot(fig)

#Plot of Gaussian Spread of Position
fig1,ax = plt.subplots(figsize=(20, height))
ax.set_title("Gaussian Spread of Position",fontsize=30)
ax.plot(x,u)
ax.set_xlabel("x",fontsize=30)
ax.set_ylabel("u(x)",fontsize=30)
st.pyplot(fig1)




