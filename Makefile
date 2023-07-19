devbucket:
	docker exec matheus-dr-localstack-1 awslocal s3 mb s3://matheus-dr-dev-s3-blog

updev:
	docker compose -f docker-compose.dev.yml up app postgres localstack -d
	make devbucket
