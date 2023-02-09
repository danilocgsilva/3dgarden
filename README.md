# 3dgarden

Several experiments applying programming to 3d space.

## Where is the center of universe?

I am not confortable saying that everything is the center of the universe. I understand that, once everything comes from the same point, so everything can be considered the center of universe. The problem with that is that, if there were an expansion, so this expansion still have a center, a point in the space where..., bit hard to explain and define, but stuffs will be more clear after some 3d representation.

The first chalenge to deal is to randonly set a direction on the 3d space where objects will be pointed. Let's say, a vector. After the vector defined, so them we can define a speed.

The first idea is to use some sort of calculation involving trigonometry. One result is the `tri_party.py`. Fail to create the first objective, but did created an interesting effect. For this script, you can play with values from `ra1` and `ra2` (radius1 and radius2, representing angles in two axis). Also can play with the range parameter, but caution here! A much large number in range may freeze your Blender, with will took a long time to create such dense number of tiny cubes.
