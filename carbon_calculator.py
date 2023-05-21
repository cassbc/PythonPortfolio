import math

def tree_carbon():
    #Get input circumference of tree, measured at 1.3m height
    units = input('Enter units (cm or inches): ')

    circumference = input('Enter tree circumference: ')
    
    #Convert units to metric if not already

    if units == 'inches':
        circumference = float(circumference)
        circumference = circumference * 2.54
    elif units == 'cm':
        circumference = float(circumference)
        
    diameter = circumference / math.pi

    #Calculate the biomass of the tree, above and below ground
    above_ground_biomass = 0.0998 * (diameter**2.5445)

    #Calculate above and below ground biomass
    total_biomass = above_ground_biomass * 1.24

    #Calculate growth rate per annum
    growth_rate = 0.208 * (total_biomass**0.763)

    #Calculate carbon storage of tree
    carbon = total_biomass * 0.47

    #Calculate CO2
    co2 = carbon * 3.6663
    rounded_co2 = round(co2,2)
    
    print('Total CO2 in tree = {}'.format(rounded_co2) + 'kg')
