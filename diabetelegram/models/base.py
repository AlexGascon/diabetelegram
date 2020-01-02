from pynamodb.models import Model


class BaseMeta:
    read_capacity_units = 1
    write_capacity_units = 1
    region = "eu-west-1"
