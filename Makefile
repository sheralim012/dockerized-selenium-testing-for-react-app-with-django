test:
	@docker compose up --build -d
	@docker compose exec -T django python manage.py test --no-input
	@docker compose down --remove-orphans
