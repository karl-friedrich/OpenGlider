from openglider.Vector import rotation_3d
import math
###########entweder klasse oder funktion die funktion erzeugt


def rotation(aoa, arc, zrot):
    """Rotation Matrix for Ribs, aoa, arcwide-angle and glidewise angle in radians"""

    rot=rotation_3d(arc+math.pi/2,[-1,0,0])
    axis=rot.dot([0,0,1])
    rot=rotation_3d(aoa,axis).dot(rot)
    axis=rot.dot([0,1,0])
    rot=rotation_3d(zrot,axis).dot(rot)
    rot=rotation_3d(-math.pi/2,[0,0,1]).dot(rot)
    
    return rot