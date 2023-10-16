#pip install ipywidgets


import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, integrate, oo, exp
import ipywidgets as widgets
from IPython.display import display

# Create a function to update the plot and integral calculation
def update_plot(change):
    x_val = x_slider.value
    integral_expr = (exp(-2*np.pi*x_sym) - exp(-4*np.pi*x_sym)) / x_sym
    result = integrate(integral_expr, (x_sym, 0, x_val))

    plt.figure(1)
    plt.clf()

    plt.subplot(121)
    plt.plot(x, y)
    plt.ylim(-10, 10)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of f(x)')

    plt.subplot(122)
    plt.text(0.5, 0.5, r'$\int_{0}^{\infty}\frac{e^{-2\pi x}-e^{-4\pi x}}{x}dx$', fontsize=14)
    plt.text(0.5, 0.4, f'Result: {result}', fontsize=14)
    plt.axis('off')
    plt.title('Integral Calculation')

# Create a slider for the input value
x_sym = symbols('x')
x_slider = widgets.FloatSlider(
    value=1.0,
    min=0.01,
    max=10,
    step=0.01,
    description='x_val:',
    continuous_update=False
)

x_slider.observe(update_plot, 'value')

# Initial plot
x = np.linspace(-5, 5, 100)
y = (x**2 - 1) / (x - 1)
update_plot(None)

# Display the widgets
display(x_slider)
