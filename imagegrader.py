import json

class ImageGrader(object):
    class exifAttribute(object):
        def __init__(self, name, label, matcher, insights):
            self.name = name 
            self.label = label
            self.matcher = matcher
            self.insights = insights
            #self.grade = None

        #def set_matcher(self, matcher):
        #    self.matcher = matcher

        #def set_insights(self, insights):
            #self.insights = {"low": insights[0], "ok": insights[1], "high": insights[2]}

        #def set_grade(self, grade):
        #    self.grade = grade

    HIGH = 2
    OK = 1
    LOW = 0
    INF = float("inf")
    NEG_INF = -INF
    attributes = {"iso": None,
                "f_stop": None,
                "focal_length": None,
                "shutter_speed": None
                }

    def __init__(self):
        pass

    def grade(self, exif_data):
        results = {}
        #print(self.attributes)
        for attribute in exif_data:
            #print(attribute)
            value = exif_data[attribute]
            grade = self.attributes[attribute].matcher(value)
            #self.attributes[attribute].set_grade(grade)
            insight = self.attributes[attribute].insights[grade]
            label = self.attributes[attribute].label
            results[attribute] = {"label": label, "value": exif_data[attribute] ,"grade": grade, "insight": insight}
        return results

    def range_matcher(self, min_val, max_val):
        def matcher(data):
            if data < min_val:
                return self.LOW
            elif data > max_val:
                return self.HIGH
            return self.OK
        return matcher

    def threshold_matcher(self, threshold):
        def matcher(data):
            if data > threshold:
                return self.HIGH
            return self.OK
        return matcher

    def add_attribute(self, exif_attr):
        self.attributes[exif_attr.name] = exif_attr

    def add_iso_attr(self, insights, threshold):
        exif_attr = self.exifAttribute("iso", "ISO", self.threshold_matcher(threshold), insights)
        self.add_attribute(exif_attr)

    def add_fstop_attr(self, insights, min_fstop, max_fstop):
        exif_attr = self.exifAttribute("f_stop", "Aperture Size", self.range_matcher(min_fstop, max_fstop), insights)
        self.add_attribute(exif_attr)

    def add_focal_length_attr(self, insights, min_focal, max_focal):
        exif_attr = self.exifAttribute("focal_length", "Focal Length", self.range_matcher(min_focal, max_focal), insights)
        self.add_attribute(exif_attr)

    def add_shutter_speed_attr(self, insights, min_speed, max_speed):
        exif_attr = self.exifAttribute("shutter_speed", "Exposure Time", self.range_matcher(min_speed, max_speed), insights)
        self.add_attribute(exif_attr)

    #def add_matcher(attribute, matcher):
    #    matchers[attribute] = matcher


class LandscapeGrader(ImageGrader):
    def __init__(self):
        iso_insights = ["Low ISO is good!",
                "Great!",
                "Try to keep your ISO lower to get rid of nasty graining."]
        f_stop_insights = [
                "Stepping down your aperture will provide you with a wider depth of field." + \
                "This will make a greater part of the scenery appear in focus.",
                "Great!",
                "While shooting landscapes small aperture is mostly the way to go. \n" + \
                "But going too far might lose you some of that sweet sharpness."]
        focal_length_insights = ["Wide is good!",
                "Great!",
                "Using a wider focal length will give your photo a more dramatic look and will capture more of the scenery."]
        shutter_speed_insights = ["Low!",
                "Great!",
                "As long as you used a tripod you are golden. \n" + \
                "For hand-holding you should consider using faster shutter speeds."
                ]

        self.add_iso_attr(iso_insights, 1600)
        self.add_fstop_attr(f_stop_insights, 5.6, self.INF)
        self.add_focal_length_attr(focal_length_insights, self.NEG_INF, 20)
        self.add_shutter_speed_attr(shutter_speed_insights, 1/4000, 30)

class GraderFactory(object):
    def __init__(self):
        pass

    def create_factory(self, classification):
        if classification.lower() == 'nature landscape':
            return LandscapeGrader()
        #elif classification.lower() == "people portraits":
        #    return PortraitGrader()
