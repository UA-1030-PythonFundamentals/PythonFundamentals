#Calculate smth for sphere

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius=radius
        self.mass=mass
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round((4/3)*3.14159265359*(self.radius**3),5)
    def get_surface_area(self):
        return round(4*3.14159265359*(self.radius**2),5)
    def get_density(self):
        return round(self.mass/Sphere.get_volume(self),5)