#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

import eos.db

class Market():
    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance == None:
            cls.instance = Market()

        return cls.instance


    def getMarketRoot(self):
        """
        Get the root of the market tree.
        Returns a list, where each element is a tuple container: the ID, the name and the icon of the group
        """

        marketGroups = (9, #Modules
                        1111, #Rigs
                        157, #Drones
                        11, #Ammo
                        1112, #Subsystems
                        24) #Implants & Boosters
        groups = (920, ) #Effect Beacons
        root = []
        for id in marketGroups:
            mg = eos.db.getMarketGroup(id)
            root.append((id, mg.name, mg.icon.iconFile))

        for id in groups:
            g = eos.db.getGroup(id)
            root.append((id, g.name, g.icon.iconFile))

        return root