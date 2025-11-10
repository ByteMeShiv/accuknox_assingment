class Rectangle:
    def __init__(self,length,width) -> None:
        self.length = length
        self.width = width
    def __iter__(self):
        for key,value in self.__dict__.items():
            yield {key,value}


shape = Rectangle(10,15)
print("Creating a Rectangle(10, 5)")

print("Iterating over the rectangle:")
for i in shape:
    print(i)