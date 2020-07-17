"""Classes for melon orders."""

import random

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    


    #Splurge Pricing
    def get_base_price(self):
        """Calculates base price using splurge pricing"""

        base_price = random.randrange(5, 10)

        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price


        #Price for christmas melons
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        #Flat fee of $3 for all international orders with less than 10 melons
        if self.order_type == "international" and self.qty < 10:
            total += 3

        #Splurge Pricing Total
        if 




        return total



    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government melon order"""
    order_type = "government"
    tax = 0

    def __init__(self, species, qty, passed_inspection):
        """Initialize Govt melon order attributes"""

        self.species = species
        self.qty = qty
        self.passed_inspection = False



    def mark_inspection(self, passed):
        """Marks that Govt melon has been inspected"""
        
        self.passed_inspection = passed

