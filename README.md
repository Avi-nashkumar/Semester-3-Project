# Semester-3-Project
This is a recommendation system which would recommend any user a project if he/she uploads his/her resume.

*PROBLEM STATEMENT*
whenever we are asked to work on a project we get confused on how to do that. we spend lot of time in thinking what project to choose. so we came up with this idea of project recommendation system. We thought that people generally write all their skills in their Resume. So it would be better to extract their skills from there and based on their skills , some projects will be recommended to the person who is looking forward to working on any project .

*IMPLEMENTATIONS DETAILS*
We implemented our project in different iterations. First we started with resume parsing . For resume parsing we used various python packages like: 
Pdfminer 
Spacy 
Pandas 
Numpy 
Using these packages we were able to extract information from resume. Spacy library comes with a pre-trained model ‘Named Entity Recognition’ which we used to extract names. To extract skills, we created our own dataset containing technical skills. If the skills in the resume matched the skills in the dataset then the skills were stored in an array. Similarly we created a dataset of project names from where we recommend the project.  
For the frontend part we use another python tool i.e. PyQt5. We used this PyQt5 to create our user interface and then interlinked it with the resume parser code which is in the backend. 

*Limitations*
• Valid for only resumes with PDF format 
• Not a collaborative filtering recommendation. 
• Dataset is small since it has to be created ourselves 
• Difficulty level of project depends on the skills defined.   
