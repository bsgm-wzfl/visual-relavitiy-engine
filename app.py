import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from relativity import length_contraction, time_dilation

c = 299792458

st.title("🚀 Visual Relativity Engine")
st.markdown("### Explore Time Dilation and Length Contraction in Special Relativity")

v_frac = st.slider("Velocity (as a fraction of c)", 0.01, 0.99, 0.8)
v = v_frac * c

L0 = st.number_input("Proper Length (meters)", 1.0, 100.0, 10.0)
t0 = 1.0  # 1 second

L = length_contraction(L0, v)
T = time_dilation(t0, v)

st.markdown(f"**Contracted Length:** {L:.2f} m")
st.markdown(f"**Dilated Time:** {T:.2f} s (for 1s proper time)")

fig, ax = plt.subplots()
ax.set_xlim(0, 15)
ax.set_ylim(0, 1)
rect = plt.Rectangle((0, 0.4), L, 0.2, color='blue')
ax.add_patch(rect)
ax.set_title(f"Object moving at {v_frac:.2f}c")
st.pyplot(fig)