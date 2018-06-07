sparklanes
==========

[![PyPI version](https://badge.fury.io/py/sparklanes.svg)](https://badge.fury.io/py/sparklanes) [![Build Status](https://travis-ci.org/ksbg/pyspark-etl.svg?branch=example)](https://travis-ci.org/ksbg/pyspark-etl?branch=example) [![Coverage Status](https://coveralls.io/repos/github/ksbg/pyspark-etl/badge.svg?branch=example)](https://coveralls.io/github/ksbg/pyspark-etl?branch=example) ![pylint Score](https://mperlet.github.io/pybadge/badges/9.92.svg) [![Doc status](https://sparklanes.readthedocs.io/en/latest/?badge=latest)](https://sparklanes.readthedocs.io)

sparklanes is a lightweight data processing framework for Apache Spark
written in Python. It was built with the intention to make building
complex spark processing pipelines simpler, by shifting the focus
towards writing data processing code without having to spent much time
on the surrounding application architecture.

Data processing pipelines, or *lanes*, are built by stringing together
encapsulated processor classes, which allows creation of lane definitions
with an arbitrary processor order, where processors can be easily
removed, added or swapped.

Processing pipelines can be defined using *lane configuration YAML files*,
to then be packaged and submitted to spark using a single command.
Alternatively, the same can be achieved manually by using the framework's
API.

Documentation
-------------

Find the documentation on [sparklanes.readthedocs.io](https://sparklanes.readthedocs.io).

Also check out the [example Jupyter notebook](example/iris_example.ipynb).
