A backport of the zipfile module from Python 3.8, which contains notable improvements such as the "strict_timestamps" keyword argument (which enables the creation of reproducible zip archives).

installation::

    pip install zipfile38

usage:

.. code:: python

    if sys.version_info >= (3, 8):
        import zipfile
    else:
        import zipfile38 as zipfile


