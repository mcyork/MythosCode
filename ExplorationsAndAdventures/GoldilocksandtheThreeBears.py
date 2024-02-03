def taste_porridge(porridge_temperatures):
    for index, temperature in enumerate(porridge_temperatures):
        if temperature == "just right":
            print(f"Goldilocks finds the porridge of bear {index + 1} just right.")
            break

def test_chair(chair_sizes):
    for index, size in enumerate(chair_sizes):
        if size == "just right":
            print(f"Goldilocks finds the chair of bear {index + 1} just right.")
            break

def test_bed(bed_softness):
    for index, softness in enumerate(bed_softness):
        if softness == "just right":
            print(f"Goldilocks finds the bed of bear {index + 1} just right and falls asleep.")
            break

def goldilocks_adventure():
    porridge_temperatures = ["too hot", "too cold", "just right"]
    chair_sizes = ["too big", "too small", "just right"]
    bed_softness = ["too hard", "too soft", "just right"]
    
    taste_porridge(porridge_temperatures)
    test_chair(chair_sizes)
    test_bed(bed_softness)

goldilocks_adventure()
