class RelationException(Exception):
    def __init__(self,p1,p2):
        self.per1=p1
        self.per2=p2
    def __str__(self):
        return  self.p1, self.p2

try:
    raise RelationException("Mommy", "Daddy")

except RelationException as e:
    print("Are you sure that", e.per1, "and", e.per2, "are in love with each other?")