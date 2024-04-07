# Copyright (C) 2012-2014 NVIDIA Corporation.  All rights reserved.
#
# Copyright (C) 2023 hanai3Bi
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

gpu_dvfs_table = [
    [ 550000, 0 , 0 , 0 , 0 , 0 ],
    [ 550000, 0 , 0 , 0 , 0 , 0 ], 
    [ 550000, 0 , 0 , 0 , 0 , 0 ], 
    [ 550000, 0 , 0 , 0 , 0 , 0 ], 
    [ 550000, 0 , 0 , 0 , 0 , 0 ],  
    [ 550000, 0 , 0 , 0 , 0 , 0 ],  
    [ 550000, 0 , 0 , 0 , 0 , 0 ],
    [ 550000, 0 , 0 , 0 , 0 , 0 ], 
    [ 838712,  -7304, -552,  119,  -3750,   -2 ],  
    [ 880210,  -7955, -584,    0,  -2849,   39 ],  
    [ 926398,  -8892, -602,  -60,   -384,  -93 ], 
    [ 970060, -10108, -614, -179,   1508,  -13 ],     
    [ 1060665, -16075, -497, -179,   3213,    9 ],  
    [ 1117576, -16093, -648,    0,   1077,   40 ], 
    [ 1094475, -12688, -648,    0,   1077,   40 ], 
    [ 1124475, -12688, -648,    0,   1077,   40 ], 
    [ 1145060, -12688, -648,    0,   1077,   40 ],
    [ 1163644, -12688, -648,    0,   1077,   40 ]
]

gpu_freq_table = [76800, 153600, 230400, 307200, 384000, 460800, 537600, 614400, 691200, 768000, 844800, 921600, 998400, 1075200, 1152000, 1228800, 1267200, 1305600]

temp_list = [-25, 20, 30, 50, 70, 90]

def div_round_closest(value, scale):
    if value > 0:
        return ((value) + (scale / 2)) / scale
    else:
        return ((value) - (scale / 2)) / scale

def round5(number):
    return math.ceil(number / 5000) * 5000

def get_voltage(speedo, freq_index, temp_index):
    mv = div_round_closest(gpu_dvfs_table[freq_index][2] * speedo, 100)
    mv = div_round_closest((mv + gpu_dvfs_table[freq_index][1]) * speedo, 100) + gpu_dvfs_table[freq_index][0]

    mvt = div_round_closest(gpu_dvfs_table[freq_index][3] * speedo, 100) + gpu_dvfs_table[freq_index][4] + div_round_closest(
            gpu_dvfs_table[freq_index][5] * temp_list[temp_index], 10)
    mvt = div_round_closest(mvt * temp_list[temp_index], 10)

    final_volt = mv + mvt
    final_volt = round5(final_volt)
    final_volt /= 1000

    return int(final_volt)

speedo = int(input("Input GPU speedo: "))
warnings = []

if speedo >= 1800:
    print("This is for Mariko only, Erista users aren't allowed here.")
elif speedo <= 1400:
    print("Do you have a potato switch?")
else:
    print("GPU Frequency\tVoltage (mV)")
    print("----------------------------------")
    print("76.8-614.4 MHz  Use your vmin or 691.2 MHz voltage value.")
    for i, freq in enumerate(gpu_freq_table):
        if freq >= 691000: 
            voltage = get_voltage(speedo, i, 3) 
            if freq == 1228800 and voltage >= 800:
                warnings.append(f"Warning: Voltage for {freq / 1000} MHz can exceed PMIC limit!")
            elif freq == 1267200 and voltage >= 790:
                warnings.append(f"Warning: Voltage for {freq / 1000} MHz can exceed PMIC limit!")
            elif freq == 1305600 and voltage >= 780:
                warnings.append(f"Warning: Voltage for {freq / 1000} MHz can exceed PMIC limit!")
            print(f"{freq / 1000} MHz\t\t{voltage} mV")

for warning in warnings:
    print(warning)



