a = float(input('Введите первую сторону треугольника: '))
b = float(input('Введите вторую сторону треугольника: '))
c = float(input('Введите третью сторону треугольника: '))

if a == b == c:
    print("Треугольник равносторонний")
elif a + b < c or b + c < a or a + c < b:
    print('Такого треугольника не может быть!')
elif a == b or b == c or a == c:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')


