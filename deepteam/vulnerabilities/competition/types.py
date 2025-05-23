from enum import Enum
from typing import Literal


class CompetitionType(Enum):
    COMPETITOR_MENTION = "competitor mention"
    MARKET_MANIPULATION = "market manipulation"
    DISCREDITATION = "discreditation"
    CONFIDENTIAL_STRATEGIES = "confidential strategies"


CompetitionTypes = Literal[
    CompetitionType.COMPETITOR_MENTION.value,
    CompetitionType.MARKET_MANIPULATION.value,
    CompetitionType.DISCREDITATION.value,
    CompetitionType.CONFIDENTIAL_STRATEGIES.value,
]
