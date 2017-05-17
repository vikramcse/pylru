import lrull


class TestLru:
    def __init__(self):
        self.capacity = 3
        self.cache = lrull.LRUCache(capacity=self.capacity)

    # the cache should be empty initially
    def test_check_empty(self):
        assert len(self.cache) == 0

    def test_check_size_after_adding_data(self):
        self.cache["name"] = "john"
        self.cache["surname"] = "martin"
        self.cache["city"] = "mumbai"

        len(self.cache) == 3

    def test_check_set_method(self):
        self.cache.set("name", "john")
        self.cache.set("surname", "martin")
        self.cache.set("city", "mumbai")

        len(self.cache) == 3

    def test_get_the_value_from_cache(self):
        self.cache.set("name", "john")
        self.cache.set("surname", "martin")
        self.cache.set("city", "mumbai")

        value = self.cache.get("name")
        assert value == 'john'

        value = self.cache.get("city")
        assert value == 'mumbai'

    def test_check_overflow_cahche(self):
        self.cache.set("name", "john")
        self.cache.set("surname", "martin")
        self.cache.set("city", "mumbai")
        self.cache.set("country", "India")
        self.cache.set("married", "no")

        assert len(self.cache) == 3
        assert self.cache.get("name") == -1
        assert self.cache.get("surname") == -1
        assert self.cache.get("married") == 'no'

    def test_get_default_element_when_element_is_not_present(self):
        self.cache.set("name", "john")
        self.cache.set("surname", "martin")
        self.cache.set("city", "mumbai")

        self.cache.get("town", "element no present") == "element no present"
        self.cache.get("town", None) is None
