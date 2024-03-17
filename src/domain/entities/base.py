from dataclasses import asdict, dataclass


@dataclass(kw_only=True)
class Base:
    id: int
    
    def as_dict(self):
        return asdict(self)

    def columns(self):
        return self.as_dict(self).keys()

