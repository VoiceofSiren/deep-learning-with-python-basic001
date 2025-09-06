class Animal:
    def speak(self):
        print("소리를 냅니다.")
    def run(self):
        print("뛰어갑니다.")

class Cat(Animal):
    def speak(self):
        print("야옹!")

cat = Cat()
cat.speak()
cat.run()