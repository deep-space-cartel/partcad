Development
###########

===========
Environment
===========

VS Code
-------

1. Run ``python.createEnvironment`` command.
   - Select only ``./requirements.txt`` to install all dependencies for docs
   , ``partcad`` & ``partcad-cli``


=============
Documentation
=============

Doc could be rendered and served on changes in `./docs` dir:

.. code-block:: bash

  cd docs
  sphinx-autobuild --host 0.0.0.0 --open-browser -b html "source" "build"

- ``--host 0.0.0.0`` is required in case if you running `sphinx-autobuild` in
  Dev Containers and accessing HTML using host browser. Docs will be served on
  http://127.0.0.1:8000/

There is also `sphinx-serve` Python module which also could be used for similar
functionality.

=======
Testing
=======

* https://download.virtualbox.org/virtualbox/7.0.22/VirtualBox-7.0.22-165102-Win.exe
* https://developer.hashicorp.com/vagrant/install?product_intent=vagrant

=========
Profiling
=========

cProfile
--------

You can use ``cProfile`` & ``snakeviz`` to profile CLI application, for example:

.. code-block:: bash

  python -m cProfile -o pc-version.prof $(command -v pc) version
  snakeviz pc-version.prof

yappi
-----

.. code-block:: bash

  python -m yappi -f callgrind --output-file=pc-version.callgrind $(command -v pc) version
  gprof2dot -f callgrind -s pc-version.callgrind > pc-version.dot
  dot -Tpng pc-version.dot -o pc-version.png


flameprof
---------

.. code-block:: bash

  flameprof -o /tmp/pc-version.svg -r $(command -v pc) version
