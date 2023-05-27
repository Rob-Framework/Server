from slam_handler.slam import process
from slam_handler.display import Display
from slam_handler.pointmap import PointMap

import open3d as o3d

pmap = PointMap()
display = Display()

pcd = None
visualizer = None

def init():
	global pcd, visualizer
	
	pcd = o3d.geometry.PointCloud()
	visualizer = o3d.visualization.Visualizer()
	visualizer.create_window(window_name="3D plot", width=960, height=540)

def loop(frame):
	img, tripoints, kpts, matches = process(frame)
	xyz = pmap.collect_points(tripoints)

	if kpts is not None or matches is not None:
		display.display_points2d(frame, kpts, matches)
	else:
		pass
	display.display_vid(frame)

	if xyz is not None:
		display.display_points3d(xyz, pcd, visualizer)
	else:
		pass