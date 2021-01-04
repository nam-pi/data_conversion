"""The module for the Nampi data entry form sheet and related classes.

Classes:
    Column: Headings for columns in the Google sheet.
    Table: Names of the available tables.
    Nampi_data_entry_form: The data entry form wrapper class

"""
from modules.google_sheet import Google_sheet
from modules.no_value import NoValue


class Table(NoValue):
    """Names of the available tables."""

    AUTHORS = "Authors"
    BIRTHS = "Births"
    COMPLEX_EVENTS = "Complex Events"
    DEATHS = "Deaths"
    EVENT_DEFINITIONS = "Event Definitions"
    GROUPS = "Groups"
    OBJECT_CREATIONS = "Object Creations"
    OBJECTS = "Objects"
    OCCUPATIONS = "Occupations"
    PERSONS = "Persons"
    PLACES = "Places"
    SOURCES = "Sources"
    STATUSES = "Statuses"
    TITLES = "Titles"


class Column:
    """Headings for the columns in the available tables."""

    added_status = "Added Status"
    author = "Author"
    comment = "Comment"
    community_astheim = "Community Astheim"
    community_gaming = "Community Gaming"
    earliest_date = "Earliest Possible Date"
    event_definition = "Event Definition"
    event_place = "Event Place"
    exact_date = "Exact Date"
    family_name = "Family name"
    family_name_gender_neutral = "Family Name Gender Neutral Form"
    family_name_with_group = "Family with Group"
    gender = "Gender"
    geoname_id = "Geonames-ID"
    given_name = "Given name"
    gnd_id = "GND ID"
    interpretation_date = "Interpretation Date"
    is_a = "Is a"
    latest_date = "Latest Possible Date"
    name = "Name"
    part_of = "Part of"
    person = "Person"
    religious_name = "Religious name"
    removed_status = "Removed Status"
    source = "Source"
    source_location = "Source Location"
    started_occupation = "Started Occupation"
    status_occupation_in_group = "Status/Occupation in Group"
    stopped_occupation = "Stopped Occupation"
    title = "Title"
    type = "Type"
    wikidata = "Wikidata"


class Nampi_data_entry_form(Google_sheet):
    """Wrapper around the tables of the NAMPI data entry form on Google sheets."""

    def __init__(
        self,
        cache_path: str,
        credentials_path: str,
        cache_validity_days: int,
    ):
        """Initialize the class.

        Parameters:
            cache_path: The path to cache the individual tables so they do not need to be refetched on each execution of the script. Needs to exist.
            credentials_path: The path to the Google Service Account credentials to access Google Sheets. Needs to exist.
            cache_validity_days: The number of days cached files stay valid and are not refetched.
        """
        super().__init__(
            "NAMPI Data Entry Form v2",
            cache_path,
            credentials_path,
            cache_validity_days,
            Table,
        )
