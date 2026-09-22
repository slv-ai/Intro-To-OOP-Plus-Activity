from .student import Student
class HighSchoolStudent(Student):
    def __init__(self,name,grade,classes,parking_privileges = False,clubs= None):
        super().__init__(name,grade,classes)
        self.parking_privileges = parking_privileges
        self.clubs = clubs
    def join_club(self,club_names):
        self.clubs.append(club_names)
        return self.clubs
    def display_parking_message(self):
        has_message = "has parking privileges" if self.parking_privileges else "does not have parking privileges"
        return f"{self.name.capitalize()} {has_message}"
    def display_clubs(self):
            club_str = ", ".join(self.clubs)
            if club_str:
                return f"{self.name.capitalize()} is a member of the following clubs: {club_str}"
            return f"{self.name.capitalize()} is not a member of any clubs."

    def summary(self):
        super().summary()
        parking_message = self.display_parking_message()
        clubs_message = self.display_clubs()
        return "\n" .join([super().summary(), parking_message, clubs_message])

