hotel_room_availability = {"101":False, "102":True}
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def add_rooms(hotel,room_number):
    if room_number not in hotel:
        hotel[room_number] = True
        print(f"Room {room_number} added.")
    else:
        print(f"Room {room_number} already exists")
        
def is_available(hotel,room_number):
    return hotel.get(room_number, False) #Indicate the room is not available

def book_room(hotel, room_number):
    if is_available(hotel, room_number):
        hotel[room_number] = False
        print(f"Room {room_number} booked for John Doe")
    else:
        print(f"Room {room_number} is not avalable or does not exist.")
        
def display_room(hotel):
    for room, available in hotel.items():
        status = "Available" if available else "Booked"
        print(f"Room {room}: {"Status"} {hotel_room_availability}")
        
while True:
    print("\n Hotel Management System")
    print("1.Add Room\n2: Book Room\n3: Check Room Availability\n4: Display Rooms\n5: Check Out")
    choice = input("Enter room number to add: ")
    
    if choice == "1":
        room = input("Enter room number to add:")
        add_rooms(hotel_rooms,room)
        
    elif choice == "2":
        room = input("Enter room number to book:")
        book_room(hotel_rooms,room)
        
    elif choice == "3":
        room = input("Enter room number to check availability:")
        available = is_available(hotel_rooms,room,hotel_room_availability)
        print(f"Room {room} is {'available' if available else 'not available'}")
    
    elif choice == "4":
        display_room(hotel_rooms)
        
    elif choice == "5":
        print("Checking out John Doe from 102")