test:
	@docker compose up -d
	@docker compose down --remove-orphans
