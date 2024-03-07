# Build Circle Superheroes tech test

Superheroes and villains are always battling it out, but how do we know who wins? In this test, we will deploy a simple lambda to find out.

The superhero and villain characters along with their stats are stored in a public json file in AWS S3 - https://s3.eu-west-2.amazonaws.com/build-circle/characters.json. When the lambda is deployed you can run the lambda with a query like https://my-lambda-hash.lambda-url.eu-north-1.on.aws/?hero=Superman&villain=Joker and the returned result should be some information about the winner.

During a battle, the character with the highest score wins.

We expect the solution to be simple, readable, and secure.

For this exercise, we need to deploy a lambda function with:

* A publicly accessible lambda URL.
* The data source URL as an environment variable 'data_url'.
* Some cloud watch alerts for when the lambda throws an exception.

The lambda code for deployment can be found in `lambda-function.py` and it shouldn't require modification. You can use any framework for deploying infrastructure such as the CDK, or Terraform.
