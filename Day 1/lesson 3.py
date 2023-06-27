
a = 20
b = 37

print(a + b) #მიმატება

print(b - a) #გამოკლება

print(a * b) #გამრავლება

print(b / a) #გაყოფა

print(a ** b) #ხარისხში აყვანა 

print(b // a) #გაყოფის დროს მხოლოდ მთელ რიცხვს გვიჩვენებს, ანუ რამდენჯერ ჯდება ერთი რიცხვი მეორეში

print(b % a) #გაყოფის შემდეგ ნაშთი

print(a > b) #False
print(a < b) #True
print(a == b) #False
print(a >= b) #False
print(a <= b) #True
print(1 > 1) #False
print(1 < 1) #False
print(1 >= 1) #True
print(1 <= 1) #True

# or = რომელიმე მათგანიც, რომ ჭეშმარიტი აღმოჩნდეს დაწერს True-ს
# and = ყველა მათგანი უნდა იყოს ჭეშმარიტი თუ გვინდა, რომ True შედეგი მივიღოთ, ერთი რომც იყოს ჭეშმარიტი და მეორე არა, მაინც False შედეგს მივიღებთ

print(a > b or a < b) #True
print(a > b and a < b) #False

n = 25

print(a < n and b > n) #True
print(a > n and b < n) #False
print(a <= n and b >= n) #True
print(a >= n and b <= n) #False

print( 1 < 0 or 20 == 4 or a > b or n < b or True == 1) #True
print( 1 < 0 and 20 == 4 and a > b and n < b and False == 1) #False
