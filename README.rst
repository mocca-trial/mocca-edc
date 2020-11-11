|pypi| |travis| |codecov| |downloads| |pyup|



mocca-edc
---------


Liverpool School of Tropical Medicine


http://www.isrctn.com/


See also https://github.com/clinicedc/edc



Installation
------------

To setup and run a test server locally

You'll need mysql. Create the database

.. code-block:: bash

  mysql -Bse 'create database mocca character set utf8;'


Create a virtualenv, clone the main repo and checkout master

.. code-block:: bash

  conda create -n edc python=3.8
  conda activate edc


Clone the main repo and checkout master

.. code-block:: bash

  mkdir ~/app
  cd app
  https://github.com/mocca-trial/mocca-edc.git
  cd ~/app/mocca-edc
  git checkout master


Copy the test environment file

.. code-block:: bash

  cd ~/app/mocca-edc
  git checkout master
  cp .env.tests .env


Edit the environment file (.env) to include your mysql password in the ``DATABASE_URL``.

.. code-block:: bash

  # look for and update this line
  DATABASE_URL=mysql://user:password@127.0.0.1:3306/inte


Continue with the installation

.. code-block:: bash

  cd ~/app/mocca-edc
  git checkout master
  pip install .
  pip install -U -r requirements
  python manage.py migrate
  python manage.py import_randomization_list
  python manage.py import_holidays


Create a user and start up `runserver`

.. code-block:: bash

  cd ~/app/mocca-edc
  git checkout master
  python manage.py createsuperuser
  python manage.py runserver


Login::

  localhost:8000



.. |pypi| image:: https://img.shields.io/pypi/v/mocca-edc.svg
    :target: https://pypi.python.org/pypi/mocca-edc

.. |travis| image:: https://travis-ci.com/mocca-trial/mocca-edc.svg?branch=develop
    :target: https://travis-ci.com/mocca-trial/mocca-edc

.. |codecov| image:: https://codecov.io/gh/mocca-trial/mocca-edc/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/mocca-trial/mocca-edc

.. |downloads| image:: https://pepy.tech/badge/mocca-edc
   :target: https://pepy.tech/project/mocca-edc

.. |pyup| image:: https://pyup.io/repos/github/mocca-trial/mocca-edc/shield.svg
    :target: https://pyup.io/repos/github/mocca-trial/mocca-edc/
    :alt: Updates
