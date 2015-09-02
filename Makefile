
build-image:
	docker build -t rcelha/textteaser .

test:
	docker run --rm	-v "${PWD}:/usr/src/app:ro" rcelha/textteaser python test.py

bash:
	docker run -it --rm	-v "${PWD}:/usr/src/app:ro" rcelha/textteaser bash