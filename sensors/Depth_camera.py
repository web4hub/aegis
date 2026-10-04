import pyrealsense2 as rs
import numpy as np

class DepthCamera:
    def __init__(self):
        self.pipeline = rs.pipeline()
        cfg = rs.config()
        cfg.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        cfg.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
        self.pipeline.start(cfg)

    def get_frames(self):
        frames = self.pipeline.wait_for_frames()
        depth = np.asanyarray(frames.get_depth_frame().get_data())
        color = np.asanyarray(frames.get_color_frame().get_data())
