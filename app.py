import streamlit as st
import pandas as pd
import numpy as np

st.latex("P(x)= a\cdot x^2+ b\cdot x+c")
a=st.number_input('a', key=1,value=1)
b=st.number_input('b', key=2,value=1)
c=st.number_input('c', key=3,value=1)
if b**2-4*a*c<0:
    st.text('La cuadrática no tiene raíces reales')
else:
    r1=(-b+np.sqrt(b**2-4*a*c))/(2*a)
    r2=(-b-np.sqrt(b**2-4*a*c))/(2*a)
    st.text('Las raices son {} y {}'.format(r1,r2))