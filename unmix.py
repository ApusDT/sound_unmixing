import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
from scipy.io import wavfile


# Function to read and create matrix of computable data
# Input :
# - file_list : the list of input files
# Output :
# - the sound rate
# - the matrix of data
def prepare_data(file_list):
    data_list = list()
    for i in range(len(file_list)):
        rate,data = wavfile.read(file_list[i])
        data_list.append(data)
    return rate,np.c_[data_list].T

# Function to apply ICA algorithm on data
# Input :
# - data : the matrix of mixed sounds
# - components : the number of different sources of sounds
# Output :
# - matrix of unmixed sounds
def unmix_data(data,components):
    ica = FastICA(n_components=components)
    S_ = ica.fit_transform(data)
    return S_

# Function to write sound files from matrix of data
# Input :
# - data : the matrix of sounds
# - sound_rate : the rate of the sounds
# - folder : the output folder where the files will be saved
def write_data(data,sound_rate,folder):
    data_list = data.tolist()
    for col in range(data.shape[1]):
        out = list(map(lambda x: x[col],data_list))
        wavfile.write("{}/output{}.wav".format(folder,col),sound_rate, np.array(out))

# Main function
def main():
    sound_rate, sound_mat = prepare_data(input_files)
    unmix_mat = unmix_data(sound_mat,components)
    write_data(unmix_mat,sound_rate,output_folder)


if __name__ == "__main__":
    components = int(sys.argv[1])
    output_folder = sys.argv[2]
    input_files = [sys.argv[3+i] for i in range(len(sys.argv[3:]))]
    main()