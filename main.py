#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import time
import sys
import calendar
from os import system
from prettytable import PrettyTable
from categories import Categories


class Receipt():
    """docstring for Receipt"""
    def __init__(self, arg):
        self.month = None
        self.computer_read = False
        l_arg = len(arg)
        system("./congregate.sh")
        try:
            self.month = int(sys.argv[1])
        except:
            try:
                self.month = int(arg[0])
            except:
                self.user_month()
        if (l_arg is 3 and sys.argv[2] == "-c") or l_arg is 2 and arg[1] == "-c":
            self.computer_read = True

        self.fieldheader = None
        self.categories_int, self.categories_names, self.categories_list = Categories().create()
    
    def main(self):
        with open("congregated_input.csv", "r") as input_file:
            reader = csv.DictReader(input_file)
            self.fieldheader = ["Month"] + reader.fieldnames
            self.writeinit()
            for row in reader:
                    if self.nonexpenses(row["Transaktion"].lower()):
                        continue
                    row["Month"] = calendar.month_abbr[time.strptime(row["Datum"], "%Y-%m-%d").tm_mon]
                    row["Kategori"] = self.expenses(row["Transaktion"].lower())
                    row["Belopp"] = abs(self.myfloat(row["Belopp"]))
                    self.write(row)
        input_file.close()
        self.summing()
        return(self.printing())

    def summing(self):
        with open("output.csv", "r") as new_input:
            reader = csv.DictReader(new_input)
            for row in reader:
                cat = row["Kategori"]
                amount = float(row["Belopp"])
                d = time.strptime(row["Datum"], "%Y-%m-%d").tm_mon
                if d == self.month:
                    for counter in range(0, len(self.categories_int)):
                        if cat == self.categories_names[counter]:
                            self.categories_int[counter] += amount
                        elif counter == len(self.categories_int):
                            self.categories_int[counter] += amount
        new_input.close()


    def writeinit(self):
        with open("output.csv", "w") as output_file:
            writer = csv.DictWriter((output_file), fieldnames=self.fieldheader)
            writer.writeheader()

    def write(self, row):
        with open("output.csv", "a") as output_file:
            writer = csv.DictWriter((output_file), fieldnames=self.fieldheader)
            if any(row):
                writer.writerow(row)

    def expenses(self, string):
        i = 0
        for categori in self.categories_list:
            for word in categori:
                if word in string:
                    return self.categories_names[i]
            i += 1
        return self.categories_names[i]

    def nonexpenses(self, string):
        non =   [
                "överföring", "inbetalning", "studiestöd", "lön", "utlägg",
                "insättning", "141229 okq8", "mor"
                ]
        for word in non:
            if word in string:
                return True

    def myfloat(self, string):
        return float(string.replace('.', '').replace(',', '.'))

    def user_month(self):   
        try:
            self.month = int(input("Which month? "))
            if self.month > 12 or self.month < 1:
                raise
            return self.month
        except:
            print("Use an integer between 1-12 ")
            self.user_month()

    def printing(self):
        sums = self.categories_int
        if(self.computer_read):
            s = round(sum(sums))
            sums.append(s)
            return(sums)
        else:
            t = PrettyTable(['Kategori', 'Utgift [kr]'])
            t.align="l"
            i = 0
            for value in sums:
                t.add_row([self.categories_names[i], round(value)])
                i += 1
            print()
            print(t)
            print(
                "\nTotal spendings for %s was: %g kr\n" % 
                (calendar.month_name[self.month], abs(round(sum(sums))))
                )


Receipt(sys.argv).main()
