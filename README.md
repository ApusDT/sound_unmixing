# sound_unmixing

Few people are speaking at the same time and microphones have recorded voices. The aim of this code is to separate the voice and be able to obtain an audible data of their talks.

# Algorithm
The algorithm that has been used is Independent Component Analysis (ICA). The aim of ICA is to separate signals into additive components.
Its main assumptions are :
- mixed signals must be a linear combination of sources signal
- source signals are indepedent
- source signals are non-Gaussian

As a result of that, it is possible to approximate matrix `W` from the relation `X = WH` with X the mixed signal and H the source signals. W is the weight matrix, often present in Machine Learning algorithms.
 
# Jupyter Lab
An interactive computation has been created in a lab. Graphs bring us the ability to better visualize the extracted voices.

# Command Line
In order to separate input data, the following command can be used : `python unmix.py P output_folder input1.wav input2.wav ...`
with P an integer that is the number of people speaking simultaneously, the number of components.
The script outputs P files.
