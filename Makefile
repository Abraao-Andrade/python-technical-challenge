test:
	# python manage.py test tests --pattern="*_test.py"
	pytest tests -vv -p no:warnings
