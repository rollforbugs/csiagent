import enum


@enum.unique
class Status(enum.IntEnum):
    ONLINE = 0
    AWAY = 1
    BUSY = 2
    INVISIBLE = 3
    OFFLINE = 4
