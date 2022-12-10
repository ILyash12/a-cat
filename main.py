 class Cat:
	def all(self, name):
		self.name = name
		self.satiety = 10
		self.sleepy = 10
        self.gladness = 15
	def live(self):
		print(self.name, 'is alive')
	def eat(self):
		print('Eating time')
        self.satiety += 10
        self.sleepy += 5
        self.gladness += 10
    def sleep|(self):
        print('Sleeping time')
        self.satiety -= 10
        self.sleepy -= 10
        self.gladness += 5

cat = Cat('Tihon')
cat.live()
c1 = Cat('Tihon')
c1.live()
c1.eat()
c1.sleep()