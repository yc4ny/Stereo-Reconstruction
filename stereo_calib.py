import numpy as np
import utils

def LinearTriangulation(K1,K2, C1, R1, C2, R2, x1, x2):

    I = np.identity(3)
    C1 = np.reshape(C1, (3, 1))
    C2 = np.reshape(C2, (3, 1))

    P1 = np.matmul(K1, np.column_stack((R1,C1)))
    P2 = np.matmul(K2, np.column_stack((R2,C2)))

    p1T = P1[0,:].reshape(1,4)
    p2T = P1[1,:].reshape(1,4)
    p3T = P1[2,:].reshape(1,4)

    p_dash_1T = P2[0,:].reshape(1,4)
    p_dash_2T = P2[1,:].reshape(1,4)
    p_dash_3T = P2[2,:].reshape(1,4)

    all_X = []
    for i in range(x1.shape[0]):
        if x1[i][0] == 0 or x2[i][0] == 0:
            all_X.append(([0,0,0,0]))
            continue 

        x = x1[i,0]
        y = x1[i,1]
        x_dash = x2[i,0]
        y_dash = x2[i,1]


        A = []
        A.append((y * p3T) -  p2T)
        A.append(p1T -  (x * p3T))
        A.append((y_dash * p_dash_3T) -  p_dash_2T)
        A.append(p_dash_1T -  (x_dash * p_dash_3T))

        A = np.array(A).reshape(4,4)

        _, _, vt = np.linalg.svd(A)
        v = vt.T
        x = v[:,-1]
        all_X.append(x)
    return np.array(all_X)

def Triangulation_nl(point3d, P1, P2, x1, x2):
    R1 = P1[:,:3]
    C1 = -R1.T @ P1[:,3]
    R2 = P2[:,:3]
    C2 = -R2.T @ P2[:,3]

    p1 = np.concatenate([C1, utils.Rotation2Quaternion(R1)])
    p2 = np.concatenate([C2, utils.Rotation2Quaternion(R2)])

    lamb = 0.1
    n_iter = 100
    X_new = point3d.copy()
    for i in range(0,point3d.shape[0]):
        pt = point3d[i,:]
        for j in range(n_iter):
            proj1 = R1 @ (pt - C1)
            proj1 = proj1[:2] / proj1[2]
            proj2 = R2 @ (pt - C2)
            proj2 = proj2[:2] / proj2[2]

            dfdX1 = ComputePointJacobian(pt, p1)
            dfdX2 = ComputePointJacobian(pt, p2)

            H1 = dfdX1.T @ dfdX1 + lamb * np.eye(3)
            H2 = dfdX2.T @ dfdX2 + lamb * np.eye(3)
            J1 = dfdX1.T @ (x1[i,:] - proj1)
            J2 = dfdX2.T @ (x2[i,:] - proj2)
            if np.linalg.det(H1) == 0 or np.linalg.det(H2) == 0:
                continue
            delta_pt = np.linalg.inv(H1) @ J1 + np.linalg.inv(H2) @ J2
            pt += delta_pt

        X_new[i,:] = pt
    return X_new

def ComputePointJacobian(X, p):
    R = utils.Quaternion2Rotation(p[3:])
    C = p[:3]
    x = R @ (X - C)

    u = x[0]
    v = x[1]
    w = x[2]
    du_dc = R[0, :]
    dv_dc = R[1, :]
    dw_dc = R[2, :]

    dfdX = np.stack([
        (w * du_dc - u * dw_dc) / (w**2),
        (w * dv_dc - v * dw_dc) / (w**2)
    ], axis=0)

    return dfdX

def reprojectionError(openpose, projectionMatrix, keypoint3d): 
    #Reprojection to original image space
    reproject = np.zeros((25,2))
    ones = np.ones((25,1))
    keypoint3d = np.column_stack((keypoint3d,ones))
    for i in range (0,25):  
        point2D = np.matmul(projectionMatrix ,keypoint3d[i])
        utils.homogeneous_2D(point2D)
        reproject[i][0] = point2D[0]
        reproject[i][1] = point2D[1]
        reproject[np.isnan(reproject)] = 0 
    
    #Calculating Reprojection error 
    sum_error = 0; 
    numPoints = 0;
    for i in range (0,25):
        if reproject[i][0]==0 or reproject[i][1]==0 or openpose[i][0] == 0 or openpose[i][1] ==0:
             continue 
        dist = np.linalg.norm(openpose[i]-reproject[i])
        sum_error = sum_error + dist 
        numPoints += 1 

    return sum_error/numPoints

def reprojectedPoints(projectionMatrix, keypoint3d): 
    reproject = np.zeros((25,2))
    ones = np.ones((25,1))
    keypoint3d = np.column_stack((keypoint3d,ones))
    for i in range (0,25):  
        if keypoint3d[i][0] == 0:
            continue
        point2D = np.matmul(projectionMatrix ,keypoint3d[i])
        utils.homogeneous_2D(point2D)
        reproject[i][0] = point2D[0]
        reproject[i][1] = point2D[1]
        reproject[np.isnan(reproject)] = 0 
    return reproject 
