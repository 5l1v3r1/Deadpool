#!/usr/bin/env python3

import phoenixAES

phoenixAES.convert_r8faults_file("r8faults", "r9faults", encrypt=False)
phoenixAES.crack_file("r9faults", encrypt=False)
