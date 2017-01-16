import nbformat

# -----------------------------------------------------------------------------


# Terminal colours
class tint:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# -----------------------------------------------------------------------------


class NbCat(object):

    def __init__(self, nb_file):
        # Labels for the cell type
        self.CELL_TYPE = {'code': tint.BLUE + '[C]:' + tint.END,
                          'markdown': tint.GREEN + '[M]:' + tint.END}

        # Outputs in red
        self.OUT = tint.RED + '[Out]:' + tint.END

        with open(nb_file) as _file:
            # File instance and notebook version:
            self.nb = nbformat.read(_file, 4)

    def print_notebook(self):

        print('-' * 80 + '\n')

        for cell in self.nb['cells']:

            # New lines are formatted to be aligned with the first outputs line
            # which contains the output label (we just add a number of empty
            # characters)
            cell_input = cell['source'].replace('\n', '\n' + ' ' * 7)
            print('{:<15} {}\n'.format(self.CELL_TYPE[cell['cell_type']],
                                       cell_input))

            # For code cells we check the output type and print accoding to it
            # (we still need to check for Figures)
            if cell['cell_type'] == 'code':
                if cell['outputs']:
                    cout = cell['outputs'][0]
                else:
                    print('\n' + '-' * 80 + '\n')
                    continue

                if cout['output_type'] == 'execute_result':
                    print('{} {}'.format(self.OUT, cout['data']['text/plain']))

                elif cout['output_type'] == 'stream':
                    txt = cout['text'].replace('\n', '\n' + ' ' * 7)
                    print('{} {}'.format(self.OUT, txt))

            print('\n' + '-' * 80 + '\n')
