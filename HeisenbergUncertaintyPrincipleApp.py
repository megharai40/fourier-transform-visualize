from hydralit import HydraApp
import streamlit as st
from FourierTransform import FourierTransformApp
from wavepacket import wavepacketapp


if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!
    app = HydraApp(title='Heisenberg Uncertainty Principle',favicon="🐙")
  
    #add all your application classes here
    app.add_app("Fourier Transform Visualiser", icon="🏠", app=FourierTransformApp())
    app.add_app("Wavepacket Visualiser",icon="🔊", app=wavepacketapp())

    #run the whole lot
    app.run()
