#!/bin/python

from python_terraform import *
tf = Terraform(working_dir='/root/Desktop/terraform/Demo-1')
tf.plan(no_color=IsFlagged, refresh=False, capture_output=True)
approve = {"auto-approve": True}
print(tf.plan())
print(tf.apply(**approve))
