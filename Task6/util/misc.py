class Misc:
    @staticmethod
    def clamp(what, fr, to):
        return max(fr, min(what, to))
