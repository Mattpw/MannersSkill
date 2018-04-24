# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

#Setting author to my name Mattpw (Matthew Wright)
__author__ = 'Mattpw'

LOGGER = getLogger(__name__)


# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.


class Manners(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MannersSkill, self).__init__(name="MannersSkill")
    
    #The constructor that initializes each of the commands
    def Initialize(self): 
        Hello_intent = IntentBuilder("HelloIntent").   \
            require("HelloKeyword").build()
        self.register_intent(Hello_intent, self.handle_Hello_intent)
        
        How_are_you_intent = IntentBuilder("HowAreYouIntent"). \
            require("HowAreYouKeyword").build()
        self.register_intent(How_are_you_intent, self.handle_How_are_you_intent)


 
    #The contructors that define each of the command messages    
    def handle_Hello_intent(self, message):
        self.speak_dialog("Hello")

    def handle_How_are_you_intent(self, message):
        self.speak_dialog("How.are.you")

    def stop(self):
        pass

    def create_skill():
        return MannersSkill()

#To do list
#Test this code on the linux portal
#debug the code
#add the utterance for each of the above

