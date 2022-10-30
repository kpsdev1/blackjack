# BlackJack
This is a command line Blackjack game I created for my Portfolio Project 3 in Python and is played in a terminal hopsted on Heroku. 
The aim of blackjack is to get 21 also know as BlackJack or as close as possible without busting(busting is when you go above 21). If you go
bust the dealer automatically wins and if you have 21 or are closer to 21 than the dealer then you win. If the dealer lands on 17 or more they must 
stand which means to stay and not take another card. If the dealer is below 17 they must hit which means they have to take another card.

## Table of Contents
1. [UX Design](#ux-design)
2. [Features](#features)
3. [Demo](#Demo)
4. [Future Features](#future-features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)

## UX Design:

## Features:

## Demo:

## Future Features:

## Technologies Used:

## Testing:

## Bugs:

## Deployment:
This game was deployed on Heroku. The following steps were used to deploy the game to Heroku.
- First make sure you are signed into Heroku.
- Then on the main dashboard select **New** and then choose **Create new app** from the drop down menu.
- Then you will need to choose a name for your project(this name has to be unique to Heroku) and also choose the region, based on where you are located(As im in Ireland I chose Europe)
and then click on **Create app**.
- Then go to the **Settings** tab.
- In **Settings** click on **Reveal Config Vars** and enter the following key **Port** with the Value of **8000**.
- If you are using a Google sheets API in your project you will need to enter **Creds** as another **Reveal Config Var**.
- Then scroll down to **Buildpacks** and click **Add buildpack** choose **Python** and then click **Save changes**.
- Repeat the above step and select **nodejs** and click **Save changes**.
- Then go to the **Deploy tab**.
- Under **Deployment method** choose Github and then click **Connect to GitHub** you will be probably be prompted to sign into your Github.
- Then you can search for you GitHub repository, in my case this was **blackjack** and click **connect**.
- To deploy automatically you will need to select **Enable Automatic Deploys** which will rebuild the app everytime you push a change to GitHub.
- To deploy manually go to the **Manual deploy** section below and click **Deploy Branch**. Just remember you will need to do this everytime you make a change to your
code on Github.
- Below you will see **your app was sucessfully deployed** with a **view** button below this that will take you to the url of you deployed project.

## Credits:

## Acknowledgements:
- I would like to thank my mentor Adegbenga Adeye for all help throughout the project and for being really positive about the course.
- I would like to thank Code Institutes Slack Communtiy as this helped me so much when I got stuck on part of my project and also with course challenges.
- I would also like to thank our chort facilitators Kenan Wright and Kasia Bogucka, for answering any course related questions I asked and for porviding us with a weekly study schedule.