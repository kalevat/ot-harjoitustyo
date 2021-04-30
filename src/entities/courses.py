class Courses:
    """Kurssitiedoista vastaava luokka"""

    def __init__(self, course_name, credit, date):
        """Luokan konstruktori

        Args:
            course_name: kurssin nimi
            credit: opintopisteet
            date: tenttipäivämäärä
        """

        self.course_name = course_name
        self.credit = credit
        self.date = date
