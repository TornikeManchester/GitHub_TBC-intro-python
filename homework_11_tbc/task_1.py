def temperature(c, f):
    celsius = (f - 32) * 5/9
    fahrenheit = (c * 9/5) + 32

    print(f'Degrees of {f} fahrenheit would be {celsius} degrees of celsius')
    print(f'Degrees of {c} celsius would be {fahrenheit} degrees of fahrenheit')
