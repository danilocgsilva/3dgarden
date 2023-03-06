import bpy

print_decay = True
curve_object = bpy.data.curves.new("CurveObject", type="CURVE")
curve_object.dimensions = "3D"

line_height = 1
points = []
for i in range(2,20,1):
    distance = i / 2
    decay_power =  pow(distance, 2)
    points.append(line_height / decay_power)
    if print_decay:
        print('Decay power: ' + str(decay_power) + ', distance: ' + str(distance))

spline = curve_object.splines.new(type="POLY")
spline.points.add(len(points)-1)

for pointLoop in range(len(points)):
    spline.points[pointLoop].co = (0, pointLoop / 2, points[pointLoop], 1)
    
curve_obj = bpy.data.objects.new("graph", curve_object)
bpy.context.scene.collection.objects.link(curve_obj)
