import os
import SMArt
from SMArt.md import pipeline
from SMArt.md.gromacs.io.ana import read_xvg_data
from SMArt.md.data_st import MD_Parameters
import numpy as np
import subprocess
import argparse


def read_data(fd):
    for i in np.arange(0,1.05,0.05):
        data = read_xvg_data(fd + '/FE_MD_{i:.3f}.xvg'.format(i=i))
        return check_data(data)

def check_data(data):
    for xvg_file in data:
        if data[0][0] == 0.000 and data[-1][0] == 5000.00:
            return FE_ana()
            print('Run complete')
            return
        else:
            print('Missing xvg files')
            return
        
def FE_ana():
    parent_dir = fd
    path = os.path.join(parent_dir)
    os.chdir(path)
    process = subprocess.Popen('gmx bar -f ./FE_MD_*.xvg -o -oi > output_analysis.txt', shell=True, stdout=subprocess.PIPE)
    process.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input target folder')
    parser.add_argument('-d', '--fd', dest='fd', help='target folder', type=str, required=True)
    args = parser.parse_args()
        
    fd = args.fd.strip()
    fd = os.path.abspath(fd) + '/'
    
    read_data(fd)
    