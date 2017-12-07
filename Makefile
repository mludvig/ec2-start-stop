ec2-start-stop.yml: ec2-start-stop.template.yml ec2-start-stop.lambda.py
	./import-files.py --yaml $< > $@
