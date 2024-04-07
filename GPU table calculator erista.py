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

cvb_coeff = [814294, 856185, 898077, 939968, 981860, 1023751, 1065642, 1107534, 1149425, 1191317, 1233208, 1275100, 1316991]
gpu_freq_table = [76800, 153600, 230400, 307200, 384000, 460800, 537600, 614400, 691200, 768000, 844800, 921600, 998400]

def round_closest(value, scale):
    if value > 0:
        return ((value + (scale / 2)) / scale)
    else:
        return ((value - (scale / 2)) / scale)

def round5(number):
    return int(round(number / 5.0)) * 5

speedo = int(input("Enter gpu speedo: ")) 

offset = 40 if speedo <= 2060 else 60

for i in range(13):
    cvb_coeff[i] -= offset * 1000

if speedo < 1900:
    print("This is for Erista only, Mariko users aren't allowed here.")
elif speedo > 2200:
    print("How did this SoC end up in a switch?")
else:
    print("\nFrequency (MHz)\tVoltage (mV)")
    for entry in range(13):
        freq_MHz = float(gpu_freq_table[entry] / 1000)

        mv = round_closest(-940 * speedo, 100)
        mv = round_closest((mv + 8144) * speedo, 100) + cvb_coeff[entry]

        temp = 50  

        mvt = round_closest(808 * speedo, 100) + -21583 + round_closest(226 * temp, 10)
        mvt = round_closest(mvt * temp, 10)
        final_volt = math.ceil((mv + mvt) / 1000)
        vmin = 750 if freq_MHz <= 537 else 780 if freq_MHz == 614 else 800 if freq_MHz == 691 else 830 if freq_MHz == 768 else 855 if freq_MHz == 844 else 880 if freq_MHz == 921 else 915 if freq_MHz == 998 else 812
        final_volt = max(final_volt, vmin)
        final_volt = round5(final_volt)
        
        if freq_MHz == 691.2:
            print(f"76.8-691.2 MHz\t{final_volt} mV")
        elif freq_MHz > 691.2:
            print(f"{freq_MHz} MHz\t{final_volt} mV")
