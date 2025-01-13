module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "jomaws-lambda1"
  description   = "My 41.6% cool lambda function"
  handler       = "index.lambda_handler"
  runtime       = "python3.12"

  source_path = "./lambda-code/src/lambda-function1"
}