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
* Denver clearly had the largest county turnout with 82.8% of voters. We used an if statement to determine that it was the largest turnout. We compared the number of voters and percentages of each county to each other in the if statement. 
<img width="710" alt="winning_county" src="https://user-images.githubusercontent.com/103657822/168495044-8a8e3af3-3005-4e93-aedb-2533415bcd55.png">
<img width="288" alt="winning_county_txt" src="https://user-images.githubusercontent.com/103657822/168495046-2c7074ab-acef-4231-96ea-ee3ed593fce5.png">
* Charles Casper Stockham, Diana Degette, and Raymon Anthony Doane were three available candidates in the US Congressional election. Raymon Doane only had 3.1% of voters which is 11,606 people. Chales Stockham had a total of 23.0% (85,213) voters. Diana DeGette had the largest amount of voters totaling 272,892 people which calculates to be 73.8%. We used the same methods to calculate the candidate information as the county information. Once again, we added the candidates name to the dictionary along with a vote when the name is found on a row of data through an if statement. As for finding the percentage of votes for each candidate we used a for loop to compare the candidates vote to the total votes. 
<img width="543" alt="candidate_results" src="https://user-images.githubusercontent.com/103657822/168495611-ea6bfca4-f5d7-45a5-8818-906cfb91d0fc.png">
<img width="515" alt="candidate_percentages" src="https://user-images.githubusercontent.com/103657822/168495613-64a5e670-61f6-48d6-bfe4-6db4460532e9.png">
<img width="292" alt="candidate_results_txt" src="https://user-images.githubusercontent.com/103657822/168495621-b943c09a-7a8d-4974-b02c-c238e85d4704.png">
* Diana Degette won the election by a landslide. She had 73.8% of voters from the counties which totaled to be 272,892 voters. We determined that she was the winner through an if statement by comparing all of the votes and percentages of each candidate. 
<img width="539" alt="winning_candidate" src="https://user-images.githubusercontent.com/103657822/168495698-0d104d62-4c22-4fd6-8a7e-e70980485019.png">
<img width="230" alt="winning_candidate_txt" src="https://user-images.githubusercontent.com/103657822/168495699-3584f0d5-a871-4c6c-a2a6-e9816cb8e635.png">
## Election-Audit Summary
This python code can be used in a number of different situations. For example, the code could be modified to be used for an election as small as high school president election to as high as the presidential election. Additionally, you could modify this code to do recounts. If someone were to challenge an election you could use a modified version of this code to recount the ballots in a quick, efficient method.   
