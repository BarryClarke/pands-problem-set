# Program that displays a plot of the functions x, x*x and 2 to the power of x
# Barry Clarke 27th Mar 2019
# Rev1 - Updated to compute f(x) at intervals of 0.1, rather than intervals of 1 as previous

import numpy
import matplotlib.pyplot as plot
import pylab                        # Pylab allows the addition of a legend in a plot. Reference: https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible

# setup of the plot chart
x = numpy.arange(0, 4.01, 0.1)


# setting up the plot title and axes labels
pylab.title('Plot of x, $x^{2}$ and $2^{x}$ as a function of x', fontweight='bold')    # Superscripts in python plots. Reference: https://stackoverflow.com/questions/21226868/superscript-in-python-plots
pylab.xlabel('x', fontweight='bold')
pylab.ylabel('f(x)', fontweight='bold')
# Setting up each f(x), along with a legend
pylab.plot(x, x, 'r-', label='x')
pylab.plot(x, x**2, 'b-', label='$x^{2}$')
pylab.plot(x, 2**x, 'g-', label='$2^{x}$')
pylab.legend(loc='upper left')
# Setting up the axes limits
pylab.axis([0, 5, 0, 18])

pylab.show()