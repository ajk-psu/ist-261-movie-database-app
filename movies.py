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
        self.attribute_list = ['Title', 'Genre', 'Age Rating', 'Release Year', 'Director', 'Writer', 'Starring Actor', 'Country of Origin', 'Publishing Company', 'Run Time (in minutes)', 'IMDb Score', 'Amount of User Votes']
    
    def add_movie(self, movie):
        """
        Adds the specified Movie object to the data list, at the end of the list.

        Args:
            movie (str): _Description_: The Movie object to be addded.
        """
        self.data_list.append(movie)
    
    def remove_movie(self, index):
        """
        Removes the Movie object at the specified index. (This should also delete the Movie object itself as it will have 0 references after operation.)

        Args:
            index (int): _Description_: The index of the Movie object to be removed from the data list.
        """
        del(self.data_list[index])
    
    def update_movie_attribute(self, index, attribute, new_value):
        pass
    
    def search_by_attribute(self, search_attribute, search_value, return_index = False):
        """
        Searches the data list for Movies objects with the given attribute that matches the given search value.

        Args:
            search_attribute (str): _Description_: The Movie object attribute to search for.
            search_value (str, int, float): _Description_: The value to search for.
            return_index (bool, optional): _Dscription_. When set to True, this method will instead return a list of indexes of where each matching Movie was found in the data_list. Defaults to False.

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
        print(f'Title: {self.data_list[index].title}\n'
              f'Genre: {self.data_list[index].genre}\n'
              f'Age Rating: {self.data_list[index].age_rating}\n'
              f'Relase Year: {self.data_list[index].year}\n'
              f'Director: {self.data_list[index].director}\n'
              f'Writer: {self.data_list[index].writer}\n'
              f'Starring Actor: {self.data_list[index].actor}\n'
              f'Country of Origin: {self.data_list[index].country}\n'
              f'Publishing Company: {self.data_list[index].company}\n'
              f'Run Time (in minutes): {self.data_list[index].run_time}\n'
              f'IMDb Score: {self.data_list[index].score}\n'
              f'Amount of User Votes: {self.data_list[index].votes}\n'
              )
    
    def print_entire_table(self):
        for attribute in self.attribute_list:
            print(f'{attribute}', end='\t\t')
        print()
        for movie in self.data_list:
            print(f'{movie.title}\t\t{movie.genre}\t\t{movie.age_rating}\t\t{movie.year}\t\t{movie.director}\t\t{movie.writer}\t\t{movie.actor}\t\t{movie.country}\t\t{movie.company}\t\t{movie.run_time}\t\t{movie.score}\t\t{movie.votes}')
        
        
# If this file is launched as as script, print an error message alerting the user to open the correct file.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' in order to launch the Python Movie Database Manager.\n')