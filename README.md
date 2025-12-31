# The Lipstick Effect on the Big Screen
Analyzing the Correlation Between Economic Indicators and Popular Media Genres

## Project Overview
This research project investigates the relationship between macroeconomic instability in some selected countries and shifts in consumer preferences within the entertainment industry. Specifically, it aims to determine whether negative economic indicators—such as rising unemployment rates, high inflation with a spike in popularity for "escapist" genres (e.g., , Comedy) in movies and television series.

## Motivation
The primary motivation for this research is to understand how macroeconomic instability influences the psychological needs of the people, as reflected in their entertainment choices. Specifically, this project aims to test the validity of the 'Lipstick Effect' in the entertainment industry. In economics, the Lipstick Effect is the theory that during recessions, consumers will still buy expensive goods, but they switch to smaller, affordable luxuries (like premium lipstick) rather than large purchases (like cars or houses).

In this context, a movie ticket or a streaming subscription represents that 'affordable luxury.' This study seeks to understand if economic distress drives a shift toward 'Escapist' genres as a coping mechanism, or if audiences prefer 'Realist' or darker genres (Horror, Drama) that mirror their societal anxiety.

## Hypotheses

Null Hypothesis (H0):  There is no significant correlation between economic downturns (indicated by unemployment rates, inflation, or GDP decline) and the popularity of escapist media genres.

Alternative Hypothesis (H1):  There is a positive correlation between economic downturns and the popularity of escapist media genres. 

### Selected Countries:
Turkey
Turkey exhibits extreme economic volatility, with the Misery Index peaking at 78.27 in H1 2024.
Hypothesis:
If the Escapism Theory holds, periods of high economic distress should lead to increased consumption of escapist genres.
Italy
Italy shows a stable disinflationary trend, with the Misery Index declining from 15.94 to 7.98 over the sample period.
Hypothesis:
Improving economic conditions should reduce the relative demand for escapist content and shift preferences toward realist genres.
   
## Data Collecting
This study combines two main datasets:
Netflix Viewing Data
The dataset contains the most-watched Netflix movies and TV shows, categorized by genre and aggregated by country and semi-annual periods. Each year is divided into two periods:
First half: January–June
Second half: July–December
The analysis covers the period from 2023 to the first half of 2025 for Turkey and Italy.
Macroeconomic Data
Inflation and unemployment rates were collected from Trading Economics for each country and semi-annual period.
These two indicators were summed to construct the Misery Index, a commonly used proxy for economic distress.

Genre Classification Framework
To test the Escapism Hypothesis, genres were grouped into two conceptual categories:
Escapist Genres
Comedy, Fantasy, Sci-Fi, Adventure, Action, Romance, Animation
Realist Genres
Drama, Crime, Thriller, Horror, War, Documentary, Biography, History
Genres outside these groups were excluded to preserve a clean binary comparison.

## Methodology
For each country and period:
Total views were aggregated by genre category.
The Escapist Share was calculated as:
Escapist Views / (Escapist + Realist Views)
The analysis employed:
Pearson correlation to test linear relationships between economic distress and genre preference.
Chi-square tests to detect structural changes in genre preferences over time.
T-tests for cross-country comparison of average escapist consumption.

## Results: Turkey
Statistical Findings
Pearson correlation :
r = −0.018, p = 0.948
Chi-square test:
p < 0.001
Interpretation
The Chi-square test indicates that genre preferences changed over time.
However, the near-zero Pearson correlation shows that these changes are not explained by economic distress.
In other words, although viewing preferences fluctuate, they do not respond systematically to worsening economic conditions.
Cultural Interpretation
Turkey shows a structurally high preference for both comedy and drama, regardless of macroeconomic stress.
Escapist consumption appears to be culturally stable rather than economically reactive.

## Results: Italy
Statistical Findings
Pearson correlation:
r ≈ 0.80, p ≈ 0.10
Chi-square test:
p < 0.001
Interpretation
Although the sample size limits statistical power, Italy exhibits a strong positive relationship between economic distress and escapist genre consumption.
As the Misery Index rises, Italian audiences consistently increase their consumption of comedy and fantasy, supporting the Escapism Theory.
Italy thus behaves as a “sensitive market”, where cultural consumption responds to economic conditions.

## Cross-Country Comparison
Average Escapist Share
Turkey: ~47%
Italy: ~35%
Difference: ≈ 12 percentage points
Statistical Test
One-sided t-test: p ≈ 0.05–0.10

## Final Interpretation
Italy confirms the Escapism Theory:
Economic stress leads to a clear and interpretable shift toward escapist content.
Turkey contradicts the theory:
Despite severe economic distress, genre preferences remain largely unchanged, indicating cultural inertia rather than economic sensitivity.

Economic hardship alone does not universally produce escapist behavior.
Cultural baseline preferences matter as much as — and sometimes more than — macroeconomic conditions.
In stable economies, cultural consumption reacts to economic signals.
In chronically unstable economies, escapism may already be normalized, leaving little room for marginal change.

## AI USAGE
In this project, Artificial Intelligence tools were used to assist with the general coding process. The AI was particularly helpful for data visualization, as it provided the necessary code to create clear graphs and charts. These visuals played a key role in analyzing the relationship between economic indicators and the popularity of specific media genres, making the results easier to understand and interpret.

## Machine Learning
// to do 2nd of jan

## Limitations and Future Work
The primary limitation of this research was the difficulty in accessing historical data. Specifically, consistent Netflix viewership data prior to 2023 was not available, which restricted the analysis to the 2023–2025 period. This relatively short timeframe makes it challenging to observe long-term trends between economic shifts and audience preferences. Future studies could improve this research by extending the timeline to cover a full economic cycle and by including data from other streaming platforms to gain a broader perspective on consumer behavior.



