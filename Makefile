devbucket:
	docker compose -f docker-compose.dev.yml exec localstack awslocal s3 mb --region sa-east-1 s3://matheus-dr-dev-s3-blog

updev:
	docker compose -f docker-compose.dev.yml up app postgres localstack -d
	make devbucket

downdev:
	docker compose -f docker-compose.dev.yml down
