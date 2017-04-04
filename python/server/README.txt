For development on personal account: 

- Make sure python version is 2.7
- Install serverless
- Install necessary libs in requirements.txt 
- Set up AMZ account and set AMZ creds as environment variables (I put my personal creds in bash_profile)
- Had to make custom psyco2 lib.  See https://github.com/jkehler/awslambda-psycopg2.  Used 9.5.4 postgres and 2.7.1 psyco2
- Copy the connection string from dbtools.py and paste into "get_connect_str():".  This is a temporary hack.  DO NOT PUSH THIS UP TO GITHUB!

For the initial deploy to your personal account: "serverless deploy"
To make incremental changes to the handler function "serverless deploy function --function hello"



For prod development: 

- Had to make custom psyco2 lib.  See https://github.com/jkehler/awslambda-psycopg2.  Used 9.5.4 postgres and 2.7.1 psyco2