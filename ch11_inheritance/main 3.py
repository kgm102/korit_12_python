## 1. 슈퍼 클래스 Shape 정의
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        # call1() 유형: 매개변수 없고 리턴값 없이 출력만 수행
        print(self.name)



## 2. 서브 클래스 Circle 정의
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        # 생성 시 문구 출력
        print(f'반지름이 {self.radius}인 {self.name}이 생성되었습니다.')

    def area(self):
        # call3() 유형: 매개변수 없고 리턴값 있음
        return 3.14 * self.radius * self.radius

    def draw(self):
        # 오버라이딩: 넓이 출력
        print(f'이름이 {self.name}인 원의 넓이는 {self.area()} 입니다.')



## 3. 서브 클래스 Rectangle 정의
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        # 생성 시 문구 출력
        print(f'너비가 {self.width}, 높이가 {self.height}인 {self.name}이 생성되었습니다.')

    def area(self):
        # call3() 유형
        return self.width * self.height

    def draw(self):
        # 오버라이딩: 넓이 출력
        print(f'이름이 {self.name}인 직사각형의 넓이는 {self.area()} 입니다.')



## 4. 실행부
circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

print() # 줄바꿈용

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')