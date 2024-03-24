from dataclasses import asdict, dataclass
from typing import Optional


@dataclass(kw_only=True)
class Base:
    id: Optional[int] = None
    key: str
    
    def as_dict(self):
        return asdict(self)

    def columns(self):
        return self.as_dict(self).keys()

