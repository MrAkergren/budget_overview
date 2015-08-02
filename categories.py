# -*- coding: UTF-8 -*-

class Categories():
    def __init__(self):
        pass
     
    def create(self):
        pub_and_rest_int = 0
        fika_int = 0
        groceries_int = 0
        hobby_int = 0
        transport_int = 0
        clothes_int = 0
        misc_int = 0

        pub_and_rest_list =     [
                                "bar","kebab","spice", "tredgarn", "hotels",
                                "fajitas", "systembolaget" ,"sabaidi", 
                                "subway", "sushi", "brygg", "rest", "burger",
                                "pizz", "thai", "max", "kitchen","bofhus", "tre sma"
                                ]

        fika_list =             [
                                "espres", "cake", "cafe"
                                ]

        groceries_list =        [
                                "willys", "hemköp", "ica", "coop", "mathem", 
                                "livs"
                                ]

        hobby_list =            [
                                "sf", "webhallen", "hi fi", "game", "spotify", 
                                "biljettforum", "domaner", "twitch", "liseberg",
                                ]

        transport_list =        [
                                "vasttrafik", "sl ", "sj ", "preem"
                                ]

        clothes_list =           [
                                "jc ", "dressman", "dftba", "design", 
                                "loplabbet"
                                ]

        return (
            [pub_and_rest_int, fika_int, groceries_int, hobby_int, transport_int, clothes_int, misc_int], 
            ["Pub_och_Restaurang","Fika","Livsmedel","Hobby","Transport", "Kläder", "Övrigt"],
            [pub_and_rest_list, fika_list, groceries_list, hobby_list, transport_list, clothes_list]
        )