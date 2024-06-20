from dataclasses import dataclass


@dataclass
class Aggregate:
    """Combine domain entities to the one Aggregate to work with"""
    pass


@dataclass
class RootAggregate(Aggregate):
    pass