# %% tags=["keep"]
from dataclasses import dataclass


@dataclass
class Project:
    name: str
    assets: float
