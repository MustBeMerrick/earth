We begin by defining the variables as seen in figure 1. 
We assume the sun is orbiting in a plane parallel to the x-y plane, at some height, $h$, above the ground, with orbital radius, $R$. We place the origin of our coordinate system at the observer, yielding the following vector-valued parameterized position of the sun as a function of $t$

$$\vec{s} = x(t)\hat{i}+y(t)\hat{j}+z(t)\hat{k}$$

where, 

$$x(t) = m+Rcos(2\pi ft - \frac{\pi}{2})$$

$$y(t) = n-Rsin(2\pi ft - \frac{\pi}{2})$$

$$z(t) = h$$


With the following parameter definitions:

<p align=center> Sun orbit centered at $(m,n)$ </p>
<p align=center> $R$: Sun orbit radius </p>
<p align=center> $h$: sun height above ground </p>
<p align=center> $f=1/T$, where $T=24$ hrs </p>
<p align=center> $t$: time of day, in hrs </p> 

Note that the phase shifting of $sin$ and $cos$ in the $x(t)$ and $y(t)$ components of the sun's position simply allow for the following boundary conditions:

<p align=center> Sun rises in east $(+x)$ and sets in west $(-x)$ </p>
<p align=center> $t=0$: Midnight (sun furthest from observer) </p>
<p align=center> $t=12$: Noon (sun closest to observer) </p>

The math can be simplified a bit by choosing a coordinate system such that the center of the sun's orbit (directly due north) lies on the y-axis itself, resulting in no x-offset $(m=0)$. The vector-valued position of the sun thus becomes

$$x(t) = Rcos(2\pi ft - \frac{\pi}{2})$$

$$y(t) = n-Rsin(2\pi ft - \frac{\pi}{2})$$

$$z(t) = h$$

The x-y component, $\vec{r}$, is given by just the x and y components of $\vec{s}$. The magnitude of r can be computed using the L2 norm, and is given by

$$\| \vec{r} \| = \sqrt{R^2+n^2-2Rnsin(2\pi ft - \frac{\pi}{2})}$$ 

From figure 1, a relationship between $\phi$ and $\| \vec{r} \|$ is given by

$$tan(\phi) = \frac{\| \vec{r} \|}{h} = \frac{\sqrt{R^2+n^2-2Rnsin(2\pi ft - \frac{\pi}{2})}}{h}$$

And ultimately solving for $\phi$ yields

$$\phi = tan^{-1}\left[\frac{\sqrt{R^2+n^2-2Rnsin(2\pi ft - \frac{\pi}{2})}}{h}\right]$$

We've now defined $\phi$, the angle between the sun and the vertical axis, with respect to the observer, as a function of $t$ (where $R$, $n$, $h$, and $f$ are constant).


