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



