''' This module provides functions for creating a series of project folders.
    More specifically, this module contains functions that will 
    create folders in the working directory in four ways:
        -range of years
        -from a list of names(also will modify the name by removing white spaces and captitals)
        -with a standard prefix
        -create a folder every few seconds
 '''

#####################################
# Import Modules at the Top
#####################################

# Import modules from standard library
import pathlib 
import time



#import local utilities module that creates a byline
import utils_garrett 

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()


#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    for year in range(start_year, end_year + 1 ):
        year_path=project_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)

  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Creates a series of folders from a list

    Argument needed: folder_list - list of folders to create
                     optional: to_lowercase, default is false - makes names of folders lowercase
                     optional: remove_spaces, default is false - removes whitespaces from name of folder
    '''
    print(f"FUNCTION CALLED: create_folders_from_list {folder_list}")

    #iterate through list of folders, creating a directory for each one
    for folder in folder_list:
        #make folder list lower case if True
        if to_lowercase == True:
            folder = folder.lower()

        # replace whitespace in folder list elements if remove_space is True
        if remove_spaces == True:
            folder = folder.replace(" ", "")

        #save the folder to the correct path
        folder_path=project_path.joinpath(str(folder))
        folder_path.mkdir(exist_ok=True)


  
#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    '''
    Create folders with a designated prefix.
    
    Arguments:
    folder_list - list of folders that need prefix added
    prefix - string to be appended in front of folder name
    '''

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_prefixed_folders with prefix: {prefix} and folder_list={folder_list}")

    for folder in folder_list:
        folder_path=project_path.joinpath(prefix + folder)
        folder_path.mkdir(exist_ok=True)

  

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int, number_of_folders: int ) -> None:
    '''
    Create folders periodically.
    
    Arguments:
    duration_seconds - how often to create a folder
    number_of_folders - set the upper limit of folders created
    '''
    
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folder_periodically duration_seconds{duration_seconds}")
    
    #intialize the folder 
    folder_counter = 1

    #loop continously to create folders, until program is stopped
    while folder_counter >= 1:
        
        #indicate the function is running
        print(f"Will save folder {folder_counter} in {duration_seconds} seconds, press ctrl + C to quit")

        #wait duration_seconds
        time.sleep(duration_seconds)
        
        #save the folder
        folder_path=project_path.joinpath(str(folder_counter))
        folder_path.mkdir(exist_ok=True)
        
        #increment the counter
        folder_counter += 1

        #stop loop for running forever
        if folder_counter > number_of_folders:
            break
        


  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {utils_garrett.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    number_of_folders: int = 4 #number of folders that will be created
    create_folders_periodically(duration_secs, number_of_folders)


    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

