class NHTSAClient(object):
    """
    The HTTP client that interacts with the National
    Highway Traffic Safety Administration's APIs in
    order to provide programmatic access to them. This
    class contains the logic for interacting with that API
    using Python.
    """

    DEFAULT_API_PATH = 'http://www.nhtsa.gov/webapi/'

    def __init__(self, api_path=None):
        """
        Creates a new instance of the NHTSAClient. Takes an argument
        allowing to change the base API URL (for proxies, etc.)

        :param api_path: The API base path (for generating URLs)
        :type api_path: str
        """

        # Use the parameter if provided, otherwise use the default
        self.api_path = api_path if api_path else self.DEFAULT_API_PATH

    @property
    def model_years(self):
        """
        Returns a list of years that data is available for
        at the NHTSA.

        :return: A list of years
         :rtype: list
        """

        return None

    def makes(self, year=None):
        pass

    def models(self, make, year=None):
        pass

    def recalls_from_campaign(self, campaign_number):
        pass

    @property
    def recalls(self):
        # TODO: Implement me

        return None

    def get_recalls(self, year, make, model):
        """

        :param make:
        :param year:
        :return:
        """

        pass

    def locate_safety_seat_inspection(self, location, speaks_spanish=False):
        by_state = False

        if len(location) == 2:
            by_state = True

        pass

    def locate_safety_seat_inspection_from_pos(self, lat, lon, miles=50):
        pass

    def complaints(self):
        """
        Returns a full list of all vehicle complaints
        :return:
        """
        pass

    def get_complaint_odi(self, odi):
        """
        Looks up a list of complaints based off the ODI number.

        :param odi: The ODI identifier

        :return: The Complaint object
        :rtype: nhtsa.data.Complaint
        """

        pass

    def get_complaints(self, year, make, model):
        """
        Returns all vehicle complaints for a specific car model's year.

        :param year: The production year
        :param make: The car manufacturer
        :param model: The car model

        :return: A list of complaints
         :rtype: list
        """

        pass

    def penalities(self, year=None):
        """
        Returns information about civil penalties handed to car manufacturers
        for failing to comply with Federal law, usually with withholding/delaying
        a recall.

        :param year: The fiscal year to look up

        :return: nhtsa.data.PenaltyData
        """

        if not year:
            pass

        pass

    def ratings(self, variant):
        """
        Returns information about the NHTSA's 5-Star safety rating system,
        containing information about every single model of every car.

        In order to use this however, you must find the variant name with
        the make, model, and year information you have.

        Example:

            client = NHTSAClient()
            variants = client.get_model_variants('2009', 'Toyota', 'Prius')

            variant = variants[0] # [] => nhtsa.data.ModelVariant
            ratings = client.ratings(variant.id)

            print(ratings[0])
            # <VehicleRating[5346]: '2009 Toyota Prius 4-DR.w/SAB'>

        :param variant: The variant of the car model
        :type variant: nhtsa.data.ModelVariant

        :return: A list of CrashRating objects
        :rtype: list
        """

        pass

    def get_model_variants(self, year, make, model):
        """
        Returns a list of ModelVariants that contain both the name of the
        variant and it's NHTSA ID.

        :param year: The production year
        :param make: The car manufacturer
        :param model: The car model

        :return: A list of ModelVariants
         :rtype: list
        """

        pass
