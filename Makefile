.PHONY: build release run test
.DEFAULT_GOAL := build

# https://github.com/facebookresearch/faiss/tags
FAISS_RELEASE := latest
EXTERNAL_PORT := 8080
GPROJECT_ID := chronopin-209507
GRELEASE := latest

build:
	docker build \
		--build-arg FAISS_RELEASE \
		--tag 123wowow123/faiss-web-service:$(FAISS_RELEASE) \
		.

release:
	docker push 123wowow123/faiss-web-service:$(FAISS_RELEASE)

run:
	docker run \
		--rm \
		--interactive \
		--tty \
		--publish $(EXTERNAL_PORT):5000 \
		123wowow123/faiss-web-service:$(FAISS_RELEASE)

test:
	curl 'localhost:$(EXTERNAL_PORT)/ping'
	curl 'localhost:$(EXTERNAL_PORT)faiss/search?q=war'
	curl 'localhost:$(EXTERNAL_PORT)/faiss/add' -X POST -d '{"id": 9999, "sentence": "war in ukrain"}'

gbuild:
	docker build -t us-west1-docker.pkg.dev/$(GPROJECT_ID)/faiss/faiss-web-service:$(GRELEASE) .

grelease:
	docker push us-west1-docker.pkg.dev/$(GPROJECT_ID)/faiss/faiss-web-service:$(GRELEASE)

gupdate:
	kubectl set image deployment/faiss-web-service faiss-web-service=us-west1-docker.pkg.dev/$(GPROJECT_ID)/faiss/faiss-web-service:$(GRELEASE)

grun:
	docker run --rm -p $(EXTERNAL_PORT):5000 us-west1-docker.pkg.dev/$(GPROJECT_ID)/faiss/faiss-web-service:$(GRELEASE)

grefresh:
	make gbuild
	make grelease
