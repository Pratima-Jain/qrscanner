import random

subject = ["Shahrukh Khan", "Amitabh Bachchan", "Salman Khan", "A Blue Cat", "A group of Monkeys "]

action = ["launches", "dances with a parrot", "eats", "declares war "]

place = ["at red fort", "in mumbai local train", "a plate of samosas", "inside parliament", "at ganga ghat" ]

while True:
    subjects = random.choice(subject)
    actions = random.choice(action)        
    places = random.choice(place)
    
    headline = f"BREAKING NEWS: {subjects} {actions} {places}"
    print("\n" + headline)

    user_input = input("\nwould you like to generate another headline? (yes/no): ").strip().lower() 
    if user_input == 'no':
        break

print("\nThank you for using the Random Facts Generator! Have a fun day! ")



