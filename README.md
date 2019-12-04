[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/signetlabdei/sem-example/master?filepath=Analysis.ipynb)

# What is this repository? #

This repository contains an example of how you can use
[SEM](https://github.com/signetlabdei/sem) to run your `ns-3` simulations,
analyze the results, and share them with the community.

Keep reading for an overview of the contents of this example repository, and
clone the repo to follow along and experiment by yourself:

```shell
git clone --recurse-submodules https://github.com/signetlabdei/sem-example
```

# The SEM workflow #

---

**NOTE**

This section describes the contents of this repo. If you want a step-by-step
guide on how to initialize your own SEM project, follow [this
section](#Kickstarting-your-own-ns-3-simulation-campaign).

---

The file structure you see in this repo is meant to provide a reference on how
to structure your SEM projects, and explain its components before you go on and
create your own. What you see here is very similar to what you can expect to end
up with when analyzing your very own ns-3 simulations using SEM: an ns-3
installation in the `ns-3` folder, a `results` folder containing the outcomes of
the simulations you ran through SEM, a set of tools to inspect what your
simulation is doing in the `visualization` folder, a script to obtain and plot
some results called `analysis.py`, and a report showing the results of your
analysis in the `report` folder.

## The ns-3 submodule ##

First of all, notice that we have an `ns-3` folder - since the point of SEM is
to run and analyze ns-3 simulations, you will always need to have an `ns-3`
folder to work on.

## Interactive discovery with Jupyter notebooks ##

Since SEM runs on Python, it can be used as an interface between ns-3 and the
data visualization facilities provided by Jupyter notebooks. To see how this can
be done, either run your own Jupyter notebook server locally by issuing the
`jupyter notebook` in a shell or launch [a fully working online example on
binder](https://mybinder.org/v2/gh/signetlabdei/sem-example/master?filepath=Analysis.ipynb).

## The analysis script ##

Jupyter notebooks can be handy for interactive sessions and for looking at your
simulation results, however some users prefer more streamlined and REPL-based
development. Check out the `analysis.py` file to get an idea of this workflow:
the main steps to obtain results are the same as in the Jupyter notebook
example, but this file also shows how to save the parsed data in external files.

## Saving results and pulling them in from LaTeX ##

Inside the `report` folder you can find an example of a simple LaTeX report
containing figures generated from data output by the `analysis.py` SEM script.

# Kickstarting your own ns-3 simulation campaign #

If you plan on creating your own simulation campaign using the workflow we just
described, here's a set of commands and steps that will get you started in no
time:

1. Create a folder for your analysis
2. Inside the folder, clone the ns-3 installation you will run simulations with
3. Create a Python script to perform the analysis in - here we will call it
   `analysis.py`, but you can choose whatever name best fits your purpose.
