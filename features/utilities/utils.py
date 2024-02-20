def search_in_list(field_to_search, value_to_search, list_where_search):
    filter_result_list = []
    for e in list_where_search:
        if e[field_to_search] == value_to_search:
            filter_result_list.append(e)
    return filter_result_list

