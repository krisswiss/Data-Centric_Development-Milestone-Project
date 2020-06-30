# Shoesycling

### Data-Centric_Development-Milestone-Project

The purpose of this project is to create a website that allows users to read, edit, create and delete cycling shoes and reviews.
As a cyclist I know how hard it is to find a pair of cycling shoes, especially in Ireland, the only options are to buy online. I always thought it would be very handy to have all of the different shoes in one place, so I could find more information about them and read some user reviews, which would help in making a purchase decision.
That is the reason I decided to create that project, which I hope to work on further and put into producition.<br/> 
Users can browse shoes, read about each shoe which includes main features of the shoe and if they find the description to be inaccurate or incomplete edit it. 
Another functionality is an option to add new shoe or remove an existing one if e.g. it is not a cycling shoe. 
Users can also view, add, edit and remove reviews for each shoe and also give star ratings from one to five. </br>


## UX

### User stories

- As a user A</br> 
I want to add a shoe. I open the Shoesycling site, click on the “Add Shoe” option in the navigation bar on the top right corner. This brings me to a different page and here the user is presented with eight headings to fill out to create their review. These headings include “Brand”, “Model”, “Type of cycling”, “Gender”, “Sole material”, “Retention system”, “Description” and “Picture URL”. All of which are required and clearly stated in red writing next to the heading “required” with exception to the Picture URL which is optional as stated in green writing next to this heading. To fill in each heading I simply click on the space to write and it turns green indicating I can write. I manually fill in the brand, model and description while the remaining headings have drop down options to choose from. I can then click “Add shoe” to add this shoe to the site or I can click the “cancel” option beside it if I change my mind. Once I have added the shoe I am brought to a separate page showing the results of all the shoes where my recently added shoe is. If I click cancel however, I am then brought to the opening page of the site.</br>
- As a user B</br>
I want to simply view shoe reviews for both the road and mountain biking. I click on the option “All Shoes” which is located on the navigation bar on the top right between “Home” which I can click at any time to return to the home page and “Add Shoe” if I want to add my own shoe to this site. Once I click on “All Shoes” I am brought to the next page where I can see all of the shoes. Each shoe is presented and contained in its own visual box so as to separate each shoe clearly. I see an image of the shoe taking up most of the box, beneath the image is the name of the shoe and under the name is “Reviews” written clearly in blue text. I want to see the features of this shoe first so I can click on the image or the name of the shoe and I am not brought to another page, the features of the shoe are presented replacing the image. I can click out of this to see the image and no features if I wish. I click on reviews as I want to view the reviews for this shoe. This brings me to the next page where I see the image of the shoes, its features and the description of the shoe. I scroll down further to see the reviews and each review is contained in its own box neatly separated from one another with a heading for example “Not the best for Crankbrother cleats”. I click into this review as the heading interests me. I then see the whole review and the box in which the heading is displayed, enlarges. The star ratings from one to five are also visible on the review before and after clicking it.</br>
- As a user C</br>
I want to edit a review to add to it as I think a valid point was made and I would like to add to the point being made. I follow the above steps as user B and once I am viewing the review after I have clicked on it I have the option to “Edit Review” in this review box. I am then brought to another page where I am presented with the headings to fill out as explained above. I
decide to only edit the review and not its title or rating so I click on the space and it turns green as further detail to indicate the location in which I am writing. I am happy with the changes made so I click the option at the bottom of the headings “Save”. I can also decide to click “Cancel” located beside the “Save” option if I change my mind.</br>
- As a user D</br>
I want to remove a review as I disagree with its content. I follow the above steps as user B and once I am viewing the review after I have clicked on it I have the option to “Remove Review” which is beside the “Edit Review” option (as seen in user c) in this review box. The page is refreshed without the review I just removed.</br>

 
### Strategy
The core focus in the design was to make it as easy as possible to access the information about cycling shoes. I wanted to provide users with full functionality to read about different cycling shoes and rate / review them. 
I also wanted the users to have full control over shoes and their reviews, so they could edit information, if unaccurate or missing, but also add new shoes and reviews as well as deleting them.

### Scope
For those accessing the website, I wanted to provide a simple, yet effective way of searching for different types of cycling shoes. I want to include all CRUD features to my app for both shoes and reviews.

### Structure
All shoes are displayed in Materialize Cards with links to reviews and more shoe details. Add shoe and add review functionality uses Materialize input/select forms with validation and required attributes for most features. Shoe description and picture URL are not required. If not submitted, stock picture will display instead and instruction to add description.</br>
Based on the selection from home page, shoes are grouped together - either road or mtb shoes.</br>
Each shoe is then displayed individually with name and picture clearly visible and main features presented underneath. Below that user has an option to add review, edit shoe description or delete it.</br>
Reviews are grouped under each shoe in user friendly format</br>

### Skeleton
Information is presented in a user friendly way - simplicity is the king here!</br>
I did not want to overhwelm user from the beggining of the journey, so with each step, more information relating to the shoe is displyed, which makes it more engaging.</br>
First, user can watch a video on how to choose their schoes and / or read the article about different types and features.</br>
After that on top of the page they are 2 pictures which work as links to filter the results based on the type of cycling.</br>
On the next page results are presented in simple cards with just a picture and name and model of the shoe. User can click on the picture wchich will reveal main features of the shoe. Below is the link to full description and reviews.</br>
After selecting the shoe user wants to view, another page opens with detailed description, fullsize picture, features and description. Below user can read reviews, which are presented in another engaging way - expandable accordion from Materialize.</br>


### Wireframes

#### Desktop
[Home](https://github.com/krisswiss/Data-Centric_Development-Milestone-Project/blob/master/wireframes/01.Home.JPG)</br>
[All Shoes](https://github.com/krisswiss/Data-Centric_Development-Milestone-Project/blob/master/wireframes/02.All%20Shoes.JPG)</br>
[Each Shoe](https://github.com/krisswiss/Data-Centric_Development-Milestone-Project/blob/master/wireframes/03.%20Each%20Shoe.JPG)</br>
[Add/Edit Shoe](https://github.com/krisswiss/Data-Centric_Development-Milestone-Project/blob/master/wireframes/04.%20Add%20Edit%20Shoe.JPG)</br>

### Sufrace Plane
I aimed for simple, yet modern design, hence the choince of white background contracting with elegant dark navy navigation bar and footer.</br>
Fonts used are very neutral, clear and easy to read.</br>
All buttons have been styled to change colors when hovered based on the action:
- Add, green
- Edit, blue
- Remove, red
to further indicate desired action and make it as user friendly and attractive as possible.

## Technologies
1.	HTML
2.	CSS
3.	Flask
4.  Python
5.  Mongo DB
6.  Materialize CSS
7.  JavaScript
7.  jQuery


### Existing Features:
-	Create Read Update Delete features are available and fully working on both collections.
-	User can filter results based on type of cycling - road or mountain bike.
-	Each shoe and review can be easily accessed to read, edit, update or delete.
-   Each shoe can be reviewed and rated (which is displayed with star icons).

### Features left to implement:
- In the future I would like to add more filtering options - especially in "all shoes" page, where user could combine different shoe features and only results matching that combination would be returned. Ideally, I would like to use JavaScript for it to make it work dynamically (without pressing any buttons)
- I would also like to add sort by filters for shoes and reviews and additional field, datestamp, in my reviews DB with the date it has been added, so the reviews are displayed, and could be filtered, based on the date they have been added.
- I would also like to add authentication, so users can create accounts and only make changes to their own reviews and shoes.
- I would also like to add more fields to add more pictures and present them in a carousel. Ideally I would also use different DB which lets user store images in the most popular formats and not uploading the URL's.
- I would also like to be able to change text to star icons in add review select option.

### Implementation of business logic:

Footer has been expanded to include links to purchase shoes, which will generate commision to the site owner based on per click rate.

## Testing
I believe I have achieved my goals by providing the user with clean, simple and intuitive design.</br>

Information is easily accessible and easy to read.</br>

CRUD functionality has been tested manually both during development and after deployment.</br>

Use of required attribute helped to force some basic structure in DB, which might help at a later stage to filter the results.</br>

Site has been tested for responsiveness with google inspect tool, but also on my own Laptop, tablet and mobile. In addition to this, I have shared my link with several friends, including actively working software developers, who have tested it all on different devices (Sony Z5 compact, Samsung S8, Huawei P20lite), operating systems(windows, mac os) and browsers(chrome, safari, internet explorer) and confirmed they didn’t come across any issues with neither responsiveness or CRUD functionality.</br>

After applying each change to app.py I was manually testing every possible scenario to make sure it works. Every possible CRUD scenario on both shoes and reviews have been also tested manually after deployment.</br>

HTML and CSS Code has been validated in w3 validator with no major issues.</br>
The only errors that are showing are for HTML code regarding the comments length.

## Deployment
Website is hosted using GitHub pages, deployed directly from the master branch.</br>
GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub.</br>
In order to deploy this to GitHub Pages, I first pushed my commits to GitHub. The process for this was as follows:</br>
1. Opened new terminal</br>
2. Added any files to be commited with command line 'git add .'.</br>
3. Then commited any final changes made with command line 'git commit -m "comment here"'.</br>
4. Checked status to ensure file tree was clean with command line 'git status'.</br>
5. Pushed files with command line 'git push'.</br>
Changes successfully pushed to remote repository, created in the beginning of the project.</br>

To run locally, you can clone this repository directly into the editor of your choice by pasting 'git clone https://github.com/krisswiss/Data-Centric_Development-Milestone-Project' into your terminal. Before working with the code, make sure to open requirements.txt and install appropriate files.</br>

The site has been deployed using Heroku. The process for deploying to Heroku is as follows:</br>

In your Heroku account, create a new app
1. Under the setting tab in the app, reveal and change the 'config vars' to IP 0.0.0.0 and PORT 5000.
2. Ensure in your app you have in your app files in GitHub a Procfile with the following: 'web: python app.py', and you project requirements in a requirements.txt file.
3. In Heroku, in your app and under the 'deploy' tab, choose the GitHub deployment method. In the app connected to GitHub section find and select the app you wish to deploy.
4. Choose either automatic or manual deploys. In whichever you choose, select the branch in the GitHub repository you wish to deploy.</br>
Final deployed site is [here](https://shoesycling.herokuapp.com/).</br>


***This is for educational use only.***
