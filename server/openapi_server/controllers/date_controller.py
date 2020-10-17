from openapi_server.models.error import Error  # noqa: E501
# from openapi_server.models.date_annotation import DateAnnotation  # noqa: E501
# from openapi_server.models.page_response import PageResponse  # noqa: E501
# from openapi_server.models.user import User
import openapi_server.db_connection as db
from flask import jsonify
from openapi_server.util.configuration import Config


def dates_read_all(limit=None, offset=None):  # noqa: E501
    """Get all date annotations

    Returns the date annotations # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: PageResponse
    """
    res = None
    try:
        values = db.load_config()

        conn = db.get_connection_local_pg(values)
        cursor = conn.cursor()
        select_anno = "SELECT id, noteid , start ,  stop - start as len, " \
            "text, category, type from i2b2_data.public.pat_annotations " \
            "where category = 'DATE' LIMIT %s OFFSET %s"
        cursor.execute(select_anno, (limit, offset))
        all_rows = cursor.fetchall()
        items = []
        for row in all_rows:
            id = row[0]
            # userCreated = User(username="unknown", first_name="Unknown",
            #                    last_name="User")
            # userUpdated = User(username="unknown", first_name="Unknown",
            #                    last_name="User")
            # 'createdBy' : userCreated , 'updatedByBy' : userUpdated
            items.append({'id': id, 'noteId': row[1], 'start':  row[2],
                          'length':  row[3], 'text': str(row[4]),
                          'category': str(row[5]),  'type': str(row[6])})
            # items.append(DateAnnotation(id, row[1], row[2], row[3], row[4],
            #                             ''))

        # Set next url to empty if this is the last page
        next = ""
        if len(all_rows) == limit:
            next = "%s/annotations/dates?limit=%s&offset=%s" % \
                (Config().server_api_url, limit, offset + limit)

        res = {'links': next, 'items': items}
    except Exception as error:
        res = Error(None, "Internal error", 500, str(error))
    finally:
        cursor.close()
        conn.close()

    return jsonify(res)
