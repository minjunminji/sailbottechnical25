

def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    if angle >= 360 or angle < -360: # Normalize to [-360, 360)
        angle = angle % 360
    if angle >= 180: # Normalize to [-180, 180)
        angle -= 360
    if angle < -180: # Normalize to [-180, 180)
        angle += 360

    return angle


def normalize_360(angle):
    return angle % 360


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """

    # Normalize all angles to [0, 360)
    first_angle = normalize_360(first_angle) 
    middle_angle = normalize_360(middle_angle)
    second_angle = normalize_360(second_angle)

    if first_angle > second_angle: 
        if first_angle - second_angle > 180 and middle_angle > first_angle or middle_angle < second_angle:
            return True # Reflex case when first angle greater than second
        elif first_angle - second_angle <= 180 and middle_angle > second_angle and middle_angle < first_angle:
            return True # Non-reflex case when first angle greater than second
    if first_angle < second_angle:
        if second_angle - first_angle > 180 and middle_angle > second_angle or middle_angle < first_angle:
            return True # Reflex case when first angle less than second
        elif second_angle - first_angle <= 180 and middle_angle > first_angle and middle_angle < second_angle:
            return True # Non-reflex case when first angle less than second

    return False # Equal case and all other cases
