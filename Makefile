build:
	docker build -t jzhaowandb/wandb-actions:latest .

run: build
	docker run -e WANDB_API_KEY -e JOB_CONFIG jzhaowandb/wandb-actions:latest

push:
	docker push jzhaowandb/wandb-actions:latest

