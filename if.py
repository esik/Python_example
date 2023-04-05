# BMW
cars = ['lada', 'suzuki', 'bmw', 'volvo']
for car  in cars:
    if car == 'bmw':
        print('This is',car.upper())
    else:
        print(car)

# alien_color
alien_color = input('please input collor green|yellow|red ')
if alien_color == 'green':
    print('player get 5 coin')
elif alien_color == 'yellow':
    print('player get 10 coin')
elif alien_color == 'red':
    print('player get 15 coin')
else :
    print('You lose')