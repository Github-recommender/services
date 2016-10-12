Serverless service for github recommendation engine
===================

This service consists of APIs used for the recommendation engine.

----------


Setting up
-------------

1) Install serverless

    npm install -g serverless
    
    Note: Install npm: sudo apt install npm
 
2) Clone this repository 

    git clone https://github.com/Github-recommender/services.git

3) **cd** into the directory and install all the dependencies to the project directory

    cd services && pip install -r requirements.txt -t ./

4) Create an AWS account.

5) Configure your system. Use this [guide](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

6) Deploy the service

    serverless deploy
