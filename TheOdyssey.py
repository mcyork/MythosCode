import asyncio

async def journey_to_ithaca():
    adventures = ["Cyclops", "Lotus Eaters", "Sirens", "Scylla and Charybdis", "Calypso"]
    for adventure in adventures:
        await asyncio.sleep(1)  # Simulate the time taken for each adventure
        print(f"Odysseus encounters {adventure}.")

asyncio.run(journey_to_ithaca())
