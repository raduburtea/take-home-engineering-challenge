# take-home-engineering-challenge

I have built a CLI application that displays the closest k restaurants to the provided location. I have chosen to develop the application in this way as
I do not have any previous experience building a CLI app and I wanted to experiment with it.

## How it works

First you would have to clone the repo and then cd into it:
```
git clone 
cd take-home-engineering-challenge
```
Let's suppose our coordinates are (37.7899138671344, -122.405232892524). In order to get the 3 closest restaurants to your location you have to run the following command:

```
python -m find_nearest_restaurants find -- 37.7899138671344 -122.405232892524 3 
```
The result would look like this:
```
                                                           Restaurant Name                                           Address  Distance
0                                                            Spice Affairs     SUTTER ST: CLAUDE LN to GRANT AVE (216 - 299)  0.000000
1                                         San Francisco Street Foods, Inc.  POST ST: KEARNY ST to ROBERT KIRK LN (100 - 140)  0.000764
2  San Francisco Carts & Concessions, Inc. DBA Stanley's Steamers Hot Dogs    GEARY ST: GRANT AVE to STOCKTON ST (100 - 199)  0.002000
```

## Engineering choices

- I have developed the project in Python as this is the language I am the most familiar with. 
- In order to store the data and preprocess it I have used a Pandas dataframe as it allows easy and fast preprocessing of data, as well as an extended set of further functionality if the scope of this project would need to be extended.
- I have developed the CLI interface using the [Typer library](https://typer.tiangolo.com), as it is easy to learn, use and scale.
- For the backend of the app I have used an Object Oriented Designed as it is the most appropiate and tried following most of the SOLID principles.

## What I would have done if I had more time

- I would have removed all the hard coding from the pandas dataframe in find_restaurants.py and add it to a config file from which I would take the values.
- Since the distance measure offered by the distance between latitude and longitude is not very indicative of actual walking or driving distance I would use the Bing Distance Matrix API to compute the real-life distance and the estimated time to arrival. I have tried using the [pybaf library](https://pypi.org/project/pybaf/) for this but due to the lack of time and documentation of the library I did not have time to finish this.
- I would have also liked to build a web API that would display the current location and closest restaurants on a map.
- I would have added tests for each component to get 100% test coverage.


