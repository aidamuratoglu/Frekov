# Frekov
 Frekov is an application of the Markov chain model to Suzan Frecon's paintings.

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


I would say this system is relatively creative. It's not as *innovative* as I'd like it to be,
but I think it's pretty novel. Looking back over my code, I realize how closely I followed
the markov_musician example Prof. Harmon offered for the class. Still, I think this code is
creative in its application of shapes and backgrounds - quite literally, the program creates
collages based on an existing artist's work. I also think the code is creative in the ways it
uses space. 

Sources: I used some posts on Stack Overflow, Kim Hancock talked through some of the earlier 
parts of the project with me, and I'd like to thank my roommates for putting up with me this week.