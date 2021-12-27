import numpy as np

def select_screen():
    """
    'Function is to be called by listener and it is the first function in the chain
    of the process of painting over an image. It should give the user the possibility to
    select a part of the screen and return the coordinates of the rectangle
    of the wanted part of the screen.'
    :input: None
    :return: tuple(int, int), tuple(int, int) parameters of the top left and bottom right vertices
    of the screen parts
    """
    return None

def take_ss(top_left: tuple, bottom_right: tuple) -> np.ndarray:
    """
    :param top_left: tuple of XY coordinates of the top left vertex of the ss rectangle
    :param bottom_right: tuple of XY coordinates of the bottom right vertex of the ss rectangle
    :return: np.ndarray containing the screenshot image
    """
    return None