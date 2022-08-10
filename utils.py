import numpy as np 

def Quaternion2Rotation(q):
    """
    Convert a quaternion to rotation matrix
    Parameters
    ----------
    q : ndarray of shape (4,)
        Unit quaternion (w, x, y, z)
    Returns
    -------
    R : ndarray of shape (3, 3)
        The rotation matrix
    """
    w = q[0]
    x = q[1]
    y = q[2]
    z = q[3]

    R = np.empty([3, 3])
    R[0, 0] = 1 - 2 * y**2 - 2 * z**2
    R[0, 1] = 2 * (x*y - z*w)
    R[0, 2] = 2 * (x*z + y*w)

    R[1, 0] = 2 * (x*y + z*w)
    R[1, 1] = 1 - 2 * x**2 - 2 * z**2
    R[1, 2] = 2 * (y*z - x*w)

    R[2, 0] = 2 * (x*z - y*w)
    R[2, 1] = 2 * (y*z + x*w)
    R[2, 2] = 1 - 2 * x**2 - 2 * y**2

    return R

def Rotation2Quaternion(R):
    """
    Convert a rotation matrix to quaternion
    Parameters
    ----------
    R : ndarray of shape (3, 3)
        Rotation matrix
    Returns
    -------
    q : ndarray of shape (4,)
        The unit quaternion (w, x, y, z)
    """
    q = np.empty([4,])

    tr = np.trace(R)
    if tr < 0:
        i = R.diagonal().argmax()
        j = (i + 1) % 3
        k = (j + 1) % 3

        q[i] = np.sqrt(1 - tr + 2 * R[i, i]) / 2
        q[j] = (R[j, i] + R[i, j]) / (4 * q[i])
        q[k] = (R[k, i] + R[i, k]) / (4 * q[i])
        q[3] = (R[k, j] - R[j, k]) / (4 * q[i])
    else:
        q[3] = np.sqrt(1 + tr) / 2
        q[0] = (R[2, 1] - R[1, 2]) / (4 * q[3])
        q[1] = (R[0, 2] - R[2, 0]) / (4 * q[3])
        q[2] = (R[1, 0] - R[0, 1]) / (4 * q[3])

    q /= np.linalg.norm(q)
    # Rearrange (x, y, z, w) to (w, x, y, z)
    q = q[[3, 0, 1, 2]]

    return q

def homogeneous_2D(point2D): 
    point2D[0] = point2D[0]/point2D[2]
    point2D[1] = point2D[1]/point2D[2]
    point2D[2] = point2D[2]/point2D[2]
    return point2D

def homogeneous_cartesian(homo): 
    for j in range (0,25): 
        homo[j][0] = homo[j][0] / homo[j][3]
        homo[j][1] = homo[j][1] / homo[j][3]
        homo[j][2] = homo[j][2] / homo[j][3]
        homo[j][3] = homo[j][3] / homo[j][3]   
    
    return homo