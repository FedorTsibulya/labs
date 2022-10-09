class Shape():
    width = 0
    height = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    
    def set_widht(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
        
    
    
class Triangle(Shape):
    area = 0

    def get_area(self):
        return self.area
    
    def set_area(self):
        self.area = self.width * self.height * 0.5
    
    
    
class Rectangle(Shape):
    area = 0   
    
    def get_area(self):
        return self.area
    
    def set_area(self):
        self.area = self.width * self.height
        

if __name__ == "__main__":
    triangle = Triangle(14, 4)
    triangle.set_area()
    rectangle = Rectangle(16, 6)
    rectangle.set_area()
    print(triangle.get_area())
    print(rectangle.get_area())