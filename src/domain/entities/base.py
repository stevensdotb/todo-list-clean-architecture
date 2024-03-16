from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Base:
    id: Optional[str]

    def as_dict(self):
        return asdict(self)
    
    def columns(self):
        return self.to_dict(self).keys()

