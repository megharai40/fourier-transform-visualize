import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt

st.title("Fourier Transform Visualizer")
#Slider

sig = st.sidebar.slider('Spread of k (sigma)',0.01,10.00,2.00 )  # min: , max: , default: 
height = st.sidebar.slider('Height of plots',0,20,7)

ko=0.00
xo=0.00
n=1000
k=np.linspace(-10.00,10.00,n)
x=np.linspace(-10.00,10.00,n)

ak=[]
fk=[]
for i in range(n):
  fk.append((sig/np.sqrt(2*np.pi))*np.exp((-0.5*sig**2)*(k[i]-ko)**2)) #from lecture 11

u=[]
for i in range(n):
  u.append(np.exp(-0.5*((x[i]-xo)/sig)**2))

fig,ax = plt.subplots(figsize=(20, height))
ax.plot(k,fk)
ax.set_xlabel("k")
ax.set_ylabel("A(k)")
st.pyplot(fig)

fig1,ax = plt.subplots(figsize=(20, height))
ax.plot(x,u,)
ax.set_xlabel("x")
ax.set_ylabel("u(x)")
st.pyplot(fig1)
