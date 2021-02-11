Python 2.7.16 (default, Jan 26 2020, 23:50:38) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import numpy as np

def f(x):
    """function to test in our derivative
    program"""
    return x**3 - 5*x + 2

def analytic_deriv_f(x):
    """The analytic derivative of
     x**3 - 5*x + 2."""
    return 3*x**2 - 5

def absolute_error(truth, computed):
    """returns the absolute error between
    the computed and true value"""
    return np.abs(truth-computed)

def relative_error(truth, computed):
    """returns the relative error between
    the computed and true value"""
    return ((analytic_deriv_f - absolute_error) / absolute_error)

def forward_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the forward
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x)
    denominator = h
    return numerator/denominator

def central_difference(x, h, func=None):
    """Computes the numerical derivative
    of an arbitrary function using the central
    difference method.
    x: point at which to evaluate the func
    h: stepsize to compute the secant
    func: a valid python function"""
    numerator = func(x+h)-func(x-h)
    denominator = 2*h
    return numerator/denominator

if __name__ == "__main__":
    print("The central difference of x**3 - 5*x + 2,"+
          " evaluated at 0, with stepsize 0.01, is:")
    print(str(forward_difference(0, 0.01, f)))

    print("Generating data for part 1 of problem 1")
    #Data for part 1, over the range -5-->5
    output_data_fullrange = []
    h = 0.01
    #loop over an array from -5 to 5  in steps of 0.01
    for x_val in np.arange(-5, 5, h):
        #calculate analytic derivative, fw diff, and central diff
        analytic_diff = analytic_deriv_f(x_val)
        fw_diff = forward_difference(x_val, h, f)
        central_diff = central_difference(x_val, h, f)
        #store this as a tuple
        data = (x_val, analytic_diff, \
                fw_diff, central_diff)
        #append this to a list
        output_data_fullrange.append(data)

    #save this as an output textfile for plotting
    fname_part1 = 'problem_1_1_data.txt'
    np.savetxt(fname_part1, #filename
               np.array(output_data_fullrange), #data to save
               delimiter=',', #how to separate values in the file
               header=("function: x**3-5x+3\n"+
               "x, analytic_deriv(x), fw_diff(x), central_diff(x)"),
               fmt = '%.05f')#<--5 digits of precision, look up "format codes"
    print("Saved data to: "+fname_part1+"\n\n")

    print("Generating data for part 2 of problem 1")
    #now you do the rest...
    
>>> #The plot of the error in the approximation from the forward and central difference method, at the value x=0, as a function of h
>>> x = 0
>>> error_data_fullrange =[]
>>> for h_val in np.arange(-5, 5, x):
	ab_error = absolute_error(h_val, h, f)
	re_error = relative_error(h_val, h, f)
	data = (h_val, ab_error, re_error)
	error_data_fullrange.append(data)

	

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for h_val in np.arange(-5, 5, x):
ZeroDivisionError: division by zero
>>> error_data_fullrange =[]
>>> x = 0
>>> for h_val in np.arange(-5, 5, x):
	ab_error = absolute_error(h_val, h, f)
	re_error = relative_error(h_val, h, f)
	data = (h_val, ab_error, re_error)
	error_data_fullrange.append(data)

	

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    for h_val in np.arange(-5, 5, x):
ZeroDivisionError: division by zero
>>> h_val = h(0)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    h_val = h(0)
NameError: name 'h' is not defined
>>> import matplotlib.pyplot as plt
>>> if __name__ == "__main__":
    fname_part1 = 'problem_1_1_data.txt'
    data_to_plot = np.loadtxt(fname_part1,
                              delimiter=',',
                              skiprows=2)
    print("Data to plot:")
    print(data_to_plot)

    

Traceback (most recent call last):
  File "<pyshell#17>", line 5, in <module>
    skiprows=2)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/lib/npyio.py", line 729, in loadtxt
    fh = iter(open(fname, 'U'))
IOError: [Errno 2] No such file or directory: 'problem_1_1_data.txt'
>>> """wow i really have no clue what is going on here..."""
'wow i really have no clue what is going on here...'
>>> data = (relative_error, h(x)):
	
SyntaxError: invalid syntax
>>> data = (relative_error, h(x))

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data = (relative_error, h(x))
NameError: name 'relative_error' is not defined
>>> data = relative_error(h(x))

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data = relative_error(h(x))
NameError: name 'relative_error' is not defined
>>> """what does that mean???!!!! it was already declared in the begining im gonna lose my mind"""
'what does that mean???!!!! it was already declared in the begining im gonna lose my mind'
>>> """i want to plot the reletavistic error to function of h using matplotlib and then using a log scale, i feel like i know what to do but exicute it"""
'i want to plot the reletavistic error to function of h using matplotlib and then using a log scale, i feel like i know what to do but exicute it'
>>> 
