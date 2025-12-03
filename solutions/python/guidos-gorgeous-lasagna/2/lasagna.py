"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 10



def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
        
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of layers lasagna will have.
    :return: int - preperation time for all layers in minutes.

    Function that takes the numbers of layers to add to the lasagna as
    an argument and returns preparation time for all layers.
    """
    return 2 * number_of_layers
    


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate elapsed time in minutes or minutes spent in the kitchen cooking lasagna.

    :param number_of_layers: int - number of layers.
    :param elapsed_bake_time: int - number of minutes the lasgna has spent baking in oven already.
    :return: int - preparation time for all layers in minutes.

    Function that takes the numbers of layers to add to the lasagna
    and elapsed time baking as arguments and returns total minutes spend in the kitchen cooking.
    """ 
    
    return  (2 * number_of_layers) + elapsed_bake_time