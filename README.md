# Udacity US bikeshare project

## Overview

In this project, you will make use of Python program to explore and analyze data related to bike share systems for three major cities in the United States: Washington, Chicago, and New York City. You will write code to import the data and answer user questions regarding it by calculating  descriptive statistics. You will also write a script that takes in raw input to create an interactive experience on the terminal to show these statistics.

## Bike Share Data

Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. These systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B. They can also return it to the same location if they'd like to just go for a ride. Each bike can serve several users per day.

It is very easy for a user of the system to access a dock within the network to unlock or return bicycles. These systems also provide a range of data that can be used to explore how these bike-sharing systems are used.

In this project, you will use data provided by Gallivant, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.
The Datasets

Randomly curated data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same six columns:

   - Start Time (e.g., 2017-01-01 00:07:57)
   - End Time (e.g., 2017-01-01 00:20:53)
   - Trip Duration (in seconds - e.g., 776)
   - Start Station (e.g., Broadway & Barry Ave)
   - End Station (e.g., Sedgwick St & North Ave)
   - User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two additional columns:

   - Gender
   - Birth Year

The original files are large, but they can be accessed here if you'd like to see them (Washington, Chicago, New York City). The original files had more columns and also differed in format in many cases. Some data cleaning has been performed to condense these files to the above core six columns in order to make your analysis and the evaluation of your Python skills more straightforward.

## Statistics Computed

You will learn about bike share use in Washington, Chicago, and New York City by calculating a variety of descriptive statistics. In this project, you'll write code to provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time)

   - most common month
   - most common day of week
   - most common hour of day

2. Popular stations and trip

   - most common start station
   - most common end station
   - most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

   - total travel time
   - average travel time

4. User info

   - counts of each user type
   - counts of each gender (only available for NYC and Chicago)
   - earliest, most recent, most common year of birth (only available for NYC and Chicago)

## The Files

To answer these questions using Python, you will need to write a Python script. To help guide your work in this project, a template with helper code and comments is provided in a bikeshare.py file, and you will do your scripting in there also. You will need the three city dataset files too:

   - washington.csv
   - chicago.csv
   - new_york_city.csv


## Disclaimer

Data and project specifications were provided by [Udacity](https://www.udacity.com/).