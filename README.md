# Case study: Contributing to an Open Source project

## Make the two badges green / show 100%

[![Build Status](https://travis-ci.org/paris-swc/2016-03-29-testing-exercise.svg?branch=master)](https://travis-ci.org/paris-swc/2016-03-29-testing-exercise)
[![Coverage Status](https://coveralls.io/repos/github/paris-swc/2016-03-29-testing-exercise/badge.svg?branch=master)](https://coveralls.io/github/paris-swc/2016-03-29-testing-exercise?branch=master)

## Getting started

* Fork this github repository to your own user account on github
* Clone the repository from your own fork so that you can work on it on your
  computer.
* Login to [Travis CI](https://travis-ci.org) with your GitHub account and activate (your fork of) this repo for testing.
* Login to [Coveralls](https://coveralls.io) with your GitHub account and activate (your fork of) this repo for code coverage analysis.
* Edit this README file and replace all mentions of `paris-swc` in the links with your user name.

## Improve the code
* Implement missing functions to make the unit tests pass (run tests either locally or let Travis run them for you each time you push changes).
* Increase the test coverage to 100% by making [all lines](https://coveralls.io/github/paris-swc/2016-03-29-testing-exercise?branch=master) green.

### How to run the tests locally
To run the test on your machine, use the [pytest](http://pytest.org) package (should already come pre-installed with Anaconda).

In the directory where you cloned the repository, run:
```Python
py.test -v preprocess.py
```

