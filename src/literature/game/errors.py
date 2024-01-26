from dataclasses import dataclass

from ..cards import Card


class LiteratureError(Exception):
    pass


@dataclass
class ActionError(LiteratureError):
    source_player: int


@dataclass
class TargetPlayerError(ActionError):
    target_player: int


class TargetPlayerSameTeamError(TargetPlayerError):
    pass


class TargetPlayerDeadError(TargetPlayerError):
    pass


class TargetPlayerOpponentTeamError(TargetPlayerError):
    pass


class OutOfTurnError(ActionError):
    turn: int


# Move type specific errors
## Ask errors
@dataclass
class IllegalAskError(ActionError):
    ask: Card


# class IllegalAskSameTeam(IllegalAskError, TargetPlayerSameTeamError):
#     pass

# class IllegalAskPlayerDead(IllegalAskError, TargetPlayerDeadError):
#     pass

# class IllegalAskOutOfTurn(IllegalAskError, OutOfTurnError):
#     pass


## Gift errors
class IllegalGiftError(ActionError):
    pass


# class IllegalGiftPlayerDeadError(IllegalGiftError, TargetPlayerDeadError):
#     pass

# class IllegalGiftOutOfTurnError(IllegalGiftError, OutOfTurnError):
#     pass

# class IllegalGiftDisallowedError(IllegalGiftError):


## Declare errors
@dataclass
class IllegalDeclareError(ActionError):
    extra_cards: list[Card]
    missing_cards: list[Card]
    wrong_cards: map[Card, int]
    opponent_cards: list[Card]
