# TinyDrive URL
https://tinydrive.herokuapp.com

## Team Members

- Robert Augustynowicz - [RobertAugustynowicz](https://github.com/RobertAugustynowicz) (1003511078)
- Abbas Rattansi - [arattansi1](https://github.com/arattansi1) (1004266206)
- Wayne Ying - [yingwe](https://github.com/yingwe) (1002437721)


## Description

__TinyDrive__ is a web application that has taken inspiration from many of the tools we may use on a daily basis. It allows a user to upload a file to the application and generate or customize the URL that links to the uploaded file. The uploader can set permissions on the URL that put restrictions on any users the file is shared with. Permissions include a time frame that the URL is valid for and read/write privileges. A user can upload and edit text files, common images files, and Microsoft Office files through the web interface.


## Final Version

- The website gives the user the ability to upload files to the website database.

- The owner will be able to create a URL once a file is uploaded so that they will have quick and shareable access to the uploaded files across all platforms with a browser.

- Uploaded files have an expiration date which will be added for the scheduled deletion ranging from minutes to days of time live.

- An account system is be put in place.

- The account system uses OAuth 2.0 for authentication.

- A permission system will be put into place to protect the files uploaded by a user regarding viewing and downloading or changing the files located at the URL.

- The permission system allowing URLs to be public, or private

- Capabilities to re-upload files in order to replace the current file with an edited or updated version, without having to change or create the URL in use.

- Once a file has been updated, a history of the previous file will be kept available until the expiration date.

- you can also overwrite the deadline and delete the url on command

## Technology

- [__Bootstrap__](https://getbootstrap.com/) is a HTML, CSS, and JavaScript framework. It allows for easy to use elements templates (i.e. modern forms, pricing charts, display modules etc.) to be embedded in our application.

- [__Django__](https://www.djangoproject.com/) is a Python based web framework. Through the use of a programming language it allows users to quickly pick up and understand the framework through the logic employed by it. It comes preloaded with authentication libraries as well as an SQLite database which comes with the standard Python library, but also allows easy integration of other foreign databases.

- [__Postgres__](https://www.postgresql.org/) is a open source relational databse which employes sql. This is used as the main database for heroku.

- [__Auth0__](https://auth0.com/) is a token based system which passes a token once authenticated though facebook google twitter as well as account sign up with email. This token provides a users unique authentication id which allows for client specific infaromation.

- [__cloudinary__](https://cloudinary.com/) is an online cloud server which allows for the sorage of files uploaded by the user. It is used with heroku as heroku has very limited space for uploaded files.

- [__heroku__](https://www.heroku.com/) is a cloud deployment platform which we decided to use to deploy our web app. We found that it was easily used with the current django framework we were using with only slight modifications. Also with git integration it made deployment simple and quick.
 


## Technical Challenges

As with any project, it is common to face challenges along the way. We want to ensure that potential challenges we face can be easily overcome with the appropriate amount of planning.

- We would like to allow the user to upload directories into the application directly, rather than only single files at a time. This feature would make usage of the application much easier for users who want to share multiple files at a time and do not want to generate multiple URLs. However, it can be challenging to upload any directory as it has relatively new browser support, and each file type and size must be properly checked before allowing the upload.

- We would also like give the user the ability to edit images they upload (similar to a lighter version of photoshop on the web). This can be challenging as modifying image files will require advanced HTML5, and we need to integrate the modified output with the rest of the application.

- We would also face challenges in managing the concurrency between edited files. For example, we need to consider whether to allow users to edit at the same time and find a way to merge edited files together (similar to a git merge), or limit the editing to only one user at a time.

- The final two challenges are the most common yet the most challenging. Before we can complete anything in this assignment, we must be able to comfortably use the framework and any potential libraries we may include in the assignment. The learning curve, while not too steep, may be a roadblock in trying to do some of the things we are used to doing using different technologies we have already had experience with.

- Finally, we must be able to deploy the application in an effective manner, without bugs and errors and give any user the ability to use the application live. Deploying the application on a server, or using a website hosting service is completely new to us; proper configuration will be challenging and require learning and research.
