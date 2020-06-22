# n
scale: str = input('What do you want to convert to kgs or lbs? ')

weight_kgs: str = 'kgs'
weight_lbs: str = 'lbs'

if scale == weight_kgs:
    weight_kgs: str = input('What is your weight? in lbs ')
    weight_kgs: float = int(weight_kgs) * 2.204623
elif scale == weight_lbs:
    weight_lbs: str = input('What is your weight? in kgs ')
    weight_lbs: float = int(weight_lbs) * 0.4535924

kgs: str = 'kgs'
lbs: str = 'lbs'

if scale == kgs:
    print('Your weight is: ', weight_kgs, ' kgs')
elif scale == lbs:
    print('Your weight is: ', weight_lbs, ' lbs')
else:
    exit()
