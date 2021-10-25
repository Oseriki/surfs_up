# surfs_up
SQLite Analysis

Tools: SQLite, SQLAlchemy, Python, Pandas, Flask

## Overview of analysis:
The purpose of the analysis is to generate temperature data for the months of June and December in Oahu, which will be used to determine the sustainability of the proposed surf and ice cream shop business in the island. 

## Results
Data was retrieved from a flat SQLite file and then transformed into a DataFrame via Pandas.  Further analysis was conducted using pandas to generate descriptive statistic for the temperature of Oahu for the months of June and December. Also, the outcomes were compiled as an API and uploaded to a browser via flask for easy visualization for decision makers.

### Three key differences in weather between June and December. 
- Slight difference in average temperature in June and December. Specifically, the average temperature in June is 74.9°F, and the average temperature for December is 71°F.

- Equally, there is slight difference in the standard deviation of temperature in the two months. The standard deviation of temperature in June and December are 3.26°F and 3.75°F, respectively. This shows that minimal temperature changes occur across board during these two months. 

- Minimum Temperature. The minimum temperature in December appears to be significantly lower than the minimum temperature recorded in June. The minimum temperature in June is 64°F and it is 56°F in December.

## Summary:
Based on the temperature analysis, Oahu looks like a perfect location for the surf and ice cream shop business. 
-	The average temperature for both June and December appear to be suitable for the business.
-	The standard deviation results show minimal deviation in temperature change, which will help to sustain the business yearlong. 
-	Based on the analysis, the only concern is the low temperature in December. Results show that minimum temperature in December is significantly lower than that of June.

### In addition to the temperature analysis, the following analyses be performed to gather more data 
-	Precipitation Analysis. This analysis will provide information on the frequency of precipitation in Oahu during the year. This is particularly important because high amount precipitation can impact the business negatively. 
-	Hurricane Analysis. Since Oahu is an island, it will be important to perform an analysis of hurricane activities in that location because this can directly impact the business.
