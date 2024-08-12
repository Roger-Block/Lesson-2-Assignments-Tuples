#================================================================
#================ Lesson 2: Assignments | Tuples ================
#================================================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1. Tuple Mastery in Python~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Objective:
    # The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

# Task 1: 
    # Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

            # "Itinerary 1: Alice - From New York to London"
            #  "Itinerary 2: Bob - From Tokyo to San Francisco"

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================

def format_flight_itineraries(itineraries):
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        print(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")


itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Steve", "Hong Kong", "Singapore"), ("Taylor", "Sacramento", "Burbank"), ("Felicity", "Fresno", "San Francisco")]
format_flight_itineraries(itineraries)
print("\n\n\n\n","="*80,"\n\n")

#================================================================================================


#~~~~~~~~~~~~~~ 2. Python Data Structure Challenges in Real-World Scenarios~~~~~~~~~~~~~~~~~~~~~~

# Objective: 
    # This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

# Task 1: 
    # Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: 
    # You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

        # library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

    # Add functionality to insert new books into library.
    # Ensure that adding a duplicate book is handled appropriately (hint: do a membership check to see if the new book is already in the library).

#================================================================================================
#=====================================Begin Code=================================================
#================================================================================================

def add_book(library, book):
    if book not in library:
        library.append(book)
        print("Book added successfully!")
    else:
        print("This book already exists in the library.")


# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add new books to the library
add_book(library, ("To Kill a Mockingbird", "Harper Lee"))
add_book(library, ("1984", "George Orwell"))  # Trying to add a duplicate book

# Print the updated library in markdown format
print("Library Data:")
for i, book in enumerate(library, start=1):
    title, author = book
    print(f"{i}. {title} by {author}")


                                    #======= END OF CODE =========


# Author: Roger Block