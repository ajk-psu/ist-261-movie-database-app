"""
 _summary_

Returns:
    _type_: _description_
"""

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
        

class MovieDatabase:
    """
     _summary_
    """
    
    def __init__(self):
        self.data_list = []
        self.search_list = []
        self.attribute_list = ['Title', 'Genre', 'Age Rating', 'Release Year', 'Director', 'Writer', 'Lead Actor', 'Country of Origin', 'Publishing Company', 'Run Time', 'IMDb Score', 'Amount of Votes']
    
    def add_movie(self, movie):
        """
        Adds the specified Movie object to the data list at the end of the list.

        Args:
            movie (str): The Movie object to be addded.
        """
        self.data_list.append(movie)
    
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
    

    def search_by_attribute(self, search_attribute, search_value, return_index = False):
        """
        Searches the data list for Movies objects with the given attribute that matches the given search value.

        Args:
            search_attribute (str): The Movie object attribute to search for.
            search_value (str, int, float): The value to search for.
            return_index (bool, optional): When set to True, this method will instead return a list of indexes of where each matching Movie was found in the data_list. Defaults to False.

        Returns:
            Returns a list of Movie objects that match the criteria. If return_index is set to True, returns a list of indexes of where each matching Movie object was found in the data_list.
        """
        search_results = []
        search_results.clear() # For safety
        for index, movie in enumerate(self.data_list):
            if getattr(movie, search_attribute) == search_value:
                if return_index is True:
                    search_results.append(index)
                else:
                    search_results.append(movie)
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
    def convert_to_actual_attribute(descriptive_attribute):
        """
        Converts the given descriptive attribute to the actual attribute it refers to in code. For example, 'Publishing Company' becomes company.

        Args:
            descriptive_attribute (str): 
        """
        pass
    
    @staticmethod
    def print_table(list):
        """
        Prints a formatted table with the given list of data.

        Args:
            list (list): The list to construct the formatted table from.
        """
        print(f'{'Title':60} {'Genre':15} {'Age Rating':15} {'Release Year':15} {'Director':25} {'Writer':25} {'Lead Actor':25} {'Country of Origin':25} {'Publishing Company':50} {'Run Time':10} {'IMDb Score':15} {'Amount of Votes':15}')
        print('-' * 310)
        
        if len(list) == 0:
            print(f'{'There are no movie records to display.':^310}')
        else:
            for movie in list:
                print(f'{movie.title:60} {movie.genre:15} {movie.age_rating:15} {movie.year:<15} {movie.director:25} {movie.writer:25} {movie.actor:25} {movie.country:25} {movie.company:50} {movie.run_time:<10} {movie.score:<15} {movie.votes:<15}')
        
        print('-' * 310, '\n')
        
# If this file is launched as as script, print an error message alerting the user to open the correct file.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' in order to launch the Python Movie Database Manager.\n')