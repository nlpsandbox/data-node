from mongoengine import Document
import pprint
import six


class BaseDocument(Document):
    meta = {
        'abstract': True
    }

    # def to_dict(self):
    #     """Returns the model properties as a dict

    #     :rtype: dict
    #     """
    #     result = {}

    #     for attr, _ in six.iteritems(self.openapi_types):
    #         value = getattr(self, attr)
    #         if isinstance(value, list):
    #             result[attr] = list(map(
    #                 lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
    #                 value
    #             ))
    #         elif hasattr(value, "to_dict"):
    #             result[attr] = value.to_dict()
    #         elif isinstance(value, dict):
    #             result[attr] = dict(map(
    #                 lambda item: (item[0], item[1].to_dict())
    #                 if hasattr(item[1], "to_dict") else item,
    #                 value.items()
    #             ))
    #         else:
    #             result[attr] = value

    #     return result

    # def to_str(self):
    #     """Returns the string representation of the model

    #     :rtype: str
    #     """
    #     return pprint.pformat(self.to_dict())

    # def to_json(self):
    #     return {}
    #     # return {
    #     #     "_id": str(self.pk),
    #     #     "first_name": self.first_name,
    #     #     "last_name": self.last_name,
    #     #     "username": self.username,
    #     #     "password": self.password
    #     # }
