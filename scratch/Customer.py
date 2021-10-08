class Customer:
    def __init__(self, fname, sname, tier=('free', 0)):
        self.fname = fname
        self.sname = sname
        self.tier = tier

    @property
    def name(self):
        return ' '.join([self.fname, self.sname])

    @classmethod
    def premium(cls, fname, sname):
        return cls(fname, sname, tier=('premium', 10))

    def can_access(self, check):
        return False if self.tier == 'free' and check['tier'] == 'premium' else True

    def bill_for(self, months):
        return self.tier[1] * months


if __name__ == '__main__':
    # This won't run until you implement the `Customer` class!

    marco = Customer('Marco', 'Polo')  # Defaults to the free tier
    print(marco.name)  # Marco Polo
    print(marco.can_access({'tier': 'free', 'title': '1812 Overture'}))  # True
    print(marco.can_access(
        {'tier': 'premium', 'title': 'William Tell Overture'}))  # False

    # Build a customer around the ('premium', 10$/mo) streaming plan.
    victoria = Customer.premium("Alexandrina", "Victoria")
    print(victoria.can_access(
        {'tier': 'free', 'title': '1812 Overture'}))  # True
    print(victoria.can_access(
        {'tier': 'premium', 'title': 'William Tell Overture'}))  # True
    print(victoria.bill_for(5))  # => 50 (5 months at 10$/mo)
    print(victoria.name)  # Alexandrina Victoria
