test:
	@docker compose build
	@docker compose run -T django python manage.py test --no-input
	@docker compose down --remove-orphans
