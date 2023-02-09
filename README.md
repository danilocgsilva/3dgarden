# 3dgarden

Several experiments applying programming to 3d space.

## Blender, I great tool to use

[Blender](https://www.blender.org/) is the first place where I will test the scripts and algorithms. So currently, all scripsts presented here will be runned in Blender. You can do it as well! Download Blender, go to the scripting tab (check tabs right at the right of main menus in Windows), open the script and execute with the *play* icon or with the `alt` + `p` shortcut.

## Where is the center of universe?

I am not confortable saying that everything is the center of the universe. I understand that, once everything comes from the same point, so everything can be considered the center of universe. The problem with that is that, if there were an expansion, so this expansion still have a center, a point in the space where..., bit hard to explain and define, but stuffs will be more clear after some 3d representation.

The first chalenge to deal is to randonly set a direction on the 3d space where objects will be pointed. Let's say, a vector. After the vector defined, so them we can define a speed.

The first idea is to use some sort of calculation involving trigonometry. One result is the `tri_party.py`. Fail to create the first objective, but did created an interesting effect. For this script, you can play with values from `ra1` and `ra2` (radius1 and radius2, representing angles in two axis). Also can play with the range parameter, but caution here! A much large number in range may freeze your Blender, with will took a long time to create such dense number of tiny cubes.

## The sphere of cubes

I know that a got the success for defining a random direction vector when objects plotted randomly forms a sort of sphere. This is what I got in the `randomsphere.py`. There you can check the range, where prints 500 tiny cubes forming a sphere. The deal here is all cubes have exact same distance from the center, so we can take all three axis values over the space and considers its as a 3d vector representation.

## Performance quirks (in Blender)

The `randomsphere.py` script also calculates the time took to generate all 500 cubes. It took very different times each iteration. The first time I run the script, it usually tooks around 2700 milliseconds. The second time, tooks around 9020. The third time, for exact same 500 cubes, tooks 17560. I can delete all cubes and run script again. Them, the time took is *reseted*, again taking around 2700 milliseconds. This strongly suggests that for each new cube creation, the performance is heavilly affected by the objects that already exists in the scene. SO here, i think that is a good place to Blender programmers works to gain some efficiency. For me makes not sense. But I also would like to know what happens behind the scenes to justify why the new object creation heavily is impacted by the objects that currently exists.

I also runned a test to create at once 1500 cubes. Then it tooks 33149 milliseconds! Cleared the scene, runned once more, takes 32935 milliseconds. It is little more than the sum of the time took for each 500 spehre generated at once! Quite strange! But also interesting to know what happens.

Another thing to note is that, althought in the time when the Blender are creating the spheres it is supposedly to do so in the fastest possible way. Why the processor may hold yourself from doing a task that is heavyweight? In fact, during the script execution, the Blender are completly freezed, showing that it is completly busy and nothing can be done further in current Blender. Also, the fan is throtled, and processor temperature is rised (just a little). Everything shows that some heavy work is beign performend by the processor. But during the script execution, I opened the Windows Task Manager to see the processor usage graphs. And it sticks with just 18%! So still there are other 82% of processor capacity idled. The theory is that this is due to the internal Blender algorithms be unable to use all processors cores at once. That are a big sort of operations that can use just a single core at once. This problem isn't new. The exact same situation existed when I used the 3ds max, more than 10 years ago. The only 3d operation that assuredly could use the processor at it's full power is the rendering, but rendering was not the only heavy weight operations that exists in 3d work. Since from the computers starts to ship with more than one single processing unit, more than 15 years ago, when the clock speed wasn't possible to be rised, softwares still remained working with just one core.

### The way of 10.000 cubes

All the tests untill now is beign done with a quite powerfull processor (to the time of this writting). I am using a computer shipped with an Intel i7 12700H. Also have a NVidia RTX 3060 laptop GPU for 3d handling.

In much older hardware (in 3ds max), few millons of polygons wasn't much thing to handle. I remember that subdividing s geometry to 2 millions polygons still could be handled fluidly. The things starts to be unconfortable with more than 5 millions of polygons (sorry, I do not remember what GPU was I was using in that time).

10.000 *stuffs* inside a modern computer like I am using seems not to be much thing. In fact, manipullating a scene with 10.000 tiny cubes have no quirks. Once the chanllenge was to handle tons of polygons at once in a scene. Now we have other issues.

For example, using the exact same script to generate spheres, to generate 10.000 cubes, it tooks 2273134 ms! Or, almost 38 minutes. But this

