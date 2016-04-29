class Car(object):
    def __init__(self, year, make=None, model=None):
        """
        Creates a new Car object, which can represent either only
        a model year, a type of make in that year, or a specific car model
        (having all model, make, year filled out).

        :param year: The manufacture year
        :param make: The car manufacturer
        :param model: The model of the car
        """

        if not isinstance(year, int):
            raise AttributeError('Year must be an integer')

        self.year = year
        """ int: The model year """

        self.make = make
        """ str: The car manufacturer identifier """

        self.model = model
        """ str: The model name, ex: Honda _Civic_ """

    @property
    def is_complete(self):
        """
        A car object is only considered complete if it has completed
        and valid year, make, and model data.

        :return: The car is a complete object
         :rtype: bool
        """

        return (None not in [self.year, self.make, self.model])
