# nb_cat

Print Jupyter notebooks on a terminal. We provide a `setup.py` file to
install the package using `pip`, which adds an executable to your
`../bin/` folder and call this script using `nb_cat FILE`.

If we execute the test notebook:

```
@: nb_cat test_nb.ipynb

--------------------------------------------------------------------------------

[M]:   # Test notebook


--------------------------------------------------------------------------------

[C]:   # Import some libraries
       import numpy as np


--------------------------------------------------------------------------------

[C]:   np.arange(7)

[Out]: array([0, 1, 2, 3, 4, 5, 6])

--------------------------------------------------------------------------------

...

```

## TODO:

* Convert LaTeX strings to unicode using:
  https://github.com/phfaist/pylatexenc/blob/master/pylatexenc/latex2text.py
  That repo needs to be updated to be compatible with Python 3

* Check for Matplotlib Figures or Images
