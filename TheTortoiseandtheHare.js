def race(path_length):
    tortoise_speed = 1
    hare_speed = 5
    hare_sleep_threshold = path_length // 2
    hare_position = 0
    tortoise_position = 0

    while tortoise_position < path_length and hare_position < path_length:
        tortoise_position += tortoise_speed
        if hare_position < hare_sleep_threshold:
            hare_position += hare_speed
        else:
            print("Hare is sleeping...")
        
        if tortoise_position > hare_position and hare_position >= hare_sleep_threshold:
            print("Tortoise takes the lead! Slow and steady wins the race.")

    if tortoise_position >= path_length:
        winner = "Tortoise"
    else:
        winner = "Hare"

    return f"The winner is the {winner}!"

# Start the race
print(race(10))
