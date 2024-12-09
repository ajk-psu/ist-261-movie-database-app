"""
Program executes here.
"""
import user_interface
import movies

# Variable and Class Definitions
console_interface = user_interface.ConsoleUI('Title', 'Body')
"""ConsoleUI: Main instance of ConsoleUI object to control the user interface with."""

movie_data = movies.MovieDatabase()
"""MovieDatabase: Main instance of MovieDatabase used to store and manage data regarding Movie objects"""

new_movie_entry = []
"""list: List used to hold attributes that will be used to construct a new Movie object."""

search_results = []
"""list: List to be used when searching movie_list. Results of movie_list searches should be stored in this list. Make sure to clear before starting a new search to avoid messing up results"""

title_string = ''
"""str: Used to hold the title of the movie the user wishes to perform an operation on."""

close_program = False
"""bool: Boolean used to determine when the program should be closed. When False, the program continues to run. When True, program closes."""

menu_done = False
"""bool: Boolean used to determine if the current menu loop the program is running has finished."""

task_done = False
"""bool: Boolean used to determine if the current task loop the program is running has finished."""
    
user_selection = -1
"""int: Integer used to store the user's selected option."""


# Method Defintions
def get_title_string():
    """
    Prompts the user to enter the Title of a movie. Does not allow blank (null) responses.

    Returns:
        Returns string containing the title of a movie.
    """
    title_string = console_interface.prompt_ask_for_string('Enter the title of the movie', replace_blank=False)
    while len(title_string) == 0:   
        title_string = console_interface.prompt_ask_for_string('You must enter a title for the movie. Please enter a title', replace_blank=False)
    return title_string

def select_a_result(search_results, movie_data):
    """
    If a search result returns more than one result when only one is needed for an operation (such as deleting or updating), this method prompts the user to select one result to be used for further operations.

    Args:
        search_results (list): List of indexes
        movie_data (list): Corresponding list of movie data to crawl through

    Returns:
        Returns integer of the selected result to continue operations with.
    """
    for number, index in enumerate(search_results):
        print(f'Result Number {number + 1}:   {movie_data.data_list[index].title} ({movie_data.data_list[index].year}): Genre: {movie_data.data_list[index].genre} - Directed by {movie_data.data_list[index].director} and starring {movie_data.data_list[index].actor}.')
    print()
    
    # 1 needs to be subtracted from the user's response so that it corresponds to an index (do not allow an out of range entry).
    selected_result = int(console_interface.prompt_ask_for_number(f'Please enter the result number you wish to delete')) - 1
    while selected_result not in range(len(search_results)):
        selected_result = int(console_interface.prompt_ask_for_number(f'That is not a valid choice. Please enter one of the result numbers')) - 1
    return selected_result
                            
    
# Main program loop starts here.
if __name__ == '__main__':
    
    while close_program is False:
        
        menu_done = False # Set menu_done to False when entering the main menu to avoid making it impossible to enter the sub-menus.
        console_interface.update_screen('Main Menu', 'Welcome to the Python Movie Database Manager! Please select an option below.')
        user_selection = console_interface.prompt_options_menu('Add or Remove a Movie', 'Update a Movie', 'Search for Movies', 'Import Data from CSV', 'Export Data to CSV', 'Exit Application', 'DEV: DEBUGGING')
    
        # Add or Remove Movie Branch
        if user_selection == 1:
            
            while menu_done is False:
                console_interface.update_screen('Add or Remove a Movie', 'From this menu, you can add a new movie to the database or remove one. Please select an option to continue.')
                user_selection = console_interface.prompt_options_menu('Add a New Movie', 'Remove an Existing Movie', 'Return to Main Menu')
                
                # Add a Movie Branch
                if user_selection == 1:
                    task_done = False
                    
                    console_interface.update_screen('Add a New Movie', 'To add a new movie to the database, please first enter the title of the movie you wish to add.')
                    
                    # Get Title attribute (do not allow blanks)
                    title_string = get_title_string()
                    
                    #Get rest of movie attributes from user
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
                    
                        # Confirm details
                        console_interface.update_screen(f'Confirm Details for {title_string}', f'You are about to add {title_string} to the database. Please confirm the deatils you entered are correct.')
                        for (attribute, item) in zip(movie_data.attribute_list, new_movie_entry):
                            print(f'{attribute}: {item}')
                        task_done = console_interface.prompt_yes_or_no(f'\nAre these details correct and do you want to add {title_string} to the database? If you need to change a detail, answer \'No\' to go back')
                    
                    # Append movie to the movie_list
                    movie_data.add_movie(movies.Movie(*new_movie_entry))
                    console_interface.update_screen(f'{title_string} Added!', 'The movie has been successfully added to the database!')
                    console_interface.prompt_enter_to_continue()
                
                # Remove a Movie Branch
                elif user_selection == 2:
                    task_done = False
                    confirm_remove = False
                    """bool: Boolean used to confirm user's choice"""
                    search_results.clear() # Clear search_results to avoid polluting the next search results with results from an old search.
                    
                    console_interface.update_screen('Remove an Existing Movie', 'To remove a movie, please enter the title of the movie you woud like to remove. Please note that removing a movie cannot be undone!')
                    
                    # Get Title attribute, do not allow blanks
                    title_string = get_title_string()
                    
                    # Search for matching Title
                    search_results = movie_data.search_by_attribute('title', title_string, return_index=True)
                    
                    if len(search_results) == 0:    # No results
                        console_interface.update_screen(f'{title_string} Not Found!', f'The movie {title_string} does not appear to exist in the database. Check your spelling and try again.')
                        console_interface.prompt_enter_to_continue()
                        
                    elif len(search_results) == 1:  # 1 Result
                        found_title = movie_data.data_list[search_results[0]].title
                        # Confirm removal
                        console_interface.update_screen(f'Removing {found_title}...', f'The movie {found_title} has been found in the database. Please note that removing a movie cannot be undone! If you want this movie back later, you will have to manually add it or import again.')
                        confirm_remove = console_interface.prompt_yes_or_no(f'Remove {found_title} from the database? [Note: This cannot be undone!]')
                        if confirm_remove is True:
                            # Remove movie
                            movie_data.remove_movie(search_results[0])
                            console_interface.update_screen(f'{title_string} Removed!', f'{title_string} has now been removed from the database.')
                            console_interface.prompt_enter_to_continue()
                        else:
                            # Cancel removal
                            console_interface.update_screen(f'Canceled {found_title} Removal', f'The removal operation has been canceled. {found_title} will remain in the database.')
                            console_interface.prompt_enter_to_continue()
                        
                    else: # More than 1 result: User must select which movie they would like to delete.
                        console_interface.update_screen(f'Multiple Matches for {title_string} Found!', f'There are {len(search_results)} movies that have the title of {title_string}.')
                        
                        user_selection = select_a_result(search_results, movie_data)
                            
                        # Confirm removal
                        found_title = movie_data.data_list[search_results[user_selection]]
                        console_interface.update_screen(f'Removing {found_title.title} ({found_title.year})...', f'You have selected {found_title.title} ({found_title.year}) to be removed from the database. Please note that removing a movie cannot be undone! If you want this movie back later, you will have to manually add it or import again.')
                        confirm_remove = console_interface.prompt_yes_or_no(f'Remove {found_title.title} ({found_title.year}) from the database? [Note: This cannot be undone!]')
                        if confirm_remove is True:
                            # Remove movie
                            del movie_data.data_list[search_results[user_selection]]
                            console_interface.update_screen(f'{title_string} Removed!', f'{title_string} has now been removed from the database.')
                            console_interface.prompt_enter_to_continue()
                        else:
                            # Cancel removal
                            console_interface.update_screen(f'Canceled {found_title.title} ({found_title.year}) Removal', f'The removal operation has been canceled. {found_title.title} ({found_title.year}) will remain in the database.')
                            console_interface.prompt_enter_to_continue()

                # Return to Main Menu Branch
                else:
                    menu_done = True
                        
        # Update a Movie Branch
        elif user_selection == 2:
            while menu_done is False:
                console_interface.update_screen('Update a Movie', 'From here, you can select a movie entry to edit and update its information.')
                console_interface.prompt_enter_to_continue()
                menu_done = True
            
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
            
            movie_data.print_entire_table()
                
            console_interface.prompt_enter_to_continue()
            
        # User has entered an invalid option (either it is not an integer or it is not a valid integer.)
        else:
            console_interface.update_screen('Error: Invalid Option!', 'You have entered an invalid option.')
            console_interface.prompt_enter_to_continue()
    
    console_interface.update_screen('Good Bye!', 'Thank you for using the Python Movie Database Manager! \nThe application has now been closed.')
