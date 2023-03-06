import bpy

curve_object = bpy.data.curves.new("CurveObject", type="CURVE")
curve_object.dimensions = "3D"

line_height = 1
points = []
for i in range(1,10,1):
    decay_power =  pow(i, 2)
    points.append(line_height / decay_power)

spline = curve_object.splines.new(type="POLY")
spline.points.add(len(points)-1)

for pointLoop in range(len(points)):
    spline.points[pointLoop].co = (0, pointLoop, points[pointLoop], 1)
    
curve_obj = bpy.data.objects.new("graph", curve_object)
bpy.context.scene.collection.objects.link(curve_obj)
