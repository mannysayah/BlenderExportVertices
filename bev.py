# written by: Manny Sayah 2019
# dataismore.com
# enjoy!
import bpy

outputFile = '{where you want to save it}/mesh.csv'

verts = [ bpy.context.object.matrix_world @ v.co for v in bpy.context.object.data.vertices ]

rows = [ ";".join([ str(v) for v in co ]) + "\n" for co in verts ]

f = open( outputFile, 'w' )
f.writelines( rows )
f.close()
