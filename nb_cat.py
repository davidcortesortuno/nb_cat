import nbformat


# -----------------------------------------------------------------------------

class tint:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

# -----------------------------------------------------------------------------

cell_type = {'code': tint.BLUE + '[C]:' + tint.END,
             'markdown': tint.GREEN + '[M]:' + tint.END}

with open('FeGe_parameters.ipynb') as nb_file:
    # File instance and notebook version:
    nb = nbformat.read(nb_file, 4)

for cell in nb['cells']:
    print('{:<6} {}'.format(cell_type[cell['cell_type']],
                            cell['source'].replace('\n',
                                                   '\n' + ' ' * 7)
                            ))
    # for source in cell['source'].split('\n'):
    #     print('     {}'.format(source))

    if cell['cell_type'] == 'code':
        print('[Out]: {}'.format(cell['outputs'])
              )

    print('-' * 80)
