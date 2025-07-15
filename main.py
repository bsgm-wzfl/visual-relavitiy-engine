import matplotlib.pyplot as plt
import matplotlib.animation as animation
from relativity import time_dilation, length_contraction, gamma, c

# Set initial parameters
v = 0.8 * 299792458
L0 = 10  # meters
t0 = 1   # seconds

L = length_contraction(L0, v)
T = time_dilation(t0, v)

fig, ax = plt.subplots()
ax.set_xlim(0, 15)
ax.set_ylim(0, 1)
rect = plt.Rectangle((0, 0.4), L0, 0.2, color='blue')
ax.add_patch(rect)

def animate(frame):
    contracted_length = length_contraction(L0, v)
    rect.set_width(contracted_length)
    rect.set_x(frame * 0.1)
    return rect,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.title("Length Contraction at v = 0.8c")
plt.show()

import time

def simulate_clocks(v, duration=10):
    t0 = 0
    tmoving = 0
    g = gamma(v)
    start = time.time()
    while time.time() - start < duration:
        t0 += 1
        tmoving += 1 / g
        print(f"Rest Clock: {t0:.2f}s | Moving Clock: {tmoving:.2f}s")
        time.sleep(1)

simulate_clocks(0.8 * c)

v_input = float(input("Enter speed as fraction of c (e.g. 0.5): ")) * c
L0 = 10
print("Contracted length:", length_contraction(L0, v_input))