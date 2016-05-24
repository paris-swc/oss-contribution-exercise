# Case study: Contributing to an Open Source project

## Make the badge green

[![Build Status](https://travis-ci.org/paris-swc/oss-contribution-exercise.svg?branch=master)](https://travis-ci.org/paris-swc/oss-contribution-exercise)

## Getting started

* Fork this github repository to your own user account on github
* Clone the repository from your own fork so that you can work on it on your
  computer.
* Login to [Travis CI](https://travis-ci.org) with your GitHub account and activate (your fork of) this repo for testing.
### Optional
  * Edit this README file and replace all mentions of `paris-swc` in the link above with your user name.
  * **Note:** changing the README file in this way is not something you'd do in a real project -- you do not want to include such a modification in the changes you contribute back to a project!


## Improve the code
* Implement missing functions to make the unit tests pass (run tests either locally or let Travis run them for you each time you push changes).

### How to run the tests locally
To run the test on your machine, use the [pytest](http://pytest.org) package (should already come pre-installed with Anaconda).

In the directory where you cloned the repository, run:
```
$ py.test
```
