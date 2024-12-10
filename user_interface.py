"""
Creates, destroys, and prints user interface elements to the console.
"""

import os

class ConsoleUI:
    """
    Creates, destroys, and prints user interface objects to the console.
 
    Attributes:
        header (str): Text that will be displayed in the user interface's Header section (this should not change during runtime).
        title (str): Text that will be displayed in the user interface's Title section.
        body (str): Text that will be displayed in the user interface's Body section.
        
    Todo:
        * Write more descriptive class description.
    """
    
    UI_WIDTH = 200
    """int: Determines how wide (in characters) the console user interface is allowed to be."""

    HEADER_TEXT = 'Python Movie Database Manager'
    """str: The text to be displayed in the Header section of user interface."""
    
    def __init__(self, title, body):
        """
        Initializes new ConsoleUI object.

        Args:
            title (str, optional): Text to be displayed in the Title section of the user interface. Defaults to STARTUP_TITLE.
            body (str, optional): Text to be displayed in the Body section of the user interface. Defaults to STARTUP_BODY.
        """
        self.header = ConsoleUI.HEADER_TEXT
        self.title = title
        self.body = body
        
    def clear_screen(self):
        """Clears the console/terminal of all output."""
        # Check to see what operating system is being used and use appropriate clear command.
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
    def print_screen(self):
        """Prints out each section (Header, Title, Body, and Options menu) of the user interface to the console to create a screen for the user."""
        self.clear_screen()
        
        # Print Header section
        print('=' * ConsoleUI.UI_WIDTH)
        print(f'|{self.header:^{ConsoleUI.UI_WIDTH - 2}}|')
        print('=' * ConsoleUI.UI_WIDTH, '\n')
        
        # Print Title section
        print(f'{self.title:^{ConsoleUI.UI_WIDTH}}')
        print('-' * ConsoleUI.UI_WIDTH, '\n')
        
        # Print Body section
        print(f'{self.body}\n')
        
    def update_screen(self, new_title = None, new_body = None):
        """
        Changes title and body attributes to supplied strings (if supplied) and redraws the screen.
        
        Note: If you need to change the body text only, call this function with object_name.update_screen(new_body='New string here').
        
        Args:
            new_title (str, optional): _Description_: Text to change the object's title attribute to. Defaults to None (Null).
            new_body (str, optional): _Description_: Text to change the object's body attribute to. Defaults to None (Null).
        """
        if new_title is not None:
            self.title = new_title
        
        if new_body is not None:  
            self.body = new_body
        
        self.print_screen()
    
    # These fuctions are for collecting user data.
    def prompt_options_menu(self, *available_options):
        """
        Constructs an options menu from the arguments passed through to this function and prompts the user to select one of them.
        
        Args:
            available_options (tuple): _Description_: Tuple containing options to print out to console.
            
        Raises:
            ValueError: _Description_: Inappropriate argument value (of correct type).
            
        Returns:
            selected_option (int): _Description_: Integer containing the user's selected option
        """
        selected_option = 0
        
        print('Available Options:')
        
        for option in available_options:
            print(f'   {available_options.index(option) + 1}: {option}')
            
        print(f'\nPlease enter your choice (1 - {len(available_options)}):', end=' ')
        
        while True:
            try:
                selected_option = int(input())
                if selected_option < 1 or selected_option > len(available_options):
                    raise ValueError
                else:
                    return selected_option
                
            except ValueError:
                # TODO: selected_option always prints out 0 here for whatever reason. Fix this so it prints out the actual user's input.
                print(f'\'{selected_option}\' is not a valid option. A valid option would be a number between 1 and {len(available_options)}, corresponding to the option you would like to choose.')
                print(f'\nPlease enter your choice (1 - {len(available_options)}):', end = ' ')
                
            except:
                print(f'\nUnknown error occurred. Please try again.')
                print(f'\nPlease enter your choice (1 - {len(available_options)}):', end = ' ')
              
                
    def prompt_yes_or_no(self, question):
        """
        Constructs a yes-or-no prompt for the user to answer then collects the user's input.

        Args:
            question (str): _Description_: Question to ask the user.

        Returns:
            Returns True if the user answers "Yes", returns False if the user enters "No"
        """
        selected_option = input(f'{question} (Yes or No): ')
        
        while True:
            if selected_option == 'Yes' or selected_option == 'yes' or selected_option == 'Y' or selected_option == 'y':
                return True
            elif selected_option == 'No' or selected_option == 'no' or selected_option == 'N' or selected_option == 'n':
                return False
            else:
                print(f'\'{selected_option}\' is not a valid option. Please enter either \'Yes\' or \'No\' (\'Y\' and \'N\' are also acceptable).\n')
                selected_option = input(f'{question} (Yes or No): ')


    def prompt_ask_for_string(self, question, replace_blank = True):
        """
        Prompts the user to respond to a given question and returns that response in a string.

        Args:
            question (str): _Description_: Question to ask the user.
            replace_blank (bool, optional) _Description_: When set to True, if the user enters nothing for a prompt, the methods returns the string 'Unknown'

        Returns:
            Returns user's response to the prompt in the form of a string.
        """
        
        user_response = input(f'{question}: ')
        
        if replace_blank is True and len(user_response) == 0:
            return 'Unknown'
        else:
            return user_response
        
    
    
    def prompt_ask_for_number(self, question, get_float = False, replace_blank = True):
        """
        Prompts the user to enter a number, returns the user's selected number as either a float or an integer.
        
        Note: If you want to make sure the number the user enters is returned as a float, set get_float to True when calling this method.

        Args:
            question (str): _Description_: Question to ask the user.
            get_float (bool, optional): _Description_: When set to True, this method will attempt to return a float type instead of an integer. Defaults to False.
            replace_blank (bool, optional): _Description_: When set to True, if the user enters nothing the method will return 0. Defaults to True.
            
        Raises:
            ValueError: _Description_: Inappropriate argument value (of correct type).

        Returns:
            Returns user's response to the prompt in the form of either an integer or float depending on if get_float was set to True or False.
        """

        print(f'{question}:', end = ' ')
        
        while True:
            user_response = input()
            
            if replace_blank is True and len(user_response) == 0:
                if get_float:
                    return 0.0
                else:
                    return 0
            else:
                if get_float:
                    try:
                        float(user_response)
                        return user_response
                    except:
                        print('That is not a valid number. Please enter a number:', end = ' ')
                else:
                    try:
                        int(user_response)
                        return user_response
                    except:
                        print('That is not a valid whole number. Please enter a whole number (no decimals):', end = ' ')
    
    def prompt_enter_to_continue(self):
        """Halts application and prompts the user to press their Enter key to continue."""
        input('Press Enter to continue...')

# If this file is launched as as script, print an error message alerting the user to open the correct file.
if __name__ == '__main__':
    print('\nError: File launched as script!\nThe program does not launch from this file!\nPlease execute \'main.py\' in order to launch the Python Movie Database Manager.\n')