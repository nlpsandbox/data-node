import connexion
import six

from openapi_server.models.date_annotation import DateAnnotation  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server import util
import openapi_server.db_connection as db
from flask import jsonify
import json

def dates_read_all( ):  # noqa: E501
    """Get all date annotations

    Returns the date annotations # noqa: E501

    :param note: 
    :type note: list | bytes

    :rtype: List[DateAnnotation]
    """
    # if connexion.request.is_json:
    #     note = [Note.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    # return 'do some magic!'

    """Get a clinical note by ID

     Returns the clinical note for a given ID # noqa: E501

     :param id: The ID of the clinical note to fetch
     :type id: str

     :rtype: Note
     """
    values = db.load_config()

    conn = db.get_connection_local_pg(values)
    cur = conn.cursor()
    select_anno = 'SELECT id, noteid , start ,  stop - start as len, text, category, type from  i2b2_data.public.pat_annotations where category = \'DATE\' '
    cur.execute(select_anno  )
    all_rows = cur.fetchall()
    res = []
    for row in all_rows:
        id = row[0]
        dict = {'id': id, 'noteId': row[1] , 'start':  row[2] ,  'length':  row[3] , 'text': str(row[4]),  'category': str(row[5]),  'type': str(row[6])}
        res.append(dict)

    return jsonify(res)
