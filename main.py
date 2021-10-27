# -*- coding: utf-8 -*-

import os
import shutil
import pytest


if os.path.exists('./Test_report/report'):
	shutil.rmtree('./Test_report/report')
else:
	print('文件不存在，无法删除')
if os.path.exists('./Test_report/test_date'):
	shutil.rmtree('./Test_report/test_date')
else:
	print('文件不存在，无法删除')

pytest.main(['-s','--alluredir', './Test_report/test_date'])
os.system('allure generate ./Test_report/test_date -results -o ./Test_report/report')