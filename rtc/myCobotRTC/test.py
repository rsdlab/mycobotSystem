#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import math3d

# print(dir(math3d))
#vec = math3d.Vector()
#trans_matrix = [[1, 0, 0, 10], [0, 1, 0, 20], [0, 0, 1, 30]]
trans_matrix = [[math.cos(0.3), -math.sin(0.3), 0, 10],
                [math.sin(0.3), math.cos(0.3), 0, 20], [0, 0, 1, 30]]
trans = math3d.Transform(trans_matrix)


print(dir(trans))
print(trans.get_pos().x)
print(trans.get_pos().y)
print(trans.get_pos().z)
print(trans.get_matrix())
print(trans.get_array())
print(trans.get_orient())
print(trans.get_pose_vector())
