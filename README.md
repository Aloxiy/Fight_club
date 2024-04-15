# Fight Club Project

This is a pet project that simulates a fight club. The project includes several classes and decorators, and uses asynchronous functions with asyncio. It also includes a connection to a PostgreSQL database.

## Classes

### Fighter

The Fighter class is the base class for all fighters in the fight club. It has attributes for the fighter's name, health, and power, as well as methods for attacking and defending.

### Boxer and Karateka

The Boxer and Karateka classes are subclasses of the Fighter class. They inherit all of the attributes and methods of the Fighter class, and also have their own unique abilities. Both classes also inherit from the Healing class.

### Octagon

The Octagon class is where the fights between fighters take place. It has a method for starting a fight between two fighters, which continues until one of the fighters' health reaches zero.

## Decorators

### Time measurement

This decorator is used to measure the time it takes for a function to run. It can be used to optimize the performance of the fight club simulations.

### Chance

This decorator is used to add a chance of success or failure to a function. It can be used to simulate the unpredictability of real fights.

## Asynchronous functions

All functions in the project are asynchronous, using the asyncio library. This allows for multiple fights to be simulated at the same time, improving the efficiency of the project.

## Database connection

The project includes a connection to a PostgreSQL database, which can be used to store information about fighters and their stats, as well as the results of past fights.