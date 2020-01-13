|pypi|

A backport of the zipfile module from Python 3.8, which contains notable improvements such as the "strict_timestamps" keyword argument (which enables the creation of reproducible zip archives).

installation::

    pip install zipfile38

usage:

.. code:: python

    if sys.version_info >= (3, 8):
        import zipfile
    else:
        import zipfile38 as zipfile

---

shout out to `Thomas Kluyver's backport for 3.6 <https://gitlab.com/takluyver/zipfile36>`_ and `Markus Scheidgen's backport for 3.7 <https://github.com/markus1978/zipfile37>`_.

.. |pypi| image:: https://img.shields.io/pypi/v/zipfile38.svg
   :target: https://pypi.org/project/zipfile38/
