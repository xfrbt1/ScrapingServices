from reader_consumer.client.module_func import read_store_func
from reader_consumer.core.settings import settings as s

if __name__ == "__main__":
    settings = s()
    read_store_func(settings)
