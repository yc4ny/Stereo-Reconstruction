import open3d as o3d 
import numpy as np 

dlt_keypoint = np.load("keypoints_3d/nl.npy")

lines = [[0, 15], [0, 16], [15, 17], [16, 18], [0, 1], [1, 2], [2, 3], [3, 4],
        [1, 5], [5, 6], [6, 7], [1, 8], [8,9], [8,12], [9,10], [10,11], [11,24], [11,22], [22,23], [12,13]
        , [13,14], [14,21], [14,19], [19,20]]
colors = [[1, 0, 0] for i in range(len(lines))]
# line_set = o3d.geometry.LineSet()
# line_set.points = o3d.utility.Vector3dVector(dlt_keypoint[0])
# line_set.lines = o3d.utility.Vector2iVector(lines)
# line_set.colors = o3d.utility.Vector3dVector(colors)
# o3d.visualization.draw_geometries([line_set])
vis = o3d.visualization.Visualizer()
vis.create_window()
for j in range (0,851):
    line_set = o3d.geometry.LineSet()
    line_set.points = o3d.utility.Vector3dVector(dlt_keypoint[j])
    line_set.lines = o3d.utility.Vector2iVector(lines)
    line_set.colors = o3d.utility.Vector3dVector(colors)
    vis.add_geometry(line_set)
    ctr = vis.get_view_control()
    ctr.change_field_of_view(60.0)
    ctr.set_front([ -0.33772111998121612, 0.27792873082682185, -0.89927752429359942 ])
    ctr.set_up([ 0.17798370125143831, -0.91931835007481233, -0.35096377776711307 ])
    ctr.set_zoom(1.2200000000000004)
    vis.update_geometry(line_set)
    vis.poll_events()
    vis.update_renderer()
    vis.capture_screen_image("3d_keypoint_img/" + str(j) + "_output.jpg")
    vis.remove_geometry(line_set)


vis.destroy_window()


# {
# 	"class_name" : "ViewTrajectory",
# 	"interval" : 29,
# 	"is_loop" : false,
# 	"trajectory" : 
# 	[
# 		{
# 			"boundingbox_max" : [ 611.13276844923064, 388.49271414428762, 3193.9718037482467 ],
# 			"boundingbox_min" : [ 32.803214651651871, -1217.1075027675793, 2218.3312428740846 ],
# 			"field_of_view" : 60.0,
# 			"front" : [ -0.33772111998121612, 0.27792873082682185, -0.89927752429359942 ],
# 			"lookat" : [ -123.92969744327998, -178.48855899714425, 2150.6651797712061 ],
# 			"up" : [ 0.17798370125143831, -0.91931835007481233, -0.35096377776711307 ],
# 			"zoom" : 1.2200000000000004
# 		}
# 	],
# 	"version_major" : 1,
# 	"version_minor" : 0
# }