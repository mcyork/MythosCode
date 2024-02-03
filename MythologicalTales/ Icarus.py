def icarus_flight(max_height, sun_distance):
    """
    Simulates Icarus's flight towards the sun.
    Args:
    - max_height: The maximum safe height Icarus can fly without melting his wings.
    - sun_distance: The height at which Icarus reaches the sun.
    """
    current_height = 0
    wing_condition = "intact"
    
    while wing_condition == "intact":
        current_height += 1  # Icarus flies higher with each iteration
        print(f"Icarus is flying at {current_height} meters.")
        
        if current_height > max_height:
            wing_condition = "melting"
            print("Icarus has flown too close to the sun. His wings begin to melt.")
        
        if current_height == sun_distance:
            wing_condition = "melted"
            print("Icarus's wings have melted completely, and he begins to fall.")
            break
    
    if wing_condition == "melted":
        print("Icarus falls into the sea. Let his fate be a warning about the perils of hubris.")
    else:
        print("Icarus has safely returned to the ground, heeding his father's advice.")

icarus_flight(max_height=10, sun_distance=15)
