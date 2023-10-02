import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (18,10)
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['axes.linewidth'] = 1

font = {'size': 16}
plt.rc('font', **font)

# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "sans-serif",
#     "font.serif": ["Computer Modern Serif"],
#     })

# plt.rcParams['font.sans-serif'] = "Arial"

plt.rc('ytick.major', size=7)
plt.rc('xtick.major', size=7)
plt.rc('ytick.major', width=1)
plt.rc('xtick.major', width=1)

plt.rcParams['axes.spines.top'] = True
plt.rcParams['axes.spines.bottom'] = True
plt.rcParams['axes.spines.left'] = True
plt.rcParams['axes.spines.right'] = True

plt.rc('ytick.minor', size=4)
plt.rc('xtick.minor', size=4)
plt.rc('ytick.minor', width=1)
plt.rc('xtick.minor', width=1)

plt.rcParams['xtick.major.pad']= 8
plt.rcParams['ytick.major.pad']= 8

plt.rc('lines', linewidth=2)

def title(ax, title='title', fontsize=20, fontweight='bold', pad=15):
    
    ax.set_title(title, fontweight=fontweight, pad=pad)

    return