from .LoadableObject import LoadableObjectBase, LoadableObjectContainer, LoadableTypeEnum

class GuildUpgradeCost:
    def __init__(self, json=None):
        self.type = None
        self.name = None
        self.count = None
        self.item = None

        if(json is not None):
            self.populate(json)

    def populate(self, json):
        self.type = json.get("type", None)
        self.name = json.get("name", None)
        self.count = json.get("count", None)

        if("item_id" in json):
            self.item = LoadableObjectContainer(json["item_id"], LoadableTypeEnum.Item)

class GuildUpgrade(LoadableObjectBase):
    def __init__(self, id):
        self.id = id
        self.name = None
        self.description = None
        self.type = None
        self.icon = None
        self.build_time = None
        self.required_level = None
        self.experience = None
        self.prerequisites = []
        self.costs = []

    def _populate_inner(self, json):
        self.name = json.get("name", None)
        self.description = json.get("description", None)
        self.type = json.get("type", None)
        self.icon = json.get("icon", None)
        self.build_time = json.get("build_time", None)
        self.required_level = json.get("required_level", None)
        self.experience = json.get("experience", None)

        if("prerequisites" in json):
            for prereq_data in json["prerequisites"]:
                self.prerequisites.append(LoadableObjectContainer(prereq_data, LoadableTypeEnum.GuildUpgrade))

        for cost_data in json["costs"]:
            self.costs.append(GuildUpgradeCost(cost_data))

class Guild(LoadableObjectBase):
    def __init__(self, id):
        self.id = id
        self.motd = None
        self.influence = None
        self.aetherium = None
        self.favor = None
        self.name = None
        self.tag = None

    def _populate_inner(self, json):
        self.motd = json.get("motd", None)
        self.influence = json.get("influence", None)
        self.aetherium = json.get("aetherium", None)
        self.favor = json.get("favor", None)
        self.name = json.get("name", None)
        self.tag = json.get("tag", None)
