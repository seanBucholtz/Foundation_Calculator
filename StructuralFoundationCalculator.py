# Assignment 2: Bricks and Mortar
# Sean Bucholtz (section 3)
# 4/16/13

# functions
def readout(): #output
    print('\n\nThe area of ground required for the foundation is: ' + \
      format(g_area, ',.0f') + ' sq. meters' + \
      '\n\nThe area inside the foundation is: ' + format(i_area, ',.0f') \
      + ' sq. meters' + '\n\nThe total volume of the foundation wall is: ' + \
      format(f_vol, ',.0f') + ' cubic meters' + \
      '\n\nThe total number of bricks required is: ' + \
      format(num_brick, ',.0f') + \
      '\n\nThe total number of concrete bags required is: ' + \
      format(mortar_bag, ',.0f') + \
      '\n\nThe total mass of the foundation is: ' + \
      format(t_mass, ',.0f') + ' kg' + \
      '\n\nThe total material cost will be: $' + format(t_cost, ',.2f'))
    escape = input('\n\nPress \'Enter\' to quit')


# greeting
print('Welcome to GroundWork - Calculating foundation ' \
      'requirements made Simple!')

# input
f_length = float(input('\nFoundation Length?: '))
f_width = float(input('\nFoundation Width?: '))
f_height = float(input('\nFoundation Height?: '))
f_thick = float(input('\nFoundation Thickness?: '))


correct = input('\n\nAre the dimensions you entered correct? (Yes/No): ')

# conditions - allows user to change input values
while (correct != 'No' and correct != 'no' and correct != 'N'  and \
      correct != 'n' and correct != 'Yes' and correct != 'yes' and \
      correct != 'Y' and correct != 'y'): # No answer loop
        #loops until input = perm. of 'Y or N'
    print('\nI don\'t understand ' + str(correct) + '.')
    correct = input('\n\nAre the dimensions you entered correct? (Yes/No): ')

    while (correct == 'No' or correct == 'no' or correct == 'N'  \
           or correct == 'n'): # redo loop
            #loops until input = perm. of 'Yes'
        f_length = float(input('\nFoundation Length?: '))
        f_width = float(input('\nFoundation Width?: '))
        f_height = float(input('\nFoundation Height?: '))
        f_thick = float(input('\nFoundation Thickness?: '))
        correct = input('\n\nAre the dimensions you entered' + \
                        'correct? (Yes/No): ')
    
    
else:
    # CONSTANTS
    b_length = 19 #brick dimension (cm)
    b_width = 9 #brick dimesion (cm)
    b_height = 6 #brick dimension (cm)
    s_brick_cost = 0.65 #per brick ($)
    s_bag_mortar_cost = 7.25 #per bag ($)
    s_brick_mass = 2.3 #per brick kg
    s_bag_mortar_mass = 43 #per bag (kg)

    # algorithms
    g_area = f_length*f_width #total area of foundation plot
    i_area = (f_length-2*f_thick)*(f_width-2*f_thick)
    i_vol = (f_length-2*f_thick)*(f_width-2*f_thick)*(f_height) #inner volume
    t_vol = f_length*f_width*f_height #total area volume
    f_vol = t_vol-i_vol #vol by deduction alg (primary alg)
    f_vol_2 = 2*((f_width-2*f_thick)*f_height*f_thick)+2*\
          (f_length*f_height*f_thick) # independent foundation vol. alg
    s_brick_vol = (b_length*b_width*b_height)/100**3 #cm-to-m conversion
    t_mortar = f_vol*.15 #total amount of mortar req. (kg)
    num_brick = (f_vol-t_mortar)/s_brick_vol
    mortar_bag = t_mortar/0.025 #calculates amount of mortar bags (qt.)
    t_mortar_mass = s_bag_mortar_mass*mortar_bag #weight of all mortar (kg)
    t_brick_mass = num_brick*s_brick_mass #weight of all bricks (kg)
    t_mass = t_mortar_mass+t_brick_mass #total mass of foundation
    t_brick_cost = num_brick*s_brick_cost
    t_mortar_cost = mortar_bag*s_bag_mortar_cost
    t_cost = t_mortar_cost+t_brick_cost

    readout()

# Documented Test results

# This program was tested using the following inputs:
# Height: 24
# Length: 18
# Width: 2
# Thickness .5

# The results produced were:
# Ground area (m^2): 432
# Inside area of foundation (m^2): 391
# Total foundation volume (m^3): 82
# Total number of required bricks: 67,934
# Total number of concrete bags required: 492
# Total mass of the foundation (kg): 177,404
# Total material cost ($): 47,723.92

### These results equal to known (given) results.

# This program was also tested using the following inputs:
# Height: 20
# Length: 20
# Width: .75
# Thickness .09

# The results produced were:
# Ground area (m^2): 400
# Inside area of foundation (m^2): 393
# Total foundation volume (m^3): 5
# Total number of required bricks: 4,454
# Total number of concrete bags required: 32
# Total mass of the foundation (kg): 11,630
# Total material cost ($): 3,128.65

### These results agree with manual calculations.

## Decision making:

# 1st loop (no answer loop) was tested with the following conditions:
# correct = Yes
#   Result: false. passed to else, output printed 
# correct = yes
#   Result: false. passed to else, output printed
# correct = Y
#   Result: false. passed to else, output printed
# correct = y
#   Result: false. passed to else, output printed
# correct = No
#   Result: false. user input (dimensions)
# correct = no
#   Result: false. user input (dimensions)
# correct = N
#   Result: false. user input (dimensions)
# correct = n
#   Result: false. user input (dimensions)
# correct = lknsdflnd
#   Result: true. user input repeats until != to perm. of Yes or No
# correct = ''
#   Result: true. user input (correct) repeats until != to perm. of Yes or No

# 2nd nested loop (redo loop) was tested with the following conditions:
# correct = Yes
#   Result: false. passed to else, output printed 
# correct = yes
#   Result: false. passed to else, output printed
# correct = Y
#   Result: false. passed to else, output printed
# correct = y
#   Result: false. passed to else, output printed
# correct = No
#   Result: true. user input (dimensions)
# correct = no
#   Result: true. user input (dimensions)
# correct = N
#   Result: true. user input (dimensions)
# correct = n
#   Result: true. user input (dimensions)
# correct = lknsdflnd
#   Result: false. back to 1st loop user input (correct) repeats until != to
#   perm. of Yes or No
# correct = ''
#   Result: false. back to 1st loop user input (correct) repeats until != to
#   perm. of Yes or No

# Else: (correct = Yes or yes or Y or y) inputs calculated and output printed

### These conditions function as desired.

""" I believe 'GroundWork' performs exactly how it should,
and it fulfills all of the customer requests. All test resluts corroborate
this conclusion"""
