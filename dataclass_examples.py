
# https://medium.com/@omerg7493/pythons-data-class-59098f4a2044

@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)
    
    def to_dict(self):
        return asdict(self)
