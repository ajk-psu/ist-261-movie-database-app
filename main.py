"""
Program executes here.
"""

import user_interface
import movies

# Variable and Class Definitions
console_interface = user_interface.ConsoleUI('Title', 'Body')
"""ConsoleUI: Main instance of ConsoleUI object to control the user interface with."""

MOVIE_ATTRIBUTES = ['Title', 'Genre', 'Age Rating', 'Release Year', 'Director', 'Writer', 'Starring Actor', 'Country of Origin', 'Publishing Company', 'Run Time (in minutes)', 'IMDb Score', 'Amount of User Votes']
"""list: List used to contain the Movie class attributes for reference elsewhere (such as printing the header row in a table)."""

movie_list = []
"""list: List used to contain Movie objects."""

new_movie_entry = []
"""list: List used to hold attributes that will be used to construct a new Movie object."""

search_results = []
"""list: List to be used when searching movie_list. Results of movie_list searches should be stored in this list. Make sure to clear before starting a new search to avoid messing up results"""

close_program = False
"""bool: Boolean used to determine when the program should be closed. When False, the program continues to run. When True, program closes."""

menu_done = False
"""bool: Boolean used to determine if the current menu loop the program is running has finished."""

task_done = False
"""bool: Boolean used to determine if the current task loop the program is running has finished."""
    
user_selection = -1
"""int: Integer used to store the user's selected option."""


# Main program loop starts here.
if __name__ == '__main__':
    
    while close_program is False:
        
        menu_done = False
        console_interface.update_screen('Main Menu', 'Welcome to the Python Movie Database Manager! Please select an option below.')
        user_selection = console_interface.prompt_options_menu('Add or Remove a Movie', 'Update a Movie', 'Search for Movies', 'Import Data from CSV', 'Export Data to CSV', 'Exit Application', 'DEV: DEBUGGING')
        
        
        # TODO: Finish each branch
        # Add or Remove Movie Branch
        if user_selection == 1:
            
            while menu_done is False:
                
                console_interface.update_screen('Add or Remove a Movie', 'From this menu, you can add a new movie to the database or remove one. Please select an option to continue.')
                user_selection = console_interface.prompt_options_menu('Add a New Movie', 'Remove an Existing Movie', 'Return to Main Menu')
                
                # Add a Movie Branch
                if user_selection == 1:
                    title_string = ''
                    task_done = False
                    
                    console_interface.update_screen('Add a New Movie', 'To add a new movie to the database, please first enter the title of the movie you wish to add.')
                    
                    # Get Title attribute
                    title_string = console_interface.prompt_ask_for_string('Enter the title of the movie', replace_blank=False)
                    while len(title_string) == 0:   
                        title_string = console_interface.prompt_ask_for_string('You must enter a title for the movie. Please enter a title', replace_blank=False)
                    
                    #Get rest of movie attributes
                    while task_done is False:
                        console_interface.update_screen(f'Adding {title_string} to the Database', f'Please fill out the following details about {title_string}. If you are unsure of a detail, you may leave that field blank.')

                        new_movie_entry.clear()
                        new_movie_entry.append(title_string)
                        new_movie_entry.append(console_interface.prompt_ask_for_string('Please enter the genre of this movie'))
                        new_movie_entry.append(console_interface.prompt_ask_for_string('Please enter the MPAA age rating of this movie'))
                        new_movie_entry.append(console_interface.prompt_ask_for_number('Please enter the year this movie released in'))
                        new_movie_entry.append(console_interface.prompt_ask_for_string('Please enter the director of this movie'))
                        new_movie_entry.append(console_interface.prompt_ask_for_string('Please enter the head writer of this movie'))
                        new_movie_entry.append(console_interface.prompt_ask_for_string('Please enter the starring actor of this movie'))
                        new_movie_entry.append(console_interface.prompt_ask_for_string('Please enter the country this movie orignated from'))
                        new_movie_entry.append(console_interface.prompt_ask_for_string('Please enter the company that published this movie'))
                        new_movie_entry.append(console_interface.prompt_ask_for_number('Please enter the run time of this movie (in minutes)'))
                        new_movie_entry.append(console_interface.prompt_ask_for_number('Please enter the IMDb score of this movie', get_float=True))
                        new_movie_entry.append(console_interface.prompt_ask_for_number('Please enter how many users voted on this movie on IMDb'))
                    
                        console_interface.update_screen(f'Confirm Details for {title_string}', f'You are about to add {title_string} to the database. Please confirm the deatils you entered are correct.')
                        for (attribute, item) in zip(MOVIE_ATTRIBUTES, new_movie_entry):
                            print(f'{attribute}: {item}')
                    
                        task_done = console_interface.prompt_yes_or_no(f'\nAre these details correct and do you want to add {title_string} to the database? If you need to change a detail, answer \'No\' to go back')
                    
                    movie_list.append(movies.Movie(*new_movie_entry))
                    console_interface.update_screen(f'{title_string} Added!', 'The movie has been successfully added to the database!')
                    console_interface.prompt_enter_to_continue()
                
                # Remove a Movie Branch
                # TODO: FINISH THIS!
                elif user_selection == 2:
                    title_string = ''
                    task_done = False
                    confirm_remove = False
                    search_results.clear()
                    
                    console_interface.update_screen('Remove an Existing Movie', 'To remove a movie, please enter the title of the movie you woud like to remove. Please note that removing a movie cannot be undone!')
                    
                    # Get Title attribute
                    title_string = console_interface.prompt_ask_for_string('Enter the title of the movie', replace_blank=False)
                    while len(title_string) == 0:   
                        title_string = console_interface.prompt_ask_for_string('You must enter a title for the movie. Please enter a title', replace_blank=False)
                    
                    # Search for matching Title
                    for index, movie in enumerate(movie_list):
                        if title_string == movie.title:
                            search_results.append(index)
                    
                    if len(search_results) == 0:    # No results
                        console_interface.update_screen(f'{title_string} Not Found!', f'The movie {title_string} does not appear to exist in the database. Check your spelling and try again.')
                        console_interface.prompt_enter_to_continue()
                        
                    elif len(search_results) == 1:  # 1 Result
                        console_interface.update_screen(f'Removing {title_string}...', f'The movie {title_string} has been found in the database. Please note that removing a movie cannot be undone! If you want this movie back later, you will have to manually add it or import again.')
                        confirm_remove = console_interface.prompt_yes_or_no(f'Remove {title_string} from the database? [Note: This cannot be undone!]')
                        
                    else: # More than 1 result
                        console_interface.update_screen(f'Multiple Matches for {title_string} Found!', f'There are {len(search_results)} movies that have the title of {title_string}.')
                        
                        for number, index in enumerate(search_results):
                            print(f'Result Number {number + 1}:    {movie_list[index].title} ({movie_list[index].year}): {movie_list[index].genre} - Directed by {movie_list[index].director} and starring {movie_list[index].actor}.')
                        print()
                        
                        user_selection = console_interface.prompt_ask_for_number(f'Please enter the result number you wish to delete:')

                # Return to Main Menu Branch
                else:
                    menu_done = True
                        
        # Update a Movie Branch
        elif user_selection == 2:
            console_interface.update_screen('Update a Movie', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Search for Movies Branch
        elif user_selection == 3:
            console_interface.update_screen('Search for a Movie', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Import Data from CSV Branch
        elif user_selection == 4:
            console_interface.update_screen('Import Data from CSV', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Export Data to CSV Branch
        elif user_selection == 5:
            console_interface.update_screen('Export Data to CSV', 'Sorry! This feature has not be implemented yet! You will be returned to the main menu.')
            console_interface.prompt_enter_to_continue()
            
        # Exit Application Branch
        elif user_selection == 6:
            # TODO: Add a prompt asking the user if they would like to save their data to an external CSV file before quitting the application.
            console_interface.update_screen('Exiting Application...', 'You are about to close the application.')
            close_program = console_interface.prompt_yes_or_no('Are you sure you want to quit?')
            
        # DEBUG BRANCH: REMOVE ONCE APPLICATION IS FINISHED
        elif user_selection == 7:
            console_interface.update_screen('Debug Testing', 'Dev option branch for testing. Please delete before submitting.\nPrinting contents of movie_list:')
            
            for movie in movie_list:
                print(f'{movie.title}\t\t{movie.genre}\t\t{movie.age_rating}\t\t{movie.year}\t\t{movie.director}\t\t{movie.writer}\t\t{movie.actor}\t\t{movie.country}\t\t{movie.company}\t\t{movie.run_time}\t\t{movie.score}\t\t{movie.votes}\t\t')
                
            console_interface.prompt_enter_to_continue()
            
        # User has entered an invalid option (either it is not an integer or it is not a valid integer.)
        else:
            console_interface.update_screen('Error: Invalid Option!', 'You have entered an invalid option.')
            console_interface.prompt_enter_to_continue()
    
    console_interface.update_screen('Good Bye!', 'Thank you for using the Python Movie Database Manager! \nThe application has now been closed.')
