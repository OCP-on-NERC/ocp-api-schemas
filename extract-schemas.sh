#!/bin/sh

kubectl get --raw /openapi/v2 > openapi.json
openapi2jsonschema \
	--kubernetes \
	--expanded \
	--strict \
	-o schemas/master-standalone openapi.json
