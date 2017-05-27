#!/usr/bin/env python

# Author: Anderson Banihirwe, 2017

import os
import time
from .sparkjob import SparkJob
import re
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sparkyellow.lsfsparkjob')

class LSFSparkJob(SparkJob):
	"""Class for submitting spark jobs with LSF scheduler"""
	_submit_command = 'bsub < %s'
	_job_regex = 'Job <(\d+)>'
	_kill_command = 'bkill'
	_get_current_jobs = 'bjobs -o "job_name stat jobid"'

	def _peek(self):
		return subprocess.check_output(["bpeek", str(self.jobid)]).decode()


