"""
Implementation of Markov properties to create paintings based on
a selection of Suzan Frecon's paintings.

Dependencies: numpy, PIL
"""

from PIL import Image
import numpy as np

class Frekov:
    def __init__(self):
        """Simulates a painter that relies on a simple Markov chain.
            Args:
                transition_matrix (dict): list of shapes and their 
                    probabilites based on their respective paintings.
        """
        self.transition_matrix = {
            "a": {"a": 0.2, "b": 0.7, "c": 0.25, "d": 0.25, "e": 0.25, "f": 0.25},
            "b": {"a": 0.7, "b": 0.2, "c": 0.25, "d": 0.25, "e": 0.25, "f": 0.25},
            "c": {"a": 0.02, "b": 0.02, "c": 0.02, "d": 0.9, "e": 0.02, "f": 0.02},
            "d": {"a": 0.9, "b": 0.02, "c": 0.02, "d": 0, "e": 0.02, "f": 0.02},
            "e": {"a": 0.1, "b": 0.2, "c": 0.1, "d": 0.1, "e": 0.3, "f": 0.2},
            "f": {"a": 0.2, "b": 0.1, "c": 0.2, "d": 0.1, "e": 0.1, "f": 0.3}
        }
        self.shape_names = list(self.transition_matrix.keys())
    
    def create_components(self, current_shape="1", shape_count=3):
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
        
        print(*components, sep = ", ")

        return components

    def get_next_shape(self, current_shape):
        """Decides which shape to choose next based on the current shape. 
            Args:
                current_shape (str): current shape being added to painting.
            Returns:
                a string representing the next shape to add.
        """
        return np.random.choice(
            self.shape_names,
            p=[self.transition_matrix[current_shape][next_shape] \
            for next_shape in self.shape_names]
        )    

    def get_background(self):
        """Chooses random background for new painting based on a selection of 
            3 backgrounds from Frecon paintings. 
            
            Returns: 
                background (string): name of background file to call.
        """
        return f"background_{np.random.randint(1,3)}"

    def turn_to_shape(self, components):
        """Creates a list of shapes (Images) based on the following args:    
            Args:
                components (list): list of shapes (as integers) 
                    to use in painting.
        
            Returns:
                shapes (list): list of shapes (as Images) to use in painting. 
        """
        shapes = []
        for i in components:
            im = Image.open(f"{components[i-1]}.jpg")
            shapes.append(im)

        return shapes
    
    def make_painting(self, components):
        """Creates a collage consisting of the chosen background and given shapes.
            Args:
                shapes (list): list of shapes (as Images). 

            Returns:
                painting (Image): new painting with background and new shapes.
        """
        shape_data = self.turn_to_shape(components)
        painting = Image.new(self.get_background, (1400, 1725))
        height = painting.size
        thumbnail_height = height//len(shape_data)
        i = 0
        x = 0
        y = 0
        while i < len(shape_data):
            print(i, x, y)
            painting.paste(shape_data[i], (x,y))
            i += 1
            y += thumbnail_height
        painting.save("new-painting.jpg")


def main():
    painting_maker = Frekov()

    new_painting = painting_maker.create_components(current_shape="1", \
        shape_count=2)

    print("Making next painting....")
    print("Copying shapes to file...")
    painting_maker.make_painting(new_painting)
    print("Process complete!")

if __name__ == "__main__":
    main()