# Frekov
 Frekov is an application of the Markov chain model to Suzan Frecon's paintings.

To set up and run the code, you can manually choose a background color from the lists of
background colors at the top of the file. Currently, the program is hard-coded with 
background_1, a beautiful deep blue color. If you'd like to choose a different background
color, refer to the backgrounds in assets - these file names align with the dictionary
keys in BACKGROUND_COLORS. Copy and paste the three integers into line 89, where you
currently see three integers (these are the RGB values for the newly generated background).
Once you've chosen your background colors, feel free to adjust the "current_shape" 
and "shape_count" variables in main - these refer to the number of shapes the program will 
choose to "paint" onto the background and the shape the Markov chain will start on. Lastly,
depending on your IDE, move the image files from "assets" into a folder the IDE can read.
Once you've chosen these parameters and set thim into place, run the code and create a 
Frekov painting!

I have loved Suzan Frecon's paintings for a while now. A Brooklyn Rail interview with
her starts with this Julia Kristeva quote from *Giotto's Joy*: "How can we find our way 
through what separates words from what is both without a name and more than a name: 
a painting? What is it that we are trying to go through? The space of the very act of naming?"
I find it personally meaningful in the context of this project, as well. Parsing Frecon's
paintings into backgrounds and shapes, assigning letters to them, and manipulating them
at will has added another level to Kristeva's initial inquiry. How can we find our way
through what separates strings from reality? On a more immediate level, what does it mean
to assign letters--totally changing the naming structure and its implicit meaning--to shapes?
Does it take away from their power as objects that exist within the built world of a painting?
Frecon is known for her expansive color palette, large canvas size, and her many repeating
shapes. When I first learned about this project, my mind immediately jumped to her work. How
could I create a program inspired by her paintings, these somewhat iterative, gorgeous works
of art? 

This project has been very challenging and quite rewarding. I have learned a *lot* of 
python in a relatively short period of time (about a week), reverse engineered a program,
and spent many hours debugging. Most importantly, I have spent many hours thinking about what
computional creativity looks like. I learned about ints, tuples, dictionaries, debugged a lot,
learned about docstring and other python style guides. I pushed myself outside my comfort zone
by taking on a project that was much more intense than I was expecting. 

For a future project, I would like to create a program that generates titles for these
new Frekov images. For instance, frecon-1 (in assets) is called "mars indigo." I would also
like to work on creating a program that generates its own transition matrix (rather than a
hard-coded one). I would also like to figure out a way to take out the white space around the 
shapes, use random to create f-strings that call different backgrounds (listed in assets as
background_1.jpg, etc.). It would look something like this: f"background_{random.randint(1,3)}". 
I think I can do this with treating the global variables of background colors as tuples. For a
future day!
