EC2 instance Start / Stop scheduler
===================================

Simple demo of EC2 instance scheduled starting / stopping using Lambda function
and scheduled CloudWatch Events.

Usage
-----

Deploy `ec2-start-stop.yml` using CloudFormation, change the stack parameters
as necessary.

For help with the **Start / StopCronExpression** syntax check out
[Schedule Expressions for Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html).

Note that the Start/Stop time is in **GMT Timezone** (yeah, what an annoyance for
us in regions that change to and from Daylight Saving Time 2x per year...).

Make changes
------------

The main template `ec2-start-stop.yml` has been generated from `src/ec2-start-stop.template.yml`
to which the lambda function code from `src/ec2-start-stop.lambda.py` has been inserted using
`src/import-files.py`.

**Don't edit the generated `ec2-start-stop.yml` template!**

Instead modify the _"template-template"_ `src/ec2-start-stop.template.yml` and/or `src/ec2-start-stop.lambda.py`
and run `make` or

    ~/ec2-start-stop $ make
    ./import-files.py --yaml ec2-start-stop.template.yml > ec2-start-stop.yml

Then deploy the generated `ec2-start-stop.yml`

Author
------

[Michael Ludvig](https://aws.nz)

License
-------

[Public domain](https://creativecommons.org/share-your-work/public-domain/) or [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/)
