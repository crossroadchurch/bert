# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=120 tabstop=4 softtabstop=4

###############################################################################
# Bert - Bert easily records talks                                            #
# --------------------------------------------------------------------------- #
# Copyright (c) 2015 NikuKatansa                                              #
# --------------------------------------------------------------------------- #
# This program is free software; you can redistribute it and/or modify it     #
# under the terms of the GNU General Public License as published by the Free  #
# Software Foundation; version 2 of the License.                              #
#                                                                             #
# This program is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for    #
# more details.                                                               #
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with this program; if not, write to the Free Software Foundation, Inc., 59  #
# Temple Place, Suite 330, Boston, MA 02111-1307 USA                          #
###############################################################################

import numpy, sys
import scipy.io.wavfile
import matplotlib.pyplot as plt

def normalise(in_file, out_file):
    rate, data = scipy.io.wavfile.read(in_file)
    normalise_factor = 32767/numpy.amax(abs(data))
    print("Normalise factor = " + str(normalise_factor))
    data_norm = numpy.asarray(data*normalise_factor, dtype=numpy.int16)
    scipy.io.wavfile.write(out_file, rate, data_norm)
    plt.plot(data[::4410])
    plt.plot(data_norm[::4410])
    plt.show()
    return

def compress(in_file, out_file):
    rate, data = scipy.io.wavfile.read(in_file)
    max_value = numpy.amax(abs(data))
    mean_value = numpy.mean(abs(data))
    std_dev_value = numpy.std(abs(data))
    median_value = numpy.median(abs(data))
    print("Max value = " + str(max_value))
    print("Mean = " + str(mean_value))
    print("Median = " + str(median_value))
    print("Std dev = " + str(std_dev_value))

    return


if len(sys.argv) > 1:
    if(sys.argv[1][-4:]) == ".wav":
        normalise(sys.argv[1], sys.argv[1][:-4] + '_normalised.wav')
        compress(sys.argv[1], sys.argv[1][:-4] + '_compressed.wav')
    else:
        print("Invalid file name")

else:
    print("Please enter the filename of the audio file to process as a command line argument")
