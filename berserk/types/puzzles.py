from __future__ import annotations

from enum import Enum

from typing_extensions import TypedDict

from .common import Color


DifficultyLevel = Literal["easiest", "easier", "normal", "harder", "hardest"]


class PuzzleUser(TypedDict):
    id: str
    name: str
    color: Color
    rating: int


class PuzzlePerf(TypedDict):
    key: str
    name: str


class PuzzleGame(TypedDict):
    id: str
    perf: PuzzlePerf
    rated: bool
    players: List[PuzzleUser]
    pgn: str
    clock: str


class PuzzleInfo(TypedDict):
    id: str
    rating: int
    plays: int
    solution: List[str]
    themes: List[str]
    initialPly: int


class PuzzleData(TypedDict):
    game: PuzzleGame
    puzzle: PuzzleInfo


class PuzzleRace(TypedDict):
    # Puzzle race ID
    id: str
    # Puzzle race URL
    url: str


class Difficulty(str, Enum):
    EASIEST = "easiest"
    EASIER = "easier"
    NORMAL = "normal"
    HARDER = "harder"
    HARDEST = "hardest"
