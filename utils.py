import settings


class CalculatePercentage():
    def __init__(self):
        self.width = settings.WIDTH
        self.height = settings.HEIGHT
    
    def width_prct(self, percentage):
        return (self.width / 100) * percentage

    def height_prct(self, percentage):
        return (self.height / 100) * percentage


# calc_prct = CalculatePercentage()
# print(calc_prct.height_prct(25))  # output: 180
