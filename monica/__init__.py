from monica import version

# define the version before the other imports since these need it
__version__ = version.__version__

from monica.client import MonicaClient