from knotprot_download import *


def run_download_loop(download_dir):
    proteins = get_proteins()
    i = 0
    for protein in proteins:
        i += 1
        download_link(download_dir, protein)
    print(f'Retrieved {i} files')


if __name__ == '__main__':
    download_dir = 'data_images'
    setup_download_dir(download_dir)

    #run_download_loop(download_dir)
    time_it(run_download_loop, download_dir)

