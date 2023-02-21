# Big Bang script

* [Was the center of universe reached?](#Was-the-center-of-universe-reached?)
* [The quadratic decay discover](#The-quadratic-decay-discover)
* [The list of scripts in the folder](#The-list-of-scripts-in-the-folder)

Is a Big Bang an explosion which throws matter to all directions in different speeds? The scripts in the current folder is about it. Good enough as an scripting exercise to see working in the 3d space. We can do something like this and see the Big Bang? If so, them you can certify that the center of the universe can be located!

The following scripts are written in python designed to work with Blender.

## Was the center of universe reached?

Naively, after creating the script that throws objects in random direction with random speeds, I assumed that I could see an chaotic, but homogeneous matter (cubes) distribuition through the space. But this was not checked. Instead, there was noticed a concentration of matter in the more central area of explosion. The homogenity of matter is an important attribute from universe that was not reached. So there are two hypotheses: first, that the visible portion of the universe are so tiny in relation to all existing matter that some *geometry* in the galaxies was not able to be checked. Second (more reasonable): that things beign throwed to all directions in random speeds does not represents well the big bang explosion.

## The quadratic decay discover

## The list of scripts in the folder

Follows the scripts in the folder:

### `big_bang.py`

It can be copy and pasted in Blender script editor, and execute normally. This creates 1000 animated cubes, to random direction and random speed. In the style of a *big bang*. You can play with the variable `creation_amount` to alter the amount of cubes.

### `big_bang_and_save.py`

Designed to work in background. It import `big_bang.py` to create the cubes and its animation. Then saves in `created` folder. So you can latter open and check the final result. The file name will be like `bigbang-1676853419.806358.blend`. This numbers means the timestamp of when the file is created.

To use it:

1. Navigate to the current script folder.

2. Execute with the following command: `blender --background --python big_bang_and_save.py`. No that the Blender must be executable through command line, which is acquired when you put the Blender executable folder in the `PATH` environment variable.

### `join_files.py`

It joins files located in the `created` folder. To use it:

1. Navigate to the current script folder.

2. Execute the following command: `blender --python join_files.py`. As in the previous script, you must have Blender acessible through command line.
