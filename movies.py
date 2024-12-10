# TODO: Module and Class docstrings

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
        
    def add_movie(self):
        pass
    
    def update_movie(self):
        pass
    
    def remove_movie(self):
        pass

# TODO: Everything here.

# If this file is launched as as script, print an error message alerting the user to open the correct file.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' in order to launch the Python Movie Database Manager.\n')