import pandas as pd
import os
import regex

Path = r"../Ilhup/"

def get_files_in_folder(folder_path, suffix = None):
    """
    Returns a list of the files that end with the specified suffix.
    :param folder_path: 
    :param suffix: 
    :return: list of files
    """
    list_of_files = []
    for file in folder_path:

    return list_of_files

def execute_script_on_df(df, script):
    """

    :param df:
    :param script:
    :return:
    """


import os



def print_directory_structure(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


if __name__ == '__main__':
    print_directory_structure(Path)
