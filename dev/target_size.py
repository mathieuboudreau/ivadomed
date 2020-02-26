##############################################################
#
# This scripts compute the distribution of lesion size,
# in vox and in mm3.
#
# Could work with tumour or SC etc.
#
# It filters using "target_suffix" and "contrast_test"
# from config file.
#
# Usage: python dev/target_size.py -c <config_file_path>
#
# Example: python dev/target_size.py -c config/config.json
#
##############################################################

import os
import json
import argparse
import numpy as np
import nibabel as nib
import seaborn as sns
import matplotlib.pyplot as plt

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="Config file path.")

    return parser


def print_stats(arr):
    print('\tMean: {}'.format(np.mean(arr)))
    print('\tMedian: {}'.format(np.median(arr)))
    print('\tInter-quartile range: [{}, {}]'.format(np.percentile(arr, 25), np.percentile(arr, 75)))


def plot_distrib(arr, label, fname_out):
    fig = plt.figure()

    sns.distplot(arr, hist=False, kde=True, rug=True,
                 color = 'darkblue',
                 kde_kws={'linewidth': 3},
                 rug_kws={'color': 'black'})

    plt.xlabel(label)
    plt.ylabel('Density')
    fig.savefig(fname_out)
    print('\tSave as: '+fname_out)

def run_main(args):

    with open(args.c, "r") as fhandle:
        context = json.load(fhandle)

    path_folder = os.path.join(context['bids_path'], 'derivatives', 'labels')

    vox_lst, mm3_lst = [], []
    for s in os.listdir(path_folder):
        s_fold = os.path.join(path_folder, s, 'anat')
        if os.path.isdir(s_fold):
            for f in os.listdir(s_fold):
                c = f.split(s+'_')[-1].split(context["target_suffix"])[0]
                if f.endswith(context["target_suffix"]+'.nii.gz') and c in context["contrast_test"]:
                    f_path = os.path.join(s_fold, f)
                    im = nib.load(f_path)
                    data = im.get_data()
                    px, py, pz = im.header['pixdim'][1:4]
                    del im

                    if np.any(data):
                        n_vox = np.count_nonzero(data)
                        vox_lst.append(n_vox)
                        mm3_lst.append(n_vox * px * py * pz)

    print('\nTarget distribution in vox:')
    print_stats(vox_lst)
    plot_distrib(vox_lst, context["target_suffix"]+' size in vox',
                     context["target_suffix"]+'_vox.png')

    print('\nTarget distribution in mm3:')
    print_stats(mm3_lst)
    plot_distrib(mm3_lst, context["target_suffix"]+' size in mm3',
                     context["target_suffix"]+'_mm3.png')

if __name__ == '__main__':
    parser = get_parser()
    arguments = parser.parse_args()
    run_main(arguments)
