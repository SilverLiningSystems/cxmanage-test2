# Copyright (c) 2012, Calxeda Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# * Neither the name of Calxeda Inc. nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
# TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.


""" Various objects used by tests """

import random
import tempfile

from cxmanage.image import Image

def random_file(work_dir, size):
    """ Create a random file """
    contents = "".join([chr(random.randint(0, 255))
        for a in range(size)])
    filename = tempfile.mkstemp(prefix="%s/" % work_dir)[1]
    open(filename, "w").write(contents)
    return filename

class TestImage(Image):
    def valid_type(self):
        return True

class TestSensor:
    """ Sensor result from bmc/target """
    def __init__(self, sensor_name, sensor_reading):
        self.sensor_name = sensor_name
        self.sensor_reading = sensor_reading

class TestSlot:
    """ Slot info for a partition """
    def __init__(self, slot, slot_type, offset=0,
            size=0, version=0, daddr=0, in_use=None):
        self.slot = "%2i" % slot
        self.type = {
                2: "02 (S2_ELF)",
                3: "03 (SOC_ELF)",
                10: "0a (CDB)",
                11: "0b (UBOOTENV)"
            }[slot_type]
        self.offset = "%8x" % offset
        self.size = "%8x" % size
        self.version = "%8x" % version
        self.daddr = "%8x" % daddr
        self.in_use = {None: "Unknown", True: "1", False: "0"}[in_use]
