"""
Program executes here.
"""
import user_interface
import movies
import os

def main():
    console_interface = user_interface.ConsoleUI('Title', 'Body')
    """ConsoleUI: Main instance of ConsoleUI object to control the user interface with."""
    
    movie_database = movies.MovieDatabase()
    """MovieDatabase: Main instance of MovieDatabase used to store and manage data regarding Movie objects"""

    search_results = []
    """list: List to be used when searching movie_list. Results of movie_list searches should be stored in this list. Make sure to clear before starting a new search to avoid messing up results"""

    close_program = False
    """bool: Boolean used to determine when the program should be closed. When False, the program continues to run. When True, program closes."""
    
    while not close_program:
        menu_done = False
        task_done = False
        confirm_operation = False
        
        console_interface.update_screen('Main Menu', 'Welcome to the Python Movie Database Manager!\nFor the best viewing experience, please maximize this window. To get started, select an option below.')
        user_selection = console_interface.prompt_options_menu('Add or Remove a Movie', 'Update a Movie', 'Search and Display Movies', 'Import Data from CSV', 'Export Data to CSV', 'Exit Application', 'DEV: DEBUGGING')
        
        
        # Add or Remove Movie Branch
        if user_selection == 1: 
            while not menu_done:
                console_interface.update_screen('Add or Remove a Movie', 'From this menu, you can add a new movie to the database or remove one. Please select an option to continue.')
                user_selection = console_interface.prompt_options_menu('Add a New Movie', 'Remove an Existing Movie', 'Return to Main Menu')
                
                # Add a Movie Branch
                if user_selection == 1:
                    task_done = False
                    console_interface.update_screen('Add a New Movie', 'To add a new movie to the database, please first enter the title of the movie you wish to add.')
                    
                    # Get Title attribute (do not allow blanks) 
                    title_string = console_interface.prompt_ask_for_string('Enter the title of the movie', allow_blank=False)
                    new_movie_entry = movies.Movie.construct_new_movie(title_string, console_interface, movie_database)
                    
                    # Append movie to the movie_database
                    movie_database.add_movie(movies.Movie(*new_movie_entry))
                    console_interface.update_screen(f'{title_string} Added!', 'The movie has been successfully added to the database!')
                    console_interface.prompt_enter_to_continue()
                
                # Remove a Movie Branch
                elif user_selection == 2:
                    task_done = False
                    search_results.clear()
                    
                    console_interface.update_screen('Remove an Existing Movie', 'To remove a movie, please enter the title of the movie you woud like to remove. Please note that removing a movie cannot be undone!')
                    
                    # Search for movie
                    title_string = console_interface.prompt_ask_for_string('Enter the title of the movie', allow_blank=False)
                    search_results = movie_database.search_by_attribute(console_interface, 'title', title_string, return_index=True, return_multiple=False)
                    
                    if not search_results:
                        console_interface.update_screen(f'{title_string} not found!', f'{title_string} could not be found in the database. Check your spelling and try again.')
                        console_interface.prompt_enter_to_continue()
                    else:
                        index = search_results[0]
                        # Confirm removal
                        movie_to_remove = (f'{movie_database.data_list[index].title} ({movie_database.data_list[index].year})')
                        console_interface.update_screen(f'Removing {movie_to_remove}...', f'The movie {movie_to_remove} can be removed from the database. Please note that removing a movie cannot be undone! If you want this movie back later, you will have to manually add it or import again.')
                        confirm_operation = console_interface.prompt_yes_or_no(f'Remove {movie_to_remove} from the database? [Note: This cannot be undone!]')

                        if confirm_operation:
                            movie_database.remove_movie(index)
                            console_interface.update_screen(f'{movie_to_remove} Removed!', f'{movie_to_remove} has now been removed from the database.')
                            console_interface.prompt_enter_to_continue()
                        else:
                            console_interface.update_screen(f'Canceled {movie_to_remove} Removal', f'The removal operation has been canceled. {movie_to_remove} will remain in the database.')
                            console_interface.prompt_enter_to_continue()

                # Return to Main Menu Branch
                else: 
                    menu_done = True
                       
                        
        # Update a Movie Branch
        elif user_selection == 2:
            while not menu_done:
                task_done = False
                search_results.clear()
                
                console_interface.update_screen('Update a Movie', 'From here, you can select a movie entry to edit and update its information. Please select an option below.')
                user_selection = console_interface.prompt_options_menu('Edit a Movie\'s Details', 'Return to Main Menu')
                
                # Update a Movie
                if user_selection == 1:
                    console_interface.update_screen('Update a Movie', 'To begin editing, please enter the title of the movie you wish to edit.')
                    
                    # Search for movie
                    title_string = console_interface.prompt_ask_for_string('Enter the title of the movie', allow_blank=False)
                    search_results = movie_database.search_by_attribute(console_interface,'title', title_string, return_index=True, return_multiple=False)
                    
                    if not search_results:
                        console_interface.update_screen(f'{title_string} not found!', f'{title_string} could not be found in the database. Check your spelling and try again.')
                        console_interface.prompt_enter_to_continue()
                    else:
                        index = search_results[0]
                        while not task_done:
                            console_interface.update_screen(f'{movie_database.data_list[index].title} Information', f'Here is the information on {movie_database.data_list[index].title}. Please select which detail you would like to edit below.')
                            movie_database.print_movie_details_list(index)
                    
                            user_selection = console_interface.prompt_ask_for_string('Please enter the attribute you wish to change. If you are done, type \'Done\' instead', allow_blank=False)
                            # Make sure the user entered a valid attribute or entered the sentinel value 'Done' or 'done'.
                            while user_selection not in movie_database.attribute_list and user_selection != 'Done' and user_selection != 'done':
                                user_selection = console_interface.prompt_ask_for_string('That is not a valid attribute. Please enter the movie detail you wish to edit as it exactly appears above. If you are done, type \'Done\' instead', allow_blank=False)
                        
                            if user_selection == 'Done' or user_selection == 'done':
                                task_done = True
                            else:
                                new_value = console_interface.prompt_ask_for_string(f'Please enter the new value for this movie\'s {user_selection}')
                                movie_database.update_movie_attribute(index, user_selection, new_value)
                                console_interface.prompt_enter_to_continue()
                # Return to Main Menu
                else:
                    menu_done = True
            
            
        # Search for Movies Branch
        elif user_selection == 3:
            while not menu_done:
                task_done = False                
                search_results.clear()
                
                console_interface.update_screen('Search and Display Movies', 'From this menu you can choose to search for a movie by attribute and display the movies currently in the database.\n'
                                                f'\nThere are currently {len(movie_database.data_list)} record(s) in the database.\n\nPlease select an option below to continue.')
                user_selection = console_interface.prompt_options_menu('Begin a Search', 'Display All Movies', 'Return to Main Menu')

                # Movie Search Menu Loop
                if user_selection == 1:
                    while not task_done:
                        
                        console_interface.update_screen('Movie Search Menu', f'Welcome to the search menu, please select an operation below.\nCurrent search results: {len(search_results)} records')
                        user_selection = console_interface.prompt_options_menu('Search by Attribute', 'Sort Current Search Results', 'Display Current Search Results', 'Clear Current Search Results', 'Export Search Results to CSV File', 'Return to Previous Menu')
                        
                        # Search by Attribute
                        if user_selection == 1:
                            console_interface.update_screen('Search by Attribute', f'The attributes you can search in are listed below. To begin searching, please type the attribute you wish to search exactly how it appears.')
                            for attribute in movie_database.attribute_list:
                                print(f'{attribute}', end=' '*15)
                            print('\n')
                            
                            attribute = console_interface.prompt_ask_for_string('Please enter the attribue you wish to search from here', allow_blank=False)
                            while attribute not in movie_database.attribute_list:
                                attribute = console_interface.prompt_ask_for_string('That is not a valid attribute. Please enter the movie attribute you wish to search through as it exactly appears above', allow_blank=False)
                            
                            user_selection = console_interface.prompt_ask_for_string('Now enter the term you would like to search for')
            
                            attribute_to_search = movie_database.convert_to_actual_attribute(attribute)
                            
                            # If search_results is empty, the first search should be done on movie_database to populate it.
                            # From there on, every search is then performed on search_results rather than the main database.
                            if not search_results:
                                search_results.extend(movie_database.search_by_attribute(console_interface, attribute_to_search, user_selection))
                            else:
                                ongoing_search = search_results.copy()
                                search_results.clear()
                                search_results.extend(movie_database.search_by_attribute(console_interface, attribute_to_search, user_selection, ongoing_search))
                            
                            console_interface.update_screen(f'Searching for {user_selection} in {attribute}', f'Search completed! There are {len(search_results)} search result(s).\n'
                                                            'To display your search results, please select the second option in the next menu. If you wish to refine your search (search the search results), please enter option one on the next menu.')
                            console_interface.prompt_enter_to_continue()
                        
                        # Sort Search Results
                        # TODO: Implement this
                        elif user_selection == 2:
                            pass
                        
                        # Display Current Search Results
                        elif user_selection == 3:
                            console_interface.update_screen('Movie Search Results', f'Amount of search results: {len(search_results)} records')
                            movie_database.print_table(search_results)
                            console_interface.prompt_enter_to_continue()
                            
                        # Clear Current Search Results
                        elif user_selection == 4:
                            console_interface.update_screen('Movie Search Menu - Warning!', f'You are about to clear your current search ({len(search_results)} records)!')
                            confirm_operation = console_interface.prompt_yes_or_no('Are you sure you wish to clear your current search results?')
                            if confirm_operation:
                                search_results.clear()
                                console_interface.update_screen('Movie Search Menu - Search Results Cleared', 'Your search results have been cleared.')
                                console_interface.prompt_enter_to_continue()
                            else:
                                continue
                        # Export Search Results to CSV File
                        # TODO: Implement this
                        elif user_selection == 5:
                            console_interface.update_screen('Movie Search Results - Export Search Results to CSV File', 'This feature has not been implemented yet! Sorry!')
                            console_interface.prompt_enter_to_continue()
                        # Return to Previous Menu
                        else:
                            if len(search_results) > 0:
                                console_interface.update_screen('Warning! - Ongoing Search', 'You currently have an ongoing search! Exiting this menu will result in the search results being lost.\n'
                                                                'If you wish to save your current search results, please go back and use the "Export Search Results to CSV File" option.')
                                task_done = console_interface.prompt_yes_or_no('Are you sure you want to exit the Movie Search Menu and lose your progress?')
                            else:
                                task_done = True
                
                # Display All Movies   
                elif user_selection == 2:
                    console_interface.update_screen('Display All Movie Records', 'Here are all the movies and their details currently loaded into the Pythom Movie Database Manager.\n\n'
                                                    f'There are currently {len(movie_database.data_list)} record(s) in the database.')
                    movie_database.print_table(movie_database.data_list)
                    console_interface.prompt_enter_to_continue()
                
                # Return to Main Menu
                else:
                    menu_done = True
            
            
        # Import Data from CSV Branch
        elif user_selection == 4:
            console_interface.update_screen('Import Data from CSV', 'From this menu, you can import external movie data from a comma-seperated value (CSV) file.\n'
                                            'You will need to have a properly formatted CSV file to import data from. Check the user documentation for more information.')
            file_path = console_interface.prompt_ask_for_string('Please enter the location of the CSV file you wish to import', allow_blank=False)
                
            # File not found: Ask the user if they would like to create a file instead.
            if not os.path.isfile(file_path):
                console_interface.update_screen('Import Data from CSV - Error - File Not Found', f'The file: "{file_path}" does not exist.')
                confirm_operation = console_interface.prompt_yes_or_no('Would you like to create a new CSV file?')
                if confirm_operation:
                    movie_database.export_to_csv(file_path, movie_database.data_list)
                    console_interface.update_screen('Import Data from CSV - File Created', f'Empty CSV file created at "{file_path}".')
                else:
                    console_interface.update_screen('Import Data from CSV - Returning to Main Menu', 'No file was created.')         
            else:
                imported_movies = movie_database.import_from_csv(file_path)
                
                if imported_movies:
                    movie_database.add_movies(imported_movies)
                    console_interface.update_screen('Import Data from CSV - Import Success!', f'{len(imported_movies)} movie records have been added to the database!')
                else:
                    console_interface.update_screen('Import Data from CSV - No Movies Imported', 'No valid movies found in the file. You will be returned to the Main Menu.')
                    
            console_interface.prompt_enter_to_continue()
            menu_done = True
            
            
        # Export Data to CSV Branch
        elif user_selection == 5:
            if not movie_database.data_list:
                console_interface.update_screen('Export Data to CSV - Error!', 'There are no records currently in the database to export. You will need to have at least one '
                                                'entry in the database to be able to export to a CSV file.')
            else:
                console_interface.update_screen('Export Data to CSV', 'From this menu, you can export the current database to to an external comma-seperated value (CSV) file '
                                                'for use with another program or to load into this program at a later time.')
                
                file_path = console_interface.prompt_ask_for_string('Please enter the file location and file name of the CSV file to export to', allow_blank=False)
                movie_database.export_to_csv(file_path, movie_database.data_list)
                console_interface.update_screen('Export Data to CSV - Export Success!', f'Movie data succesfully exported to {file_path}')
            
            console_interface.prompt_enter_to_continue()
            
            
        # Exit Application Branch
        elif user_selection == 6:
            # TODO: Add a prompt asking the user if they would like to save their data to an external CSV file before quitting the application.
            console_interface.update_screen('Exiting Application...', 'You are about to close the application.')
            close_program = console_interface.prompt_yes_or_no('Are you sure you want to quit?')
            
            
        # DEBUG BRANCH: REMOVE ONCE APPLICATION IS FINISHED
        elif user_selection == 7:
            console_interface.prompt_enter_to_continue()
                    
                    
        # User has somehow entered an invalid option.
        else:
            console_interface.update_screen('Error: Invalid Option!', 'You have entered an invalid option.')
            console_interface.prompt_enter_to_continue()
    
    console_interface.update_screen('Good Bye!', 'Thank you for using the Python Movie Database Manager! \nThe application has now been closed.')


if __name__ == '__main__':
    main()