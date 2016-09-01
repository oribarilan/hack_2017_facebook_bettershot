from imagegrader import LandscapeGrader

test_exif = {"iso": 200,
        "f_stop": 30,
        "focal_length": 14,
        "shutter_speed": 10}

result = LandscapeGrader().grade(test_exif)
print(result)
