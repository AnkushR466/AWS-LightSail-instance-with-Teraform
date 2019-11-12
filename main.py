#!/bin/python

from python_terraform import *
tf = Terraform(working_dir='/home/ja/terraform/demo-3', variables={'count':enter})
tf.plan(no_color=IsFlagged, refresh=False, capture_output=True)
approve = {"auto-approve": True}
print(tf.plan())
print(tf.apply(**approve))