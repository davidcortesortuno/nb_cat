import nbformat

cell_type = {'code': 'C', 'markdown': 'M'}

with open('FeGe_parameters.ipynb') as nb_file:
    # File instance and notebook version:
    nb = nbformat.read(nb_file, 4)

for cell in nb['cells'][:2]:
    print('{:<5}: {}'.format(cell_type[cell['cell_type']],
                             cell['source'] ))
    # for source in cell['source'].split('\n'):
    #     print('     {}'.format(source))

    if cell['cell_type'] == 'code':
        print('[Out]: {}'.format(cell['outputs'])
              )

    print('-' * 80)
