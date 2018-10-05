ec2-start-stop.yml: src/ec2-start-stop.template.yml src/ec2-start-stop.lambda.py
	$(SHELL) -c "cd src; ./import-files.py --yaml ec2-start-stop.template.yml" > $@
