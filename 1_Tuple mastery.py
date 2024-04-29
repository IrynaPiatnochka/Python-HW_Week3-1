# flight itinerary: (traveler_name, origin, destination)

flight_itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def flight_itin(list):
    for index, itinerary in enumerate(flight_itinerary):
        count = index +1
        print(f"Itinerary {count}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}")

flight_itin(flight_itinerary)
                 


              