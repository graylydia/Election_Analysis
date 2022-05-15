# US Congressional Election Audit
## Overview of Election Audit
### Purpose
In this challenge, we assisted Tom in creating a Python code for an election audit for the US Congressional precinct in Colorado. Through this code we were able to determine the total number of votes, the total number of votes for each county, the county with the largest turnout of voters, the total number of votes for each candidate, and the winner of the election. Additionally, we were able to calculate the percentages for each county and candidate based on the total votes. 
## Election Audit Results
* There were 369,711 total votes cast in this US congressional election. Below is a screenshot of how these votes were calculated. We initialized the variable total_votes to 0 and then used a for loop to run through all of the data and add 1 to total_votes.
<img width="266" alt="total_votes" src="https://user-images.githubusercontent.com/103657822/168483127-609bab05-8dd0-4a9e-8f3d-7549f8117828.png">
<img width="235" alt="total_votes_txt" src="https://user-images.githubusercontent.com/103657822/168483394-5ba8ae92-86ef-45af-8da2-5ef33fdc6a4e.png">
* As for each county, Arapahoe had the least amount of voters. 24,801 people voted in Arapahoe county which is only 6.7% of total voters. Jefferson had 38,855 (10.5%) people that voted. Denver had 82.8% of voters. 306,055 people went to vote in the Denver county. We used a decision statement to first determine if the county was in the county dictionary and then added a vote to the county when running through the data. To calculate the percentages we used another for loop. 
<img width="529" alt="county_votes" src="https://user-images.githubusercontent.com/103657822/168494709-2f585ebf-4dff-4574-a1ff-2f2612d14e50.png">
<img width="651" alt="county_percentages" src="https://user-images.githubusercontent.com/103657822/168494711-6e1cc3a1-1710-4245-9e6a-58d3a6ea9bcb.png">
<img width="256" alt="county_votes_txt" src="https://user-images.githubusercontent.com/103657822/168494813-6648d75e-fc35-4be4-9e72-0ee68414c2bd.png">

