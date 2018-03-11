from abc import ABCMeta, abstractmethod
from enum import Enum
from .LoadableObject import LoadableObjectBase, LoadableObjectContainer, LoadableTypeEnum

class LogTypeEnum(Enum):
    Joined = "joined"
    Invited = "invited"
    Kicked = "kicked"
    RankChanged = "rank_change"
    Treasury = "treasury"
    Stash = "stash"
    Motd = "motd"
    Upgrade = "upgrade"
    Influence = "influence"

class LogEntry(metaclass=ABCMeta):
    def __init__(self, id, json=None):
        self.id = id
        self.time = None
        self.type = None
        self.user = None

        if(json is not None):
            self.populate(json)

    def populate(self, json):
        self.time = json.get("time", None)
        self.type = json.get("type", None)
        self.user = json.get("user", None)
        self._populate_inner(json)

    @abstractmethod
    def _populate_inner(self, json):
        raise NotImplementedError()

class LogUnknown(LogEntry):
    def __init__(self, id, json=None):
        super().__init__(id, json)

    def _populate_inner(self, json):
        pass

class LogEntryJoined(LogEntry):
    def __init__(self, id, json=None):
        super().__init__(id, json)

    def _populate_inner(self, json):
        pass

class LogEntryInfluence(LogEntry):
    def __init__(self, id, json=None):
        self.activity = None
        self.total_participants = None
        self.participants = []
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.activity = json.get("activity", None)
        self.total_participants = json.get("total_participants", None)
        self.participants = json.get("participants", [])

class LogEntryInvited(LogEntry):
    def __init__(self, id, json=None):
        self.invited_by = None
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.invited_by = json.get("invited_by", None)

class LogEntryKicked(LogEntry):
    def __init__(self, id, json=None):
        self.kicked_by = None
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.kicked_by = json.get("kicked_by", None)

class LogEntryRankChanged(LogEntry):
    def __init__(self, id, json=None):
        self.changed_by = None
        self.old_rank = None
        self.new_rank = None
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.changed_by = json.get("changed_by", None)
        self.old_rank = json.get("old_rank", None)
        self.new_rank = json.get("new_rank", None)

class LogEntryTreasury(LogEntry):
    def __init__(self, id, json=None):
        self.item = None
        self.count = None
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.item = LoadableObjectContainer(json["item_id"], LoadableTypeEnum.Item)
        self.count = json.get("count", None)

class LogEntryStash(LogEntry):
    def __init__(self, id, json=None):
        self.operation = None
        self.item = None
        self.count = None
        self.coins = None
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.operation = json.get("operation", None)
        self.item = LoadableObjectContainer(json["item_id"], LoadableTypeEnum.Item) if json.get("item_id", 0) != 0 else None
        self.count = json.get("count", None)
        self.coins = json.get("coins", None)

class LogEntryMotd(LogEntry):
    def __init__(self, id, json=None):
        self.motd = None
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.motd = json.get("motd", None)

class LogEntryUpgrade(LogEntry):
    def __init__(self, id, json=None):
        self.action = None
        self.upgrade = None
        self.recipe_id = None
        super().__init__(id, json)

    def _populate_inner(self, json):
        self.action = json.get("action", None)
        self.upgrade = LoadableObjectContainer(json["upgrade_id"], LoadableTypeEnum.GuildUpgrade)
        self.recipe_id = json.get("recipe_id", None)
