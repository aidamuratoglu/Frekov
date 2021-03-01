"""
Implementation of Markov properties to create paintings based on
a selection of Suzan Frecon's paintings.

Dependencies: numpy, PIL
"""

from PIL import Image
import numpy as np

# Potential colors to hard-code into line 89 to change background color.
# Colors derived from running a getpixel() command on input backgrounds.
BACKGROUND_COLORS = {
    "background_1": (10, 84, 119),
    "background_2": (58, 41, 59),
    "background_3": (94, 45, 40)
}

class Frekov:
    def __init__(self, transition_matrix):
        """Simulates a painter that relies on a simple Markov chain.
            Args:
                transition_matrix (dict): list of shapes and their 
                    probabilites based on their respective paintings.
        """
        self.transition_matrix = transition_matrix
        self.shape_names = list(self.transition_matrix.keys())
    
    def create_components(self, current_shape="a", shape_count=3):
        """Generates a list of shapes to be added to a painting.  
            Args:
                current_shape (str): current shape being added to painting.
                
                shape_count (int): how many shapes to include.

            Returns:
                components (list): list of shapes as strings.
        """
        components = []

        while len(components) < shape_count:
            next_shape = self.get_next_shape(current_shape)
            components.append(next_shape)
            current_shape = next_shape
        
        return components

    def get_next_shape(self, current_shape):
        """Decides which shape to choose next based on the current shape. 
            Args:
                current_shape (str): current shape being added to painting.
            Returns:
                a string representing the next shape to add.
        """
        probabilities = []
        
        for next_shape in self.shape_names:
            probabilities.append(self.transition_matrix[current_shape][next_shape])
               
        return np.random.choice(
            self.shape_names, p=probabilities
        )

    def turn_to_shape(self, components):
        """Creates a list of shapes (Images) based on the following args:    
            Args:
                components (list): list of shapes (as integers) 
                    to use in painting.
        
            Returns:
                shapes (list): list of shapes (as Images) to use in painting. 
        """
        shapes = []

        for shape in components:
            im = Image.open(f"{shape}.jpg")
            shapes.append(im)

        return shapes
    
    def make_painting(self, components):
        """Creates a collage consisting of a background and given shapes.
            Args:
                shapes (list): list of shapes (as Images). 

            Returns:
                painting (Image): new painting with background and new shapes.
        """
        shape_data = self.turn_to_shape(components)
        painting = Image.new("RGB", (1600, 1925), (58, 41, 59))
        height, width = painting.size
        print("height: ", height)
        int(height)
        thumbnail_height = int(height)//len(shape_data)
        i = 0
        x = 0
        y = 0
        while i < len(shape_data):
            painting.paste(shape_data[i], (x,y))
            i += 1
            x += 1
            y += thumbnail_height
        painting.save("new-painting.jpg")


def main():
    painting_maker = Frekov({
        "a": {"a": 0.2, "b": 0.7, "c": 0.025, "d": 0.025, "e": 0.025, "f": 0.025},
        "b": {"a": 0.7, "b": 0.2, "c": 0.025, "d": 0.025, "e": 0.025, "f": 0.025},
        "c": {"a": 0.02, "b": 0.02, "c": 0.02, "d": 0.9, "e": 0.02, "f": 0.02},
        "d": {"a": 0.9, "b": 0.02, "c": 0.02, "d": 0.02, "e": 0.02, "f": 0.02},
        "e": {"a": 0.1, "b": 0.2, "c": 0.1, "d": 0.1, "e": 0.3, "f": 0.2},
        "f": {"a": 0.2, "b": 0.1, "c": 0.2, "d": 0.1, "e": 0.1, "f": 0.3}
    })

    new_painting = painting_maker.create_components(current_shape="d", \
        shape_count=2)

    print("Making next painting....")
    print("Copying shapes to file...")
    painting_maker.make_painting(new_painting)
    print("Process complete!")

if __name__ == "__main__":
    main()