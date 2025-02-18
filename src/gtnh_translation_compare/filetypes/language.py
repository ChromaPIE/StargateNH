from enum import Enum
from typing import List


class Language(Enum):
    en_US = "en_US"
    zh_CN = "zh_CN"

    @classmethod
    def from_str(cls, s: str) -> "Language":
        return cls(s)

    @classmethod
    def values(cls) -> List[str]:
        return [_.value for _ in cls.__members__.values()]

    @classmethod
    def values_except_en_us(cls) -> List[str]:
        return [_.value for _ in cls.__members__.values() if _ != cls.en_US]
