import math

def tree_carbon():
    #Get input circumference of tree, measured at 1.3m height
    units = input('Enter units (cm or inches): ')

    circumference = input('Enter tree circumference: ')
    
    #Convert units to metric if not already

    if units == 'inches':
        circumference = float(circumference)
        circumference = circumference * 2.54
    else units == 'cm':
        circumference = float(circumference)
        
    diameter = circumference / math.pi

    #Calculate the biomass of the tree, above and below ground
    above_ground_biomass = 0.0998 * (diameter**2.5445)

    #Calculate above and below ground (roots) biomass
    #To keep things generalised, we're using the IPCC recommendation that below-ground biomass account for an additional
    #average of 26% of the above-ground biomass 
    #Source: IPCC Good Practice Guidance for Land Use, Land-Use Change and Forestry, pg. 4.103, link: https://www.ipcc-nggip.iges.or.jp/public/gpglulucf/gpglulucf_files/GPG_LULUCF_FULL.pdf
    total_biomass = above_ground_biomass * 1.26

    #Calculate growth rate per annum
    growth_rate = 0.208 * (total_biomass**0.763)

    #Calculate carbon storage of tree
    carbon = total_biomass * 0.47

    #Calculate CO2
    co2 = carbon * 3.6663
    rounded_co2 = round(co2,2)
    
    print('Total CO2 in tree = {}'.format(rounded_co2) + 'kg')
