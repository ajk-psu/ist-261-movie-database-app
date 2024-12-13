import csv

class Movie:
    def __init__(self, title, genre, age_rating, year, director, writer, actor, country, company, run_time, score, votes):
        self.title = title
        self.genre = genre
        self.age_rating = age_rating
        self.year = year
        self.director = director
        self.writer = writer
        self.actor = actor
        self.country = country
        self.company = company
        self.run_time = run_time
        self.score = score
        self.votes = votes
    
    @staticmethod
    def construct_new_movie(title_name, console_interface, movie_database):
        new_movie_entry = []
        task_done = False
        
        while not task_done:
            console_interface.update_screen(f'Adding {title_name} to the Database', f'Please fill out the following details about {title_name}. If you are unsure of a detail, you may leave that field blank.') 
            new_movie_entry.clear()
            new_movie_entry.append(title_name)
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
            console_interface.update_screen(f'Confirm Details for {title_name}', f'You are about to add {title_name} to the database. Please confirm the deatils you entered are correct.')
            for (attribute, item) in zip(movie_database.attribute_list, new_movie_entry):
                print(f'{attribute}: {item}')
            print()
            task_done = console_interface.prompt_yes_or_no(f'Are these details correct and do you want to add {title_name} to the database? If you need to change a detail, answer \'No\' to go back')
        
        return new_movie_entry
        

class MovieDatabase:
    """
     _summary_
    """
    
    def __init__(self):
        self.data_list = []
        self.attribute_list = ['Title', 'Genre', 'Age Rating', 'Release Year', 
                               'Director', 'Writer', 'Lead Actor', 'Country of Origin', 'Publishing Company',
                               'Run Time', 'IMDb Score', 'Amount of Votes']
    
    def add_movie(self, movie):
        """
        Adds the specified Movie object to the data list at the end of the list.

        Args:
            movie (str): The Movie object to be addded.
        """
        self.data_list.append(movie)
    
    def add_movies(self, movies):
        """
        Takes a list of Movie objects and adds them to the data list at the end of the list.

        Args:
            movies (list): List of movies to add to the database.
        """
        self.data_list.extend(movies)
    
    def remove_movie(self, index):
        """
        Removes the Movie object at the specified index. 
        This should also delete the Movie object itself as it should have 0 references after operation.

        Args:
            index (int): The index of the Movie object to be removed from the data list.
        """
        del(self.data_list[index])
    
    def update_movie_attribute(self, index, attribute, new_value):
        """
        Changes an existing Movie object's attribute.

        Args:
            index (int): The index where the Movie object is located in the data list.
            attribute (str): The attribute of the Movie object to change.
            new_value (str, int, float): The new value to change the attribute's value to.
        
        Raises:
            ValueError: _Description_: Inappropriate argument value (of correct type). May be raised when editing an attribute of integer or float type.
        """
        # Use string attribute to determine which Movie object attribute to change.
        # For attributes that store either an integer or float, attempt to convert type first. If conversion fails, do not change attribute value.
        if attribute == 'Title':
            self.data_list[index].title = new_value
            print('Title updated!')
        elif attribute == 'Genre':
            self.data_list[index].genre = new_value
            print('Genre updated!')
        elif attribute == 'Age Rating':
            self.data_list[index].age_rating = new_value
            print('MPAA age rating updated!')
        elif attribute == 'Release Year':
            try:
                int(new_value)
                self.data_list[index].year = new_value
                print('Release year updated!')
            except:
                print('You have enter an invalid entry for this attribute. Release year must be an integer (no decimals).\n'
                      'The value for this attribute will not be changed.')
        elif attribute == 'Director':
            self.data_list[index].director = new_value
            print('Director updated!')
        elif attribute == 'Writer':
            self.data_list[index].writer = new_value
            print('Main writer updated!')     
        elif attribute == 'Lead Actor':
            self.data_list[index].actor = new_value
            print('Lead actor updated!')
        elif attribute == 'Country of Origin':
            self.data_list[index].country = new_value
            print('Country of origin updated!')
        elif attribute == 'Publishing Company':
            self.data_list[index].company = new_value
            print('Publishing company updated!')
        elif attribute == 'Run Time':
            try:
                int(new_value)
                self.data_list[index].run_time = new_value
                print('Run time updated!')
            except:
                print('You have enter an invalid entry for this attribute. Run time is recorded in minutes and must be an integer (no decimals).\n'
                      'The value for this attribute will not be changed.')
        elif attribute == 'IMDb Score':
            try:
                float(new_value)
                self.data_list[index].score = new_value
                print('IMDb score updated!')
            except:
                print('You have enter an invalid entry for this attribute. IMDb score must be a number.\n'
                      'The value for this attribute will not be changed.')
        elif attribute == 'Amount of Votes':
            try:
                int(new_value)
                self.data_list[index].votes = new_value
                print('Amount of IMDb user votes updated!')
            except:
                print('You have enter an invalid entry for this attribute. IMDb score must be a number.\n'
                      'The value for this attribute will not be changed.')
        else:
            print('Unknown attribute. No value will be changed.')
    
    def sort_by_attribute(self, sort_attribute, ascending, external_list = None):
        pass

    def search_by_attribute(self, console_interface, search_attribute, search_value, external_list = None, return_index = False, return_multiple = True):
        """
        Searches the data list for Movies objects with the given attribute that matches the given search value.

        Args:
            console_interface (ConsoleUI): A console_interface object is passed to this method to allow this method to draw user interface elements.
            search_attribute (str): The Movie object attribute to search for.
            search_value (str, int, float): The value to search for.
            external_list (list, optional): This method can be performed on an external list of Movie objects. If passed to this method, the search is performed on it instead of the MovieDatabase's own list.
            return_index (bool, optional): When set to True, this method will instead return a list of indexes of where each matching Movie was found in the data_list. Defaults to False.
            return_multiple (bool, optional): When set to False, this method will prompt the user to select one search result from a list of matching results and then return that result only.

        Returns:
            Returns a list of Movie objects that match the criteria. If return_index is set to True, returns a list of indexes of where each matching Movie object was found in the data_list.
        """
        search_results = []
        search_results.clear()
        
        if external_list is None:
            list_to_search = self.data_list
        else:
            list_to_search = external_list
        
        # If the user is searching an attribute that is a number type, convert the search_value to the correct type before
        if search_attribute == 'year' or search_attribute == 'run_time' or search_attribute == 'votes':
            try:
                search_value = int(search_value)
            except:
                print('Error: The search value could not be converted into the correct type (int) before the search was performed.')
        elif search_attribute == 'score':
            try:
                search_value = float(search_value)
            except:
                print('Error: The search value could not be converted into the correct type (float) before the search was performed.')
        
        # Search by attribute
        for index, movie in enumerate(list_to_search):
            if getattr(movie, search_attribute) == search_value:
                if return_index:
                    search_results.append(index)
                else:
                    search_results.append(movie)
        
        # If return_multiple is set to false and the search has multiple results, begin the process to prompt the user to only select one.
        if not return_multiple and len(search_results) > 1:
            console_interface.update_screen(f'Multiple Matches for {search_value} Found!', f'There are {len(search_results)} movies that match this criteria. Please select the appropriate one to continue with.')
            
            if return_index:
                for number, index in enumerate(search_results):
                    print(f'Result Number {number + 1}:  {self.data_list[index].title} ({self.data_list[index].year}): Genre: {self.data_list[index].genre} - Directed by {self.data_list[index].director} and starring {self.data_list[index].actor}.')
            else:
                console_interface.update_screen(f'Multiple Matches for {search_value} Found!', f'There are {len(search_results)} movies that match this criteria. Please select the appropriate one to continue with.')
                for index, movie in enumerate(search_results):
                    print(f'Result Number {index + 1}:  {movie.title} ({movie.year}): Genre: {movie.genre} - Directed by {movie.director} and starring {movie.actor}.')
            
            # 1 is added to the index the user sees to be more "user friendly" (otherwise Result Number would start at 0). Because of this, 1 must be subtracted from the input to get it back in index range. 
            selected_result = int(console_interface.prompt_ask_for_number(f'\nPlease enter the result number of the movie to continue working with')) - 1
            while selected_result not in range(len(search_results)):
                selected_result = int(console_interface.prompt_ask_for_number(f'That is not a valid choice. Please enter one of the result numbers')) - 1
            
            search_results = search_results[selected_result:selected_result + 1]
            
        return search_results
    
    def print_movie_details_list(self, index):
        """
        Prints all the attribute details for a specified Movie object instance.

        Args:
            index (int): The index of where the specified Movie object instance is located within data_list.
        """
        print(f'Title: {self.data_list[index].title}\n'
              f'Genre: {self.data_list[index].genre}\n'
              f'Age Rating: {self.data_list[index].age_rating}\n'
              f'Release Year: {self.data_list[index].year}\n'
              f'Director: {self.data_list[index].director}\n'
              f'Writer: {self.data_list[index].writer}\n'
              f'Starring Actor: {self.data_list[index].actor}\n'
              f'Country of Origin: {self.data_list[index].country}\n'
              f'Publishing Company: {self.data_list[index].company}\n'
              f'Run Time (in minutes): {self.data_list[index].run_time}\n'
              f'IMDb Score: {self.data_list[index].score}\n'
              f'Amount of User Votes: {self.data_list[index].votes}\n'
              )
        
    @staticmethod
    def import_from_csv(file_path):
        """
        Imports movies from a CSV file and returns a list of Movie objects.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            list: A list of Movie instances.
        """
        movie_list = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        movie_list.append(Movie(
                            title = row['Title'],
                            genre = row['Genre'] if row['Genre'] else 'Unknown',
                            age_rating = row['Age Rating'] if row['Age Rating'] else 'Unknown',
                            year = int(row['Release Year']) if row['Release Year'] else 0,
                            director = row['Director'] if row['Director'] else 'Unknown',
                            writer = row['Writer'] if row['Writer'] else 'Unknown',
                            actor = row['Lead Actor'] if row['Lead Actor'] else 'Unknown',
                            country = row['Country of Origin'] if row['Country of Origin'] else 'Unknown',
                            company = row['Publishing Company'] if row['Publishing Company'] else 'Unknown',
                            run_time = int(row['Run Time']) if row ['Run Time'] else 0,
                            score = float(row['IMDb Score']) if row ['IMDb Score'] else 0.0,
                            votes = int(row['Amount of Votes']) if row ['Amount of Votes'] else 0
                        ))
                    except ValueError as ve:
                        print(f"Skipping invalid row: {row}, Error: {ve}")
            print(f"Successfully imported {len(movie_list)} movies from '{file_path}'.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
        except KeyError as ke:
            print(f"Error: Missing column in CSV: {ke}")

        return movie_list
    
    @staticmethod
    def export_to_csv(file_path, movie_list):
        """
        Exports a list of Movie objects to a CSV file.

        Args:
            file_path (str): The path to the CSV file.
            movie_list (list): A list of Movie instances to export.
        """
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Title', 'Genre', 'Age Rating', 'Release Year', 
                                                          'Director', 'Writer', 'Lead Actor', 'Country of Origin', 
                                                          'Publishing Company', 'Run Time', 'IMDb Score', 'Amount of Votes'])
                writer.writeheader()
                for movie in movie_list:
                    writer.writerow({
                        'Title': movie.title,
                        'Genre': movie.genre,
                        'Age Rating': movie.age_rating,
                        'Release Year': movie.year,
                        'Director': movie.director,
                        'Writer': movie.writer,
                        'Lead Actor': movie.actor,
                        'Country of Origin': movie.country,
                        'Publishing Company': movie.company,
                        'Run Time': movie.run_time,
                        'IMDb Score': movie.score,
                        'Amount of Votes': movie.votes
                    })
            print(f"Successfully exported {len(movie_list)} movies to '{file_path}'.")
        except IOError as e:
            print(f"Error writing to file '{file_path}': {e}")
    
    @staticmethod
    def convert_to_actual_attribute(descriptive_attribute):
        """
        Converts the given descriptive attribute to the actual attribute it refers to in code. For example, 'Publishing Company' becomes company.

        Args:
            descriptive_attribute (str): 
        """
        if descriptive_attribute == 'Title':
            return 'title'
        elif descriptive_attribute == 'Genre':
            return 'genre'
        elif descriptive_attribute == 'Age Rating':
            return 'age_rating'
        elif descriptive_attribute == 'Release Year':
            return 'year'
        elif descriptive_attribute == 'Director':
            return 'director'
        elif descriptive_attribute == 'Writer':
            return 'writer'
        elif descriptive_attribute == 'Lead Actor':
            return 'actor'
        elif descriptive_attribute == 'Country of Origin':
            return 'country'
        elif descriptive_attribute == 'Publishing Company':
            return 'company'
        elif descriptive_attribute == 'Run Time':
            return 'run_time'
        elif descriptive_attribute == 'IMDb Score':
            return 'score'
        elif descriptive_attribute == 'Amount of Votes':
            return 'votes'
        else:
            print('Unknown attribute.')
    
    @staticmethod
    def print_table(list_to_print):
        """
        Prints a formatted table with the given list of data.

        Args:
            list_to_print (list): The list to construct the formatted table from.
        """
        print(f'{'Title':60} {'Genre':15} {'Age Rating':15} {'Release Year':15} {'Director':25} {'Writer':25} {'Lead Actor':25} {'Country of Origin':25} {'Publishing Company':50} {'Run Time':10} {'IMDb Score':15} {'Amount of Votes':15}')
        print('-' * 310)
        
        if len(list_to_print) == 0:
            print(f'{'There are no movie records to display.':^310}')
        else:
            for movie in list_to_print:
                print(f'{movie.title:60} {movie.genre:15} {movie.age_rating:15} {movie.year:<15} {movie.director:25} {movie.writer:25} {movie.actor:25} {movie.country:25} {movie.company:50} {movie.run_time:<10} {movie.score:<15} {movie.votes:<15}')
        
        print('-' * 310, '\n')
        
# If this file is launched as as script, print an error message alerting the user to open the correct file.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' in order to launch the Python Movie Database Manager.\n')