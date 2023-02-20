# Big Bang script

Follows the scripts in the folder:

## `big_bang.py`

It can be copy and pasted in Blender script editor, and execute normally. This creates 1000 animated cubes, to random direction and random speed. In the style of a *big bang*. You can play with the variable `creation_amount` to alter the amount of cubes.

## `big_bang_and_save.py`

Designed to work in background. It import `big_bang.py` to create the cubes and its animation. Then saves in `created` folder. So you can latter open and check the final result. The file name will be like `bigbang-1676853419.806358.blend`. This numbers means the timestamp of when the file is created.

To use it:

1. Navigate to the current script folder.

2. Execute with the following command: `blender --background --python big_bang_and_save.py`. No that the Blender must be executable through command line, which is acquired when you put the Blender executable folder in the `PATH` environment variable.

## `join_files.py`

It joins files located in the `created` folder. To use it:

1. Navigate to the current script folder.

2. Execute the following command: `blender --python join_files.py`. As in the previous script, you must have Blender acessible through command line.
