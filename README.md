# 3dgarden

Several experiments applying programming to 3d space.

* [Blender, a grat tool to use](#Blender--a-grat-tool-to-use)
* [3d in javascript](#3d-in-javascript)
* [Where is the center of universe?](#Where-is-the-center-of-universe?)
* [How to position cubes forming a sphere at random position in the space?](#How-to-position-cubes-forming-a-sphere-at-random-position-in-the-space?)
* [The way of the 10.000 sphere](#The-way-of-the-10.000-cubes)

## Blender, a great tool to use

[Blender](https://www.blender.org/) is the first place where I will test the scripts and algorithms. So currently, much of the work will be runned in Blender. You can do it as well! Download Blender, go to the scripting tab (check tabs right at the right of main menus in Windows), open the script and execute with the *play* icon or with the `alt` + `p` shortcut.

## 3d in javascript

Having experiments done in javascript is also interesting, because doing it in javascript (in webbrowser frontend) is an obvious way to offer interactivity to people, that may inspect a 3d scne right on the browser.

Browser ships with technologies as WebGL to use graphic cards capabilities and offers 3d experiences. There's also some javascript libraries frameworks like [Three.js](https://threejs.org/) and [Babylon.js](https://www.babylonjs.com/) designed to make the 3d web publishing easier.

Some 3d experiments was done in this project and you can check it in the `threejs` folder. Check its [README.md](threejs/README.md).

## Where is the center of universe?

I am not confortable saying that everything is the center of the universe. I understand that, once everything comes from the same point, so everything can be considered the center of universe. The problem with that is that, if there were an expansion, so this expansion still have a center, a point in the space where..., bit hard to explain and define, but stuffs will be more clear after some 3d representation.

The first chalenge to deal is to randonly set a direction on the 3d space where objects will be pointed. Let's say, a vector. After the vector defined, so them we can define a speed.

The first idea is to use some sort of calculation involving trigonometry. One result is the `tri_party.py`. Fail to create the first objective, but did created an interesting effect. For this script, you can play with values from `ra1` and `ra2` (radius1 and radius2, representing angles in two axis). Also can play with the range parameter, but caution here! A much large number in range may freeze your Blender, with will took a long time to create such dense number of tiny cubes.

* [Check the sphere of cubes tests in Blender](sphere_of_cubes.md)

## How to position cubes forming a sphere at random position in the space?

We got both scripts written in Python and in Javascript.

In python, the snippet can be found in `blender_scripts/randomsphere_onepass.py` in the `getVector` function:

```python
from random import random

def getVector():
    x = random() * 2 - 1
    y = random() * 2 - 1
    z = random() * 2 - 1
    
    distance_from_center = math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
    
    vx = x * (1 / distance_from_center)
    vy = y * (1 / distance_from_center)
    vz = z * (1 / distance_from_center)

    return (vx, vy, vz)
```

The javascript counterpart can be found in `threejs/environment/src/building_environment/getVector.js`:
```javascript
const getVector = () => {
    const x = Math.random() * 2 - 1
    const y = Math.random() * 2 - 1
    const z = Math.random() * 2 - 1

    const distance_from_center = Math.sqrt(x ** 2 + y ** 2 + z ** 2)

    const vx = x * (1 / distance_from_center)
    const vy = y * (1 / distance_from_center)
    const vz = z * (1 / distance_from_center)

    return {
        x: vx,
        y: vy,
        z: vz
    }
}

export default getVector
```

The idea of script is:

* Pass one: calculates random number between -1 and 1 and assign to three different values a random result, each one representing a random *amount* of displacement from the origin in the 3d space.

* Pass two: here we calculates the *distance of center* variable present in both script. It is just the function of *calculating the distance between two points in 3d space* beign aplied. Much more simple, because one of the points aways is the center of 3d space (position 0, 0, 0) makes us cut some of the function stuff.

* Pass three, the normalization: the intent of those calculations is merely get a vector random direction. The resulting point already is in an random direction, but to considers it as a vector direction, it must have a distance equal to 1 from the center. So the next step is to *normalize* the three axis value so they have a distance equal to 1. The resulting equation is just a equivalente function to check the proportionality for all three axis so the distance matches 1. Just multiplies all three axis to this same proportion.

## The way of the 10.000 cubes

The first thing after knowing the function find a vector position is to play with it and test softwares, languages and frameworks on its capabilities.

You can check the sections below.

* [Blender experiments](blender/sphere_of_cubes.md)
* [Javascript experiments](threejs/environment/README.md)
* [Facing Blender and Three.js performance](blender_x_threejs.md)

## Shooting the fragments

The 10.000 cubes experiments allowed the research for some introdutory knowledge to simulate particles from an expasion, going to any direction, taking variets of speeds (a graph of the big bang?). The function of random direction in 3d space are done. Now is time to animate stuffs.

More details about this task in [Big Bang of cubes](blender/big_bang_of_cubes/README.md)

