import logging
logging.basicConfig(filename="dict_module.log", level = logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')

class TupleMethods:
    def __init__(self,t):
        """ Initializing tuple values """
        try:
            if type(t) == tuple:
                self.t = t
                logging.info(f"Tuple object created with value: {t}")
            else:
                logging.error("Raising exception since tuple is not passed")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def count_tuple(self,x):
        """ This method will return number of occurances"""
        try:
            c=0
            for i in self.t:
                if x == t:
                    c += 1
            logging.info(f"number of occurences of parameter {x} in the tuple : {c}")
            return c
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def index_tuple(self,x):
        """ This method will return the parameter first index """
        try:
            for i , j in enumerate(self.t):
                if x == j:
                    logging.info(f"Parameter: {x} found at position : {i} in the Tuple {self.t}")
                    return i
            raise Exception(f"Parameter: {x} is not found in tuple: {self.t}")
        except Exception as e:
            print(e)
            logging.exception(str(e))
