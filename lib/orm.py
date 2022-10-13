
class ModelMixin:
    def to_dict(self):
        data = {}
        for field in self._meta.fields:
            name = field.attname
            value = self.__dict__[name]
            data[name] = value
        return data