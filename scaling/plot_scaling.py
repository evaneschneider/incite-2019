#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

gpu=np.array([1, 8, 64, 512, 4096])
ttot=np.array([23.3, 44.6, 49.9, 58.1, 97.9])
tinit=np.array([9.39, 12.0, 13.5, 21.7, 58.9])
tsinit = ttot - tinit
tcomm=np.array([1.53, 13.0, 13.3, 13.7, 15.0])
tvl=np.array([12.8, 20.9, 24.6, 24.0, 25.3])



bg_size = 0.1
tg_size = 0.02
lg_size = 0.10
rg_size = 0.03

wx = 1.0 - lg_size - rg_size
wy = 1.0 - bg_size - tg_size

fsize = 5.

fig = plt.figure(figsize=(fsize,fsize*wx/wy))

yave = tsinit[2]
yl = [yave,yave]
xl = [0.8,2e4]
plt.plot(xl,yl,linestyle='--',color="0.75",linewidth=2)
yave = tvl[2]
yl = [yave,yave]
xl = [0.8,2e4]
plt.plot(xl,yl,linestyle='--',color="0.75",linewidth=2)
yave = tcomm[2]
yl = [yave,yave]
xl = [0.8,2e4]
plt.plot(xl,yl,linestyle='--',color="0.75",linewidth=2)

hfont = {'fontname':'Helvetica'}
plt.xticks(**hfont)
plt.yticks(**hfont)


plt.text(1.5,38,'Cholla Weak Scaling',color="0", fontsize=12, **hfont)

plt.text(3.0e2,38,'Total time',color="purple", fontsize=10, **hfont)
plt.text(3.0e2,26,'Integration',color="blue", fontsize=10, **hfont)
plt.text(3.0e2,16,'Communication',color="red", fontsize=10, **hfont)

ms = 5

plt.plot(gpu,tsinit,color="purple",linewidth=3,alpha=0.7)
plt.plot(gpu,tsinit,'o',color="purple",markersize=ms,alpha=0.7)
plt.plot(gpu,tvl,color="blue",linewidth=3,alpha=0.7)
plt.plot(gpu,tvl,'o',color="blue",markersize=ms,alpha=0.7)
plt.plot(gpu,tcomm,color="red",linewidth=3,alpha=0.7)
plt.plot(gpu,tcomm,'o',color="red",markersize=ms,alpha=0.7)

plt.xscale('log')
plt.xlim([0.9,1e4])
plt.ylim([0,40])
plt.ylabel(r'Wall Clock Time for 256$^3$ Cells per V100 GPU', fontsize=12, **hfont)
plt.xlabel(r'Summit GPUs', fontsize=12, **hfont)
#plt.show()

s = "weak_scaling_adiabatic.png"
plt.tight_layout()
plt.savefig(s, bbox_inches="tight", dpi=300)
plt.clf()
