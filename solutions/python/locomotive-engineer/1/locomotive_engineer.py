"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *list_of_wagons, = args
    
    return list_of_wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_wagon, second_wagon, *others = each_wagons_id

    *repositioned_wagons, = *others, first_wagon, second_wagon

    id_1, *other_ids = repositioned_wagons

    *final_list, = id_1, *missing_wagons, *other_ids

    return final_list


def add_missing_stops(routing_dict, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    all_stops = []
  
    for stop in kwargs:

        all_stops.append(kwargs[stop])
    
    stop_dict = {'stops': all_stops}

    combined_route_info = {**routing_dict, **stop_dict}

    return combined_route_info


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    red, blue, orange = wagons_rows
    r0, r1, r2 = red
    b0, b1, b2 = blue
    o0, o1, o2 = orange
    r0w_0 = [r0, b0, o0]
    row_1 = [r1, b1, o1]
    row_2 = [r2, b2, o2]
    correct_rows = [r0w_0, row_1, row_2]
    return correct_rows
