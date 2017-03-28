For local development: 

- Install serverless
- Install necessary libs in requirements.txt
- Set up AMZ account and set AMZ creds as environment variables
- Had to make custom psyco2 lib.  See https://github.com/jkehler/awslambda-psycopg2.  Used 9.5.4 postgres and 2.7.1 psyco2

For prod development: 

- Had to make custom psyco2 lib.  See https://github.com/jkehler/awslambda-psycopg2.  Used 9.5.4 postgres and 2.7.1 psyco2