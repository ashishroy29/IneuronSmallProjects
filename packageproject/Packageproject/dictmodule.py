from collections.abc import Iterable
import logging
logging.basicConfig(filename="dict_module.log", level = logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')

class DictMethods:
    def __init__(self,d):
        """
        Initializing dict values
        """
        try:
            if type(d) == dict:
                self.d = d
                logging.info(f"Dictionary object created with value : {d}")
            else:
                logging.error("Raising exception since dictionary is not passed")
                raise Exception(f"You have not entered a dictionary :  {d}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def clear_dict(self):
        """
        This method will remove all items from dictionary
        """
        try:
            self.d = {}
            logging.info("Dictionary object Cleared")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def copy_dict(self):
        """ This method will return a shallow copy of the dict """
        try:
            new_dict = {}
            for k in self.d:
                new_dict[k] = self.d[k]
            logging.info("Created shallow copy of the dictionary")
            return dict
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def fromkeys_dict(self, it, v = None):
        """ This method will create a new dictionary with keys from iterable and values set to value. """
        try:
            if isinstance(it, Iterable):
                d = dict()
                for i in it:
                    d[i] = v
                logging.info(f"Dictionary: {d} Created from iterable {it}")
                return d
            else:
                logging.error("Raising exception since iterable is not passed")
                raise Exception (f"You have not entered a iterable: {it}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def get_dict(self,x,y = None):
        """ This function returns the value for key if key is in the dictionary, else returns default"""
        try:
            for k in self.d :
                if x == k:
                    y = self.d[x]
            logging.info(f"{y} is found in the dictionary: {self.d}")
            return y
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def items_dict(self):
        """
        This function returns list of tuples of key value pair
        """
        try:
            logging.info("Items_dict returns list of tuples of key value pair")
            return [(k,self.d[k]) for k in self.d]
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def keys_dict(self):
        """ This function returns list of keys """
        try:
            logging.info("Keys_dict returns list of keys")
            return [k for k in self.d]
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def values_dict(self):
        """
        This function returns list of values
        """
        try:
            logging.info("Values_dict returns list of values")
            return [self.d[k]for k in self.d]
        except Exception as e :
            print(e)
            logging.exception(str(e))

    def update_dict(self,x= None, **kwargs):
        """
        D.Update([x. ]**kwargs) -> None. Update D from dict/iterable x and kwargs.
        if x is present and has a.keys() method, then does: for k in x:d[k] = E[k]
        if x is present and lacks a.keys() method, then does: for k, v in x : D[k] = v
        in either case, this is followed by: for k in F: D[k] = F[k]
        """
        try:
            if x :
                if type(x) == dict:
                    for i in x:
                        self.d[i] = x[i]
                    logging.info(f"dictionary is updated with dict: {x}")
                else:
                    raise Exception(f"You have not entered a dictionary: {x}")
            if kwargs:
                for i in kwargs:
                    self.d[i] = kwargs[i]
                logging.info(f"dictionary is updated with kwargs : {kwargs}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def set_default(self,k,v = None):
        """This method will insert key with a value of default if key is not in the dictionary and return the value of keys
        if key is in the dictionary"""
        try:
            logging.info(f"parameter passed in setdefault_dict() are : {k},{v}")
            if k in self.d:
                return self.d[k]
            else:
                if v :
                    self.d[k] = v
                    return v
                else:
                    self.d[k] = None
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def pop_dict(self, k, v = None):
        """ This method will remove specified key and return the corresponding value.
        if key is not found, v is returned if given, otherwise key error is raised"""
        try:
            logging.info(f"parameter passed in pop_dict are: {k},{v}")
            for k in self.d:
                x = self.d[k]
                self.d = {i:self.d[i] for i in self.d if i != k}
                logging.info(f"item ({k},{x}) is popped out of the dictionary")
                return x
            else:
                if v:
                    return v
                else:
                    raise KeyError(f"Key {k} is not found in dictionary: {self.d}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def popitem_dict(self):
        """This function will remove and return some (key, value) pair as a 2 tuple; but raise a key error if D is empty"""
        try:
            k = self.keys_dict()
            c = ()
            if k:
                c = k[-1],seld.d[k[-1]]
                self.d = {i:self.d[i] for i in k[0:-1]}
                logging.info(f"Item ({c}) is popped out of dictionary")
                return c
            else:
                logging.error("Raising exception since dict is empty")
                raise KeyError(f"Dictionary : {self.d} is empty")
        except Exception as e:
            print(e)
            logging.exception(str(e))