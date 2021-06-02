def distance(bbox_left_upper_x, bbox_left_upper_y, bbox_right_lower_x, bbox_right_lower_y):

    # x,y values are between 0 and 1
    # x: (x value of pixel / width), y: (y value of pixel / height)
    from scipy.spatial import distance
    
    # center x,y location values of bbox
    cntr_x = float((bbox_left_upper_x + bbox_right_lower_x)/2)
    cntr_y = float((bbox_left_upper_y + bbox_right_lower_y)/2)
    
    # Coordinate Transformation
    px = round(cntr_x - 0.5, 5)
    py = round(1 - cntr_y, 5)
    
    # sy (scale factor of y) with its coefficient values, and other constant values
    ay, by = 86.29433, -6.45561
    height_camera, dst_road = 24.749, 16.579
    br, bl = 0.0, 0.0 
    sy = ay*py + by
    
    # Transform pixel values to actual distance values (meter)
    y = sy*py + br
    x = sy*px + bl
    result = round(distance.euclidean([x,y,0], [0, -dst_road, height_camera]), 1)
    return result