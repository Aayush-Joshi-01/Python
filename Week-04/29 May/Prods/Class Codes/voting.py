class Voters:
    variable = "Variable"

    def __init__(self, name: str, voter_id: int, state: str, district: str) -> None:
        self.r_id = id(self)
        self.name = name
        self.voter_id = voter_id
        self.state = state
        self.district = district
        self.vote = None

    def __str__(self) -> str:
        return f"{self.r_id} {self.name} {self.voter_id} {self.state} {self.district}"


voter1 = Voters("aayush", 1100673, "Madhya Pradesh", "Ujjain")
voter2 = Voters("prankur", 110000, "Uttar Pradesh", "Ghaziabad")
