class Message(object):
    """A message sent in a channel this bot has a presence in

    Attributes:
        id: The internal message ID
        channel_id: The channel the message was sent in
        user_id: The author of the message
        timestamp (float): The time this message was sent
            (seconds since 1970-01-01)
        body (str): The contents of the message
    """

    def __init__(self, id, channel_id, user_id, timestamp, body):
        self.id = id
        self.channel_id = channel_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.body = body


class Reply(object):
    """A reply to another message in a channel

    Attributes:
        id: The internal message ID
        message_id: The message being replied to
        user_id: The author of the message
        timestamp (float): The time this message was sent
            (seconds since 1970-01-01)
        body (str): The contents of the message
    """

    def __init__(self, id, message_id, user_id, timestamp, body):
        self.id = id
        self.message_id = message_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.body = body


class Reaction(object):
    """A reaction to a message

    Attributes:
        id: The internal reaction ID
        message_id: The message being reacted to
        user_id: The user giving the reaction
        timestamp (float): The time the reaction was added
            (seconds since 1970-01-01)
        emoji (str): The name of the emoji used
    """

    def __init__(self, message_id, user_id, timestamp, emoji):
        self.message_id = message_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.emoji = emoji


class FileUpload(object):
    """A file was uploaded to a channel

    Attributes:
        id: The internal file ID
        channel_id: The channel the file was uploaded to
        user_id: The user who uploaded the file
        timestamp (float): The time the file was uploaded
            (seconds since 1970-01-01)
    """

    def __init__(self, id, channel_id, user_id, timestamp):
        self.id = id
        self.channel_id = channel_id
        self.user_id = user_id
        self.timestamp = timestamp


class Command(object):
    """A bot command was issued

    Attributes:
        id: The internal message ID
        channel_id: The channel the command was issued from
        user_id: The user who issued the command
        timestamp (float): The time the command was issued
            (seconds since 1970-01-01)
        command (str): The command that was issued
        args (list of str): The arguments to the command
    """

    def __init__(self, id, channel_id, user_id, timestamp, command, args):
        self.id = id
        self.channel_id = channel_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.command = command
        self.args = args


class Typing(object):
    """A user has started or stopped typing

    Attributes:
        user_id: The user who started or stopped typing
        channel_id: The channel the user is/was typing in
        typing (bool): True if the user started or False if the user stopped
        timestamp (float): The time the user started/stopped typing
            (seconds since 1970-01-01)
    """

    def __init__(self, user_id, channel_id, typing, timestamp):
        self.user_id = user_id
        self.channel_id = channel_id
        self.typing = typing
        self.timestamp = timestamp


class StatusChange(object):
    """A user has changed their status

    Attributes:
        user_id: The user whose status has changed
        status: The new status of the user
        timestamp (float): The time the user changed to this status
            (seconds since 1970-01-01)
    """

    def __init__(self, user_id, status, timestamp):
        self.user_id = user_id
        self.status = status
        self.timestamp = timestamp
