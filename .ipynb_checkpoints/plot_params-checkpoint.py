import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (18,10)
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['axes.linewidth'] = 0.5

font = {'size': 13}
plt.rc('font', **font)

#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "sans-serif",
#    "font.serif": ["Computer Modern Serif"],
#    })

plt.rcParams['font.sans-serif'] = "Arial"

plt.rc('ytick.major', size=7)
plt.rc('xtick.major', size=7)
plt.rc('ytick.major', width=0.5)
plt.rc('xtick.major', width=0.5)

plt.rc('ytick.minor', size=4)
plt.rc('xtick.minor', size=4)
plt.rc('ytick.minor', width=0.5)
plt.rc('xtick.minor', width=0.5)

plt.rcParams['xtick.major.pad']= 2
plt.rcParams['ytick.major.pad']= 2

plt.rc('lines', linewidth=1)