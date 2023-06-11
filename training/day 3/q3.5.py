values = [
    100,
    105.5,
    192.56j,
    10+6j,
    '10',
    'Hello world'5,
    [10, 20, 50, 100],
    {'name': 'sachin', 'age': 24, 'language': 'python'}
]

for value in values:
    print(f'The type of {value} is {type(value).__name__}')
