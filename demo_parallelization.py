from functools import partial
from multiprocessing import Pool

from knotprot_download import *


def run_download_loop(download_dir):
    proteins = get_proteins()
    i = 0
    for protein in proteins:
        i += 1
        download_link(download_dir, protein)
    print(f'Retrieved {i} files')

def run_download_parallel(download_dir):
    proteins = get_proteins()
    download_func = partial(download_link, download_dir)
    with Pool(processes=16) as pool:
        pool.map(download_func, proteins)

def run_thumbnails_loop(my_dir):
    file_list = Path(my_dir).rglob('*.png')
    for file in file_list:
        create_thumbnail((512, 512), file)

def run_thumbnails_parallel(my_dir):
    file_list = Path(my_dir).rglob('*.png')
    create_thumbnails_func = partial(create_thumbnail, (512, 512))
    with Pool(processes=8) as pool:
        pool.map(create_thumbnails_func, file_list)


if __name__ == '__main__':
    download_dir = 'data_images'
    setup_download_dir(download_dir)
    #run_download_loop(download_dir)
    #time_it(run_download_loop, download_dir)    # 139s
    #time_it(run_download_parallel, download_dir) # 39s 4 processes
    time_it(run_download_parallel, download_dir) # 19s
    #time_it(run_thumbnails_loop, download_dir)
    time_it(run_thumbnails_parallel, download_dir)

