import module

f = module.print_water_state

module.FREEZING_POINT = 0
module.BOILING_POINT = 100

f(float(input()))