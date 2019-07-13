from enum import IntEnum, unique


@unique
class MentorCategory(IntEnum):
    """
    멘토 카테고리
    """
    JOB = 0
    ENTREPRENEUR = 1
    
    @classmethod
    def choices(cls):
        return (
            (cls.JOB.value, '취업'),
            (cls.ENTREPRENEUR.value, '창업'),
        )
