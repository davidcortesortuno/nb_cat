import nbformat
import argparse

parser = argparse.ArgumentParser(description='nb_cat')

parser.add_argument('nb_file', help='IPython notebook file')

# Parser arguments
args = parser.parse_args()


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

# Labels for the cell type
CELL_TYPE = {'code': tint.BLUE + '[C]:' + tint.END,
             'markdown': tint.GREEN + '[M]:' + tint.END}

# Outputs in red
OUT = tint.RED + '[Out]:' + tint.END

with open(args.nb_file) as nb_file:
    # File instance and notebook version:
    nb = nbformat.read(nb_file, 4)

print('-' * 80 + '\n')
for cell in nb['cells']:
    # New lines are formatted to be aligned with the first outputs line which
    # contains the output label (we just add a number of empty characters)
    cell_input = cell['source'].replace('\n', '\n' + ' ' * 7)
    print('{:<15} {}\n'.format(CELL_TYPE[cell['cell_type']],
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
            print('{} {}'.format(OUT, cout['data']['text/plain']))

        elif cout['output_type'] == 'stream':
            txt = cout['text'].replace('\n', '\n' + ' ' * 7)
            print('{} {}'.format(OUT, txt))

    print('\n' + '-' * 80 + '\n')
