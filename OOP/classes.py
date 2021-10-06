class Organs:
    def __init__(self, small_finger=None, ring_finger=None, middle_finger=None, index_finger=None, thumb=None,
                 little_toe=None, ring_toe=None, middle_toe=None, long_toe=None, big_toe=None,
                 left_ear=None, right_ear=None, left_eye=None, right_eye=None, mouth=None, nose=None, teeth=None):
        # Hand
        self.small_finger = small_finger
        self.ring_finger = ring_finger
        self.middle_finger_ = middle_finger
        self.index_finger = index_finger
        self.thumb = thumb
        # Foot
        self.little_toe = little_toe
        self.ring_toe = ring_toe
        self.middle_toe = middle_toe
        self.long_toe = long_toe
        self.big_toe = big_toe
        # Face
        self.left_ear = left_ear
        self.right_ear = right_ear
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.mouth = mouth
        self.nose = nose
        self.teeth = teeth

    def speak(self):
        print(f"this is {self.small_finger}")


# יד ימין
class Right_hand(Organs):
    def __init__(self, small_finger=None, ring_finger=None, middle_finger=None, index_finger=None, thumb=None):
        super().__init__(small_finger, ring_finger, middle_finger, index_finger, thumb)


# יד שמאל
class Left_hand(Organs):
    def __init__(self, small_finger=None, ring_finger=None, middle_finger=None, index_finger=None, thumb=None):
        super().__init__(small_finger, ring_finger, middle_finger, index_finger, thumb)


# רגל ימין
class Right_foot(Organs):
    def __init__(self, little_toe=None, ring_toe=None, middle_toe=None, long_toe=None, big_toe=None):
        super().__init__(little_toe, ring_toe, middle_toe, long_toe, big_toe)


# רגל שמאל
class Left_foot(Organs):
    def __init__(self, little_toe=None, ring_toe=None, middle_toe=None, long_toe=None, big_toe=None):
        super().__init__(little_toe, ring_toe, middle_toe, long_toe, big_toe)


# פנים
class Face(Organs):
    def __init__(self, left_ear=None, right_ear=None, left_eye=None, right_eye=None, mouth=None, nose=None, teeth=None):
        super().__init__(left_ear, right_ear, left_eye, right_eye, mouth, nose, teeth)


d1 = Face('sss')
d1.speak()
