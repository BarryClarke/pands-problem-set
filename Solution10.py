# Program that displays a plot of the functions x, x*x and 2 to the power of x
# Barry Clarke 27th Mar 2019
# Rev0 - Initial Revision

import numpy
import matplotlib.pyplot as plot
import pylab                        # Pylab allows the addition of a legend in a plot. Reference: https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible

# setup of the plot chart
x = numpy.arange(0, 5, 1)


# plot in the range of 0 to 4 curves for x, x squared, and 2 to the power of x
pylab.title('Plot of x, $x^{2}$ and $2^{x}$ as a function of x', fontweight='bold')    # Superscripts in python plots. Reference: https://stackoverflow.com/questions/21226868/superscript-in-python-plots
pylab.xlabel('x')
pylab.ylabel('f(x)')
pylab.plot(x, x, 'r-', label='x')
pylab.plot(x, x**2, 'b-', label='$x^{2}$')
pylab.plot(x, 2**x, 'g-', label='$2^{x}$')
pylab.legend(loc='upper left')
pylab.axis([0, 5, 0, 20])
pylab.show()