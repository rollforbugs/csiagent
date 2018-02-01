import abc


class Service(abc.ABC):
    """A backend chat service."""

    @abc.abstractmethod
    def connect(self):
        """Connect to the service."""
        raise NotImplementedError

    @abc.abstractmethod
    def disconnect(self):
        """Disconnect from the service."""
        raise NotImplementedError

    @abc.abstractmethod
    def supports(self, event_cls):
        """Check if a given event type is supported by the service."""
        return False

    @abc.abstractmethod
    def send(self, channel_id, body):
        """Send a message in a channel.

        Args:
            channel_id: The ID of the channel to post to.
            body: The message body.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def reply(self, message_id, body):
        """Reply to another message.

        Args:
            message_id: The ID of the message to reply to.
            body: The body of the reply.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def react(self, message_id, emoji):
        """Add an emoji reaction to a message.

        Args:
            message_id: The ID of the message to react to.
            emoji: The name of the emoji to react with.
                This can be a standard emoji or custom if there is support.

        Raises:
            ValueError: If the emoji name is invalid for the service.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def status(self, status=None, message=None):
        """Change the status of the bot user.

        Args:
            status: The status of the bot user, if supported.
            message: The status message, if supported.

        Raises:
            ValueError: If the service has no reasonable mapping for the status.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def upload(self, channel_id, file, comment=None):
        """Upload a file to the service.

        Args:
            channel_id: The ID of the channel to upload to.
            file: The file or data to upload.
            comment: A comment on the file, if there is support.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def download(self, file_id, path=None):
        """Download a file from the service.

        Args:
            file_id: The ID of the file to download.
            path: A path to save the file to.
                If None, this method returns the file's raw bytes.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def poll(self):
        """Retrieve new events from the service."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def users(self):
        """Enumerate the users on the service."""
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def channels(self):
        """Enumerate the channels on the service."""
        raise NotImplementedError
