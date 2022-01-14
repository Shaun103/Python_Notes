from dataclasses import dataclass

@dataclass
class datainfo1:
    id: str
    parent: str
    title: str
    category: str

@dataclass
class datainfo2:
    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    # date: datetime.datetime