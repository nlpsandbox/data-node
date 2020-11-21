from flask import jsonify

from openapi_server.models.service import Service  # noqa: E501


def service():  # noqa: E501
    """Get service information
    Get information about the service # noqa: E501
    :rtype: Service
    """
    service = Service(
        name="data-node",
        version="0.2.1",
        license="Apache-2.0",
        repository="github:nlpsandbox/data-node",
        description="NLP Sandbox Data Node",
        author="The NLP Sandbox Team",
        author_email="thomas.schaffter@sagebionetworks.org",
        url="https://github.com/nlpsandbox/data-node"
    )

    return jsonify(service), 200
