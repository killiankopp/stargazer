def extract_field(datas, field):
    return [data.get(field) for data in datas if field in data]
