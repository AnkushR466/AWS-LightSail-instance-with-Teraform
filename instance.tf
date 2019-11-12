resource "aws_lightsail_static_ip_attachment" "test" {
  static_ip_name = "${aws_lightsail_static_ip.test.name}"
  instance_name  = "${aws_lightsail_instance.test.name}"
}

resource "aws_lightsail_static_ip" "test" {
  name = "example"
  
}

resource "aws_lightsail_instance" "test" {
  name              = "example"
  availability_zone = "us-east-1b"
  blueprint_id      = "ubuntu_16_04"
  bundle_id         = "nano_1_0"
  key_pair_name     = "my_key"
  tag = "MageHost"
}
