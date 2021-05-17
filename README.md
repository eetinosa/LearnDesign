# LearnDesign
LearnDesign is designed to be a One stop platform for best design courses.

It’s 2021 and design is seated comfortably at the table in more companies than ever. Businesses continue to integrate design practices into their core functions and scale them across the entire organization

We understand the importance of design in businesses, why a lot of people are choosing that career path and how much help they need to get started and move on the right path, that’s why we have decided to build a one stop platform for best design courses.

# Introduction
This repository contains the python codes in these (notebooks)[https://github.com/eetinosa/LearnDesign/tree/main/Notebooks] used for webscraping , to extract design courses and their details in this (dataset)[https://github.com/eetinosa/LearnDesign/tree/main/Data].

# Webscraping Process
1.  Inspect - chose a URL as a source of data - (hackr.io)[https://hackr.io/] . Only courses relating to design was identified. These are the following design courses identified:
- Adobe Illustrator.
- Figma.
- Design Thinking.
- Adobe XD .
- Color Theory.
- Drawing.
- Prototyping.
- Sketch.
- User Interface Design.
- Graphic Design.
- User Experience Design.
- User Experience Research.
- Wireframing.

2.  Defining objects and Building Lists - Determined the features of each course required for filtering , created lists for each. The different features highlights the uniqueness of each course. The features contained in the extracted dataset
- Course Title
- Votes - ratings by other students 
- Course Link
- Author Name
- Author Link
- Hackr Link
- Course Cost
- Course Type
- Student Type

3. Extracting data - extracted data out of the HTML file ,stored it into a list. The tool/ library used was beautifulsoup. 

4. Cleaned the data and exported the data - made the data to the formats that can be used, removing unwanted sections and export data to csv and which will be used on the web application.


