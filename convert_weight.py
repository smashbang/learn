# n
scale: str = input('Convert to kgs or lbs ? ')

weight_kgs: str = 'kgs'
weight_lbs: str = 'lbs'

if scale == weight_kgs:
    weight_kgs: str = input('What is your weight? in lbs ')
    weight_kgs: float = int(weight_kgs) * 0.4535924
elif scale == weight_lbs:
    weight_lbs: str = input('What is your weight? in kgs ')
    weight_lbs: float = int(weight_lbs) * 2.204623

kgs: str = 'kgs'
lbs: str = 'lbs'

if scale == kgs:
    print('Your weight is: ', round(weight_kgs), ' kgs')
elif scale == lbs:
    print('Your weight is: ', round(weight_lbs), ' lbs')
else:
    exit()
