"""
This type stub file was generated by pyright.
"""

class BaseInstanceLoader:
    """
    Base abstract implementation of instance loader.
    """

    def __init__(self, resource, dataset=...) -> None: ...
    def get_instance(self, row): ...

class ModelInstanceLoader(BaseInstanceLoader):
    """
    Instance loader for Django model.

    Lookup for model instance by ``import_id_fields``.
    """

    def get_queryset(self): ...
    def get_instance(self, row): ...

class CachedInstanceLoader(ModelInstanceLoader):
    """
    Loads all possible model instances in dataset avoid hitting database for
    every ``get_instance`` call.

    This instance loader work only when there is one ``import_id_fields``
    field.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def get_instance(self, row): ...