import uuid


def getUUID():
    s_uuid = str(uuid.uuid5(uuid.uuid4(), ''))
    l_uuid = s_uuid.split('-')
    return ''.join(l_uuid)