x = "\\\\"
print(len(x))

print(chr(ord('p') + 2 ))
print(float("1.3"))

class A:
	def a(self):
		print('a')

class B:
	def a(self):
		print('b')

class C(B,A):
	def c(self):
		self.a()

o = C()
o.c()

def I(n):
	s = '+'
	for i in range(n):
		s += s
		yield s

for x in I(2):
	print('entre')
	print(x, end='')

#stream = open("/Users/gmunoz/Documents/hola.txt", "rt", encoding = "utf-8") # se abre el archivo hola.txt en modo lectura, devolviéndolo como un objeto de archivo

for x in open("/Users/gmunoz/Documents/hola.txt", "rt"):
	print(x)


try:
	raise Exception(1,2,3)
except Exception as e:
	print(len(e.args))
except:
	print("c")


print("hola")