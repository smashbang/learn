# n
scale: str = input('What do you want to convert to kgs or lbs? ')

kgs: str = 'kgs'
lbs: str = 'lbs'

# i
weight = input('What is your weight?  ')
weight_kgs: float = int(weight) * 2.204623
weight_lbs: float = int(weight) * 0.4535924



if scale == kgs:
    print('Your weight is: ', weight_kgs, ' kgs')
elif scale == lbs:
    print('Your weight is: ', weight_lbs, ' lbs')
else:
    exit()
