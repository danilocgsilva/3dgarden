# 3dgarden

Several experiments applying programming to 3d space.

## Blender, I great tool to use

[Blender](https://www.blender.org/) is the first place where I will test the scripts and algorithms. So currently, all scripsts presented here will be runned in Blender. You can do it as well! Download Blender, go to the scripting tab (check tabs right at the right of main menus in Windows), open the script and execute with the *play* icon or with the `alt` + `p` shortcut.

## Where is the center of universe?

I am not confortable saying that everything is the center of the universe. I understand that, once everything comes from the same point, so everything can be considered the center of universe. The problem with that is that, if there were an expansion, so this expansion still have a center, a point in the space where..., bit hard to explain and define, but stuffs will be more clear after some 3d representation.

The first chalenge to deal is to randonly set a direction on the 3d space where objects will be pointed. Let's say, a vector. After the vector defined, so them we can define a speed.

The first idea is to use some sort of calculation involving trigonometry. One result is the `tri_party.py`. Fail to create the first objective, but did created an interesting effect. For this script, you can play with values from `ra1` and `ra2` (radius1 and radius2, representing angles in two axis). Also can play with the range parameter, but caution here! A much large number in range may freeze your Blender, with will took a long time to create such dense number of tiny cubes.

* [Check the sphere of cubes tests](sphere_of_cubes.md)

