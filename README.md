# RoboSub transducers_framework 2018
<B>Overview</B>
This framework connects any transducer (in our case pressure transducer) to a raspberry pi. The program is able to convert the voltage output into pressure using the relationship between voltage and pressure obtained from a calibration curve. The goal of this framework is connect any type of pressure transducer up to three and output pressure from all of them at once. 

<B>Calibration curve</B> 
The calibration curve for any pressure transducer will need to be calculated before the framework can output pressure. Use the Ideal gas law to calculate the calibration curve. https://en.wikipedia.org/wiki/Ideal_gas_law

<B>Adding new components</B>
All transducers that have been added thus far extend the global variables and functions from the parent class transducer.py. This style should be implemented into all added transducers.





<B>NOTE</B>:  You will need to install the doxygen and graphviz packages in order to run doxygen and generate the outputs.  You can do so with the following command on linux (windows users can blow me):

-  sudo apt-get install doxygen graphviz

Then cd into the doc directory and run the following:
  
-  doxygen config.dox

After the command runs, there will be an html/ directory.  Open html/index.html in your favorite web browser.

In general use case, the documentation does <I>not</I> get checked into the repository.  The idea being that code is changing so quickly, that if someone wants up to date documentation then they can download the repository themselves and run doxygen to generate the docs.

# Thanks. Your robot overlord, Bender.
