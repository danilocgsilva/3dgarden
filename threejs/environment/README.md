# Publishing 3d into web

This is an typical node project. If you already is used to such project, you know:

```
npm install
npm run dev-default
```

After the npm install, other scripts other than `dev-default` are available as well:

```
npm run dev-2000
```
Will display 2.000 cubes randonly positioned in space forming a sphere.

```
npm run dev-10000
```
Will display 10.000 cubes randonly positioned in space forming a sphere.

This set is based on Three.js starterkit from Bruno Simon of https://threejs-journey.xyz/.

Having the things running in web is a more suitable way to publish an show things to people.

## How to play with it?

After running the project, you can spect the resulting through 3d space:

* click and drag: rotate the forming sphere
* scroll well, or drag the middle mouse button: zoom in and zoom out
* shift + click and drag: perform a *pan* move

## Performance of spheres of cubes

As you can check in the initial [README.md](../../README.md), after founding the functions required to set a vector direction, then comes the time to play with it, what is an oportunity to test the frameworks capabilities.

I got three hardware untill now to run the scene. Cutting details about overall hardware, I will only give an idea about the hardware by the processor model, so you may guess also the overall porpouse of the machine, as well as it age.

The first hardware where I play was a i7-12700H, where I have tested only on Windows 11. The performance there disapointed me a litte. The hardware are great for playing games and even to general work on Blender. But I thing that some optimizations from the framework should be required. The scene worked but with a relatively low fps. Not measured, but roughtly about 15 to 20, and also showed some instability. Interestly to say that running the Windows Task Manager, I see that it was using only 10% of the dedicated graphic card.

There's also the i7-1165G7. Kind disapoint as well, because the browser does not staded up with 10.000 cubes. As the computer tried to open the browser, it emmediately closes. Apparently some kind of memory overflow happened. This is why I created a scene with 2.000 cubes as well. So this hardware could open with no issues, authough I think that performance was bellow from what I have expected.

More impresive behaviour occurs in i5-8250U. Supposedly, the older and for less resource hungry designed hardware, what is expected the worse performance. But that don't happened! This hardware is dualbooted with Windows 11 and Linux Fedora, so I tested in both operationg system. And the performance was pretty aceptable! The 10.000 cubes scene worked without issues both in Windows and Linux. Even the performance of 10.000 cubes becomes very stable all the time, and by eye, may near from 20fps in Linux.

