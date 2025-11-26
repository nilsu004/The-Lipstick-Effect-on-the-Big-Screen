# Turkish vs Indian Movies Over Time

## Project Overview
This project analyzes the development of Turkish and Indian movies over time using IMDb data. The main focus is on understanding how Turkish movie ratings have changed across the years. In addition, Indian movies are included in the analysis to allow a comparison between the two countries.
Besides rating trends, the project also examines how movie genres differ between Turkey and India and how genre distributions have changed over time. This enrichment helps to understand whether differences in audience preferences and movie styles may explain rating trends

## Motivation
Turkey and India are two countries with rich and well-established cultural backgrounds. Movies are one of the most important ways in which culture is shared both nationally and internationally.
This project mainly focuses on the development of Turkish cinema across time using IMDb ratings as an indicator of audience evaluation. To make the analysis more meaningful, Indian movies are included as a comparison group because Indian cinema has a long and strong tradition similar to Turkey.
Another motivation behind this project is the cultural exchange between the two countries. Turkish audiences are known to enjoy Indian movies, and Turkish TV series and films are popular in India as well. This shows that the two countries may have overlapping audience tastes, which makes comparing their movies more interesting.
In addition to comparing ratings, the project also studies genre distributions to explore whether the two countries focus on different movie types (such as drama, romance, or comedy) and whether these preferences change over time.

## Hypotheses

H₁ – Trend in Turkish Movies
(H₀): There is no significant change in Turkish movie ratings over time.

(H₁): Turkish movie ratings show a significant increase over time.


H₂ – Country Comparison
(H₀): There is no significant difference between the average IMDb ratings of Turkish and Indian movies.

(H₁): There is a significant difference between the average IMDb ratings of Turkish and Indian movies.


H₃ – Genre Distribution Difference
(H₀): Turkish and Indian movies have similar genre distributions.

(H₁): Turkish and Indian movies focus on different movie genres.


H₄ – Genre Change Over Time
(H₀): The genre distribution of Turkish movies does not change over time.

(H₁): The genre distribution of Turkish movies changes over time.

## Data Collecting
The datasets were collected from Kaggle. Two separate datasets were used:
A dataset containing Turkish movies and their IMDb ratings, genres, runtime, and release year.
A dataset containing Indian movies with the same features.
The datasets were cleaned by removing missing and invalid values. Movies were also filtered based on country information to ensure that only Turkish and Indian movies were included.

## Machine Learning

After analyzing the historical trends of Turkish and Indian cinema, I wanted to take this project a step further: **Can we predict the success of a movie before it is even filmed?**

To answer this, I integrated a Machine Learning model using a **Classification approach**.

**The Logic Behind the Model**
Imagine a producer holding a script for a new movie. They know the genre (e.g., Drama) and the planned duration (e.g., 100 minutes), but they don't know if the audience will like it. My model acts as a **digital decision support system** to help answer that question.

**How It Works**
1.  **Defining Success:** First, I taught the computer what a "good movie" looks like. I established a threshold (IMDb rating of 6.5). Any movie above this score is labeled as "Successful," and anything below is labeled as "Average/Underperforming."
2.  **Learning from History:** The model analyzed thousands of past Turkish and Indian movies. It learned patterns—for example, it might notice that "History" movies in Turkey tend to be rated higher when they are longer, whereas "Comedies" might fail if they drag on too long.
3.  **Making Predictions:** Finally, the model uses these learned patterns to predict the probability of success for future movie concepts.



## Limitations and Future Work
1. The datasets may not include all movies produced in Turkey and India.
2. IMDb ratings may be biased due to differences in audience size and popularity.
3.Genre labels may be inconsistent or simplified.
4. In future work, the project could be extended by adding box office revenue, award data, or social media popularity indicators.


