def journey_of_the_ring(path, fellowship, ring_bearer, destination='Mount Doom'):
    if path[-1] == destination:
        print(f"The Ring has been destroyed by {ring_bearer}! Middle-earth is saved!")
        return True
    elif ring_bearer not in fellowship:
        print(f"{ring_bearer} has been corrupted by the Ring's power.")
        return False
    else:
        next_step = path.pop(0)  # Move to the next location on the path
        print(f"The Fellowship travels to {next_step}.")
        
        # Simulating challenges and events
        if next_step == 'Moria':
            print("They've lost Gandalf!")
            fellowship.remove('Gandalf')
        elif next_step == 'Lothlorien':
            print("The Fellowship is strengthened by the Elves.")
        elif next_step == 'Amon Hen':
            print("The Fellowship is scattered.")
            fellowship = [ring_bearer]  # Simplification for the example
            
        return journey_of_the_ring(path, fellowship, ring_bearer)

# Initial setup
path_to_mordor = ['The Shire', 'Rivendell', 'Moria', 'Lothlorien', 'Amon Hen', 'Mount Doom']
fellowship = ['Frodo', 'Sam', 'Merry', 'Pippin', 'Gandalf', 'Legolas', 'Gimli', 'Aragorn', 'Boromir']
ring_bearer = 'Frodo'

# Start the journey
journey_of_the_ring(path_to_mordor, fellowship, ring_bearer)
