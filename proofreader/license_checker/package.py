

class Package(object):

    LICENSE_TAG = 'License: '
    NAME_TAG = 'Name: '
    _meta_data = []

    def __init__(self, pkg_obj):
        # type: ('pkg_resources.DistInfoDistribution') -> None
        """
        :param pkg_obj: :class: `pkg_resources.DistInfoDistribution`
        """
        self._pkg_obj = pkg_obj

    def _extract_meta_value(self, tag):
        # type: (str, List[str]) -> str
        """Find a target value by `tag` from given meta data.

        :param tag: str
        :param meta_data: list
        :return: str
        """
        try:
            return [l[len(tag):] for l in self.meta_data if l.startswith(tag)][0]
        except IndexError:
            return '* Not Found *'

    @property
    def license(self):
        # type: () -> str
        return self._extract_meta_value(self.LICENSE_TAG)

    @property
    def meta_data(self):
        # type: () -> List[str]
        if not self._meta_data:
            for tag in ['METADATA', 'PKG-INFO']:
                try:
                    self._meta_data = list(self._pkg_obj.get_metadata_lines(tag))
                except (IOError, KeyError):
                    pass

        return self._meta_data

    @property
    def name(self):
        # type: () -> str
        return self._extract_meta_value(self.NAME_TAG)

    @property
    def version(self):
        # type: () -> str
        return self._pkg_obj.version or ''
