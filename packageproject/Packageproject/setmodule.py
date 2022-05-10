from collections.abc import Iterable
import logging
logging.basicConfig(filename="set_module.log", level = logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')


class  SetMethods:
    def __init__(self,s):
        """ Initializing set values"""
        try:
            if type(s) == set:
                self.s = s
                logging.info(f"Set Object created with value : {s}")
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set : {s}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def add_set(self,x):
        """ This method will add an element to a set"""
        try:
            l = list(self.s)
            l.append(x)
            self.s = set(l)
            logging.info(f"Element {x} is added to the set")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def clear_set(self):
        """This method will remove all elements from this set"""
        try:
            self.s = set()
            logging.info("Set is now empty")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def copy_set(self):
        """ This method will return a shallow copy of a set"""
        try:
            logging.info("Returned a shallow copy of the set..")
            l = list(self.s)
            return set(l)
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def difference_set(self,set2):
        """ This method will return the difference of two or more sets as a new set"""
        try:
            if type(set2) == set:
                s1 = set()
                for i in self.s:
                    if i not in set2:
                        s1.add(i)
                logging.info(f"Difference of sets {self.s} and {set2} : {s1}")
                return s1
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def difference_update_set(self, set2):
        """This method will remove all the elements of another set from this set"""
        try:
           if type(set2) == set:
               self.s = self.difference_set(set2)
               logging.info("Difference updates of sets is assigned to original set")
           else:
               logging.error("Raising exception since set is not passed")
               raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
        logging.exception(str(e))

    def discard_set(self,x):
        """This method will remove an element from a set if it is a member.
        if the element is not a member do nothing"""
        try:
            if x in self.s:
                self.s = self.difference_set({x})
                logging.info(f"Discard element {x} from the sets")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def intersection_set(self,set2):
        """ This method will return the intersection of two or more sets as a new set"""
        try:
            if type(set2) == set:
                s1 = set()
                for i in self.s:
                    if i in set2:
                        s1.add(i)
                logging.info(f"intersection of sets {self.s} and {set2} : {s1}")
                return s1
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def intersection_update_set(self, set2):
        """This method will update a set with the intersection itself"""
        try:
           if type(set2) == set:
               self.s = self.intersection_set(set2)
               logging.info("Intersection updates of sets is assigned to original set")
           else:
               logging.error("Raising exception since set is not passed")
               raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
        logging.exception(str(e))

    def isdisjoint_set(self,set2):
        """ This method will return True if two sets have a null intersection"""
        try:
            if type(set2) == set:
                s = self.intersection_set(set2)
                logging.info(f"Checking if {self.s} and {set2} are disjoint or not")
                return False if s else True
            else:
                logging.error("Raising Exception since set is not passed")
                raise Exception (f" You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def issubeset_set(self,set2):
        """
        This method will check whether another set contains this set
        """
        try:
            logging.info(f"Checking if {self.s} is a subset of {set2} or not")
            if type(set2) == set:
                flag = 0
                for i in self.s:
                    if i not in set2:
                        flag = 1
                return False if flag == 1 else True
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set : {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))


            ##There are many other methods, we are just trying to understand how packages and modules work here, in a structured way
            ##This can also be called as modular coding