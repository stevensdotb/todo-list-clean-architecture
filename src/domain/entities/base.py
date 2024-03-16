from dataclasses import asdict
from typing import Optional



class Base:
    id: Optional[str] = None

    def as_dict(self):
        return asdict(self)
    
    def columns(self):
        return self.to_dict(self).keys()

